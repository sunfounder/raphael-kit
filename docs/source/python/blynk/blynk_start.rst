.. note::

    ¡Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _bk_start_py:

Comenzando con Blynk
=========================

Aprenderás cómo usar Blynk en este proyecto.

Cuando actives widgets en Blynk, tu Raspberry Pi imprimirá sus valores.

Sigue los pasos a continuación y ten en cuenta que debes realizarlos en orden sin saltarte ningún capítulo.


1. Configuración de Blynk
-------------------------

1. Ve a `BLYNK <https://blynk.io/>`_ y haz clic en **START FREE**. 

    .. image:: img/sp220607_142551.png

#. Ingresa tu dirección de correo electrónico para registrar una cuenta.

    .. image:: img/sp220607_142807.png

#. Ve a tu correo electrónico para completar el registro de tu cuenta.

    .. image:: img/sp220607_142936.png

#. Después, aparecerá **Blynk Tour** y podrás leerlo para conocer la información básica sobre Blynk.

    .. image:: img/sp220607_143244.png

#. A continuación necesitamos crear una plantilla y un dispositivo, haz clic en **Cancel**.

    .. image:: img/sp220607_143608.png

#. Ve a **Developer Zone** desde la barra de navegación.

    .. image:: img/develop_zone.png

#. Crea una nueva plantilla.

    .. image:: img/new_template.png

#. Completa **NAME** (puedes usar el nombre que quieras); **HARDWARE** debe ser **Raspberry Pi**. Luego haz clic en **Done**.

    .. image:: img/sp220913_170402.png

#. Serás redirigido a la página **Info**, solo haz clic en **save** en la parte superior derecha.

    .. image:: img/sp220913_171202.png

#. Ve a la página **Devices** desde la barra de navegación.

    .. image:: img/devices.jpg

#. Crea un nuevo dispositivo.

    .. image:: img/new_devices.png

#. Desde plantilla.

    .. image:: img/create_new_device.png

#. Selecciona **TEMPLATE** como la que acabas de crear, el **DEVICE NAME** puede ser personalizado. Luego haz clic en **Create**.

    .. image:: img/sp220913_173507.png

#. Ahora deberías ver una página como esta, lo que significa que la configuración inicial de Blynk está completa.

    .. image:: img/my_device.png


2. Editar Dashboard
-------------------

1. Haz clic en **edit dashboard**.

    .. image:: img/edit_dashboard.png

#. Luego arrastra cualquier widget de **CONTROL** que desees al Dashboard. Yo arrastré un **Switch** y un **Slider**.

    .. image:: img/sp220913_180725.png

#. Toca el icono de configuración en el widget.

    .. image:: img/sp220913_180806.png

#. Crea un flujo de datos (**Datastream**), selecciona **Virtual Pin**。

    .. image:: img/sp220913_180906.png

#. Completa la configuración del flujo de datos. Aquí se creó el flujo de datos para el Switch, por lo que **DATA TYPE** se selecciona como ``Integer``, y **MIN** y **MAX** se establecen en ``0`` y ``1``. Crea y luego guarda.

    .. image:: img/sp220913_181113.png

#. Usa los mismos pasos para crear un flujo de datos para el widget Slider y, de nuevo, modifica **DATA TYPE**, **MIN** y **MAX** según tus necesidades.

    .. image:: img/sp220913_182042.png

#. Una vez terminado, haz clic en **Save And Apply** en la parte superior derecha.

    .. image:: img/sp220913_182300.png


3. Instalar la librería de Blynk
--------------------------------

Ejecuta el siguiente comando para instalar.

.. raw:: html

   <run></run>

.. code-block::

    cd ~
    git clone https://github.com/vshymanskyy/blynk-library-python.git
    cd blynk-library-python
    sudo python3 setup.py

4. Descargar el ejemplo
-----------------------

Hemos proporcionado algunos ejemplos, ejecuta el siguiente comando para descargarlos.

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~
    git clone https://github.com/sunfounder/blynk-raspberrypi-python.git


5. Ejecutar el código
---------------------

1. Ve a la página **Device Info** de Blynk, verás información en **FIRMWARE CONFIGURATION**, necesitas copiar tu **BLYNK_AUTH_TOKEN**.

    .. image:: img/sp220913_182456.png

2. Edita el código.

.. raw:: html

    <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_start.py

3. Busca la siguiente línea y pega tu ``BLYNK_AUTH_TOKEN``.

.. code-block:: 

    BLYNK_AUTH = 'YourAuthToken'

4. Ejecuta el código.

.. raw:: html

    <run></run>

.. code-block:: 

    sudo python3 blynk_start.py

5. Ve a Blynk y opera el widget en el Dashboard.

    .. image:: img/sp220913_183529.png

6. Ahora podrás ver tus acciones en el terminal.

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
