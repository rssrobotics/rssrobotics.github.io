---
layout: page
title: RSS Foundation Board
description: RSS Foundation.
---
<div>
{% for member in site.data.foundation %}
{% capture modulo %}{{ forloop.index0 | mod:3 }}{% endcapture %}
  {% if modulo == '0' or forloop.first %}
    <div class="row">
  {% endif %}
      <div class="col-4">
        <b>{{member.role}}</b> <br>
        <a href="{{member.url}}">{{ member.name }}</a> <br>
        <i>{{ member.affiliation }}</i>
      </div>
  {% if modulo == '2' or forloop.last %}
    </div>
  {% endif %}
{% endfor %}
</div>