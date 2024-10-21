.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_motor:

Motor de corriente continua (DC)
=======================================

.. image:: img/image114.jpeg
    :align: center

Este es un motor DC de 3V. Cuando aplicas un nivel alto y un nivel bajo a cada uno de los 2 terminales, girará.

* **Tamaño**: 25*20*15MM
* **Voltaje de operación**: 1-6V
* **Corriente en vacío** (3V): 70mA
* **Velocidad en vacío** (3V): 13000RPM
* **Corriente de arranque** (3V): 800mA
* **Diámetro del eje**: 2mm

El motor de corriente continua (DC) es un actuador continuo que convierte energía eléctrica en energía mecánica. Los motores DC hacen funcionar bombas rotativas, ventiladores, compresores, impulsores y otros dispositivos al producir una rotación angular continua.

Un motor DC consta de dos partes, la parte fija del motor llamada **estator** y la parte interna del motor llamada **rotor** (o **armadura** de un motor DC) que gira para producir movimiento.
La clave para generar movimiento es posicionar la armadura dentro del campo magnético del imán permanente (cuyo campo se extiende desde el polo norte hasta el polo sur). La interacción del campo magnético y las partículas cargadas en movimiento (el cable que transporta corriente genera el campo magnético) produce el par que hace girar la armadura.

.. image:: img/motor_sche.png
    :align: center

La corriente fluye desde el terminal positivo de la batería a través del circuito, pasando por las escobillas de cobre hasta el conmutador, y luego a la armadura.
Pero debido a los dos huecos en el conmutador, este flujo se invierte a mitad de cada rotación completa.
Esta inversión continua convierte esencialmente la corriente continua (DC) de la batería en corriente alterna (AC), permitiendo que la armadura experimente el par en la dirección correcta en el momento adecuado para mantener la rotación.

**Ejemplo**

* :ref:`1.3.1_c` (C Project)
* :ref:`3.1.4_c` (C Project)
* :ref:`1.3.1_py` (Python Project)
* :ref:`4.1.10_py` (Python Project)
* :ref:`1.17_scratch` (Scratch Project)