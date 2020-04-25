---
layout: page
title: Colaboradores - Escola de Pintura de Carlet
permalink: /colaboradores/
---

### Listado de artistas y colaboradores

<ul>
{% for colaborador in site.data.colaboradores %}
  <li>{{ colaborador.alias }}</li>
{% endfor %}
</ul>

