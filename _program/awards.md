---
layout: page
title: Awards
description: Award details.
priority: 6

awards: ['Best Paper', 'Best Student Paper', 'Best Systems Paper']
status: ['Winner', 'Finalist']
invisible: true
---

<!--
During the awards ceremony, we will be presenting the conference best paper
awards in addition to the [International Journal of Robotics
Research](http://journals.sagepub.com/home/ijr) best paper award.

The best conference papers are selected from a group of finalists by an awards
committee. Here is a list of past [finalists and
winners](http://www.roboticsfoundation.org/index.php/awards).

{% for award_name in page.awards %}
{% if award_name == 'Best Paper' %}
### Best Paper Award

This award is given to the best paper of the conference.

{% elsif award_name == 'Best Student Paper' %}
### Best Student Paper Award sponsored by [Springer](https://www.springer.com/us) on behalf of [Autonomous Robots](https://www.springer.com/engineering/control/journal/10514)

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

{% for award in site.data.award_finalists %}
{% for paper in site.data.papers %}
{% if award.type == award_name and award.status == award_status and award.internal_id == paper.internal_id %}
<details>
<summary><b>{{ paper.title }}</b></summary>
{{ paper.abstract }}
<br>
  [<b><a href="http://www.roboticsproceedings.org/rss14/p{{ paper.external_id }}.pdf">Full Paper</a></b>]
</details>
  {{ paper.authors }}
<br/>
{% endif %}
{% endfor %}
{% endfor %}
{% endfor %}
{% endfor %}

<br/><br/><br/><br/>
-->
