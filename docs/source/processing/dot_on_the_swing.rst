.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _dot_on_the_swing:

Punto en el Columpio
==============================

En este proyecto, se conectan 3 botones: uno para cambiar el tamaño del punto, otro para cambiar la posición y el último para cambiar el color. Si presionas los 3 botones al mismo tiempo, obtendrás un punto que se balancea y tiene un color variable.

.. image:: img/dancing_dot.png

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
    *   - :ref:`cpn_button`
        - |link_button_buy|

**Conexiones**

.. image:: img/circuit_dancing_dot.png

**Esquema**

.. code-block:: arduino

    import processing.io.*;

    // Define an instance of the Dot object
    Dot myDot;

    // Define the pins that will be reading button presses
    int[] pins = { 18, 23, 24 };

    void setup() {
        size(400, 400);
        // Change the color mode of the sketch to HSB
        colorMode(HSB, 360, 100, 100);
        noStroke();

        for (int i = 0; i < pins.length; i++) {
            GPIO.pinMode(pins[i], GPIO.INPUT_PULLUP);
        }

        // Create a Dot in the middle of the screen 
        myDot = new Dot(width / 2, height / 2, 100, 255);
    }

    void draw() {
        background(0); 

        // Modify attributes of the Dot depending on which buttons are pressed
        if (GPIO.digitalRead(pins[0]) == GPIO.LOW) {myDot.setSize();} 
        if (GPIO.digitalRead(pins[1]) == GPIO.LOW) {myDot.setPosition();} 
        if (GPIO.digitalRead(pins[2]) == GPIO.LOW) {myDot.setColor();} 

        // Update the Dot state
        myDot.update();
        // And draw it to the screen
        myDot.show();
    }

    class Dot { 

        float initX;
        float initY;
        float currentX;
        float currentY;
        int positionRange = 60;

        float initSize;
        float currentSize;
        int sizeRange = 50;

        int initColor;
        int currentColor;
        int ColorRange = 80;

        float timer = 0.0;
        float speed = 0.06;

        Dot(float x, float y, float s, int c) {
            initX = x;
            initY = y;
            currentX = x;
            currentY = y;

            initSize = s;
            currentSize = s;

            initColor = c;
            currentColor = c;
        }

        void setSize() {
            currentSize = initSize + sizeRange * sin( timer );
        }

        void setPosition() {
            currentY = initY + positionRange * cos( timer *2);
        }

        void setColor() {
            currentColor = int(initColor + ColorRange * sin( timer ));
        }

        void update() {
            timer += speed;
        }

        void show() {
            fill(currentColor, 100, 100); 
            ellipse(currentX, currentY, currentSize, currentSize);
        }
    }

**¿Cómo funciona?**

En lugar de dibujar el punto directamente, creamos una clase ``Dot`` aquí. 
Luego, declaramos el objeto (en este caso ``myDot``).

Esta es una forma sencilla de dibujar puntos con múltiples propiedades idénticas. 
Por ejemplo, si añadimos tres funciones al punto en este proyecto - cambiar tamaño, cambiar posición y cambiar color - entonces cada punto que declaremos tendrá la misma función. 
Podemos usar el mismo botón para que hagan lo mismo, o podemos usar diferentes botones para controlar cada punto por separado.

Usar **clases** hace que tu boceto sea bonito, poderoso y flexible.

`Clase (programación) - Wikipedia <https://es.wikipedia.org/wiki/Clase_(programaci%C3%B3n)>`_

A continuación, echemos un vistazo más de cerca a la clase ``Dot``.


.. code-block:: arduino

    Dot(float x, float y, float s, int c)

En la declaración, necesita pasar cuatro parámetros, que son los valores de las coordenadas X e Y de la posición, el tamaño y el color (aquí está configurado en el `modo de color HSB <https://es.wikipedia.org/wiki/Modelo_de_color_HSV>`_ ).

Cada parámetro se asignará a 2 conjuntos de valores (valor inicial y valor actual).


.. code-block:: arduino

    float initX;
    float initY;
    float currentX;
    float currentY;
    int positionRange = 60;

    float initSize;
    float currentSize;
    int sizeRange = 50;

    int initColor;
    int currentColor;
    int ColorRange = 80;

Además del valor inicial y el valor actual, también hay un conjunto de valores de rango. No es difícil entender que el valor inicial se usa para determinar el estado inicial del punto (determinado por los parámetros entrantes), mientras que el valor actual cambiará dentro del rango para hacer que el punto se mueva.

Por lo tanto, excepto por el valor de la coordenada X, los valores actuales de los otros tres parámetros se calculan de la siguiente manera:

.. code-block:: arduino

    void setSize() {
        currentSize = initSize + sizeRange * sin( timer );
    }

    void setPosition() {
        currentY = initY + positionRange * cos( timer *2);
    }

    void setColor() {
        currentColor = int(initColor + ColorRange * sin( timer ));
    }


Si estás familiarizado con las funciones trigonométricas, no debería ser difícil entender `seno y coseno <https://es.wikipedia.org/wiki/Seno>`_, que da un cambio periódico suave (de -1 a 1) del valor actual del punto.

También necesitamos agregar una semilla, ``timer``, para la variación periódica. Se añade el valor fijo en el método ``update()`` y se llama en ``draw()``.

.. code-block:: arduino

    void update() {
        timer += speed;
    }

Finalmente, el punto se muestra según el valor actual utilizando el método ``show()``, que también se llama en ``draw()``.

.. code-block:: arduino

    void show() {
        fill(currentColor, 100, 100); 
        ellipse(currentX, currentY, currentSize, currentSize);
    }

**¿Qué más?**

Habiendo dominado el uso de clases, ya puedes dibujar múltiples puntos con las mismas propiedades, así que ¿por qué no intentas hacer algo más genial?
Por ejemplo, ¿qué tal dibujar un sistema binario estable, o hacer un juego 'DUET'?
