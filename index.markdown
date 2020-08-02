---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---

Diary?

{% for post in site.posts %}
   <h4><a href="{{ post.url }}">{{post.title}}</a></h4>
   {{ post.content }}
{% endfor %}
