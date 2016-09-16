---
layout: page
title: RSS Advisory Board
description: RSS Board of advisors.
---
{% for member in site.data.advisory %}
  <a href="{{member.url}}">{{ member.name }}</a>, {{ member.affiliation }}
  
{% endfor %}
