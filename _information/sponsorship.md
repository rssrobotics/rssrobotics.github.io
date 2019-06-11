---
layout: page
title: Sponsors
description: Sponsorship information
---

We are currently planning the events and budget for RSS 2019. Sponsorship of our
conference provides an opportunity to support one of the premiere international
robotics conferences showcasing the latest research in this field. The RSS 2019
conference will bring together researchers working on the latest algorithmic and
mathematical foundations of robotics, robotics applications, and the analysis of
robotic systems. The conference will be held at the University of Freiburg and
will include invited talks as well as oral and poster presentations of refereed
papers. In addition to the technical aspects of the conference, a series of
social and industry events will provide opportunities for networking and
recruiting.

If you would like to show your presence at RSS 2019 by becoming a sponsor, please refer to our <a href="{{ site.baseurl }}/docs/RSS2019_Sponsorship.pdf">sponsorship options</a>.

<h2>RSS Banquet Sponsor</h2>
<div class="text-center" id="ss-banquet">
    {% for sponsor in site.data.sponsors %}
      {% if sponsor.support_level == "banquet" %}
      <a href="{{ sponsor.url }}">
        <img src="{{ site.baseurl }}/images/sponsors/{{ sponsor.image }}"
	width="{{ sponsor.width }}"
        alt="{{ site.sponsor_name }}"/>
      </a>
      {% endif %}
    {% endfor %}
</div>

<br/>

<h2>RSS Patrons</h2>
<div class="text-center" id="ss-patron">
    {% for sponsor in site.data.sponsors %}
      {% if sponsor.support_level == "patron" %}
      <a href="{{ sponsor.url }}">
        <img src="{{ site.baseurl }}/images/sponsors/{{ sponsor.image }}"
	width="{{ sponsor.width }}"	
        alt="{{ site.sponsor_name }}"/>
      </a>
      {% endif %}
    {% endfor %}
</div>

<br/>

<h2>RSS Benefactors</h2>
<div class="text-center" id="ss-major">
    {% for sponsor in site.data.sponsors %}
      {% if sponsor.support_level == "benefactor" %}
      <a href="{{ sponsor.url }}">
        <img src="{{ site.baseurl }}/images/sponsors/{{ sponsor.image }}"
	width="{{ sponsor.width }}"
        alt="{{ site.sponsor_name }}"/>
      </a>
      {% endif %}
    {% endfor %}
</div>
<br/>

<h2>RSS Sponsors</h2>
<div class="text-center" id="ss-major">
    {% for sponsor in site.data.sponsors %}
      {% if sponsor.support_level == "sponsor" %}
      <a href="{{ sponsor.url }}">
        <img src="{{ site.baseurl }}/images/sponsors/{{ sponsor.image }}"
	width="{{ sponsor.width }}"	
        alt="{{ site.sponsor_name }}"/>
      </a>
      {% endif %}
    {% endfor %}
</div>

<br/>

<!--
<div class="text-center" id="ss-sponsor">
<h2>RSS Small Business Sponsors</h2>
    {% for sponsor in site.data.sponsors %}
      {% if sponsor.support_level == "small" %}
      <a href="{{ sponsor.url }}">
        <img src="{{ site.baseurl }}/images/sponsors/{{ sponsor.image }}"
	width="{{ sponsor.width }}"	
        alt="{{ site.sponsor_name }}"/>
      </a>
      {% endif %}
    {% endfor %}
</div>
<br/><br/>
-->