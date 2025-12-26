.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _clickable_color_blocks:

Bloques de Color Clicables
===============================

Ya hemos intentado dibujar un punto clicable para controlar el LED, así que vamos un paso más allá y dibujemos 3 cuadrados de colores para ajustar los colores RGB.

.. image:: img/colorful_square.png

**Componentes Necesarios**

En este proyecto, necesitamos los siguientes componentes.

Es definitivamente conveniente comprar un kit completo, aquí está el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ELEMENTOS EN ESTE KIT
        - ENLACE
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

También puedes comprarlos por separado en los enlaces a continuación.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUCCIÓN AL COMPONENTE
        - ENLACE DE COMPRA

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_rgb_led`
        - |link_rgb_led_buy|

**Conexiones**

.. image:: img/image61.png

**Sketch**

.. code-block:: arduino

    import processing.io.*; // use the GPIO library

    int[] pins = { 17, 18, 27 };

    void setup() {
        for (int i = 0; i < pins.length; i++) {
            GPIO.pinMode(pins[i], GPIO.OUTPUT);
        }
        size(300, 100);
        background(255);
    }

    void draw() {
        fill(255, 0, 0);
        rect(0, 0, width/3, height);

        fill(0,255,0);
        rect(width/3, 0, 2*width/3, height);

        fill(0,0,255);
        rect(2*width/3, 0, width, height);
    }

    void mouseClicked() {
        for (int i = 0; i < pins.length; i++) {
            GPIO.digitalWrite(pins[i],GPIO.LOW);
        }
        if (mouseX<width/3){
            GPIO.digitalWrite(pins[0],GPIO.HIGH);
        }else if (mouseX>width/3&&mouseX<2*width/3){
            GPIO.digitalWrite(pins[1],GPIO.HIGH);
        }else if (mouseX>2*width/3){
            GPIO.digitalWrite(pins[2],GPIO.HIGH);
        }        
    }

**¿Cómo funciona?**

Este proyecto tiene mucho en común con :ref:`clickable_dot`, excepto que refina las condiciones para determinar el evento de clic del ratón.

Primero dibuja tres bloques de color en ``draw()``, luego obtiene qué bloque de color fue clicado basado en el valor de mouseX (la coordenada del eje X del ratón), y finalmente hace que el LED RGB se ilumine con el color correspondiente.

**¿Qué más?**

Basándonos en la adición de luz, podemos hacer que el LED RGB muestre siete colores: agregar rojo al verde produce amarillo; agregar los tres colores primarios juntos produce blanco.
Ahora puedes probarlo por ti mismo.