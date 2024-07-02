.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _audio_configuration:

Configuración de Audio
============================

.. _change_audio_output:

Cambiar Salida de Audio
-------------------------------

Si tus altavoces no emiten sonido, puede ser porque el Raspberry Pi ha seleccionado la salida de audio incorrecta, la correcta debería ser **Auriculares**. Puedes cambiar la salida de audio siguiendo estos pasos.

Introduce el siguiente comando.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo raspi-config

Selecciona **1 Opciones del Sistema**.

.. image:: img/audio1.jpg

Luego **S2 Audio**.

.. image:: img/audio2.jpg

Después de seleccionar **1 Auriculares**, presiona ``Enter`` para confirmar y selecciona ``Finish`` para salir.

.. image:: img/audio3.jpg

.. _adjust_volume:

Ajustar Volumen
-------------------

Si sientes que el volumen de los altavoces es demasiado bajo, puedes ajustarlo introduciendo el siguiente comando.

.. raw:: html

   <run></run>

.. code-block:: 

    alsamixer

.. image:: img/faq1.png

La página predeterminada se muestra a continuación.

.. image:: img/faq2.png

Presiona ``F6`` para seleccionar el modo **Auriculares**.

.. image:: img/faq3.png

Luego presiona las flechas hacia arriba y hacia abajo para ajustar el nivel de volumen, y presiona ``ESC`` para salir.

.. image:: img/faq4.png
