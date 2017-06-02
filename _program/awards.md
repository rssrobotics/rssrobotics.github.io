---
layout: page
title: Awards
description: Award details.
---
Winners are selected from a group of finalists by an awards committee.
Here is a list of past [finalists and winners](http://www.roboticsfoundation.org/index.php/awards).


### Best Paper Award

This award is given the best paper of the conference.

**Finalists:**

{% for paper in site.data.papers %}
{% for finalist in site.data.award_finalists %}
{% if finalist.type == 'best_paper' and finalist.internal_id == paper.internal_id %}
<a href="{{ site.baseurl }}/program/papers/{{ paper.external_id | prepend: '0' | slice: -2, 2 }}">
  {{ paper.title }}
</a>
<br/>
  {{ paper.authors }}
<br/>
{% endif %}
{% endfor %}
{% endfor %}
<br/>

### Best Student Paper Award

This award is given the best paper of the conference whose first author is a
student.

**Finalists:**

{% for paper in site.data.papers %}
{% for finalist in site.data.award_finalists %}
{% if finalist.type == 'best_student_paper' and finalist.internal_id == paper.internal_id %}
<a href="{{ site.baseurl }}/program/papers/{{ paper.external_id | prepend: '0' | slice: -2, 2 }}">
  {{ paper.title }}
</a>
<br/>
  {{ paper.authors }}
<br/>
{% endif %}
{% endfor %}
{% endfor %}
<br/>

### Best Systems Paper Award in Memory of [Seth Teller](http://people.csail.mit.edu/teller/)

This award is given to outstanding systems papers presented at the RSS
conference. The awards committee determines each year if a paper of sufficient
quality is among the accepted papers and may decide not to give the award. In
years when no award is given, the list of finalists will not be disclosed. This
award was given for the first time in 2015
([more information](http://www.roboticsfoundation.org/index.php/awards?id=15)).

<br/>

### Outstanding Reviewer Acknowledgement

Reviewers are the life blood of a conference. Although not an award, this
acknowledgement provides an opportunity to highlight and thank our most
outstanding reviewers nominated by the Area Chairs.

<br/><br/><br/><br/>
