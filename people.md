---
layout: page
title: People
---

# People

---

## Faculty

{% if site.data.people.faculty %}
{% for person in site.data.people.faculty %}
<div style="display: flex; gap: 1.5rem; margin-bottom: 2rem; align-items: flex-start;">
  {% if person.image %}
  <div style="flex-shrink: 0;">
    <img src="{{ person.image }}" alt="{{ person.name }}" style="width: 150px; height: 150px; object-fit: cover; border-radius: 8px;">
  </div>
  {% endif %}
  <div style="flex-grow: 1;">
    <h3 style="margin-top: 0;">{{ person.name }}</h3>
    <p><strong>{{ person.role }}</strong>{% if person.title %} — {{ person.title }}{% endif %}</p>
    {% if person.affiliation %}<p>{{ person.affiliation }}</p>{% endif %}
    {% if person.bio %}<p>{{ person.bio }}</p>{% endif %}
    <p>
      {% if person.email %}<a href="mailto:{{ person.email }}">Email</a>{% endif %}
      {% if person.website %} | <a href="{{ person.website }}" target="_blank">Website</a>{% endif %}
    </p>
  </div>
</div>
{% endfor %}
{% endif %}

---

## Graduate Students

{% if site.data.people.students %}
{% for person in site.data.people.students %}
<div style="display: flex; gap: 1.5rem; margin-bottom: 2rem; align-items: flex-start;">
  {% if person.image %}
  <div style="flex-shrink: 0;">
    <img src="{{ person.image }}" alt="{{ person.name }}" style="width: 150px; height: 150px; object-fit: cover; border-radius: 8px;">
  </div>
  {% endif %}
  <div style="flex-grow: 1;">
    <h3 style="margin-top: 0;">{{ person.name }}</h3>
    <p><strong>{{ person.role }}</strong></p>
    {% if person.bio %}<p>{{ person.bio }}</p>{% endif %}
    {% if person.website %}<p><a href="{{ person.website }}" target="_blank">Website</a></p>{% endif %}
    {% if person.email %}<p><a href="mailto:{{ person.email }}">Email</a></p>{% endif %}
  </div>
</div>
{% endfor %}
{% else %}
<p><em>We are actively recruiting graduate students. See opportunities below.</em></p>
{% endif %}

---

## Alumni

{% if site.data.people.alumni %}
{% for person in site.data.people.alumni %}
<div style="margin-bottom: 1rem;">
  <strong>{{ person.name }}</strong> — {{ person.role }}
  {% if person.current %}<br><em>Now: {{ person.current }}</em>{% endif %}
</div>
{% endfor %}
{% else %}
<p><em>No alumni yet as this is a new lab.</em></p>
{% endif %}

---

## Join Us

If you're interested in collaborating on research related to:

- Network science and representation learning
- Computational social science
- Non-Euclidean geometry for social data
- AI systems that preserve human nuance

Please reach out to Prof. Kojaku at [skojaku@binghamton.edu](mailto:skojaku@binghamton.edu).

**Note**: We currently do not have funded positions available. Prospective graduate students should apply through the [Binghamton University SSIE graduate program](https://www.binghamton.edu/ssie/) and mention interest in working with our lab. Undergraduate students at Binghamton interested in research projects are welcome to inquire about volunteer research opportunities.

---

[Back to Home](/)
