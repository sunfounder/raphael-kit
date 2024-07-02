.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más profundamente en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_speed_sensor:

Módulo Sensor de Velocidad
=================================

.. image:: img/speed_sensor1.png
    :width: 300
    :align: center

El sensor de velocidad consta de dos partes: un transmisor y un receptor. El transmisor emite luz, que luego entra en el receptor.

Si el haz de luz entre el emisor y el receptor es interrumpido por un obstáculo, el receptor no detectará la luz incidente, entonces el pin D0 emitirá un nivel bajo.

.. note::
    El pin A0 en este módulo está vacío y no hay circuito.

.. image:: img/speed_sensor2.png

**Ejemplo**

* :ref:`2.2.6_c` (C Project)
* :ref:`2.2.6_py` (Python Project)
* :ref:`1.7_scratch` (Scratch Project)