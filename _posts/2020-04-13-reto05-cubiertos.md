---
layout: post
title: Reto 5 - Cubiertos
galeria_pathname: arte/reto05
---

Ya echamos de menos las noches de fiesta, salir con los amigos, con la pareja, quizás una película de cine, y una cena agradable en un restaurante... En estos días de confinamiento, podemos fantasear con los cubiertos de casa, y servirnos la cena como si lo hiciera un chef estrellado de la guía Michelín...

---

{% for f in site.static_files %}{% if f.path contains page.galeria_pathname %}
<img src="{{ site.baseurl }}{{ f.path }}" alt="Imagen de una obra de arte" title="{{ f.basename }}" />
{% endif %}{% endfor %}

---

