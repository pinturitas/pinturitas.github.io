---
layout: post
title: Reto 2 - Zapatillas de "quédate en casa"
galeria_pathname: arte/reto02
---

Esto del confinamiento obliga... no podemos salir, ni hacer deporte, ni cenar fuera, ni ir de fiesta. Los zapatos de bonito, olvidados en el armario; son las humildes zapatillas de andar por casa las que toman el relevo y doblan turnos en nuestros pies. Aquí va nuestro homenaje a tan cómoda prenda.

---

{% for f in site.static_files %}{% if f.path contains page.galeria_pathname %}
<img src="{{ site.baseurl }}{{ f.path }}" alt="Imagen de una obra de arte" title="{{ f.basename }}" />
{% endif %}{% endfor %}

---

