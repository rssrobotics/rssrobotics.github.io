---
layout: page
title: Program Committee
description: Reviewing team.
invisible: true
---

<ul>
{% for member in site.data.pc %}
<li>{{ member.FirstName }} {{ member.LastName }} (<i>{{ member.Organization }}</i>)</li>
{% endfor %}
</ul>
