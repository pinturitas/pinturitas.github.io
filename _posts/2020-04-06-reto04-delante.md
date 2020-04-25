---
layout: post
title: Reto 4 - ¡Mira delante!
galeria_pathname: arte/reto04
---

Acabando el primer mes de confinamiento, hay que mirar al futuro con optimismo, y saber que cada día más es un día menos, para poder salir, ver a los tuyos, pasar tiempo al sol y disfrutar del aire libre. De momento, vamos a plasmar lo que cada uno tiene delante...

---

{% for f in site.static_files %}{% if f.path contains page.galeria_pathname %}
<img src="{{ site.baseurl }}{{ f.path }}" alt="Imagen de una obra de arte" title="{{ f.basename }}" />
{% endif %}{% endfor %}

---

