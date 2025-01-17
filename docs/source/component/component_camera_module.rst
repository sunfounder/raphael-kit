.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_camera_module:

Módulo de Cámara
====================================

**Descripción**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

Este es un módulo de cámara de 5MP para Raspberry Pi con sensor OV5647. Es plug and play, conecta el cable de cinta incluido al puerto CSI (Camera Serial Interface) en tu Raspberry Pi y estarás listo para usarlo.

La placa es pequeña, aproximadamente 25mm x 23mm x 9mm, y pesa 3g, lo que la hace ideal para aplicaciones móviles u otras aplicaciones donde el tamaño y el peso son críticos. El módulo de cámara tiene una resolución nativa de 5 megapíxeles y tiene una lente de enfoque fijo incorporada que captura imágenes fijas a 2592 x 1944 píxeles, y también soporta video 1080p30, 720p60 y 640x480p90.

.. note::

   El módulo solo es capaz de capturar imágenes y videos, no sonido.

**Especificaciones**

* **Resolución de imágenes estáticas**: 2592×1944 
* **Resolución de video soportada**: 1080p/30 fps, 720p/ 60fps y 640 x 480p 60/90 grabación de video 
* **Apertura (F)**: 1.8 
* **Ángulo visual**: 65 grados 
* **Dimensión**: 24mm x 23.5mm x 8mm 
* **Peso**: 3g 
* **Interfaz**: conector CSI 
* **Sistemas Operativos soportados**: Raspberry Pi OS (se recomienda la última versión) 



**Montaje del Módulo de Cámara**
-------------------------------------

En el módulo de cámara o Raspberry Pi, encontrarás un conector de plástico plano. Tira cuidadosamente del interruptor negro hasta que esté parcialmente fuera. Inserta el cable FFC en el conector de plástico en la dirección mostrada y vuelve a colocar el interruptor en su lugar.

Si el cable FFC está correctamente instalado, estará recto y no se saldrá cuando tires suavemente de él. Si no, reinstálalo nuevamente.

.. image:: img/connect_ffc.png
.. image:: img/1.10_camera.png
   :width: 700

.. warning::

   No instales la cámara con la alimentación encendida, puede dañar tu cámara.

**Ejemplo**

* :ref:`3.1.1_py` (Python Project)
* :ref:`3.1.2_py` (Python Project)
* :ref:`4.1.1_py` (Python Project)
* :ref:`4.1.4_py` (Python Project)
* :ref:`4.1.5_py` (Python Project)
* :ref:`1.10_scratch` (Scratch Project)
* :ref:`1.18_scratch` (Scratch Project)
