.. nota::

    ¡Hola, bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de vacaciones.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Revisar el ``GPIO Zero``
=================================

Si eres un usuario de Python en Raspberry Pi 5, puedes programar los GPIOs con la API proporcionada por
``GPIO Zero``.

``GPIO Zero`` es un módulo para controlar los pines GPIO de Raspberry Pi. Este paquete proporciona una gama de clases y funciones fáciles de usar para controlar los GPIO en una Raspberry Pi. Para ejemplos y documentación, visita: https://gpiozero.readthedocs.io/en/latest/.

Para probar si GPIO Zero está instalado o no, escribe en python:

.. raw:: html

   <run></run>

.. code-block::

    python

.. image:: ../python_pi5/img/zero_01.png
    :width: 100%


En la CLI de Python, ingresa ``import gpiozero``. Si no aparece ningún error, significa que
GPIO Zero está instalado.

.. raw:: html

   <run></run>

.. code-block::

    import gpiozero

.. image:: ../python_pi5/img/zero_02.png
    :width: 100%


Si quieres salir de la CLI de Python, escribe:

.. raw:: html

   <run></run>

.. code-block::

    exit()

.. image:: ../python_pi5/img/zero_03.png
    :width: 100%


