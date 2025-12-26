.. note::

    Hola, bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.7_scratch_pi5:

1.7 Alcancía
=========================

En este proyecto usaremos un módulo sensor de velocidad, Raspberry Pi y Scratch para hacer una alcancía.

Coloca un trozo de papel en el medio del módulo sensor de velocidad y verás caer una moneda en la alcancía en el escenario.

.. image:: img/1.7_header.png

Componentes necesarios
------------------------------

En este proyecto, necesitamos los siguientes componentes.

.. image:: img/1.7_component.png

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

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_speed_sensor`
        - \-

Construir el circuito
-------------------------

.. image:: img/1.7_fritzing.png

Cargar el código y ver qué pasa
---------------------------------------

Carga el archivo de código (``1.7_piggy_bank.sb3``) en Scratch 3.

Los 2 terminales en el medio del sensor de velocidad, uno envía luz y el otro recibe luz; si pones un trozo de papel en el medio para aislar la transmisión de luz, el sensor de velocidad emitirá un nivel alto. En este punto, Scratch recibe el nivel alto, luego cambia los disfraces del sprite y verás una moneda caer en la alcancía en el escenario.

Consejos sobre el sprite
-----------------------------------

Selecciona Sprite1 y haz clic en **Disfraces** en la esquina superior izquierda; sube **piggybank1.png**, **piggybank2.png** y **piggybank3.png** desde la ruta ``~/raphael-kit/scratch/picture`` mediante el botón **Cargar Disfraz**; elimina los 2 disfraces predeterminados y renombra el sprite a **piggybank**.

.. image:: img/1.7_photoInterrupter1.png

Consejos sobre los códigos
--------------------------------

.. image:: img/1.7_code2.png

Cuando pin17 está bajo (no se han puesto monedas), cambia el disfraz del sprite a **piggybank1**.

.. image:: img/1.7_code3.png

Cuando pin17 está alto (se ha puesto una moneda), cambia el disfraz del sprite a **piggybank2**, y después de 0.5s cambia a **piggybank3**, para que podamos ver una moneda caer en la alcancía en el escenario.
