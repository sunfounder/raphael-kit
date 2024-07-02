.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más profundamente en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_servo:

Servo
===========

.. image:: img/servo.png
    :align: center

Un servo generalmente está compuesto por las siguientes partes: carcasa, eje, sistema de engranajes, potenciómetro, motor de corriente continua y placa integrada.

Funciona de la siguiente manera: El microcontrolador envía señales PWM al servo, y luego la placa integrada en el servo recibe las señales a través del pin de señal y controla el motor interno para que gire. Como resultado, el motor impulsa el sistema de engranajes y luego mueve el eje después de la desaceleración. El eje y el potenciómetro del servo están conectados entre sí. Cuando el eje gira, impulsa el potenciómetro, por lo que el potenciómetro envía una señal de voltaje a la placa integrada. Luego, la placa determina la dirección y la velocidad de rotación en función de la posición actual, por lo que puede detenerse exactamente en la posición definida y mantenerse allí.

.. image:: img/servo_internal.png
    :align: center

El ángulo está determinado por la duración de un pulso que se aplica al cable de control. Esto se llama Modulación por Ancho de Pulso (PWM). El servo espera recibir un pulso cada 20 ms. La duración del pulso determinará cuánto gira el motor. Por ejemplo, un pulso de 1.5 ms hará que el motor gire a la posición de 90 grados (posición neutral).
Cuando se envía un pulso a un servo que es menor de 1.5 ms, el servo gira a una posición y mantiene su eje de salida un número de grados en sentido antihorario desde el punto neutral. Cuando el pulso es más ancho que 1.5 ms, ocurre lo contrario. El ancho mínimo y el ancho máximo del pulso que hará que el servo gire a una posición válida son funciones de cada servo. Generalmente, el pulso mínimo será de aproximadamente 0.5 ms de ancho y el máximo será de 2.5 ms de ancho.

.. image:: img/servo_duty.png
    :width: 600
    :align: center

**Ejemplo**

* :ref:`1.3.2_c` (C Project)
* :ref:`3.1.2_c` (C Project)
* :ref:`1.3.2_py` (Python Project)
* :ref:`4.1.8_py` (Python Project)


