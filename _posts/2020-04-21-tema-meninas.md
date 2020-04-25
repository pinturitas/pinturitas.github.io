---
layout: post
title: Tema - Meninas
---

Este tema surge improvisado pero sirve de inspiración "meninil".

---

{% for f in site.static_files %}{% if f.path contains 'arte/tema-meninas' %}
<img src="{{ site.baseurl }}{{ f.path }}" alt="Imagen" />
{% endif %}{% endfor %}

---

Obras de arte de la [Escola de Pintura de Carlet](https://arte.pinturitas.com) de primavera de 2020.
