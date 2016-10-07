---
layout: page
title: Organzing Committee
description: Organizing team.
---
<div>
    <div class="row">
        <div class="col-12">
            <b>Program Chair</b><br>
            <a href="http://www.cs.cmu.edu/~siddh/">Siddhartha Srinivasa</a><br>
            <i>Carnegie Mellon University</i>
        </div>
    </div>
    <div class="row">
        <div class="col-12">
            <b>General Chair</b><br>
            <a href="https://parasol.tamu.edu/~amato/">Nancy Amato</a><br>
            <i>Texas A&M University</i>
        </div>
    </div>
    <div class="row">
        <div class="col-12">
            <b>Local Arrangements Chair</b><br>
            <a href="http://karaman.mit.edu/">Sertac Karaman</a><br>
            <i>MIT</i>
        </div>
    </div>
    <div class="row">
        <div class="col-12">
            <b>Workshop Chairs</b><br>
        </div>
    </div>
    <div class="row">
            <div class="col-6">
                <a href="https://people.eecs.berkeley.edu/~anca/">Anca Dragan</a><br>
                <i>Berkeley</i>
            </div>
            <div class="col-6">
                <a href="http://robotics.cs.tamu.edu/dshell/">Dylan Shell</a><br>
                <i>Texas A&M University</i>
            </div>
    </div>
    <div class="row">
        <div class="col-12">
            <b>Presentation Chairs</b><br>
        </div>
    </div>
    <div class="row">
            <div class="col-6">
                <a href="http://www.cs.utah.edu/~thermans/">Tucker Hermans</a><br>
                <i>University of Utah</i>
            </div>
            <div class="col-6">
                <a href="http://web.stanford.edu/~anirudha/">Anirudha Majumdar</a><br>
                <i>Princeton</i>
            </div>
    </div>
    <div class="row">
        <div class="col-12">
            <b>Publication Chairs</b><br>
        </div>
    </div>
    <div class="row">
            <div class="col-6">
                <a href="http://www-bcf.usc.edu/~ayanian/">Nora Ayanian</a><br>
                <i>USC</i>
            </div>
            <div class="col-6">
                <a href="http://scottk.seas.harvard.edu/">Scott Kuindersma</a><br>
                <i>Harvard</i>
            </div>
    </div>
    <div class="row">
            <div class="col-12">
                <b>Area Chairs</b><br>
            </div>
    </div>    
{% for member in site.data.areachairs %}
  {% capture modulo %}{% cycle '0', '1', '2' %}{% endcapture %}
  {% if modulo == '0' or forloop.first %}
    <div class="row">
  {% endif %}
      <div class="col-4">
        <a href="{{member.url}}">{{ member.name }}</a> <br>
        <i>{{ member.affiliation }}</i>
      </div>
  {% if modulo == '2' or forloop.last %}
    </div>
  {% endif %}
{% endfor %}
</div>
