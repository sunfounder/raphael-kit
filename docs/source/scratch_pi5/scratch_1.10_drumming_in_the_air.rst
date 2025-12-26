.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.10_scratch_pi5:

1.10 Tocar tambores en el aire
====================================

Hoy aprenderemos a usar la cámara Raspberry Pi. Scratch tiene un módulo de expansión para la detección de video que enciende la cámara en Scratch y detecta el movimiento de objetos en el escenario.

.. image:: img/1.10_header.png

Componentes necesarios
-------------------------------

En este proyecto, necesitamos los siguientes componentes. 

.. image:: img/1.10_list.png

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
    *   - :ref:`cpn_audio_speaker`
        - \-
    *   - :ref:`cpn_camera_module`
        - |link_camera_buy|

Construir el circuito
-------------------------

.. image:: img/1.10_fritzing_speaker.png

.. image:: img/1.10_camera.png

.. note::
  
  Necesitas referirte a :ref:`cpn_camera_module` para conectar el módulo de cámara y habilitar la interfaz de cámara de Raspberry Pi.


Cargar el código y ver qué pasa
------------------------------------

Carga el archivo de código (``1.10_drumming_in_the_air.sb3``) en Scratch 3.

Haz clic en la bandera verde para iniciar el juego, coloca tu mano frente al módulo de cámara y Scratch 3 reproducirá sonidos de instrumentos cuando tu mano toque un instrumento en el área del escenario.

.. note::

  Para una mejor experiencia de juego, por favor intenta jugar en un fondo blanco para evitar interferencias con la cámara de otros objetos.

Consejos sobre el sprite
--------------------------

Primero elimina los sprites predeterminados, luego encuentra el sprite **Drum-cymbal** y el sprite **Drum-snare** y agrégalos.

.. image:: img/1.10_camera1.png

Haz clic en el ícono **Agregar Extensión** en la parte inferior izquierda de Scratch y añade las extensiones de **Música** y **Detección de Video**.

.. image:: img/1.10_scratch.png

.. image:: img/1.10_scratch2.png

Consejos sobre los códigos
-------------------------------

.. image:: img/1.10_camera3.png

Cuando se hace clic en la bandera verde, se mantiene en un ciclo detectando si nuestra mano se mueve sobre el sprite **Drum-cymbal** por más de 60. Si es así, se asume que nuestra mano tocó el sprite, en ese momento se reproduce el sonido del instrumento Open Hi-Hat.

.. note::

  La magnitud del movimiento se refiere al cambio en las coordenadas en el área del escenario, que se calcula con respecto a la cantidad de cambio en las coordenadas del objetivo de detección en el área del escenario.

.. image:: img/1.10_camera4.png

De manera similar, si se detecta que el movimiento de nuestra mano sobre el sprite **Drum-snare** es mayor de 60, se considera que nuestra mano tocó el sprite y se reproduce el sonido del instrumento de la caja.

