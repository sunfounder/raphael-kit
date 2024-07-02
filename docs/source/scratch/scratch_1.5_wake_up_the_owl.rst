.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.5_scratch:

1.5 Despierta al Búho
==============================

Hoy vamos a jugar a un juego para despertar al búho.

Cuando alguien se acerque al módulo sensor PIR, el búho se despertará de su sueño.

.. image:: img/1.5_header.png

Componentes necesarios
----------------------------------------

En este proyecto, necesitamos los siguientes componentes.

.. image:: img/1.5_component.png

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
    *   - :ref:`cpn_pir`
        - \-

Construir el circuito
----------------------------

.. image:: img/1.5_fritzing.png

Hay dos potenciómetros en el módulo PIR: uno es para ajustar la sensibilidad y el otro es para ajustar la distancia de detección. Para que el módulo PIR funcione mejor, necesitas girar ambos en sentido contrario a las agujas del reloj hasta el final.

.. image:: ../img/PIR_TTE.png
    :width: 400
    :align: center

Cargar el código y ver qué pasa
------------------------------------------

Carga el archivo de código (``1.5_wake_up_the_owl.sb3``) en Scratch 3.

Cuando te acerques al módulo sensor PIR, verás que el búho en el área del escenario abre sus alas y se despierta, y cuando te alejas, el búho volverá a dormir.


Consejos sobre el sprite
-----------------------------

Selecciona Sprite1 y haz clic en **Disfraces** en la esquina superior izquierda; sube **owl1.png** y **owl2.png** desde la ruta ``~/raphael-kit/scratch/picture`` mediante el botón **Cargar Disfraz**; elimina los 2 disfraces predeterminados y renombra el sprite a **búho**.

.. image:: img/1.5_pir1.png

Consejos sobre los códigos
--------------------------------

.. image:: img/1.3_title2.png

Cuando se hace clic en la bandera verde, el estado inicial de gpio17 se establece en bajo.

.. image:: img/1.5_owl1.png
  :width: 400

Cuando pin17 está en bajo (nadie se está acercando), cambia el disfraz del sprite búho a owl1 (estado durmiendo).

.. image:: img/1.5_owl2.png
  :width: 400

Cuando pin17 está en alto (alguien se está acercando), cambiamos el disfraz del búho a owl2 (estado despierto).
