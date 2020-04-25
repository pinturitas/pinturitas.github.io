---
layout: post
title: Reto 4 - ¡Mira delante!
---

Acabando el primer mes de confinamiento, hay que mirar al futuro con optimismo, y saber que cada día más es un día menos, para poder salir, ver a los tuyos, pasar tiempo al sol y disfrutar del aire libre. De momento, vamos a plasmar lo que cada uno tiene delante...

---

{% for f in site.static_files %}{% if f.path contains 'arte/reto04' %}
<img src="{{ site.baseurl }}{{ f.path }}" alt="Dibujo" title="{{ f.basename }}" />
{% endif %}{% endfor %}

---

