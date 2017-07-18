---
layout: page
title: Awards
description: Award details.
priority: 6

awards: ['Best Paper', 'Best Student Paper', 'Best Systems Paper']
status: ['Winner', 'Finalist']
---

Winners are selected from a group of finalists by an awards committee.
Here is a list of past [finalists and winners](http://www.roboticsfoundation.org/index.php/awards).

{% for award_name in page.awards %}
{% if award_name == 'Best Paper' %}
### Best Paper Award

This award is given to the best paper of the conference.

{% elsif award_name == 'Best Student Paper' %}
### Best Student Paper Award

This award is given to the best paper of the conference whose first author is a
student.

{% elsif award_name == 'Best Systems Paper' %}
### Best Systems Paper Award in Memory of [Seth Teller](http://people.csail.mit.edu/teller/)

This award is given to outstanding systems papers presented at the RSS
conference. The awards committee determines each year if a paper of sufficient
quality is among the accepted papers and may decide not to give the award. In
years when no award is given, the list of finalists will not be disclosed. This
award was given for the first time in 2015
([more information](http://www.roboticsfoundation.org/index.php/awards?id=15)).

{% endif %}

{% for award_status in page.status %}
{% if award_status == 'Winner' %}
**Winner:**
{% elsif award_status == 'Finalist' %}
**Finalists:**
{% endif %}

{% for paper in site.data.papers %}
{% for award in site.data.award_finalists %}
{% if award.type == award_name and award.status == award_status and award.internal_id == paper.internal_id %}
<a href="{{ site.baseurl }}/program/papers/{{ paper.external_id }}/">
  {{ paper.title }}
</a>
<br/>
  {{ paper.authors }}
<br/>
{% endif %}
{% endfor %}
{% endfor %}
{% endfor %}
{% endfor %}

### Outstanding Reviewer Acknowledgement

Reviewers are the life blood of a conference. Although not an award, this
acknowledgement provides an opportunity to highlight and thank our most
outstanding reviewers nominated by the Area Chairs.

- Jerom Le Ny
- Nikolaus Correll
- Francesco Amigoni
- Dylan Shell
- Antonis Argyros
- David Held
- Maurice Fallon
- Leslie Kaelbling

<br/><br/><br/><br/>
