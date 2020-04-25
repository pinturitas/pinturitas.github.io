---
layout: page
title: Colaboradores - Escola de Pintura de Carlet
permalink: /colaboradores/
---

### Listado de artistas y colaboradores

<ul>
{% for colaborador in site.data.colaboradores %}
  <li><strong>{{ colaborador.alias }}</strong> - <blockquote><em>{{ colaborador.bio }}</em></blockquote></li>
{% endfor %}
</ul>

