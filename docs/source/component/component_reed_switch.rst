.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_reed_switch:

Módulo de Interruptor Reed
==============================

.. image:: img/reed_switch.png
    :width: 300
    :align: center

* Utiliza un interruptor reed de tipo normalmente abierto.
* Salida del comparador, señal limpia, buena forma de onda, gran capacidad de conducción, más de 15mA.
* Voltaje de trabajo: 3.3V-5V
* Forma de salida: salida de interruptor digital (0 y 1).
* Con orificios de montaje para una fácil instalación.
* Tamaño de la placa PCB pequeña: 3.2cm x 1.4cm.
* Utiliza un comparador LM393 de voltaje amplio.

El módulo de interruptor reed consta de un interruptor reed, un potenciómetro, un comparador LM393, un LED, etc. El circuito interno se muestra a continuación, cuando el imán está cerca del módulo, se encenderá y el módulo emitirá un nivel bajo; cuando no hay magnetismo, se apagará y emitirá un nivel alto. La distancia de inducción entre el interruptor reed y el imán debe ser dentro de 1.5cm, más allá no será sensible o no se producirá el fenómeno de disparo, también se puede ajustar la sensibilidad a través del potenciómetro en el módulo.
    
.. image:: img/reedswitch_sche.jpg
    :width: 600
    :align: center

El interruptor reed, también conocido como interruptor magnético o interruptor de lengüeta.

Tiene dos láminas metálicas internas, selladas en un tubo de vidrio, que está lleno de gas inerte. Normalmente, las dos láminas se superponen, pero están separadas por un espacio, y el circuito está abierto. Cuando hay un objeto magnético cerca, las dos láminas producirán una atracción magnética mutua, que las juntará, conectando el circuito. Por lo tanto, el interruptor reed puede usarse para hacer un sensor magnético.
        
.. image:: img/HowItWorksReed.jpg

**Ejemplo**

* :ref:`2.2.4_c` (C Project)
* :ref:`2.2.4_py` (Python Project)
* :ref:`4.1.6_py` (Python Project)
* :ref:`1.6_scratch` (Scratch Project)
