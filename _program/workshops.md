---
layout: page
title: Workshops
description: Workshop times, venues, and details.
days: ['SAT', 'SUN', 'S&S']
room_pictures: ['32-123', '32-124', '32-141', '32-144', '32-155', '36-112', '36-144', '36-153', '36-155', '36-156', '34-101', '34-301', '34-302']
---

Workshops will take place July 15 and 16, 2017.
They will commence at 9:30 AM and end at 5:30 PM.
The workshop coffee breaks will be from 10:30 to 11:00 AM and 3:00 to 3:30 PM, with lunch scheduled for 12:00 - 2:00 PM.

[Here]({{ site.baseurl }}/docs/campusmap.pdf) is a labeled map of the workshop buildings.

{% for day in page.days %}
{% if day == 'SAT' %}
#### Saturday, July 15  {#sat}
{% elsif day == 'SUN' %}
#### Sunday, July 16    {#sun}
{% else %}
#### Saturday & Sunday, July 15 - 16
{% endif %}

<table class="table table-striped table-workshop">
  <thead>
    <tr>
      <th width="15%" align="center">WS</th>
      <th width="36%">Title</th>
      <th width="30%">Organizers</th>
      <th width="5%">Date</th>
      <th width="14%">Room</th>
    </tr>
  </thead>
  <tbody>
    {% for workshop in site.data.workshops %}
    {% if workshop.external_id contains day %}
    <tr>
      <td>{{ workshop.external_id }}</td>
      <td>
        <a href="{{ site.baseurl }}/program/workshops/{{ workshop.external_id | replace: '-', '' | downcase }}/">
          {{ workshop.title }}
        </a>
      </td>
      <td>
        {{ workshop.organizers | replace: ',', '<br/>' }}
      </td>
      <td>{{ workshop.date }}</td>
      {% if page.room_pictures contains workshop.room %}
      <td><a href="http://student.mit.edu/cgi-bin/display_pictures.sh?{{ workshop.room }}">{{ workshop.room }}</a></td>
      {% elsif workshop.room == '32-D463' %}
      <td><a href="http://imgur.com/a/BQv9Y">{{ workshop.room }}</a></td>
      {% elsif workshop.room == '32-G449' %}
      <td><a href="http://imgur.com/a/LC2oA">{{ workshop.room }}</a></td>
      {% else %}
      <td>{{ workshop.room }}</td>
      {% endif %}
    </tr>
    {% endif %}
    {% endfor %}
  </tbody>
</table>
{% endfor %}
