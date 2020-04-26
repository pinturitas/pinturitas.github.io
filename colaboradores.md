---
layout: page
title: Colaboradores - Escola de Pintura de Carlet
permalink: /colaboradores/
---

### Listado de autores y colaboradores

<ul>
{% for colaborador in site.data.colaboradores %}
  <li><strong>{{ colaborador.alias }}</strong> - <em>{{ colaborador.nombre }}</em><blockquote><em>{{ colaborador.bio }}</em></blockquote></li>
{% endfor %}
</ul>

