.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _draw_a_matchmaker:

Dibuja un Casamentero
==========================

Ahora estás usando el Entorno de Desarrollo de Processing (o PDE). 
No hay mucho en él; el área grande es el Editor de Texto, y hay una fila de botones en la parte superior; esta es la barra de herramientas. 
Debajo del editor está el Área de Mensajes, y debajo de eso está la Consola. 
El Área de Mensajes se utiliza para mensajes de una línea, y la Consola se usa para detalles más técnicos.

Vamos a familiarizarnos con el uso de Processing y dibujar un casamentero.

**Boceto**

Copia el boceto a continuación en Processing y ejecútalo. Aparecerá una nueva ventana de visualización y se dibujará un casamentero animado.

.. code-block:: arduino

    size(200,200);
    background(92, 168, 0); 
    rectMode(CENTER);
    rect(100,120,20,60);
    ellipse(100,80,45,45);
    line(90,150,80,170);
    line(110,150,120,170);
    line(90,110,70,100);
    line(110,110,130,100);

.. image:: img/draw_one1.png

.. note:: 

    Si lo ejecutas y el área de mensajes se vuelve roja y reporta algunos errores, entonces hay algo mal con el boceto. Asegúrate de copiar el boceto de ejemplo exactamente: los números deben estar entre paréntesis, con comas entre cada número, y las líneas deben terminar con punto y coma.


**¿Cómo funciona?**

La clave aquí es darse cuenta de que la ventana de visualización se puede tratar como un cuadrado de papel.

Cada píxel de la ventana de visualización es una coordenada (x,y) que determina la posición de un punto en el espacio. El origen (0,0) de las coordenadas está en la esquina superior izquierda, la dirección positiva del eje X es horizontal hacia la derecha, y la dirección positiva del eje Y es vertical hacia abajo.

Lo que tenemos que hacer es especificar qué forma y color deben aparecer en estas coordenadas de píxeles.

Por ejemplo, dibuja un rectángulo de ancho 20 y alto 60 con coordenadas (100,120) como el punto medio.

.. code-block:: arduino

    rectMode(CENTER);
    rect(100,120,20,60);

.. image:: img/draw_one_coodinate.png

Una vez que entendemos la relación entre la ventana de visualización y los ejes, este boceto no es difícil para nosotros, solo necesitamos entender algunas declaraciones simples de dibujo gráfico.

    * ``size(width, height)``: Define las dimensiones de la ventana de visualización en unidades de píxeles.
    * ``background(red, green, blue)``: Establece el color de fondo de la ventana de visualización.
    * ``rectMode(mode)``: Modifica la ubicación desde la que se dibujan los rectángulos cambiando la forma en que se interpretan los parámetros dados a ``rect()``.
    * ``rect(x, y, width, height)``: Dibuja un rectángulo en la pantalla.
    * ``ellipse(x, y, width, height)``: Dibuja una elipse (óvalo) en la pantalla.
    * ``line(x1, y1, x2, y2)``: Dibuja una línea (una ruta directa entre dos puntos) en la pantalla.

Para más detalles, consulta `Processing Reference <https://processing.org/reference/>`_.
