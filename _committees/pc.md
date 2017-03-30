---
layout: page
title: Program Committee
description: Reviewing team.
---

<ul class="two-col text-left" style="list-style: none;">
{% for member in site.data.pc %}
<li>{{ member.FirstName }} {{ member.LastName }} (<i>{{ member.Organization }}</i>)</li>
{% endfor %}
</ul>
