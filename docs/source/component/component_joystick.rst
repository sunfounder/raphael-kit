.. nota::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_joystick:

Módulo Joystick
=======================

.. image:: img/joystick_pic.png
    :align: center
    :width: 600

La idea básica de un joystick es traducir el movimiento de una palanca en información 
electrónica que una computadora puede procesar.

Para comunicar un rango completo de movimiento a la computadora, un joystick necesita medir 
la posición de la palanca en dos ejes: el eje X (de izquierda a derecha) y el eje Y
 (de arriba a abajo). Al igual que en la geometría básica, las coordenadas X-Y determinan 
 exactamente la posición de la palanca.

Para determinar la ubicación de la palanca, el sistema de control del joystick simplemente 
monitorea la posición de cada eje. El diseño convencional de joystick analógico hace esto 
con dos potenciómetros, o resistencias variables.

El joystick también tiene una entrada digital que se activa cuando se presiona hacia abajo.

.. image:: img/joystick318.png
    :align: center
    :width: 600
	
**Ejemplo**

* :ref:`2.1.9_c` (C Project)
* :ref:`3.1.7_c` (C Project)
* :ref:`2.1.9_py` (Python Project)
* :ref:`4.1.13_py` (Python Project)