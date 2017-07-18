---
layout: page
title: Accepted Papers
description: Accepted papers.
---

<ul>
{% for paper in site.data.papers %}
<li>
  <a href="{{ site.baseurl }}/program/papers/{{ paper.external_id }}/">
    {{ paper.title }}
  </a>
  <br/>
  {{ paper.authors }}
  {% for award in site.data.award_finalists %}
  {% if award.internal_id == paper.internal_id %}
  <br/>
  <b>{{ award.type }} Award {{ award.status }}</b>
  {% endif %}
  {% endfor %}
</li>
<br/>
{% endfor %}
</ul>
