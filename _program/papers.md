---
layout: page
title: Accepted Papers
description: Accepted papers.
invisible: false
---

<ul>
{% for paper in site.data.papers %}
  <details>
    <summary>
	<b> {{ paper.title }} </b>
    </summary>
    {{ paper.abstract }}
    <br>
    [<b><a href="{{ site.papers }}/{{ paper.external_id }}_FI.pdf">Full Paper</a></b>]
    {% if paper.has_video == "1" %}
        [<b><a href="{{ site.videos }}/{{ paper.external_id }}_VI_fi.mp4">Video</a></b>]
    {% endif %}
  </details>
  {{ paper.authors }}
<br>
<br>
{% endfor %}
</ul>
