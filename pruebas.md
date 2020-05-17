---
layout: page
title: pruebas
---

### Futuras miniaturas

{% assign galeria_pathname = "arte/reto07-roselles" %}
{% capture my_include %}{% include cuadros.html %}{% endcapture %}
{{ my_include | markdownify }}

### Futuro sistema de comentarios aquí debajo

<hr/>
<script defer src="https://commento.pinturitas.com:8080/js/commento.js"></script>
<div id="commento"></div>
<hr/>

