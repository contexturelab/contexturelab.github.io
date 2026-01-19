---
layout: page
title: Slides
---

# Slides & Presentations

Conference talks, seminars, and teaching materials from Contexture Lab.

---

## Keynote & Invited Talks

{% for talk in site.data.slides.keynote_talks %}
**{{ talk.year }}**
- **{{ talk.title }}**, {{ talk.venue }}, {{ talk.location }}, {{ talk.date }}{% if talk.slides and talk.slides != "#" %} [[Slides]]({{ talk.slides }}){% endif %}
{% endfor %}

{% assign invited_sorted = site.data.slides.invited_talks | sort: "year" | reverse %}
{% assign invited_by_year = invited_sorted | group_by: "year" %}
{% for year_group in invited_by_year %}
**{{ year_group.name }}**
{% for talk in year_group.items %}
- **"{{ talk.title }}"**, {{ talk.venue }}{% if talk.location %}, {{ talk.location }}{% endif %}, {{ talk.date }}{% if talk.slides and talk.slides != "#" %} [[Slides]]({{ talk.slides }}){% endif %}
{% endfor %}
{% endfor %}

---

## Oral Presentations

{% assign oral_sorted = site.data.slides.oral_presentations | sort: "year" | reverse %}
{% assign oral_by_year = oral_sorted | group_by: "year" %}
{% for year_group in oral_by_year %}
**{{ year_group.name }}**
{% for pres in year_group.items %}
- **"{{ pres.title }}"** ({{ pres.authors }}) — {{ pres.venue }}{% if pres.location %}, {{ pres.location }}{% endif %}, {{ pres.date }}{% if pres.slides and pres.slides != "#" %} [[Slides]]({{ pres.slides }}){% endif %}{% if pres.award %} **({{ pres.award }})**{% endif %}
{% endfor %}
{% endfor %}

---

## Poster Presentations

{% assign poster_sorted = site.data.slides.poster_presentations | sort: "year" | reverse %}
{% assign poster_by_year = poster_sorted | group_by: "year" %}
{% for year_group in poster_by_year %}
**{{ year_group.name }}**
{% for poster in year_group.items %}
- **"{{ poster.title }}"** ({{ poster.authors }}) — {{ poster.venue }}{% if poster.location %}, {{ poster.location }}{% endif %}, {{ poster.date }}{% if poster.pdf and poster.pdf != "#" %} [[PDF]]({{ poster.pdf }}){% endif %}
{% endfor %}
{% endfor %}

---

## Teaching Materials

{% for course in site.data.slides.teaching %}
- **{{ course.course }}** ({{ course.terms }}) — {{ course.institution }}{% if course.materials and course.materials != "#" %} [[Materials]]({{ course.materials }}){% endif %}
{% endfor %}

## Request Slides

Can't find the slides you're looking for? Email [skojaku@binghamton.edu](mailto:skojaku@binghamton.edu). We're happy to share slides and speaking notes for educational and research purposes.

[Back to Home](/)
