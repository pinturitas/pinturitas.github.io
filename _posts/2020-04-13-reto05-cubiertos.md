---
layout: post
title: Reto 5 - Cubiertos
---

Ya echamos de menos las noches de fiesta, salir con los amigos, con la pareja, quizás una película de cine, y una cena agradable en un restaurante... En estos días de confinamiento, podemos fantasear con los cubiertos de casa, y servirnos la cena como si lo hiciera un chef estrellado de la guía Michelín...

---

{% for f in site.static_files %}{% if f.path contains 'arte/reto05' %}
<img src="{{ site.baseurl }}{{ f.path }}" alt="Dibujo" title="{{ f.basename }}" />
{% endif %}{% endfor %}

---

