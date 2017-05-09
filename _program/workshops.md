---
layout: page
title: Workshops
description: Workshop times, venues, and details.
days: ['SAT', 'SUN', 'S&S']
---

Workshops will take place July 15 and 16, 2017.
They will commence at 9:30 AM and end at 5:30 PM.
The workshop coffee breaks will be from 10:30 to 11:00 AM and 3:00 to 3:30 PM, with lunch scheduled for 12:00 - 2:00 PM.

{% for day in page.days %}
<table class="table table-striped table-workshop">
  <thead>
    <tr>
      <th width="15%" align="center">WS</th>
      <th width="38%">Title</th>
      <th width="32%">Organizers</th>
      <th width="5%">Date</th>
      <th width="10%">Room</th>
    </tr>
  </thead>
  <tbody>
    {% for workshop in site.data.workshops %}
    {% if workshop.external_id contains day %}
    <tr>
      <td>{{ workshop.external_id }}</td>
      <td>
        <a href="{{ workshop.external_id | replace: '-', '' | downcase }}/">
          {{ workshop.title }}
        </a>
      </td>
      <td>
        {{ workshop.organizers | replace: ',', '<br/>' }}
      </td>
      <td>{{ workshop.date }}</td>
      <td>{{ workshop.room }}</td>
    </tr>
    {% endif %}
    {% endfor %}
  </tbody>
</table>
{% endfor %}
