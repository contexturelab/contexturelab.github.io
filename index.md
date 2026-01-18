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

Our research represents a fundamental shift in how we approach social data. Where traditional methods impose discrete categories and static labels, we develop techniques that reveal the continuous, dynamic context in which human behavior unfolds. We seek to map the "geometry" of how humans live, form groups, and construct knowledge—not as fixed points in space, but as fluid trajectories through a landscape of meaning.

### Core Philosophy

We draw inspiration from the Japanese philosophical distinction between *Mono* and *Koto*. **Mono (物)** refers to objects—the static nodes, fixed labels, and binary oppositions that dominate conventional data science. **Koto (事)**, by contrast, captures events and experiences—the dynamic interactions, unfolding processes, and intangible spaces between things. While other labs analyze the Mono (the dots), we analyze the Koto (the lines, the spaces, and the weaving). This distinction guides everything we do, from the questions we ask to the methods we develop.

### Research Pillars

Our work centers on **Computational Constructionism**, the project of operationalizing social constructionist theory using network science and deep learning. We treat categories like "crime," "success," or "genius" not as natural kinds but as social constructions, and we use representation learning to reverse-engineer these constructions, revealing the continuous spectrum that exists before labels are applied.

Through the lens of **The Geometry of Knowledge**, we map scientific innovation and what we call "invisible value"—the contributions that matter but go unrecognized by traditional metrics. By embedding knowledge networks in non-Euclidean spaces, particularly hyperbolic and Lorentzian geometries, we can capture hierarchical and temporal structures that Euclidean methods miss.

We are committed to developing AI systems that move **Beyond Binaries**. Our methods resist the urge to classify, instead preserving the nuance and spectrum of human diversity. This is not just a technical choice but an ethical one, reflecting our belief that simplification often does violence to the phenomena we study.

Finally, we build **Agentic Structures**—AI agents that can navigate these complex social contexts, not as external observers but as participants that understand the relational nature of meaning. These agents represent a new kind of computational tool, one that respects the contextual fabric of social reality.

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
