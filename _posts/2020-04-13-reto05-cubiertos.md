---
layout: post
title: Reto 5 - Cubiertos
---

Ya echamos de menos las noches de fiesta, salir con los amigos, con la pareja, quizás una película de cine, y una cena agradable en un restaurante... En estos días de confinamiento, podemos fantasear con los cubiertos de casa, y servirnos la cena como si lo hiciera un chef estrellado de la guía Michelín...

---

{% for f in site.static_files %}{% if f.path contains 'arte/reto05' %}
![Dibujo]({{ site.baseurl }}{{ f.path }} "Imagen")
{% endif %}{% endfor %}

---

Obras de arte de la [Escola de Pintura de Carlet](https://arte.pinturitas.com) de primavera de 2020.
