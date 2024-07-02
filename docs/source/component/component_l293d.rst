.. nota::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_l293d:

L293D
=================

L293D es un controlador de motor de 4 canales integrado en un chip de alto voltaje y alta corriente.
Está diseñado para conectarse a niveles lógicos estándar DTL, TTL y para manejar cargas inductivas (como bobinas de relés, motores de CC, motores paso a paso) y transistores de conmutación de potencia, etc.
Los motores de CC son dispositivos que convierten la energía eléctrica de CC en energía mecánica. Son ampliamente utilizados en accionamientos eléctricos por su excelente rendimiento en la regulación de velocidad.

Vea la figura de los pines a continuación. El L293D tiene dos pines (Vcc1 y Vcc2) para la fuente de alimentación.
Vcc2 se usa para alimentar el motor, mientras que Vcc1 para alimentar el chip. Dado que se usa un motor de CC de tamaño pequeño, conecte ambos pines a +5V.

.. image:: img/l293d111.png

La siguiente es la estructura interna del L293D.
El pin EN es un pin de habilitación y solo funciona con nivel alto; A significa entrada y Y salida.
Puede ver la relación entre ellos en la parte inferior derecha.
Cuando el pin EN está en nivel alto, si A está en alto, Y emite nivel alto; si A está en bajo, Y emite nivel bajo. Cuando el pin EN está en nivel bajo, el L293D no funciona.

.. image:: img/l293d334.png

* `L293D Datasheet <https://www.ti.com/lit/ds/symlink/l293d.pdf?ts=1627004062301&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FL293D>`_

**Ejemplo**

* :ref:`1.3.1_c` (C Project)
* :ref:`3.1.4_c` (C Project)
* :ref:`1.3.1_py` (Python Project)
* :ref:`4.1.10_py` (Python Project)
* :ref:`1.17_scratch` (Scratch Project)