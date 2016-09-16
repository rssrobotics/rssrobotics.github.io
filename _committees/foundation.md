---
layout: page
title: RSS Foundation Board
description: RSS Foundation.
---
{% for member in site.data.foundation %}
  <b>{{member.role}}</b>, <a href="{{member.url}}">{{ member.name }}</a>, {{ member.affiliation }}
  
{% endfor %}
