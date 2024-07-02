.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más profundamente en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_touch_switch:

Módulo de Interruptor Táctil
==================================

.. image:: img/touch168.png
    :width: 300
    :align: center

El módulo de interruptor táctil funciona detectando un cambio en la capacitancia debido a la influencia de un objeto externo. La placa táctil está cubierta con material aislante y el usuario no entra en contacto con el circuito eléctrico.

Un interruptor táctil capacitivo tiene diferentes capas: una placa aislante superior seguida de una placa táctil, otra capa aislante y luego la placa de tierra.

.. image:: img/touch169.jpeg

En la práctica, un sensor capacitivo se puede hacer en una PCB de doble cara considerando un lado como el sensor táctil y el lado opuesto como la placa de tierra del capacitor. Cuando se aplica energía a través de estas placas, las dos placas se cargan. En estado de equilibrio, las placas tienen el mismo voltaje que la fuente de alimentación.

El circuito detector táctil tiene un oscilador cuya frecuencia depende de la capacitancia del panel táctil. Cuando un dedo se acerca al panel táctil, la capacitancia adicional hace que la frecuencia de este oscilador interno cambie. El circuito detector rastrea la frecuencia del oscilador a intervalos programados, y cuando el cambio supera el umbral, el circuito desencadena un evento de pulsación de tecla.

**Ejemplo**

* :ref:`2.1.3_c` (C Project)
* :ref:`2.1.3_py` (Python Project)
* :ref:`1.9_scratch` (Scratch Project)