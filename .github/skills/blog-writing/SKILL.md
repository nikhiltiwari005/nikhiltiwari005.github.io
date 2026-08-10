---
name: blog-writing
description: "Use when drafting or revising blog posts for this Jekyll site so they follow the tone, structure, and formatting used by existing posts."
---

# Blog Writing Consistency

## Goal
Write or revise a blog post so it matches the style and structure of the existing posts in this repository.

## Workflow

1. Review examples
   - Read 2-3 similar posts from the [_posts](../../_posts) folder to identify the common pattern.
   - Note the intro style, heading depth, use of emojis, and example formatting.

2. Prepare the post
   - Create or update a markdown file in [_posts](../../_posts) using a clear slug-based filename.
   - Add front matter with title, date, categories, tags, image path/alt, and description.

3. Follow the standard structure
   - Start with a short, engaging introduction.
   - Use `###` (H3) for in-post titles and major section headings.
   - Match surrounding posts' emoji usage for headers (many posts include emojis in headings).
   - Break content into short paragraphs and bullet points.
   - Include code blocks for examples and commands.
   - Use bold emphasis for key ideas, but avoid over-decoration.

4. Match tone and pacing
   - Keep the voice practical, direct, and beginner-friendly.
   - Prefer concrete examples over abstract explanation.
   - Make each section lead naturally into the next.

5. Quality check
   - Ensure the post reads like a consistent series entry.
   - Verify the title, filename, and front matter align.
   - Check that headings, code blocks, and formatting render cleanly.
   - Remove filler and keep the article focused.

## Defaults to Preserve
- Repository style: concise, educational, and actionable.
- Markdown format: clear headings, bullets, code blocks, and short sections.
- Series tone: confident but approachable, with practical takeaways.
 - Date format: prefer `YYYY-MM-DD HH:MM:SS +0000` in front matter examples.

## When to Adapt
If the topic is different, keep the same structure and presentation style while adjusting the content to fit the subject.

## Front-matter template

Use this copy-paste front-matter as a starting point and update fields as needed:

```
---
title: "Your Post Title"
date: 2025-08-10 12:00:00 +0000
categories: ["Category Name"]
tags: []
image:
   path: /assets/img/your-image/1.png
   alt: image
description: "Short description for previews and SEO."
---
```
