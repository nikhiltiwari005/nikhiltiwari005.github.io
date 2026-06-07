---
title: Blog
icon: fas fa-pen-fancy
order: 1
---

# Blog Archive

Welcome to my tech blog! Here I share articles, insights, and learnings on software engineering, cloud technologies, and system design.

## All Posts

{% for post in site.posts %}
### [{{ post.title }}]({{ post.url }})
**{{ post.date | date: "%B %d, %Y" }}** • {% for tag in post.tags %}`{{ tag }}`{% unless forloop.last %} {% endunless %}{% endfor %}

{{ post.excerpt | strip_html | truncatewords: 30 }}

[Read more →]({{ post.url }})

---

{% endfor %}

## Categories
- 💻 **System Design** - Architecture patterns and scalability
- ☁️ **Cloud & DevOps** - Infrastructure and deployment
- 🔧 **Development** - Best practices and tools
- 🧠 **Learning** - Growth and career insights

---

*Posts are sorted by date. Use the search feature or browse by tags to find topics of interest.*
