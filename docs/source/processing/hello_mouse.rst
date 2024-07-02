.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _hello_mouse:

Hola Ratón
====================

En este proyecto, tu ratón seguirá disparando líneas hacia un punto; mueve el ratón y dibujarás una línea única de estrellas. Presiona el ratón para reiniciar el dibujo.

.. image:: img/hello_mouse1.png

**Boceto**

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

    void mousePressed() {
        pointX=mouseX;
        pointY=mouseY;
        background(192, 16, 18);
    }

**¿Cómo funciona?**

El proyecto anterior consistía en dibujar una imagen única sin ninguna animación o interacción.

Si queremos hacer un boceto interactivo, necesitamos agregar las funciones ``setup()`` y ``draw()`` (estas son funciones integradas que se llaman automáticamente) para construir el marco.

* ``setup()``: Se ejecuta solo una vez al inicio del boceto.
* ``draw()``: Se ejecuta repetidamente, donde usualmente añadimos el boceto para dibujar la animación.

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

Este boceto ya funciona sin problemas como un boceto interactivo.

A continuación, puedes agregar un evento de clic del ratón. Este evento se puede implementar con la función ``mousePressed()``, donde añadimos declaraciones para actualizar el punto objetivo y limpiar la pantalla.

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

    void mousePressed() {
        pointX=mouseX;
        pointY=mouseY;
        background(192, 16, 18);
    }

Para más detalles, consulta `Processing Reference <https://processing.org/reference/>`_.
