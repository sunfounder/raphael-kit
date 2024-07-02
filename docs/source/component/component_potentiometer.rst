.. nota::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_potentiometer:

Potenciómetro
=================

.. image:: img/potentiometer.png
    :align: center
    :width: 150

El potenciómetro es un componente resistivo con 3 terminales y su valor de resistencia puede ajustarse según una variación regular.

Los potenciómetros vienen en varias formas, tamaños y valores, pero todos tienen las siguientes características en común:

* Tienen tres terminales (o puntos de conexión).
* Tienen una perilla, tornillo o deslizador que se puede mover para variar la resistencia entre el terminal central y cualquiera de los terminales exteriores.
* La resistencia entre el terminal central y cualquiera de los terminales exteriores varía de 0 Ω a la resistencia máxima del potenciómetro a medida que se mueve la perilla, tornillo o deslizador.

Aquí está el símbolo del circuito del potenciómetro.

.. image:: img/potentiometer_symbol.png
    :align: center
    :width: 400

Las funciones del potenciómetro en el circuito son las siguientes:

#. Actuar como un divisor de voltaje

    El potenciómetro es un resistor ajustable de forma continua. Cuando ajustas el eje o el mango deslizante del potenciómetro, el contacto móvil se deslizará sobre el resistor. En este punto, se puede obtener un voltaje de salida dependiendo del voltaje aplicado al potenciómetro y del ángulo al que se haya girado el brazo móvil o el recorrido que haya realizado.

#. Actuar como un reóstato

    Cuando el potenciómetro se usa como un reóstato, conecta el pin central y uno de los otros 2 pines en el circuito. Así, se puede obtener un valor de resistencia suavemente y continuamente cambiado dentro del recorrido del contacto móvil.

#. Actuar como un controlador de corriente

    Cuando el potenciómetro actúa como un controlador de corriente, el terminal de contacto deslizante debe estar conectado como uno de los terminales de salida.

Si deseas saber más sobre el potenciómetro, consulta: `Potenciómetro - Wikipedia <https://es.wikipedia.org/wiki/Potenciómetro>`_

**Ejemplo**

* :ref:`2.1.7_c` (C Project)
* :ref:`2.1.7_py` (Python Project)


