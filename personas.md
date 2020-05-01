---
layout: page
title: Personas
permalink: /personas/
---

### Artistas y colaboradores de la Escuela de Pintura de Carlet

<ul>
{% for dato in site.data.personas %}
  <li><strong>{{ dato.alias }}</strong> - <em>{{ dato.nombre }}</em><blockquote><em>{{ dato.bio | markdownify }}</em></blockquote></li>
{% endfor %}
</ul>

