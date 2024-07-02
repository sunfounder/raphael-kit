.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.3_scratch:

1.3 Tumbler
==================

En este proyecto, haremos un juguete tumbler controlado por un interruptor de inclinación.

.. image:: img/1.3_header.png

Componentes necesarios
------------------------------

En este proyecto, necesitamos los siguientes componentes.

.. image:: img/1.3_component.png

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
    *   - :ref:`cpn_tilt_switch`
        - \-

Construir el circuito
-------------------------

.. image:: img/1.3_fritzing.png

Cargar el código y ver qué pasa
---------------------------------------------

Carga el archivo de código (``1.3_tumbler.sb3``) en Scratch 3.

Cuando el interruptor de inclinación se coloca en posición vertical, el tumbler está de pie. Si lo inclinas, el tumbler también caerá. Colócalo en posición vertical de nuevo, y el tumbler se levantará de nuevo.


Consejos sobre el sprite
------------------------------
Selecciona Sprite1 y haz clic en **Disfraces** en la esquina superior izquierda; sube **tumbler1.png** y **tumbler2.png** desde la ruta ``~/raphael-kit/scratch/picture`` a través del botón **Subir Disfraz**; elimina los 2 disfraces predeterminados y renombra el sprite a **tumbler**.

.. image:: img/1.3_add_tumbler.png

Consejos sobre los códigos
-------------------------------

.. image:: img/1.3_title2.png
  :width: 400

Cuando se hace clic en la bandera verde, el estado inicial de gpio17 se establece en bajo.

.. image:: img/1.3_title4.png
  :width: 400

Cuando el pin17 está en bajo (el interruptor de inclinación está en posición vertical), cambiamos el disfraz del sprite tumbler a tumbler1 (estado vertical).

.. image:: img/1.3_title3.png
  :width: 400

Cuando el pin17 está en alto (interruptor de inclinación inclinado), cambiamos el disfraz del sprite tumbler a tumbler2 (estado inclinado).
