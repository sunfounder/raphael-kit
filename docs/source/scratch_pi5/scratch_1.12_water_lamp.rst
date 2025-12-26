.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.12_scratch_pi5:

1.12 Lámpara de agua
====================

Hoy usaremos un gráfico de barras LED, Raspberry Pi y Scratch para hacer una lámpara de agua.

El gráfico de barras LED se encenderá en orden con la dirección de las flechas en el escenario.

.. image:: img/1.12_header.png

Componentes necesarios
----------------------

En este proyecto, necesitamos los siguientes componentes.

.. image:: img/1.12_list.png

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
    *   - :ref:`cpn_bar_graph`
        - \-

Construir el circuito
---------------------

.. image:: img/1.12_image66.png

Cargar el código y ver qué pasa
-------------------------------

Carga el archivo de código (``1.12_water_lamp.sb3``) desde tu computadora a Scratch 3.

Al hacer clic en **Arrow1**, los LED en la barra LED se encienden en secuencia de izquierda a derecha (uno a la vez) y luego se apagan. Haz clic en **Arrow2** y los LED se encenderán en orden inverso.

Consejos sobre sprites
----------------------

Elimina el sprite predeterminado y elige el sprite **Arrow1**.

.. image:: img/1.12_graph1.png

Aquí necesitaremos 2 sprites **Arrow1**, lo cual se puede hacer con el botón de duplicar.

.. image:: img/1.12_scratch_duplicate.png

Haz clic en el sprite **Arrow2** y cambia la dirección de la flecha seleccionando el disfraz 2.

.. image:: img/1.12_graph2.png

Ahora hagamos una variable.

.. image:: img/1.12_graph3.png

Nómbrala **num**.

.. image:: img/1.12_graph4.png

Sigue el mismo método para crear una lista llamada **led**.

.. image:: img/1.12_graph6.png

Después de agregarla, deberías ver la variable **num** y la lista **led** en el área del escenario.

Haz clic en **+** para agregar 10 elementos a la lista e ingresa los números de pines en orden (17,18,27,22,23,24,25,2,3,8).

.. image:: img/1.12_graph7.png

Consejos sobre los códigos
--------------------------

.. image:: img/1.12_graph10.png
  :width: 300

Este es un bloque de evento que se activa cuando se hace clic en el sprite actual.

.. image:: img/1.12_graph8.png
  :width: 300

El valor inicial de la variable **num** determina qué LED se enciende primero.

.. image:: img/1.12_graph9.png

Configura el pin correspondiente a **num** en la lista led a bajo para encender el LED y luego configura el pin correspondiente a **num-1** a alto para apagar el LED anterior.
