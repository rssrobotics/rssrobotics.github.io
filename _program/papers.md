---
layout: page
title: Accepted Papers
description: Accepted papers.
invisible: true
---

<ul>
{% for paper in site.data.papers %}
<li>
  <a href="{{ paper.external_id | prepend: '0' | slice: -2, 2 }}">
    {{ paper.title }}
  </a>
  <br/>
  {{ paper.authors }}
</li>
<br/>
{% endfor %}
</ul>
