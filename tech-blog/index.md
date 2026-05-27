---
layout: default
title: "Tech Blog"
permalink: /tech-blog/
---

<div class="blog-header">
  <div class="blog-hero-tag">Writing</div>
  <h1 class="blog-hero-title">Tech Blog</h1>
  <p class="blog-hero-sub">Notes on software engineering, systems thinking, and things I'm learning.</p>
</div>

{% assign pages_list = site.pages | where_exp: "p", "p.path contains 'pages/'" | where_exp: "p", "p.layout == 'post'" | sort: 'date' | reverse %}

{% if pages_list.size > 0 %}
  <div class="post-list-wrap">
    {% for post in pages_list %}
      {% capture post_num %}{{ forloop.index | prepend: "0" | slice: -2, 2 }}{% endcapture %}
      <div class="post-row">
        <div class="post-row-num">{{ post_num }}</div>
        <div class="post-row-body">
          {% if post.tag %}<div class="post-row-tag">{{ post.tag }}</div>{% endif %}
          <a href="{{ post.url | relative_url }}" style="text-decoration: none; color: inherit;">
            <div class="post-row-title">{{ post.title }}</div>
            {% if post.description %}<div class="post-row-desc">{{ post.description }}</div>{% endif %}
          </a>
        </div>
        <div class="post-row-right">
          <span class="post-row-date">{{ post.date | date: "%b %d, %Y" }}</span>
          <span class="post-row-arrow">→</span>
        </div>
      </div>
    {% endfor %}
  </div>
{% else %}
  <div style="padding: 60px 28px; text-align: center; color: var(--muted); font-family: 'Syne', sans-serif;">
    <div>No posts yet.</div>
    <p style="margin-top: 8px; font-size: 0.85rem;">Add .md files to <code>tech-blog/pages/</code> to get started.</p>
  </div>
{% endif %}

