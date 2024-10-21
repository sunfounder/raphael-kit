.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_keypad:

Teclado
========================

Un teclado es una matriz rectangular de 12 o 16 botones OFF-(ON).
Sus contactos se acceden a través de un conector adecuado para conexión con un cable de cinta o inserción en una placa de circuito impreso.
En algunos teclados, cada botón se conecta con un contacto separado en el conector, mientras que todos los botones comparten una tierra común.

.. image:: img/keypad314.png

Con más frecuencia, los botones están codificados en matriz, lo que significa que cada uno de ellos conecta un par único de conductores en una matriz.
Esta configuración es adecuada para sondeo por un microcontrolador, que puede ser programado para enviar un pulso de salida a cada uno de los cuatro cables horizontales por turno.
Durante cada pulso, verifica los cuatro cables verticales restantes en secuencia, para determinar cuál, si alguno, está llevando una señal.
Se deben agregar resistencias pullup o pulldown a los cables de entrada para evitar que las entradas del microcontrolador se comporten de manera impredecible cuando no hay señal presente.

**Ejemplo**

* :ref:`2.1.8_c` (C Project)
* :ref:`3.1.8_c` (C Project)
* :ref:`3.1.11_c` (C Project)
* :ref:`2.1.8_py` (Python Project)
* :ref:`4.1.14_py` (Python Project)
* :ref:`4.1.17_py` (Python Project)