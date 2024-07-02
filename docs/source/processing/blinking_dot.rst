.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _blinking_dot:

Punto Parpadeante
=====================

En este proyecto, dibujaremos un punto en Processing que parpadea sincrónicamente con el LED. Por favor, monta el circuito como se muestra en el diagrama y ejecuta el sketch.

.. image:: img/blinking_dot.png
.. image:: img/clickable_dot_on.png

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

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_led`
        - |link_led_buy|

**Conexiones**

.. image:: img/image49.png

**Sketch**

.. code-block:: Arduino

    import processing.io.*;
    int ledPin = 17; 
    boolean state = true; 

    void setup() {
        size(100, 100);
        frameRate(2); //set frame rate
        GPIO.pinMode(ledPin, GPIO.OUTPUT); //set the ledPin to output mode 
    }

    void draw() {
        state = !state;
        if (state==true) {
            GPIO.digitalWrite(ledPin, GPIO.LOW); //led on 
            fill(255, 0, 0); //set the fill color of led on
        } else {
            GPIO.digitalWrite(ledPin, GPIO.HIGH); //led off
            fill(155); //set the fill color of led off
        } 
        ellipse(width/2, height/2, width*0.75, height*0.75);
    }

**¿Cómo funciona?**

Al inicio del sketch, necesitas importar la biblioteca de funciones GPIO de Processing con ``import processing.io.*;``, lo cual es indispensable para los experimentos de circuito.

La **tasa de fotogramas** es la frecuencia con la que aparecen los bitmaps en la pantalla, expresada en hertzios (Hz). En otras palabras, es la frecuencia con la que se llama a la función ``draw()``. En ``setup()``, configurar la **tasa de fotogramas** a 2 llamará a ``draw()`` cada 0.5s.

Cada llamada a la función ``draw()`` invierte el valor de ``state`` y lo evalúa. Si el valor es ``true``, el LED se enciende y el pincel se llena de rojo; si no, el LED se apaga y el pincel se llena de gris.

Después de completar la evaluación, usa la función ``ellipse()`` para dibujar un círculo. Cabe destacar que ``width`` y ``height`` son variables del sistema utilizadas para almacenar el ancho y la altura de la ventana de visualización.

Hay otros dos puntos importantes a tener en cuenta. Al usar GPIOs, debes usar la función ``GPIO.pinMode()`` para configurar el estado de ENTRADA/SALIDA del pin, y luego usar la función ``GPIO.digitalWrite()`` para asignar un valor (ALTO/BAJO) al pin.

.. note::

    Por favor, evita usar ``delay()`` en ``draw()`` porque afectará la actualización de la ventana de visualización.
