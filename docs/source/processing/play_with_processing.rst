.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y avances exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _play_with_processing:

Juega con Processing 
=======================================

¿Qué es Processing?
-----------------------

Processing es un entorno de programación simple que se creó para facilitar el desarrollo de aplicaciones visualmente orientadas con énfasis en la animación y proporcionando a los usuarios retroalimentación instantánea a través de la interacción. 
Los desarrolladores querían un medio para “esbozar” ideas en código. 
A medida que sus capacidades han aumentado en la última década, Processing se ha utilizado para trabajos de producción más avanzados además de su papel de esbozo. 
Originalmente construido como una extensión de Java específica del dominio dirigida a artistas y diseñadores, Processing ha evolucionado hasta convertirse en una herramienta de diseño y prototipado utilizada para trabajos de instalación a gran escala, gráficos en movimiento y visualización de datos complejos.

Processing está basado en Java, pero debido a que los elementos del programa en Processing son bastante simples, puedes aprender a usarlo incluso si no sabes nada de Java. Si estás familiarizado con Java, es mejor olvidar que Processing tiene algo que ver con Java por un tiempo, hasta que te acostumbres a cómo funciona la API.

Este texto es del tutorial, `Processing Overview <https://processing.org/tutorials/overview/>`_.

Instalar Processing
------------------------

.. note:: 

    Antes de que puedas usar Processing, necesitas acceder al escritorio de Raspberry Pi de forma remota (:ref:`remote_desktop`) o conectar una pantalla para el Raspberry Pi.
.. Run the following command in Terminal to install Processing.

.. .. raw:: html

..    <run></run>

.. .. code-block:: 

..     curl https://processing.org/download/install-arm.sh | sudo sh

.. Once the installation is complete, type ``processing`` to open it.


.. .. image:: img/processing1.png


.. For a detailed tutorial, please refer to `Pi Processing <https://pi.processing.org/>`_.

#. Primero visita https://processing.org/download y selecciona la versión ``Linux（Raspberry Pi 32-bit）`` o ``Linux（Raspberry Pi 64-bit）``. Utilizando este método, siempre podrás descargar la última versión.

    O puedes usar el siguiente comando para descargar Processing desde el Terminal.

    .. code-block:: 

        wget https://github.com/benfry/processing4/releases/download/processing-1293-4.3/processing-4.3-linux-arm32.tgz

    .. code-block:: 

        wget https://github.com/benfry/processing4/releases/download/processing-1293-4.3/processing-4.3-linux-arm64.tgz

#. Se descargará un archivo ``.tar.gz``, que la mayoría de los usuarios de Linux deberían estar familiarizados con él. Extrae el archivo que acabas de descargar desde su ubicación.

    .. code-block:: 

        tar xvfz processing-xxxx.tgz

    Reemplaza xxxx con el resto del nombre del archivo, que es el número de versión. Esto creará una carpeta llamada processing-xxxx o algo similar. 

#. Luego ve a ese directorio:

    .. code-block:: 

        cd processing-xxxx

#. Y ejecútalo:

    .. code-block:: 

        ./processing

#. Con suerte, ahora la ventana principal de Processing debería ser visible.

    .. image:: img/processing2.png


Instalar Hardware I/O
---------------------------

Para usar los GPIO de Raspberry Pi, necesitas agregar manualmente una `biblioteca de Hardware I/O <https://processing.org/reference/libraries/io/index.html>`_.

Haz clic en ``Sketch`` -> ``Import Library`` -> ``Add Library...`` 

.. image:: img/import-00.png

Encuentra Hardware I/O, selecciónalo y luego haz clic en Instalar. Cuando se complete, aparecerá un icono de marca de verificación.

.. image:: img/import-02.png

Proyectos
-----------

.. toctree::
    draw_a_matchmaker
    hello_mouse
    blinking_dot
    clickable_dot
    clickable_color_blocks
    inflating_the_dot
    dot_on_the_swing
    metronome
    show_number
    drag_number
