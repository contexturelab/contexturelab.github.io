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
    <strong>The Contexture Lab recovers the continuity that categorical thinking erases.</strong> Reality exists as interconnected continua without natural boundaries, yet we impose categorical partitions to comprehend it—introducing bias and concealing underlying structure. We develop methods to reveal the spectra and nuance that these partitions obscure.
  </p>
</div>

<hr style="margin: 2rem 0; border: 0; border-top: 1px solid #eee;">

## Lab News

{% if site.data.news %}
<ul>
{% for item in site.data.news %}
  <li>
    <strong>{{ item.date | date: "%B %d, %Y" }}</strong> — {{ item.title }}
    {% if item.description %}
    <br><span style="margin-left: 1em;">{{ item.description | markdownify | remove: '<p>' | remove: '</p>' }}</span>
    {% endif %}
  </li>
{% endfor %}
</ul>
{% else %}
<p>No news items yet. Check back soon!</p>
{% endif %}

<hr style="margin: 2rem 0; border: 0; border-top: 1px solid #eee;">

## Press Coverage

| Outlet | Date | Link |
|--------|------|------|
| Binghamton University News | 2026-04-01 (posted 2026-05-07) | [Eureka! Researchers develop new way to detect breakthroughs in science](https://www.binghamton.edu/news/story/6153/eureka-scientists-develop-new-way-to-detect-breakthroughs-in-science) |
| Physics World | 2026-04-09 | [Have you published a disruptive paper? New machine-learning tool helps you check](https://physicsworld.com/a/have-you-published-a-disruptive-paper-new-machine-learning-tool-helps-you-check/) |
| APS Physics | 2026 | [APS Physics v19/63](https://physics.aps.org/articles/v19/63) |

<hr style="margin: 2rem 0; border: 0; border-top: 1px solid #eee;">

<div style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid #eee; font-size: 0.9rem; color: #666;">
  <p>
    The Contexture Lab is led by <a href="https://skojaku.github.io/">Sadamori Kojaku</a>, Assistant Professor in the School of Systems Science and Industrial Engineering (SSIE) at Binghamton University.
  </p>
  <p>
    <a href="mailto:skojaku@binghamton.edu" style="text-decoration: none; border-bottom: 1px solid currentColor;">skojaku@binghamton.edu</a>
  </p>
</div>
