.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.6_scratch_pi5:

1.6 Florero Desaparecedor
===============================

Ahora hagamos un pequeño truco de magia, no hagas nada y el florero de alguna manera desaparecerá.

.. image:: img/1.6_header.png

Componentes necesarios
-------------------------------------

En este proyecto, necesitamos los siguientes componentes.

.. image:: img/1.6_component.png

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
    *   - :ref:`cpn_reed_switch`
        - |link_reed_switch_buy|

Construir el circuito
-------------------------

.. image:: img/1.6_fritzing.png

Cargar el código y ver qué pasa
---------------------------------------

Carga el archivo de código (``1.6_vanishing_vase.sb3``) en Scratch 3.

Cuando uses un imán cerca del módulo del interruptor de láminas, aparecerá un florero en el escenario, quita el imán y el florero desaparecerá.

Consejos sobre el sprite
-------------------------------

Selecciona Sprite1 y haz clic en **Disfraces** en la esquina superior izquierda; sube **desk1.png** y **desk2.png** desde la ruta ``~/raphael-kit/scratch/picture`` mediante el botón **Cargar Disfraz**; elimina los 2 disfraces predeterminados y renombra el sprite a **desk**.

.. image:: img/1.6_vase.png

Consejos sobre los códigos
---------------------------------

.. image:: img/1.6_reed2.png
  :width: 400

Cuando el imán está cerca del módulo del interruptor de láminas, gpio17 está en bajo, y el disfraz del sprite **desk** se cambia a **desk1** (el florero sigue en el escritorio).

.. image:: img/1.6_reed3.png
  :width: 400

Después de quitar el imán, gpio17 está en alto, en este momento el disfraz del sprite **desk** se cambia a **desk2** (solo un escritorio).
