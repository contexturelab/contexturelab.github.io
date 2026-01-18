---
layout: home
title: Contexture Lab
---

<div style="text-align: center; margin: 2rem 0;">
  <img src="/assets/attachments/logo-lab.jpg" alt="Contexture Lab Logo" style="max-width: 400px; width: 100%; height: auto; margin-bottom: 1rem;">
</div>

# **Contexture Lab**
### *The Laboratory for Contextual Structure & Dynamics*

<div style="text-align: center; margin: 2rem 0;">
  <strong>"Mapping the Fabric of Social Reality"</strong>
</div>

---

## About the Lab

**"Contexture"** (noun): *The arrangement of parts into a whole; the act of weaving together.*

We believe that social reality is not a collection of isolated facts, but a continuous fabric woven from interactions. Traditional data science often cuts this fabric into discrete pieces—labels, categories, clusters. **Contexture Lab** exists to study the weave itself, analyzing how individual interactions allow complex social structures to emerge.

### Our Vision

* **The Shift:** From **Discrete** (Static Categories) to **Continuous** (Dynamic Context)
* **The Goal:** To map the "geometry" of how humans live, form groups, and construct knowledge

### Core Philosophy

We draw inspiration from the Japanese philosophical distinction between *Mono* and *Koto*:

* **Mono (物 - Object):** Static nodes. Fixed labels. Binary oppositions.
* **Koto (事 - Event/Experience):** Dynamic interactions. Unfolding events. The intangible "space between."

> *"Other labs analyze the Mono (the dots). We analyze the Koto (the lines, the spaces, and the weaving)."*

### Research Pillars

1. **Computational Constructionism** — Operationalizing Social Constructionism using Network Science and Deep Learning
2. **The Geometry of Knowledge** — Mapping scientific innovation and "invisible value" using non-Euclidean geometry
3. **Beyond Binaries** — Developing AI that resists binary classification, preserving the nuance and spectrum of human diversity
4. **Agentic Structures** — Building AI agents that can navigate and assist in complex social contexts

### Director

**Prof. Sadamori Kojaku**
Assistant Professor, Systems Science and Industrial Engineering
Binghamton University
[skojaku@binghamton.edu](mailto:skojaku@binghamton.edu)

---

## Lab News

{% if site.data.news %}
<ul>
{% for item in site.data.news limit:5 %}
  <li>
    <strong>{{ item.date | date: "%B %d, %Y" }}</strong> — {{ item.title }}
    {% if item.description %}
    <br><span style="margin-left: 1em;">{{ item.description }}</span>
    {% endif %}
  </li>
{% endfor %}
</ul>
{% else %}
<p>No news items yet. Check back soon!</p>
{% endif %}

---

<div style="text-align: center; margin-top: 3rem; font-size: 0.9em;">
  <p>Interested in joining the lab? See our <a href="people">People</a> page for opportunities.</p>
  <p>Explore our <a href="code-data">Code & Data</a> and <a href="slides">Slides</a>.</p>
</div>
