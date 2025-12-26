.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _install_wiringpi_pi5:

Instalar y verificar WiringPi
=======================================

``wiringPi`` es una biblioteca de GPIO en lenguaje C para Raspberry Pi. Cumple con GUN Lv3. 
Las funciones en wiringPi son similares a las del sistema de cableado de Arduino, lo que permite 
a los usuarios familiarizados con Arduino usar wiringPi más fácilmente.

``wiringPi`` incluye muchos comandos GPIO que te permiten controlar todo tipo de interfaces 
en Raspberry Pi.

Ejecuta el siguiente comando para instalar la biblioteca ``wiringPi``.

.. raw:: html

   <run></run>

.. code-block::

    sudo apt-get update
    git clone https://github.com/WiringPi/WiringPi
    cd WiringPi 
    ./build

Puedes probar si la biblioteca wiringPi se instaló correctamente con la siguiente instrucción.

.. raw:: html

   <run></run>

.. code-block::

    gpio -v

.. image:: ../img/image30.png

Verifica el GPIO con el siguiente comando:

.. raw:: html

   <run></run>

.. code-block::

    gpio readall

.. image:: ../img/image31.png

Para más detalles sobre wiringPi, puedes consultar `WiringPi <https://github.com/WiringPi/WiringPi>`_.
