.. nota::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_diode:

Diodo
=================


Un diodo es un componente electrónico con dos electrodos. Permite que la corriente fluya en una sola dirección, lo que a menudo se llama la función de "rectificación". Así, un diodo puede considerarse como una versión electrónica de una válvula de retención.

Debido a su conductividad unidireccional, el diodo se utiliza en casi todos los circuitos electrónicos de cierta complejidad. Es uno de los primeros dispositivos semiconductores y tiene una amplia gama de aplicaciones.

Según su uso, se puede clasificar en diodos detectores, diodos rectificadores, diodos limitadores, diodos reguladores de voltaje, etc.

En este kit se incluyen diodos rectificadores y diodos reguladores de voltaje.

**Diodo Rectificador**

.. image:: img/in4007_diode.png
.. image:: img/symbol_rectifier_diode.png
    :width: 200

Un diodo rectificador es un diodo semiconductor, utilizado para rectificar CA (corriente alterna) a CC (corriente continua) usando la aplicación del puente rectificador. La alternativa del diodo rectificador a través de la barrera Schottky es principalmente valorada dentro de la electrónica digital. Este diodo es capaz de conducir valores de corriente que varían desde mA hasta algunos kA y voltajes de hasta algunos kV.

El diseño de los diodos rectificadores se puede hacer con material de silicio y son capaces de conducir altos valores de corriente eléctrica. Estos diodos no son famosos, pero aún se utilizan diodos semiconductores basados en Ge o arseniuro de galio. Los diodos de Ge tienen menor voltaje inverso permisible y menor temperatura de unión permisible. El diodo de Ge tiene una ventaja en comparación con el diodo de Si, que es el bajo valor de voltaje umbral mientras opera en polarización directa.

* `Diodo de propósito general 1N400x - Wikipedia <https://en.wikipedia.org/wiki/1N400x_general-purpose_diode>`_


**Diodo Zener**

Un diodo Zener es un tipo especial de diodo diseñado para permitir de manera confiable que la corriente fluya "hacia atrás" cuando se alcanza un voltaje inverso establecido, conocido como el voltaje Zener.

Este diodo es un dispositivo semiconductor que tiene una resistencia muy alta hasta el voltaje crítico de ruptura inversa. En este punto crítico de ruptura, la resistencia inversa se reduce a un valor muy pequeño, y la corriente aumenta mientras el voltaje permanece constante en esta región de baja resistencia.

.. image:: img/zener_diode.png
.. image:: img/symbol-zener-diode.jpg


* `Diodo Zener - Wikipedia <https://en.wikipedia.org/wiki/Zener_diode>`_

**Ejemplo**

* :ref:`1.3.3_c` (C Project)
* :ref:`1.3.3_py` (Python Project)
