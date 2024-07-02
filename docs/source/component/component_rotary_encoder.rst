.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más profundamente en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_rotary_encoder:

Módulo de Codificador Rotativo
==================================

.. image:: img/rotary_encoder_pic.png
    :width: 300
    :align: center

Un codificador rotativo es un sensor de posición que convierte la rotación de una perilla en una señal de salida, indicando la dirección en la que se gira la perilla.

Los codificadores rotativos son versiones digitales de los potenciómetros, ofreciendo una mayor versatilidad. Pueden girar continuamente, mientras que los potenciómetros tienen una rotación limitada. Los potenciómetros indican la posición exacta de la perilla, mientras que los codificadores rotativos muestran cambios en la posición.

Principalmente hay dos tipos de codificadores rotativos: absolutos e incrementales (relativos). En este kit se utiliza un codificador incremental.

Los codificadores incrementales producen ondas cuadradas de dos fases, con una diferencia de fase de 90 grados, comúnmente referidas como los canales A y B.

Como se ilustra a continuación, cuando el canal A transita de un nivel alto a uno bajo, si el canal B está en un nivel alto, indica que el codificador rotativo está girando en sentido horario (CW); si en ese momento el canal B está en un nivel bajo, significa que la rotación es en sentido antihorario (CCW). Por lo tanto, al leer el valor del canal B cuando el canal A está en un nivel bajo, podemos determinar la dirección en la que gira el codificador rotativo.

.. image:: img/image206.png
    :width: 600
    :align: center
	
**Ejemplo**

* :ref:`2.1.6_c` (Proyecto en C)
* :ref:`2.1.6_py` (Proyecto en Python)
