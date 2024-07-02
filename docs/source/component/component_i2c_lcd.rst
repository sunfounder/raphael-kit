.. nota::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_i2c_lcd:

I2C LCD1602
==============

.. image:: img/i2c_lcd1602.png
    :width: 800

* **GND**: Tierra
* **VCC**: Suministro de voltaje, 5V.
* **SDA**: Línea de datos serial. Conectar a VCC a través de una resistencia pull-up.
* **SCL**: Línea de reloj serial. Conectar a VCC a través de una resistencia pull-up.

Como todos sabemos, aunque las pantallas LCD y algunas otras mejoran enormemente la interacción hombre-máquina, comparten una debilidad común. Cuando están conectadas a un controlador, múltiples IOs serán ocupados por el controlador que no tiene tantos puertos externos. Además, esto restringe otras funciones del controlador. 

Por lo tanto, se desarrolló el LCD1602 con un módulo I2C para resolver este problema. El módulo I2C tiene un chip PCF8574 I2C incorporado que convierte los datos seriales I2C en datos paralelos para la pantalla LCD.

* `Datasheet del PCF8574 <https://www.ti.com/lit/ds/symlink/pcf8574.pdf?ts=1627006546204&ref_url=https%253A%252F%252Fwww.google.com%252F>`_

**Dirección I2C**

La dirección predeterminada es básicamente 0x27, en algunos casos puede ser 0x3F.

Tomando como ejemplo la dirección predeterminada de 0x27, la dirección del dispositivo se puede modificar cortocircuitando las almohadillas A0/A1/A2; en el estado predeterminado, A0/A1/A2 es 1, y si la almohadilla está cortocircuitada, A0/A1/A2 es 0.

.. image:: img/i2c_address.jpg
    :width: 600

**Retroiluminación/Contraste**

La retroiluminación se puede habilitar con un capuchón de puente, desconecta el capuchón de puente para deshabilitar la retroiluminación. El potenciómetro azul en la parte trasera se usa para ajustar el contraste (la relación de brillo entre el blanco más brillante y el negro más oscuro).

.. image:: img/back_lcd1602.jpg

* **Capuchón de puente**: La retroiluminación se puede habilitar con este capuchón, desconéctalo para deshabilitar la retroiluminación.
* **Potenciómetro**: Se utiliza para ajustar el contraste (la claridad del texto mostrado), que aumenta en la dirección de las agujas del reloj y disminuye en la dirección contraria a las agujas del reloj.

**Ejemplo**

* :ref:`1.1.7_c` (C Project)
* :ref:`3.1.3_c` (C Project)
* :ref:`3.1.7_c` (C Project)
* :ref:`3.1.8_c` (C Project)
* :ref:`3.1.11_c` (C Project)
* :ref:`1.1.7_py` (Python Project)
* :ref:`4.1.9_py` (Python Project)
* :ref:`4.1.13_py` (Python Project)
* :ref:`4.1.14_py` (Python Project)
* :ref:`4.1.17_py` (Python Project)
