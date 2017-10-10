---
layout: page
title: Organizing Committee
description: Organizing team.
---
<div>
    <div class="row text-center">
            <b>Program Chair</b><br>
            <a href="http://verifiablerobotics.com/">Hadas Kress-Gazit</a><br>
            <i>Cornell</i><br>
            <br>
            <b>General Chair</b><br>
            <a href="http://www.cs.cmu.edu/~siddh/">Siddhartha Srinivasa</a><br>
            <i>University of Washington</i><br>
            <br>
            <b>Local Arrangements Chair</b><br>
            <a href="http://nmichael.frc.ri.cmu.edu/" >Nathan Michael</a><br>
            <i>Carnegie Mellon University</i><br>
            <br>
            <b>Publicity Chair</b><br>
            <a href="http://www.robots.ox.ac.uk/~mfallon/" >Maurice Fallon</a><br>
            <i>Oxford</i><br>
            <br>
            <b>Workshop Chairs</b><br>
            <a href="https://am.is.tuebingen.mpg.de/person/jbohg">Jeannette Bohg</a><br>
            <i>Stanford</i><br>
            <a href="https://www.csee.umbc.edu/~cmat/">Cynthia Matuszek</a><br>
            <i>University of Maryland Baltimore County</i><br>
            <br>
            <b>Presentation Chairs</b><br>
            <a href="http://prorok.me/">Amanda Prorok</a><br>
            <i>Cambridge</i><br>
            <a href="http://people.csail.mit.edu/camato/">Christopher Amato</a><br>
            <i>Northeastern</i><br>
            <br>
            <b>Publication Chairs</b><br>
            <a href="http://www.ece.rochester.edu/people/faculty/howard_tom/">Tom Howard</a><br>
            <i>University of Rochester</i><br>
            <a href="http://jacobsschool.ucsd.edu/faculty/faculty_bios/index.sfe?fmp_recid=409">Nikolay Atanasov</a><br>
            <i>UCSD</i><br>
            <br>
            <b>Web Chairs</b><br>
            <a href="http://wtabib.com/">Wennie Tabib</a><br>
            <i>CMU</i><br>
            <br>
    </div>

    <div id="area-chairs" class="row text-center">
        <b>Area Chairs</b><br>

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
