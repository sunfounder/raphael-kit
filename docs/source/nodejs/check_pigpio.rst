.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede temprano a nuevos anuncios de productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Revisar pigpio
===================

pigpio es un módulo utilizado para controlar los canales GPIO de Raspberry Pi. Este paquete proporciona algunos métodos para controlar GPIO en Raspberry Pi. Para ejemplos y documentación, visita: https://www.npmjs.com/package/pigpio.

Ingresa el siguiente comando para instalar la biblioteca pigpio.

.. raw:: html

    <run></run>

.. code-block::

    npm install pigpio

Verifica si la biblioteca se ha instalado correctamente, cambia de directorio e ingresa a nodejs:

.. raw:: html

    <run></run>

.. code-block::

    cd ~/raphael-kit/nodejs
    nodejs

.. image:: img/pigpio1.png

Luego ingresa require('pigpio'):

.. raw:: html

    <run></run>

.. code-block::

    require('pigpio')

.. image:: img/pigpio2.png   

Si aparece la pantalla anterior, la instalación de la biblioteca fue exitosa.

Si deseas salir del CLI de node, presiona Ctrl+C dos veces.

.. image:: img/pigpio3.png