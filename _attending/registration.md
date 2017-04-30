---
layout: page
title: Registration
description: Register for the conference.
invisible: false

late_registration_period: July 12 - 16

deadlines:
  Early: May 31, 2017
  Regular: July 5, 2017
  Late: July 16, 2017

prices:
  Conference + Workshops:
    Early:
      Student:  $285
      Academic: $485
      Industry: $770
    Regular:
      Student:  $385
      Academic: $635
      Industry: $1020
    Late:
      Student:  $485
      Academic: $785
      Industry: $1270
  Workshops only:
    Early:
      Student:  $135
      Academic: $185
      Industry: $320
    Regular:
      Student:  $185
      Academic: $235
      Industry: $420
    Late:
      Student:  $285
      Academic: $335
      Industry: $620
---

Early Registration Deadline: *{{ page.deadlines["Early"] }}*
<br/>
Regular Registration Deadline: *{{ page.deadlines["Regular"] }}*

Late registrations will be accepted online {{ page.late_registration_period }}, and
on-site registration will be available during the conference. Late and on-site
registrations have no guarantee of conference gift bag or banquet ticket.

If you require a visa to enter the United States, you can request a Letter of
Invitation in the registration form. If requested, you will receive an email
asking for information required to generate the letter within one business day.

<table class="table table-striped table-registration">
  <thead>
    <tr>
      <th></th>
      <th style="text-align: center">Industry</th>
      <th style="text-align: center">Academic</th>
      <th style="text-align: center">Student</th>
    </tr>
  </thead>
  <tbody>
  {% for entry in page.prices %}
  {% for pricing in entry[1] %}
  <tr align="center">
    <td align="right">
      {{ pricing[0] }} Registration: {{ entry[0] }}
      <br/>
      <!--- This line doesn't work for some reason; hacking around it -->
      <!--- Deadline: {{ page.deadlines[pricing[0]] }} -->
      {% for deadline in page.deadlines %}
      {% if deadline[0] == pricing[0] %}
      Deadline: {{ deadline[1] }}
      {% endif %}
      {% endfor %}
    </td>
    <td>{{ pricing[1]["Industry"] }}</td>
    <td>{{ pricing[1]["Academic"] }}</td>
    <td>{{ pricing[1]["Student"] }}</td>
  </tr>
  {% endfor %}
  {% endfor %}
  </tbody>
</table>

**Registration is now open: [https://www.regonline.com/RSS_2017](https://www.regonline.com/RSS_2017)**

*Note that if you wish to purchase an additional banquet ticket, please select "Conference Banquet Guest Ticket" in the form.*
