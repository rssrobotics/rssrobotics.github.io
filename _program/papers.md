---
layout: page
title: Accepted Papers
description: Accepted papers.
---

<ul>
{% for paper in site.data.papers %}
<li>
  <a href="{{ paper.external_id }}">
    {{ paper.title }}
  </a>
  <br/>
  {{ paper.authors }}
  {% for finalist in site.data.award_finalists %}
  {% if finalist.internal_id == paper.internal_id %}
  <br/>
  <b>{{ finalist.type }} Award Finalist</b>
  {% endif %}
  {% endfor %}
</li>
<br/>
{% endfor %}
</ul>
