.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.11_scratch_pi5:

1.11 Repelente de langostas
================================


Hoy usaremos un módulo de evasión de obstáculos por IR, Raspberry Pi y Scratch para hacer un juego de repeler langostas.

Coloca tu mano frente al módulo de evasión de obstáculos y verás a las langostas huyendo.

.. image:: img/1.11_header.png

Componentes necesarios
-----------------------------

En este proyecto, necesitamos los siguientes componentes.

.. image:: img/1.11_component.png

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
    *   - :ref:`cpn_avoid_module`
        - |link_obstacle_avoidance_buy|

Construir el circuito
---------------------------

.. image:: img/1.11_fritzing.png
    :width: 700
    :align: center

Cargar el código y ver qué pasa
------------------------------------------

Carga el archivo de código (``1.11_repelling_locusts.sb3``) en Scratch 3.

Coloca tu mano frente al módulo de evasión de obstáculos y verás a las langostas huyendo.


Consejos sobre el sprite
---------------------------

Selecciona Sprite1 y haz clic en **Disfraces** en la esquina superior izquierda; sube **locust1.png**, **locust2.png** y **locust3.png** desde la ruta ``~/raphael-kit/scratch/picture`` a través del botón **Cargar Disfraz**; elimina los 2 disfraces predeterminados y renombra el sprite a **locust**.

.. image:: img/1.11_ir1.png

Consejos sobre los códigos
------------------------------------

.. image:: img/1.11_ir2.png
  :width: 400

Cuando el módulo de evasión de obstáculos por IR no detecta un obstáculo (no hay mano frente a la sonda), el gpio está en alto.

.. image:: img/1.11_ir3.png
  :width: 400

Cuando gpio17 está en alto (no hay obstáculos frente al módulo de evasión de obstáculos por IR), cambia el disfraz del sprite de langosta a locust1 (las langostas se reúnen en el trigo). Por el contrario, cuando gpio17 está en bajo (coloca tu mano frente al módulo de evasión de obstáculos por IR), cambia el disfraz del sprite de langosta a locust2 (expulsar langostas), luego cambia el disfraz del sprite de langosta a locust3 (las langostas están completamente expulsadas) después de 0.5s.
