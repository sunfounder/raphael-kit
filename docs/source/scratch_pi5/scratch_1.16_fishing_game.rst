.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.16_scratch_pi5:

1.16 Juego de Pesca
==========================

Hoy, haremos un juego de pesca.

Observa el agua en el área del escenario y si ves un pez en el anzuelo, recuerda inclinar el interruptor para atraparlo.

.. image:: img/1.16_header.png

Componentes Necesarios
----------------------------

En este proyecto, necesitamos los siguientes componentes.

.. image:: img/1.16_component.png

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

Construir el Circuito
-------------------------

.. image:: img/1.16_fritzing.png

Cargar el Código y Ver Qué Pasa
-----------------------------------

Carga el archivo de código (``1.16_fishing_game.sb3``) a Scratch 3.

Verás a un niño pescando, después de un tiempo cuando el agua se mueva, puedes agitar el interruptor de inclinación para atrapar el pez.
Recuerda, si no mantienes agitado el interruptor, el pez escapará.

Consejos sobre el Sprite
---------------------------

Selecciona Sprite1, haz clic en **Disfraces** en la esquina superior izquierda; sube 6 imágenes (**fish1** a **fish6**) desde la ruta ``~/raphael-kit/scratch/picture`` a través del botón **Cargar Disfraz**; elimina los 2 disfraces predeterminados y renombra el sprite a **fish**.

.. image:: img/1.16_upload_fish.png

Consejos sobre los Códigos
------------------------------

.. image:: img/1.16_fish2.png
  :width: 400

Configura el disfraz inicial del sprite **fish** en **fish1** y asigna el valor de **fish_status** a 0 (cuando **fish_status=0**, significa que el pez no está enganchado, cuando **fish_status=1**, significa que el pez está enganchado).

.. image:: img/1.16_fish3.png
  :width: 400

Cuando **fish_status=0**, es decir, el pez aún no está enganchado, comienza el juego de pesca. Espera un tiempo aleatorio de 0 a 10 segundos, luego asigna **fish_status** a 1, lo que significa que el pez está enganchado, y envía un mensaje "El pez está mordiendo".

.. note::

  El propósito del bloque de transmisión es enviar un mensaje a otros bloques de código u otros sprites. El mensaje puede ser una solicitud o un comando.

.. image:: img/1.16_fish4.png
  :width: 400

Cuando se recibe el mensaje "El pez está mordiendo", deja que el sprite del pez cambie entre los disfraces **fish2** y **fish3** para que podamos ver al pez morder.

.. image:: img/1.16_fish5.png
  :width: 400

Después de cambiar el disfraz, si el juego no ha terminado, significa que el pez se soltó y se fue, por lo que cambiaremos el disfraz del sprite **fish** a **fish6** (estado de pez escapado).

.. image:: img/1.16_fish6.png
  :width: 400

Cuando gpio17 está alto (el interruptor de inclinación está inclinado), significa que la caña de pescar está siendo levantada. En este momento, se juzga el valor de fish_status. Si es 1, significa que la caña de pescar se levantó cuando el pez estaba enganchado y se cambia al disfraz fish4 (pez atrapado). Por el contrario, significa que la caña de pescar se levantó cuando el pez no estaba enganchado y se cambia al disfraz fish5 (nada atrapado).
