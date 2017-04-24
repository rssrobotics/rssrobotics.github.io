---
layout: page
title: Organizing Committee
description: Organizing team.
---
<div>
    <div class="row text-center">
            <b>Program Chair</b><br>
            <a href="http://www.cs.cmu.edu/~siddh/">Siddhartha Srinivasa</a><br>
            <i>Carnegie Mellon University</i><br>
            <br>
            <b>General Chair</b><br>
            <a href="https://parasol.tamu.edu/~amato/">Nancy Amato</a><br>
            <i>Texas A&M University</i><br>
            <br>
            <b>Local Arrangements Chair</b><br>
            <a href="http://karaman.mit.edu/" >Sertac Karaman</a><br>
            <i>MIT</i><br>
            <br>
            <b>Publicity Chair</b><br>
            <a href="http://www.cs.cornell.edu/~rak/" >Ross Knepper</a><br>
            <i>Cornell</i><br>
            <br>
            <b>Workshop Chairs</b><br>
            <a href="https://people.eecs.berkeley.edu/~anca/">Anca Dragan</a><br>
            <i>Berkeley</i><br>
            <a href="http://robotics.cs.tamu.edu/dshell/">Dylan Shell</a><br>
            <i>Texas A&M University</i><br>
            <br>
            <b>Presentation Chairs</b><br>
            <a href="http://www.cs.utah.edu/~thermans/">Tucker Hermans</a><br>
            <i>University of Utah</i><br>
            <a href="http://web.stanford.edu/~anirudha/">Anirudha Majumdar</a><br>
            <i>Princeton</i><br>
            <br>
            <b>Publication Chairs</b><br>
            <a href="http://www-bcf.usc.edu/~ayanian/">Nora Ayanian</a><br>
            <i>USC</i><br>
            <a href="http://scottk.seas.harvard.edu/">Scott Kuindersma</a><br>
            <i>Harvard</i><br>
            <br>
            <b>Web Chairs</b><br>
            <a href="http://www.clintonliddick.com/">Clint Liddick</a><br>
            <i>CMU</i><br>
            <a href="http://brianhou.com/">Brian Hou</a><br>
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
