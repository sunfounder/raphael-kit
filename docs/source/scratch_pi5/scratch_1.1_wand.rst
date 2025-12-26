.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.1_scratch_pi5:

1.1 Varita mágica
====================

Hoy usaremos LED, Raspberry Pi y Scratch para hacer un juego divertido. Cuando agitemos la varita mágica, el LED parpadeará.

.. image:: img/1.1_header.png

Componentes necesarios
---------------------------------

En este proyecto, necesitamos los siguientes componentes.

.. image:: img/1.1_list.png

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
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_led`
        - |link_led_buy|

Construir el circuito
-------------------------

.. image:: img/1.1_image49.png

Agregar extensión GPIO
--------------------------

Haz clic en el botón **Agregar Extensión** en la esquina inferior izquierda, luego agrega **Raspberry Pi GPIO**, una extensión que usamos para todos nuestros proyectos de Scratch.

.. image:: img/1.1_scratchled1.png
    :align: center

.. image:: img/1.1_scratchled2.png
    :align: center

.. image:: img/1.1_scratchled3.png
    :align: center

Cargar el código y ver qué pasa
-------------------------------------------

Carga el archivo de código desde tu computadora (``~/raphael-kit/scratch/code``) a Scratch 3.

.. image:: img/1.1_scratch_step1.png

.. image:: img/1.1_scratch_step2.png

Después de hacer clic en la varita mágica en el área del escenario, verás que el LED parpadea durante dos segundos.

.. image:: img/1.1_step3.png


Consejos sobre el sprite
----------------------------

Haz clic en **Subir Sprite**.

.. image:: img/1.1_upload_sprite.png

Sube **Wand.png** desde la ruta ``~/raphael-kit/scratch/picture`` a Scratch 3.

.. image:: img/1.1_upload.png

Finalmente, elimina **Sprite1**.

.. image:: img/1.1_delete.png

Consejos sobre los códigos
---------------------------------

.. image:: img/1.1_LED1.png
  :width: 300

Este es un bloque de evento cuya condición de activación es hacer clic en la bandera verde en el escenario. Se requiere un evento de activación al comienzo de todos los códigos, y puedes seleccionar otros eventos de activación en la categoría **Eventos** de la **paleta de bloques**.

.. image:: img/1.1_events.png
  :width: 300

Por ejemplo, ahora podemos cambiar el evento de activación a hacer clic en el sprite.

.. image:: img/1.1_LED2.png
  :width: 300

Este es un bloque con un número determinado de ciclos. Cuando llenamos el número 10, los eventos en el bloque se ejecutarán 10 veces.

.. image:: img/1.1_LED4.png
  :width: 300

Este bloque se usa para pausar el programa durante un período de tiempo en segundos.

.. image:: img/1.1_LED3.png
  :width: 500

Dado que se utiliza el método de nombrado BCM en Scratch, este código está configurando GPIO17 (BCM17) como 0V (nivel bajo). Dado que el cátodo del LED está conectado a GPIO17, el LED se encenderá. Por el contrario, si configuras GPIO (BCM17) como alto, el LED se apagará.
