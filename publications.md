---
layout: page
title: Publications
---

Peer-reviewed papers by the lab and by Sadamori Kojaku before the lab started (2023). **Bold** marks Sadamori Kojaku; <u>underline</u> marks a lab student.

{% assign by_year = site.data.publications.publications | group_by: "year" %}
{% for year_group in by_year %}
### {{ year_group.name }}
{% for pub in year_group.items %}
- {% for author in pub.authors %}{% assign i = forloop.index0 %}{% if pub.self contains i %}**{{ author }}**{% elsif pub.students contains i %}<u>{{ author }}</u>{% else %}{{ author }}{% endif %}{% unless forloop.last %}, {% endunless %}{% endfor %}. "{{ pub.title }}." *{{ pub.venue }}*{% if pub.volume %} {{ pub.volume }}{% endif %}{% if pub.number %}({{ pub.number }}){% endif %}{% if pub.pages %}, {{ pub.pages }}{% endif %}{% if pub.note %} ({{ pub.note }}){% endif %}.
{% endfor %}
{% endfor %}
