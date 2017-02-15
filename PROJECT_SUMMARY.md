# Project Summary

## Overview
This repository is a personal website for `nikhiltiwari005.github.io`. It includes:

- A Jekyll-based personal site using the Chirpy theme
- A blog section with posts and categories
- A resume section and a `favicon` directory for site metadata

## Key areas

### Root site
- `index.md` — main homepage (Chirpy home layout)
- `_config.yml` — Main Jekyll configuration (Chirpy theme)
- `_posts/` — Blog posts in markdown
- `_tabs/` — Static pages (About, etc.)
- `favicon/` — Icon assets and site manifest

## Current setup
- Uses Jekyll with Chirpy theme for the entire site
- Blog posts are organized in `_posts/` with front matter including `title`, `description`, `date`, `tag`, and `read_time`
- Metadata is handled by jekyll-seo-tag plugin for SEO and social sharing

## Notes for future edits
- Add new blog posts in `tech-blog/pages/` with front matter including `title`, `description`, `date`, and optional `tag` and `read_time`
- Use `{{ "/" | relative_url }}` and `{{ page.url | absolute_url }}` in templates to maintain correct links
- The root `README.md` is currently just a placeholder title

## Recommended file for AI assistants
- Use this file as the high-level project summary to avoid repeated full repository scans
- Update this document if the structure changes or new major sections are added
