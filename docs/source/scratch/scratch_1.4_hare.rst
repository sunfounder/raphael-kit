.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.4_scratch:

1.4 Liebre
================

Hoy utilizaremos un botón, Raspberry Pi y Scratch para crear una liebre con varios cambios.

Cuando presionamos el primer botón, la liebre en el área del escenario cambiará el color de su cuerpo; cuando presionamos el segundo botón, la liebre cambiará el tamaño de su cuerpo; cuando presionamos el tercer botón, la liebre dará un paso adelante.

.. image:: img/1.4_header.png

Componentes necesarios
---------------------------------

En este proyecto, necesitamos los siguientes componentes.

.. image:: img/1.4_list.png

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
    *   - :ref:`cpn_button`
        - |link_button_buy|

Construir el circuito
-------------------------

.. image:: img/1.4_scratch_button.png

Cargar el código y ver qué pasa
-------------------------------------------

Carga el archivo de código (``1.4_hare.sb3``) en Scratch 3.

Ahora puedes intentar presionar cada uno de los 3 botones para ver cómo cambia la Liebre en el escenario.


Consejos sobre el sprite
-----------------------------

Haz clic en el botón **Elegir un sprite** en la esquina inferior derecha del área del sprite, ingresa **Hare** en el cuadro de búsqueda y luego haz clic para agregarlo.

.. image:: img/1.4_button1.png

Elimina Sprite1.

.. image:: img/1.4_button2.png


Consejos sobre los códigos
------------------------------

.. image:: img/1.4_button3.png
  :width: 400

Este es un bloque de evento que se activa cuando el nivel de GPIO17 es alto, lo que significa que el botón está presionado en ese momento.

.. image:: img/1.4_button4.png
  :width: 400

Este es un bloque para cambiar el color de **Hare**, el rango del valor es 0 ~ 199, más allá de 199 volverá a cambiar desde 0 nuevamente.

.. image:: img/1.4_button5.png
  :width: 250

Este es un bloque utilizado para cambiar el tamaño del sprite, cuanto mayor sea el valor, mayor será el sprite.

.. note::
  El sprite tampoco es infinitamente grande, y su tamaño máximo está relacionado con el tamaño de la imagen original.

.. image:: img/1.4_button6.png
  :width: 200

Este es un bloque que cambia los disfraces del sprite, y cuando el disfraz de **Hare** sigue cambiando, realiza una serie de acciones coherentes. Por ejemplo, en este proyecto, hace que **Hare** dé un paso adelante.
