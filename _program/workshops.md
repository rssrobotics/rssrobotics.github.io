---
layout: page
title: Workshops
description: Workshop times, venues, and details.
---

Workshops will take place July 15 and 16, 2017.

<table class="table table-striped table-workshop">
  <thead>
    <tr>
      <th width="15%" align="center">WS</th>
      <th width="38%">Title</th>
      <th width="32%">Organizers</th>
      <th width="5%">Date</th>
      <!-- <th width="10%">Room</th> -->
    </tr>
  </thead>
  <tbody>
    {% for workshop in site.data.workshops %}
    <tr>
      <td>{{ workshop.external_id }}</td>
      <td><a href="
      {% if workshop.url %}
      {{ workshop.url }}
      {% else %}
      {{ workshop.external_id | replace: '-', '' | downcase }}/
      {% endif %}
      ">{{ workshop.title }}</a></td>
      <td>
        {{ workshop.organizers | replace: ',', '<br/>' }}
      </td>
      <td>{{ workshop.date }}</td>
      <!-- <td>{{ workshop.room }}</td> -->
    </tr>
    {% endfor %}
  </tbody>
</table>
