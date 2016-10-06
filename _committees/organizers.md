---
layout: page
title: Organzing Committee
description: Organizing team.
---
Here are the awesome organizers.
<div>
{% for member in site.data.advisory %}
  {% capture modulo %}{% cycle '0', '1', '2' %}{% endcapture %}
  {% if modulo == '0' or forloop.first %}
    <div class="row">
  {% endif %}
      <div class="col-4">
        <a href="{{member.url}}">{{ member.name }}</a> <br>
        <i>{{ member.affiliation }}</i>
      </div>
  {% if modulo == '2' or forloop.last %}
    </div>
  {% endif %}
{% endfor %}
</div>
