.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _install_the_libraries:

Instalar las Librerías
=============================

Para Usuarios de C
---------------------

BCM2835
~~~~~~~~~~~~~~~
Esta es una librería en C para Raspberry Pi (RPi). Proporciona acceso a GPIO y otras funciones de IO en el chip Broadcom BCM 2835, utilizado en la Raspberry Pi, permitiendo el acceso a los pines GPIO en el conector IDE de 26 pines de la placa RPi, para que puedas controlar e interactuar con varios dispositivos externos.

Ofrece funciones para leer entradas digitales y configurar salidas digitales, usar SPI e I2C, y acceder a los temporizadores del sistema. La detección de eventos en los pines se soporta mediante sondeo (las interrupciones no están soportadas).

Funciona en todas las versiones hasta la RPI 4 inclusive. Compatible con todas las versiones de Debian hasta Debian Buster 10.

Abre una terminal y descarga la librería ``bcm2835`` en la ruta ``~``.

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~
    wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.69.tar.gz

Descomprime el paquete.

.. raw:: html

   <run></run>

.. code-block:: 

    tar zxvf bcm2835-1.69.tar.gz

Instala la librería BCM2835 con los siguientes comandos.

.. raw:: html

   <run></run>

.. code-block:: 

    cd bcm2835-1.69
    ./configure
    make
    sudo make check
    sudo make install

* Referencia: `bcm2835 <http://www.airspayce.com/mikem/bcm2835/>`_  

Para Usuarios de Python
----------------------------

.. _create_virtual:

Creación de un Entorno Virtual
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Al usar Raspberry Pi o dispositivos similares, se recomienda instalar paquetes con ``pip`` en un entorno virtual. Ofrece aislamiento de dependencias, aumenta la seguridad del sistema, mantiene la limpieza del sistema y facilita la migración y el intercambio de proyectos, simplificando la gestión de dependencias. Estos beneficios hacen que los entornos virtuales sean una herramienta extremadamente importante y útil en el desarrollo de Python.

A continuación, se presentan los pasos para crear un entorno virtual:
**1. Crear un entorno virtual**

Primero, debes asegurarte de que tu sistema tenga Python instalado. Las versiones de Python 3.3 y posteriores vienen con el módulo ``venv`` para crear entornos virtuales, eliminando la necesidad de una instalación separada. Si estás utilizando Python 2 o una versión anterior a Python 3.3, necesitarás instalar ``virtualenv``.

* Para Python 3:

Las versiones 3.3 y posteriores de Python pueden usar directamente el módulo ``venv``:

.. raw:: html

    <run></run>

.. code-block:: shell

    python3 -m venv myenv

Esto creará un entorno virtual llamado ``myenv`` en el directorio actual.

* Para Python 2:

Si aún estás utilizando Python 2, primero necesitas instalar ``virtualenv``:

.. raw:: html

    <run></run>

.. code-block:: shell

    pip install virtualenv

Luego, crea un entorno virtual:

.. raw:: html

    <run></run>

.. code-block:: shell

    virtualenv myenv

Esto también creará un entorno virtual llamado ``myenv`` en el directorio actual.

**2. Activar el Entorno Virtual**

Después de crear el entorno virtual, necesitas activarlo para su uso.

.. note::

    Cada vez que reinicies la Raspberry Pi, o abras una nueva terminal, tendrás que ejecutar nuevamente el siguiente comando para activar el entorno virtual.

.. raw:: html

    <run></run>

.. code-block:: shell

    source myenv/bin/activate

Una vez activado el entorno virtual, verás el nombre del entorno antes del prompt de la línea de comandos, indicando que estás trabajando dentro del entorno virtual.

**3. Salir del Entorno Virtual**

Cuando hayas terminado tu trabajo y desees salir del entorno virtual, simplemente ejecuta:

.. raw:: html

    <run></run>

.. code-block:: shell

    deactivate

Esto te devolverá al entorno global de Python del sistema.

**4. Eliminar el Entorno Virtual**

Si ya no necesitas un entorno virtual en particular, puedes simplemente eliminar el directorio que contiene el entorno virtual:

.. raw:: html

    <run></run>

.. code-block:: shell

    rm -rf myenv


Luma.LED_Matrix
~~~~~~~~~~~~~~~~~~~~~~~

Esta es una biblioteca de Python 3 para la interfaz de pantallas de matriz de LED utilizando el controlador MAX7219 (a través de SPI), WS2812 (NeoPixels, incluyendo Pimoroni Unicorn pHat/Hat y Unicorn Hat HD), y APA102 (DotStar) en la Raspberry Pi y otras computadoras de placa única basadas en Linux.

#. Agrega el usuario a los grupos ``spi`` y ``gpio`` para asegurar que el usuario actual (reemplaza "pi" con tu nombre de usuario) tenga permiso para acceder a las interfaces SPI y GPIO.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell

        sudo usermod -a -G spi,gpio pi

   Después de ejecutar este comando, se recomienda reiniciar el sistema o cerrar y volver a iniciar sesión para aplicar los cambios de pertenencia al grupo.

#. Instala las dependencias necesarias: Usa ``apt`` para instalar herramientas de compilación y bibliotecas de desarrollo relacionadas. Estas bibliotecas son esenciales para compilar e instalar ciertos paquetes de Python.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
    
        sudo apt update
        sudo apt install -y build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff-dev

#. Crea un entorno virtual. Aquí, ``~/my_env`` es la ruta para el entorno virtual y puede personalizarse.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       python3 -m venv ~/my_env

#. Después de crear el entorno virtual, actívalo para su uso.

   .. note::
   
       Cada vez que reinicies la Raspberry Pi o abras un nuevo terminal, deberás ejecutar el siguiente comando nuevamente para activar el entorno virtual.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       source ~/my_env/bin/activate
   
   Una vez que el entorno virtual esté activado, verás el nombre del entorno antes del símbolo del sistema, indicando que estás trabajando dentro del entorno virtual.

#. Dentro del entorno virtual, actualiza ``pip`` y ``setuptools`` para asegurar que las versiones más recientes de los paquetes estén instaladas.
   
   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell

        pip install --upgrade pip setuptools

#. Luego, instala ``luma.led_matrix``:
   
   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell
   
        pip install luma.led_matrix

#. Después de la instalación, puedes verificar que ``luma.led_matrix`` se haya instalado correctamente ejecutando el siguiente comando. Si es exitoso, mostrará el número de versión de ``luma.led_matrix``.
   
   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell

        python3 -c "import luma.led_matrix; print(luma.led_matrix.__version__)"

#. Cuando termines de trabajar y desees salir del entorno virtual, simplemente ejecuta:
   
   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       deactivate


* Referencia: `Luma.LED_Matrix <https://luma-led-matrix.readthedocs.io/en/latest/install.html>`_



.. _mfrc522_lib:

MFRC522
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ejecute el siguiente comando para instalar la biblioteca MFRC522.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install mfrc522

La librería MFRC522 contiene dos archivos: ``MFRC522.py`` y ``SimpleMFRC522.py``.

Entre ellos, ``MFRC522.py`` es la implementación de la interfaz RFID RC522, esta librería maneja todo el trabajo pesado de la comunicación con RFID a través de la interfaz SPI de la Pi.

``SimpleMFRC522.py`` toma el archivo ``MFRC522.py`` y lo simplifica considerablemente, permitiéndote trabajar con solo unas pocas funciones en lugar de muchas.