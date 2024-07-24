.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.2_scratch_pi5:

1.2 Bolas de colores
========================

Hacer clic en las diferentes bolas de colores en el área del escenario hará que el LED RGB se ilumine en distintos colores.

.. image:: img/1.2_header.png

Componentes necesarios
---------------------------------

En este proyecto, necesitamos los siguientes componentes.

.. image:: img/1.2_list.png

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
    *   - :ref:`cpn_rgb_led`
        - |link_rgb_led_buy|

Construir el circuito
-----------------------

.. image:: img/1.2_image61.png


Cargar el código y ver qué pasa
-------------------------------------------

Después de cargar el archivo de código (``1.2_colorful_balls.sb3``) en Scratch 3, el LED RGB se iluminará en amarillo, azul, rojo, verde o morado respectivamente cuando hagas clic en la bola correspondiente.


Consejos sobre los sprites
------------------------------

Elimina el sprite predeterminado, luego elige el sprite **Ball**.

.. image:: img/1.2_ball.png

Y duplícalo 5 veces.

.. image:: img/1.2_duplicate_ball.png

Elige diferentes disfraces para estos 5 sprites **Ball** y muévelos a las posiciones correspondientes.

.. image:: img/1.2_rgb1.png

Consejos sobre los códigos
-------------------------------

Antes de entender el código, necesitamos entender el `modelo de color RGB <https://es.wikipedia.org/wiki/Modelo_de_color_RGB>`_.

El modelo de color RGB es un modelo de color aditivo en el cual la luz roja, verde y azul se combinan de diversas maneras para reproducir una amplia gama de colores.

Mezcla de colores aditiva: al añadir rojo a verde se obtiene amarillo; al añadir verde a azul se obtiene cian; al añadir azul a rojo se obtiene magenta; al añadir los tres colores primarios se obtiene blanco.

.. image:: img/1.2_rgb_addition.png
  :width: 400

Un LED RGB es una combinación de 3 LEDs (LED rojo, LED verde, LED azul) en un solo paquete, y puedes producir casi cualquier color combinando esos tres colores.
Tiene 4 pines, uno de los cuales es GND, y los otros 3 pines controlan los 3 LEDs respectivamente.

Entonces, el código para hacer que el LED RGB se ilumine en amarillo es el siguiente.

.. image:: img/1.2_rgb3.png

Cuando se hace clic en el sprite Ball (bola amarilla), configuramos gpio17 en alto (LED rojo encendido), gpio18 en alto (LED verde encendido) y gpio27 en bajo (LED azul apagado) para que el LED RGB se ilumine en amarillo.

Puedes escribir códigos para otros sprites de la misma manera para hacer que los LEDs RGB se iluminen en los colores correspondientes.
