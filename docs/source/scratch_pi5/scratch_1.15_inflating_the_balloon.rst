.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.15_scratch_pi5:

1.15 Inflando el Globo
=============================

Aquí, jugaremos un juego de inflar un globo.

Al deslizar el interruptor hacia la izquierda, comenzarás a inflar el globo, que se hará cada vez más grande. Si el globo es demasiado grande, explotará; si es demasiado pequeño, no flotará en el aire. Necesitas decidir cuándo mover el interruptor hacia la derecha para detener el inflado.

.. image:: img/1.15_header.png

Componentes necesarios
---------------------------

En este proyecto, necesitamos los siguientes componentes.

.. image:: img/1.15_component.png

Es definitivamente conveniente comprar un kit completo, aquí está el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ARTÍCULOS EN ESTE KIT
        - ENLACE
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

También puedes comprarlos por separado en los enlaces a continuación.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUCCIÓN DEL COMPONENTE
        - ENLACE DE COMPRA

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_slide_switch`
        - |link_slide_switch_buy|
    *   - :ref:`cpn_capacitor`
        - |link_capacitor_buy|

Construir el circuito
------------------------

.. image:: img/1.15_scratch_fritzing.png

Cargar el código y ver qué pasa
----------------------------------

Carga el archivo de código (``1.15_inflating_the_balloon.sb3``) a Scratch 3.

Al deslizar el interruptor hacia la izquierda, comenzarás a inflar el globo, que se hará cada vez más grande. Si el globo es demasiado grande, explotará; si es demasiado pequeño, no flotará en el aire. Necesitas decidir cuándo mover el interruptor hacia la derecha para detener el inflado.


Consejos sobre sprites
-------------------------

Elimina el sprite Sprite1 anterior, luego agrega el sprite **Balloon1**.

.. image:: img/1.15_slide1.png

En este proyecto se utiliza un efecto de sonido de explosión de globo, veamos cómo se añadió.

Haz clic en la opción **Sonido** en la parte superior, luego haz clic en **Cargar sonido** para subir ``boom.wav`` desde la ruta ``~/raphael-kit/scratch/sound`` a Scratch 3.

.. image:: img/1.15_slide2.png

Consejos sobre los códigos
------------------------------

.. image:: img/1.15_slide3.png
  :width: 500

Este es un bloque de evento, y la condición de activación es que gpio17 esté alto, es decir, que el interruptor esté deslizado hacia la izquierda.

.. image:: img/1.15_slide4.png
  :width: 400

Establece el umbral de tamaño del sprite Balloon1 en 120.

.. image:: img/1.15_slide7.png
  :width: 400

Mueve las coordenadas del sprite Balloon1 a (0,0), que es el centro del área de escenario.

.. image:: img/1.15_slide8.png
  :width: 300

Establece el tamaño del sprite Balloon1 en 50 y muéstralo en el área de escenario.

.. image:: img/1.15_slide5.png

Configura un bucle para inflar el globo; este bucle se detiene cuando el interruptor deslizante se mueve hacia la derecha.

Dentro de este bucle, el tamaño del globo aumenta en 1 cada 0.1s, y si es mayor que ``maxSize``, el globo explotará, en cuyo caso se reproducirá el sonido de explosión y el código se saldrá.

.. image:: img/1.15_slide6.png
  :width: 600

Después de que el último bucle se salga (interruptor deslizante se mueve hacia la derecha), determina la posición del sprite Balloon1 según su tamaño. Si el tamaño del sprite Balloon1 es mayor que 90, se elevará (mueve las coordenadas a (0, 90)), de lo contrario, aterrizará (mueve las coordenadas a (0, -149)).
