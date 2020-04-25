---
layout: post
title: Tema - Libre
galeria_pathname: arte/tema-libre
---

<em>La inspiración es libre y puede venir de cualquier sitio.<em>

---

{% for f in site.static_files %}{% if f.path contains page.galeria_pathname %}
<img src="{{ site.baseurl }}{{ f.path }}" alt="Imagen de una obra de arte" title="{{ f.basename }}" />
{% endif %}{% endfor %}

---

