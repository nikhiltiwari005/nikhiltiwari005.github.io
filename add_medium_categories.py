#!/usr/bin/env python3
import argparse
import re
import unicodedata
from pathlib import Path
from typing import Dict, List, Optional

try:
    from bs4 import BeautifulSoup
except ImportError:
    raise SystemExit('BeautifulSoup (bs4) is required. Install with pip install beautifulsoup4')


def normalize(text: str) -> str:
    text = unicodedata.normalize('NFKC', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text.lower()


def parse_categories_line(line: str) -> List[str]:
    line = line.strip()
    if not line.startswith('categories:'):
        return []
    value = line[len('categories:'):].strip()
    if value.startswith('[') and value.endswith(']'):
        inner = value[1:-1].strip()
        if not inner:
            return []
        parts = [p.strip() for p in re.split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', inner)]
        items = []
        for part in parts:
            part = part.strip()
            if part.startswith('"') and part.endswith('"'):
                part = part[1:-1]
            elif part.startswith("'") and part.endswith("'"):
                part = part[1:-1]
            items.append(part)
        return items
    if value:
        return [value.strip().strip('"').strip("'")]  # fallback
    return []


def safe_yaml_list(items: List[str]) -> str:
    quoted = []
    for item in items:
        escaped = item.replace('"', '\\"')
        quoted.append(f'"{escaped}"')
    return '[{}]'.format(', '.join(quoted))


def main() -> int:
    parser = argparse.ArgumentParser(description='Add Medium list categories to generated Jekyll markdown posts')
    parser.add_argument('--list-dir', type=Path, required=True, help='Path to Medium list HTML files')
    parser.add_argument('--posts-dir', type=Path, required=True, help='Path to generated markdown posts')
    parser.add_argument('--html-dir', type=Path, required=True, help='Path to original Medium post HTML exports')
    args = parser.parse_args()

    list_dir = args.list_dir
    posts_dir = args.posts_dir
    html_dir = args.html_dir

    if not list_dir.exists() or not list_dir.is_dir():
        raise SystemExit(f'List directory not found: {list_dir}')
    if not posts_dir.exists() or not posts_dir.is_dir():
        raise SystemExit(f'Posts directory not found: {posts_dir}')
    if not html_dir.exists() or not html_dir.is_dir():
        raise SystemExit(f'HTML export directory not found: {html_dir}')

    id_to_title: Dict[str, str] = {}
    for path in html_dir.glob('*.html'):
        match = re.search(r'-([0-9a-fA-F]+)\.html$', path.name)
        if not match:
            continue
        post_id = match.group(1)
        html = path.read_text(encoding='utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        title = None
        if soup.title and soup.title.string:
            title = soup.title.string.strip()
        elif soup.find('h1'):
            title = soup.find('h1').get_text(' ', strip=True)
        if title:
            id_to_title[post_id] = title

    md_title_to_path: Dict[str, Path] = {}
    for path in posts_dir.glob('*.md'):
        text = path.read_text(encoding='utf-8')
        title = None
        match = re.search(r'^title:\s*"(.*?)"', text, flags=re.M)
        if match:
            title = match.group(1)
        else:
            match = re.search(r'^title:\s*(.*)$', text, flags=re.M)
            title = match.group(1).strip() if match else None
        if title:
            md_title_to_path[normalize(title)] = path

    category_map: Dict[str, List[Path]] = {}
    unmatched = []
    for list_path in sorted(list_dir.glob('*.html')):
        html = list_path.read_text(encoding='utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        title_tag = soup.find('h1')
        category_name = title_tag.get_text(' ', strip=True) if title_tag else list_path.stem
        for anchor in soup.find_all('a', href=True):
            match = re.search(r'/p/([0-9a-fA-F]+)', anchor['href'])
            if not match:
                continue
            post_id = match.group(1)
            title = id_to_title.get(post_id)
            if not title:
                unmatched.append((post_id, category_name, list_path.name, 'missing html export title'))
                continue
            md_path = md_title_to_path.get(normalize(title))
            if not md_path:
                unmatched.append((post_id, category_name, list_path.name, title))
                continue
            category_map.setdefault(category_name, []).append(md_path)

    if not category_map:
        print('No matching posts found to update.')
        return 0

    updated_files = set()
    for category_name, paths in category_map.items():
        for md_path in paths:
            text = md_path.read_text(encoding='utf-8')
            lines = text.splitlines()
            new_lines = []
            updated = False
            for line in lines:
                if line.startswith('categories:'):
                    current = parse_categories_line(line)
                    if category_name not in current:
                        current.append(category_name)
                        new_line = f'categories: {safe_yaml_list(current)}'
                        new_lines.append(new_line)
                        updated = True
                    else:
                        new_lines.append(line)
                    continue
                new_lines.append(line)
            if updated:
                md_path.write_text('\n'.join(new_lines) + '\n', encoding='utf-8')
                updated_files.add(md_path)

    print(f'Updated {len(updated_files)} markdown files with Medium categories.')
    if unmatched:
        print('\nUnmatched list entries (no markdown file found):')
        for item in unmatched[:20]:
            print(' ', item)
        if len(unmatched) > 20:
            print(f'  ... plus {len(unmatched) - 20} more')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
