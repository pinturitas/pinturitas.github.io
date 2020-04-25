---
layout: post
title: Tema - Libre
---

<em>La inspiración es libre y puede venir de cualquier sitio.<em>

---

{% for f in site.static_files %}{% if f.path contains 'arte/tema-libre' %}
<img src="{{ site.baseurl }}{{ f.path }}" alt="Imagen" />
{% endif %}{% endfor %}

---

Obras de arte de la [Escola de Pintura de Carlet](https://arte.pinturitas.com) de primavera de 2020.
