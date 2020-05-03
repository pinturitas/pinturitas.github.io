---
layout: page
title: Artistas
---
### Artistas y colaboradores de la Escuela de Pintura de Carlet

<ul>
{% for item in site.data.artistas %}
  {% assign artistapage = site.artistas | where:"item_id", item.item_id | first %}
  {% if item.bio %}
    {% capture biocomillas %}«{{ item.bio }}»{% endcapture %}
    {% assign bio = biocomillas | markdownify %}
  {% endif %}
  <li>
    <a href="{{ artistapage.url }}"><strong>{{ item.alias }}</strong></a><em> - {{ item.nombre }}</em>
    <blockquote><em>{{ bio }}</em></blockquote>
  </li>
  {% assign bio = nil %}
  {% assign biocomillas = nil %}
  {% assign artistapage = nil %}
{% endfor %}
</ul>
 
