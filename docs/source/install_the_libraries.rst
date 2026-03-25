.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _install_the_libraries:

Instalar las Librerías
==========================

Para Usuarios de C
------------------

BCM2835
~~~~~~~~~~~~~~~
Esta es una biblioteca en C para Raspberry Pi (RPi). Proporciona acceso a GPIO y otras funciones de E/S en el chip Broadcom BCM2835 usado en la Raspberry Pi, permitiendo acceder a los pines GPIO del conector IDE de 26 pines en la placa RPi para que puedas controlar e interactuar con varios dispositivos externos.

Proporciona funciones para leer entradas digitales y configurar salidas digitales, usar SPI e I2C y acceder a los temporizadores del sistema. La detección de eventos en pines es compatible mediante sondeo (polling), ya que no se admiten interrupciones.

Funciona en todas las versiones hasta e incluyendo la RPi 4. Funciona con todas las versiones de Debian hasta Debian Buster 10.

Abre una terminal y descarga la biblioteca ``bcm2835`` en la ruta ``~``.

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

Instala la biblioteca BCM2835 con los siguientes comandos.

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
------------------------

.. _create_virtual:

Crear un Entorno Virtual
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Al usar Raspberry Pi u otros dispositivos similares, se recomienda instalar paquetes con ``pip`` dentro de un entorno virtual. Esto ofrece aislamiento de dependencias, mayor seguridad del sistema, limpieza del entorno y facilita la migración y el intercambio de proyectos, simplificando la gestión de dependencias. Estos beneficios hacen que los entornos virtuales sean una herramienta extremadamente importante y útil en el desarrollo en Python.

A continuación se explican los pasos para crear un entorno virtual:

**1. Crear un entorno virtual**

Primero, asegúrate de que tu sistema tenga Python instalado. Python 3.3 o superior incluye el módulo ``venv`` para crear entornos virtuales, sin necesidad de instalar nada adicional. Si usas Python 2 o una versión anterior a Python 3.3, necesitarás instalar ``virtualenv``.

* Para Python 3:

Python 3.3 o versiones posteriores pueden usar directamente el módulo ``venv``:

.. raw:: html

    <run></run>

.. code-block:: shell

    python3 -m venv myenv

Esto creará un entorno virtual llamado ``myenv`` en el directorio actual.

* Para Python 2:

Si aún utilizas Python 2, primero instala ``virtualenv``:

.. raw:: html

    <run></run>

.. code-block:: shell

    pip install virtualenv

Luego, crea el entorno virtual:

.. raw:: html

    <run></run>

.. code-block:: shell

    virtualenv myenv

Esto también crea un entorno virtual llamado ``myenv`` en el directorio actual.

**2. Activar el entorno virtual**

Después de crear el entorno virtual, debes activarlo para usarlo.

.. note::

    Cada vez que reinicies la Raspberry Pi o abras una nueva terminal, deberás ejecutar el siguiente comando nuevamente para activar el entorno virtual.

.. raw:: html

    <run></run>

.. code-block:: shell

    source myenv/bin/activate

Cuando el entorno virtual esté activado, verás el nombre del entorno antes del prompt, indicando que estás trabajando dentro del entorno.

**3. Salir del entorno virtual**

Cuando termines de trabajar y desees salir del entorno virtual, simplemente ejecuta:

.. raw:: html

    <run></run>

.. code-block:: shell

    deactivate

Esto te devolverá al entorno global del sistema.

**4. Eliminar el entorno virtual**

Si ya no necesitas un entorno virtual, simplemente elimina el directorio correspondiente:

.. raw:: html

    <run></run>

.. code-block:: shell

    rm -rf myenv

.. _install_luma_led_matrix:

Luma.LED_Matrix
~~~~~~~~~~~~~~~~~~~~~~~

Esta es una biblioteca para Python 3 que permite controlar pantallas de matriz LED usando el controlador MAX7219 (vía SPI), WS2812 (NeoPixels, incluyendo Unicorn pHat/Hat de Pimoroni y Unicorn Hat HD) y APA102 (DotStar) en Raspberry Pi y otras SBC basadas en Linux.

#. Agrega el usuario a los grupos ``spi`` y ``gpio`` para asegurar que tenga permisos de acceso a las interfaces SPI y GPIO (reemplaza "pi" con tu usuario).

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell

        sudo usermod -a -G spi,gpio pi

   Después de ejecutar este comando, se recomienda reiniciar o cerrar sesión y volver a iniciarla para aplicar los cambios.

#. Instala las dependencias necesarias: Usa ``apt`` para instalar herramientas de compilación y bibliotecas esenciales.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell

        sudo apt update
        sudo apt install -y build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff-dev

#. Crea un entorno virtual. Aquí, ``~/my_env`` es la ruta del entorno virtual, y puede personalizarse.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       python3 -m venv ~/my_env


#. Activa el entorno virtual.

   .. note::
   
       Cada vez que reinicies la Raspberry Pi o abras una terminal nueva, deberás volver a ejecutar este comando.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       source ~/my_env/bin/activate

   Una vez activado, verás el nombre del entorno antes del prompt.

#. Dentro del entorno virtual, actualiza ``pip`` y ``setuptools``:

   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell

      pip install --upgrade pip setuptools


#. Instala ``luma.led_matrix``:

   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell
   
     pip install luma.led_matrix

#. Verifica la instalación ejecutando:

   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell

        python3 -c "import luma.led_matrix; print(luma.led_matrix.__version__)"

#. Cuando termines, sal del entorno virtual:

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       deactivate


* Referencia: `Luma.LED_Matrix <https://luma-led-matrix.readthedocs.io/en/latest/install.html>`_

.. .. _install_mfrc522:

.. MFRC522
.. ~~~~~~~~~~~~~~~~~

.. Ejecuta el siguiente comando para instalar la biblioteca MFRC522.

.. .. raw:: html

..    <run></run>

.. .. code-block:: 

..     sudo pip3 install mfrc522

.. La biblioteca MFRC522 contiene dos archivos: ``MFRC522.py`` y ``SimpleMFRC522.py``.

.. Entre ellos, ``MFRC522.py`` implementa la interfaz del lector RFID RC522, manejando toda la comunicación a través de la interfaz SPI.

.. ``SimpleMFRC522.py`` usa ``MFRC522.py`` y simplifica enormemente su uso, permitiéndote trabajar solo con unas pocas funciones en lugar de muchas.
