---
layout: page
title: Workshops
description: Workshop times, venues, and details.
days: ['June 22', 'June 23']
invisible: false
---

The workshops will take place on June 22 and June 23 at the campus of
the <a href="https://goo.gl/maps/2iwdEFKUh1m"> Faculty of
Engineering</a> of the University of Freiburg.
<br>

Registration for the Workshops is open from 8:00 - 9:00 at Building
101, Foyer. The workshops start at 9:00. More detailed information
about the schedule of a specific workshop is available at the
workshop's website.
<br>

Please note, that there are two venues for Poster sessions. You can find a map with venues and time
slots for all workshops and their Poster sessions [here](/docs/workshops.pdf).
<br><br>

<center>
<img src="{{ site.baseurl }}/images/workshop_rooms/buildings.png" width="600" class="img-responsive">
</center>
<br><br>

{% for day in page.days %}
{% if day == 'June 22' %}
#### Saturday, June 22  <!-- {#sat} -->
{% else day == 'June 23' %}
#### Sunday, June 23    <!-- {#sun}-->
{% endif %}
<table class="table table-striped table-workshop">
  <thead>
    <tr>
      <th width="10%" align="center">WS</th>
      <th width="30%">Title</th>
      <th width="30%">Organizers</th>
      <!--<th width="10%">Date</th>-->
      <th width="10%">Building</th>
      <th width="20%">Room</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.workshops.workshops %}
    {% if item[1].date == day %}
    <tr>
      <td>{{ item[1].external_id }}</td>
      <td>
      {% if item[1].status contains 'Canceled' %}
        <strike><a href="{{ site.baseurl }}/program/workshops/{{ item[0] }}/">
          {{ item[1].title }}
        </a></strike>
        <br>
        <br>
        {% else %}
	  <a href="{{ site.baseurl }}/program/workshops/{{ item[0] }}/">
          {{ item[1].title }}
	  </a>
      {% endif %}
      </td>
      <td>
        {{ item[1].organizers | replace: ',', '<br/>' }}
      </td>
      <!--<td>
        {{ item[1].date }}
      </td>-->
      <td align="right">
          {% if item[1].building == 105 %}
	            {{ item[1].building }}
          {% else %} 
      	            <a href="{{ site.baseurl }}/program/workshops/bd{{ item[1].building }}/">
		    {{ item[1].building }}
		    </a>
	  {% endif %}
      </td>
      <td>
        {{ item[1].room }}
      </td>
    </tr>
    {% endif %}
    {% endfor %}
  </tbody>
</table>
{% endfor %}