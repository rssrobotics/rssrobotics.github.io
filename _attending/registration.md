---
layout: page
title: Registration
description: Register for the conference.
priority: 8

late_registration_period: June 22 - 26

deadlines:
  Early: May 22, 2019
  Regular: June 11, 2019
  Late: June 26, 2019

prices:
  Conference + Workshops:
    Early:
      Student:  €270
      Academic: €570
      Industry: €870
    Regular:
      Student:  €370
      Academic: €670
      Industry: €970
    Late:
      Student:  €470
      Academic: €770
      Industry: €1070
  Workshops only:
    Early:
      Student:  €130
      Academic: €280
      Industry: €430
    Regular:
      Student:  €180
      Academic: €330
      Industry: €480
    Late:
      Student:  €240
      Academic: €390
      Industry: €540
---

Early Registration Deadline: *May 22, 2019 (23:59 EDT)*
<br/>
Regular Registration Deadline: *June 11, 2019 (23:59 EDT)*

Late registrations will be accepted onsite on {{ page.late_registration_period }}.
Late registrations have no guarantee of conference materials or banquet ticket.


<!--
If you require a visa to enter the United States, you can request a Letter of
Invitation in the registration form. If requested, you will receive an email
asking for information required to generate the letter within one business day.
-->


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

<!--
**Registration is now open: [https://www.regonline.com/RSS_2018](https://www.regonline.com/RSS_2018)**

### Press Passes

Journalists may request a free press pass by emailing the [program
chair](http://roboticsconference.com/committees/organizers/). Please provide
your name, email address, organization, and any ONE of the following
credentials:

- Masthead from a current issue of a technology publication, online publication,
  or blog listing you as an editorial contributor.
- Technology article published within the past three months with your byline.
- Letter from the editor/producer on official letterhead or from a company email
  address that states you are covering RSS 2018 on assignment.
- Press photo ID from your media outlet.
- Business card from your media outlet reflecting your editorial role.

Press passes grant access to the main conference sessions and workshops only.
Access to social events and poster sessions requires a paid registration.

<br/><br/>

-->

**Registration is now open: [RSS2019 Registration](https://www.intercongress.de/cgi-bin/regform_79106.exe?company=79106&Event=1916&Language=1&Entry=9)**