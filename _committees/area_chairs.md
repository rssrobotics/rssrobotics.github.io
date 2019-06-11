---
layout: page
title: Area Chairs
description: Organizing team.
invisible: false
---
<div>
    <div id="area-chairs" class="row text-center">

    {% for member in site.data.areachairs %}
    {% capture modulo %}{{ forloop.index0 | modulo:3 }}{% endcapture %}

    {% if modulo == '0' %}<div class="row text-center">{% endif %}
        <div class="col-sm-4">
            <a href="{{ member.url }}">{{ member.name }}</a><br>
            <i>{{ member.affiliation }}</i><br>
            <br>
        </div>
    {% if modulo == '2' or forloop.last %}</div>{% endif %}

    {% endfor %}

    </div>

</div>
