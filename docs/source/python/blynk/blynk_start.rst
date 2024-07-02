.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Previsualizaciones exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones navideñas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _bk_start_py:

Comienza con Blynk
============================

En este proyecto aprenderás a usar Blynk.

Cuando actives los widgets en Blynk, tu Raspberry Pi imprimirá sus valores.

Sigue los pasos a continuación, y ten en cuenta que debes hacerlos en orden y no saltarte ningún capítulo.


1. Configuración de Blynk
-----------------------------

1. Ve a `BLYNK <https://blynk.io/>`_ y haz clic en **START FREE**. 

    .. image:: img/sp220607_142551.png

#. Ingresa tu dirección de correo electrónico para registrar una cuenta.

    .. image:: img/sp220607_142807.png

#. Ve a tu dirección de correo electrónico para completar el registro de tu cuenta.

    .. image:: img/sp220607_142936.png

#. Después aparecerá el **Blynk Tour** y puedes leerlo para aprender la información básica sobre Blynk.

    .. image:: img/sp220607_143244.png

#. A continuación, necesitamos crear una plantilla y un dispositivo, haz clic en **Cancel**.

    .. image:: img/sp220607_143608.png

#. Ve a Plantilla desde la barra de navegación.

    .. image:: img/sp220913_170029.png

#. Crear nueva plantilla

    .. image:: img/sp220913_170206.png

#. Rellena el **NOMBRE**, siéntete libre de hacerlo; **HARDWARE** debe ser **Raspberry Pi**. Luego haz clic en **Done**.

    .. image:: img/sp220913_170402.png

#. Serás redirigido a la página de información, solo haz clic en guardar en la esquina superior derecha.

    .. image:: img/sp220913_171202.png

#. Ve a la página de **Buscar** desde la barra de navegación.

    .. image:: img/sp220913_172727.png

#. Crear nuevo dispositivo.

    .. image:: img/sp220913_173259.png

#. Desde plantilla.

    .. image:: img/sp220913_173350.png

#. Selecciona **TEMPLATE** como la que acabas de configurar, **DEVICE NAME** puede ser personalizado. Luego haz clic en Crear.

    .. image:: img/sp220913_173507.png

#. Ahora deberías ver una página como esta, lo que significa que tu configuración inicial de Blynk está completa.

    .. image:: img/sp220913_173950.png

2. Editar el Tablero
--------------------------------


1. Haz clic en el icono del menú en la esquina superior derecha y selecciona editar tablero.

    .. image:: img/sp220913_180231.png

#. Luego arrastra cualquier Widget de CONTROL que desees al Tablero. Yo arrastré un Interruptor y un Control Deslizante.

    .. image:: img/sp220913_180725.png

#. Toca el ícono de configuración en el widget.

    .. image:: img/sp220913_180806.png

#. Crea un Datastream, selecciona Pin Virtual.

    .. image:: img/sp220913_180906.png

#. Completa la configuración del datastream. Aquí se creó el datastream para el Interruptor, por lo que en **DATA TYPE** selecciona ``Interger``, y configura **MIN** y **MAX** en ``0`` y ``1``. Crea y luego Guarda.

    .. image:: img/sp220913_181113.png

#. Usa los mismos pasos para crear un Datastream para el widget de control deslizante, y nuevamente, modifica **DATA TYPE**, **MIN** y **MAX** según lo que necesites.

    .. image:: img/sp220913_182042.png

#. Cuando termines, haz clic en Guardar y Aplicar en la esquina superior derecha.

    .. image:: img/sp220913_182300.png


3. Instalar la librería Blynk
----------------------------------

Ejecuta el siguiente comando para instalar.

.. raw:: html

   <run></run>

.. code-block::

    cd ~
    git clone https://github.com/vshymanskyy/blynk-library-python.git
    cd blynk-library-python
    sudo python3 setup.py

4. Descargar el Ejemplo
--------------------------------


Hemos proporcionado algunos ejemplos, por favor ejecuta el siguiente comando para descargarlos.

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~
    git clone https://github.com/sunfounder/blynk-raspberrypi-python.git


5. Ejecutar el Código
------------------------------



1. Ve a la página de Información del Dispositivo en Blynk, verás alguna información bajo **FIRMWARE CONFIGURATION**, necesitas copiar **BLYNK_AUTH_TOKEN**.

    .. image:: img/sp220913_182456.png

2. Edita el código.

.. raw:: html

    <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_start.py

3. Encuentra la siguiente línea y pega tu ``BLYNK_AUTH_TOKEN``.

.. code-block:: 

    BLYNK_AUTH = 'YourAuthToken'

4. Ejecuta el código.

.. raw:: html

    <run></run>

.. code-block:: 

    sudo python3 blynk_start.py

5. Ve a Blynk y opera el widget en el Tablero.

    .. image:: img/sp220913_183529.png

6. Ahora podrás ver tus acciones en la terminal.

.. code-block:: 

    ..
       ___  __          __
      / _ )/ /_ _____  / /__
     / _  / / // / _ \/  '_/
    /____/_/\_, /_//_/_/\_\
            /___/ for Python v1.0.0 (linux)

    Connecting to blynk.cloud:443...
    Blynk ready. Ping: 142 ms
    V0 value: ['1']
    V0 value: ['0']
    V1 value: ['3']
    V1 value: ['8']
    V0 value: ['1']







