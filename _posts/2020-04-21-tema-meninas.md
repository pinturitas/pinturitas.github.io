---
layout: post
title: Tema - Meninas
---

Este tema surge improvisado pero sirve de inspiración "meninil".

---

{% for f in site.static_files %}{% if f.path contains 'arte/tema-meninas' %}
<img src="{{ site.baseurl }}{{ f.path }}" alt="Dibujo" title="{{ f.basename }}" />
{% endif %}{% endfor %}

---

