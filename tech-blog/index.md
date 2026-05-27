---
layout: default
title: "Tech Blog"
permalink: /tech-blog/
---

<style>
  .blog-header {
    margin-bottom: 60px;
  }

  .blog-eyebrow {
    font-family: 'Syne', sans-serif;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 14px;
  }

  .blog-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: clamp(2rem, 6vw, 3rem);
    color: #fff;
    letter-spacing: -0.04em;
    line-height: 1.1;
    margin-bottom: 16px;
  }

  .blog-desc {
    font-size: 1rem;
    color: var(--soft);
    max-width: 480px;
    line-height: 1.65;
  }

  /* ── POST LIST ──────────────────────────── */
  .post-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 2px;
  }

  .post-item a {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 16px;
    padding: 20px 0;
    border-bottom: 1px solid var(--border);
    text-decoration: none;
    transition: all 0.15s;
    group: true;
  }

  .post-item a:hover .post-item-title { color: var(--accent); }
  .post-item a:hover .post-item-arrow { opacity: 1; transform: translateX(0); }

  .post-item-left {
    display: flex;
    flex-direction: column;
    gap: 6px;
    flex: 1;
  }

  .post-item-tag {
    font-family: 'Syne', sans-serif;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--accent);
  }

  .post-item-title {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 1.05rem;
    color: #fff;
    line-height: 1.3;
    transition: color 0.15s;
  }

  .post-item-desc {
    font-size: 0.88rem;
    color: var(--muted);
    line-height: 1.5;
    margin-top: 2px;
  }

  .post-item-right {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 6px;
    flex-shrink: 0;
  }

  .post-item-date {
    font-family: 'Syne', sans-serif;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.04em;
    color: var(--muted);
    white-space: nowrap;
  }

  .post-item-arrow {
    font-size: 0.9rem;
    color: var(--accent);
    opacity: 0;
    transform: translateX(-4px);
    transition: all 0.15s;
  }

  .empty-state {
    padding: 60px 0;
    text-align: center;
    color: var(--muted);
    font-family: 'Syne', sans-serif;
  }
  .empty-state p { margin-top: 8px; font-size: 0.85rem; }
</style>

<div class="blog-header">
  <div class="blog-eyebrow">Writing</div>
  <h1 class="blog-title">Tech Blog</h1>
  <p class="blog-desc">Notes on software engineering, systems thinking, and things I'm learning.</p>
</div>

{% assign pages_list = site.pages | where_exp: "p", "p.path contains 'pages/'" | where_exp: "p", "p.layout == 'post'" | sort: 'date' | reverse %}

{% if pages_list.size > 0 %}
  <ul class="post-list">
    {% for post in pages_list %}
      <li class="post-item">
        <a href="{{ post.url | prepend: site.baseurl }}">
          <div class="post-item-left">
            {% if post.tag %}<span class="post-item-tag">{{ post.tag }}</span>{% endif %}
            <span class="post-item-title">{{ post.title }}</span>
            {% if post.description %}<span class="post-item-desc">{{ post.description }}</span>{% endif %}
          </div>
          <div class="post-item-right">
            <span class="post-item-date">{{ post.date | date: "%b %d, %Y" }}</span>
            <span class="post-item-arrow">→</span>
          </div>
        </a>
      </li>
    {% endfor %}
  </ul>
{% else %}
  <div class="empty-state">
    <div>No posts yet.</div>
    <p>Add .md files to <code>tech-blog/pages/</code> to get started.</p>
  </div>
{% endif %}
