---
layout: page
title: RSS Advisory Board
description: RSS Board of advisors.
---
<div>
{% for member in site.data.advisory %}
  {% assign loopindex = forloop.index | modulo: 3 %}
  {% if modulo == '0' or forloop.first %}
    <div class="row">
  {% endif %}
      <div class="col-4">
        <a href="{{member.url}}">{{ member.name }}</a> <br>
        <i>{{ member.affiliation }}</i>
      </div>
  {% if modulo == '1' or forloop.last %}
    </div>
  {% endif %}
{% endfor %}
</div>