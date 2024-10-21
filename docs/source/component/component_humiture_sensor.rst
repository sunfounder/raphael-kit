.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_humiture_sensor:

Módulo Sensor de Humedad y Temperatura
============================================

.. image:: img/dht11_pic.png
    :width: 400
    :align: center

El sensor digital de temperatura y humedad DHT11 es un sensor compuesto que contiene una salida de señal digital calibrada de temperatura y humedad. 
La tecnología de recolección de módulos digitales dedicados y la tecnología de detección de temperatura y humedad se aplican para garantizar que el producto tenga alta fiabilidad y excelente estabilidad a largo plazo.

Solo tres pines están disponibles para su uso: VCC, GND y DATA. 
El proceso de comunicación comienza con la línea DATA enviando señales de inicio al DHT11, y el DHT11 recibe las señales y devuelve una señal de respuesta. 
Luego, el host recibe la señal de respuesta y comienza a recibir datos de humedad de 40 bits (8 bits de humedad entera + 8 bits de humedad decimal + 8 bits de temperatura entera + 8 bits de temperatura decimal + 8 bits de verificación).

.. image:: img/Dht11.png

* `Hoja de datos del DHT11 <https://components101.com/sites/default/files/component_datasheet/DHT11-Temperature-Sensor.pdf>`_

**Ejemplo**

* :ref:`2.2.3_c` (Proyecto en C)
* :ref:`2.2.3_py` (Proyecto en Python)
