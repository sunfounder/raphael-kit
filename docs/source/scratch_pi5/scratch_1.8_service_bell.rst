.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.8_scratch_pi5:

1.8 Timbre de Servicio
=============================

Hoy utilizaremos un Micro Interruptor, altavoces, un módulo amplificador de audio, Raspberry Pi y Scratch para hacer un timbre de servicio.

Toca el Micro Interruptor para hacer sonar el timbre de servicio.

.. image:: img/1.8_header.png

Componentes necesarios
---------------------------------

En este proyecto, necesitamos los siguientes componentes. 

.. image:: img/1.8_component.png

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
    *   - :ref:`cpn_micro_switch`
        - \-
    *   - :ref:`cpn_capacitor`
        - |link_capacitor_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-

Construir el circuito
---------------------------

.. image:: img/1.8_fritzing.png


Cargar el código y ver qué pasa
---------------------------------------------

Carga el archivo de código (``1.8_service_bell.sb3``) en Scratch 3.

Presiona el micro interruptor y el timbre de servicio sonará una vez.

.. note::

  Si tu Raspberry Pi está conectada a una pantalla con altavoces, es posible que no se escuche el sonido desde este altavoz externo. Consulta :ref:`change_audio_output` para la solución.

  Además, si deseas ajustar el nivel de volumen, consulta :ref:`adjust_volume`.

Consejos sobre el sprite
-------------------------------

Selecciona Sprite1 y haz clic en **Disfraces** en la esquina superior izquierda; sube **bell1.png** y **bell2.png** desde la ruta ``~/raphael-kit/scratch/picture`` mediante el botón **Cargar Disfraz**; elimina los 2 disfraces predeterminados y renombra el sprite a **bell**.

.. image:: img/1.8_travel1.png

En la opción **Sonidos**, sube el archivo ``bell.wav`` desde la ruta ``~/raphael-kit/scratch/sound`` a Scratch 3.

.. image:: img/1.8_travel2.png

Consejos sobre los códigos
-------------------------------------

.. image:: img/1.8_travel3.png
  :width: 400

Cuando pin17 está alto (el micro interruptor no está presionado), cambia el disfraz del sprite **bell** a **bell1** (estado liberado).

.. image:: img/1.8_travel4.png
  :width: 400

Presiona el micro interruptor, gpio17 está en nivel bajo. En ese momento, cambia el disfraz del sprite **bell** a **bell2** (estado presionado) y reproduce un efecto de sonido a través del altavoz.
