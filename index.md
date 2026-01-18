---
layout: home
title: Contexture Lab
subtitle: Mapping the Fabric of Social Reality
---

<div style="text-align: center; margin: 2rem 0 3rem 0;">
  <img src="/assets/attachments/logo-lab.jpg" alt="Contexture Lab Logo" style="max-width: 350px; width: 100%; height: auto;">
</div>

<div class="lab-intro" style="font-size: 1.15rem; line-height: 1.8; margin-bottom: 3rem;">
  <p>
    <strong>The Contexture Lab investigates the hidden geometry of social reality.</strong>
    We study how humans are embedded in—and directed by—fundamental structures, exploring how these invisible forces shape individual lives and collective advancement.
  </p>
  <p>
    We believe that reality consists of continuous, interconnected phenomena without clear boundaries. Yet, to make sense of the world, humans impose rigid categories and partitions. While this categorization aids interpretability, it introduces bias and obscures the underlying truth. Our mission is to recover the continuity lost in this process, revealing the nuance and spectra that define how society actually functions.
  </p>
</div>

<hr style="margin: 2rem 0; border: 0; border-top: 1px solid #eee;">

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

<hr style="margin: 2rem 0; border: 0; border-top: 1px solid #eee;">

<div style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid #eee; font-size: 0.9rem; color: #666;">
  <p>
    The Contexture Lab is led by <strong>Dr. Sadamori Kojaku</strong>, Assistant Professor in the Department of Systems Science and Industrial Engineering (SSIE) at Binghamton University.
  </p>
  <p>
    <a href="mailto:skojaku@binghamton.edu" style="text-decoration: none; border-bottom: 1px solid currentColor;">skojaku@binghamton.edu</a>
  </p>
</div>
