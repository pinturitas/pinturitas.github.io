---
layout: post
title: Tema - Meninas
galeria_pathname: arte/tema-meninas
---

Este tema surge improvisado pero sirve de inspiración "meninil".

---

{% for f in site.static_files %}{% if f.path contains page.galeria_pathname %}
<img src="{{ site.baseurl }}{{ f.path }}" alt="Imagen de una obra de arte" title="{{ f.basename }}" />
{% endif %}{% endfor %}

---

