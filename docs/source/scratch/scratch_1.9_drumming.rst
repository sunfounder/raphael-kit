.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.9_scratch:

1.9 Tambores
================

En este proyecto, tocamos el tambor con un módulo de interruptor táctil.

.. image:: img/1.9_header.png

Componentes necesarios
------------------------------

En este proyecto, necesitamos los siguientes componentes. 

.. image:: img/1.9_component.png

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
    *   - :ref:`cpn_touch_switch`
        - |link_touch_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-

Construir el circuito
------------------------

.. image:: img/1.9_fritzing.png

Cargar el código y ver qué pasa
---------------------------------------

Carga el archivo de código (``1.9_drumming.sb3``) en Scratch 3.

Cuando toques el módulo de interruptor táctil, escucharás el sonido de tambores proveniente del altavoz.

Consejos sobre el sprite
--------------------------------

Elimina el sprite predeterminado, luego busca el sprite **Drum-snare** y agrégalo, cambiando el tamaño a 200.

.. image:: img/1.9_touch1.png

Scratch tiene una extensión de **Música** para tocar instrumentos y tambores, agrégala ahora a través del botón **Agregar Extensión**.

.. image:: img/1.9_touch2.png

Consejos sobre los códigos
--------------------------------

.. image:: img/1.9_touch3.png
  :width: 400

Cuando pin17 está bajo (no se ha tocado el módulo de interruptor táctil), cambia el disfraz del sprite **Drum-snare** a **drum-snare-a**.

.. image:: img/1.9_touch4.png
  :width: 600

Cuando tocas el módulo de interruptor táctil, gpio17 está bajo. En ese momento, el disfraz del sprite **Drum-snare** se cambia a **drum-snare-b** y se reproduce el sonido del tambor en el altavoz.
