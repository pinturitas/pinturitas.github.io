---
layout: page
title: Personas
permalink: /personas/
---

### Artistas y colaboradores de la Escuela de Pintura de Carlet

<ul>
{% for item in site.data.personas %}
  <li><strong>{{ item.alias }}</strong> - <em>{{ item.nombre }}</em><blockquote><em>{{ item.bio | markdownify }}</em></blockquote></li>
{% endfor %}
</ul>

