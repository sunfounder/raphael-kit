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

**3. Instalación de Dependencias**

Con el entorno virtual activado, puedes usar pip para instalar las dependencias necesarias. Por ejemplo:

.. raw:: html

    <run></run>

.. code-block:: shell

    pip install requests

Esto instalará la librería requests en el entorno virtual actual, en lugar de en el entorno global. Este paso solo necesita realizarse una vez.


**4. Salir del Entorno Virtual**

Cuando hayas terminado tu trabajo y desees salir del entorno virtual, simplemente ejecuta:

.. raw:: html

    <run></run>

.. code-block:: shell

    deactivate

Esto te devolverá al entorno global de Python del sistema.

**5. Eliminar el Entorno Virtual**

Si ya no necesitas un entorno virtual en particular, puedes simplemente eliminar el directorio que contiene el entorno virtual:

.. raw:: html

    <run></run>

.. code-block:: shell

    rm -rf myenv


Luma.LED_Matrix
~~~~~~~~~~~~~~~~~~~~~~~

Esta es una librería en Python 3 para interactuar con pantallas de matriz LED usando el controlador MAX7219 (usando SPI), WS2812 (NeoPixels, incluyendo Pimoroni Unicorn pHat/Hat y Unicorn Hat HD) y APA102 (DotStar) en la Raspberry Pi y otras computadoras de placa única basadas en Linux.

Primero, instala las dependencias de la librería con:

.. raw:: html

   <run></run>

.. code-block:: 

    sudo usermod -a -G spi,gpio pi
    sudo apt install build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5

.. note:: warning

    Las versiones predeterminadas de pip y setuptools incluidas con apt en Raspbian son muy antiguas y pueden causar problemas al instalar componentes. Asegúrate de que estén actualizadas actualizándolas primero:

    .. raw:: html

       <run></run>

    .. code-block:: 

        sudo -H pip install --upgrade --ignore-installed pip setuptools

Procede a instalar la versión más reciente de la librería luma.led_matrix directamente desde PyPI:

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 -m pip install --upgrade luma.led_matrix


* Referencia: `Luma.LED_Matrix <https://luma-led-matrix.readthedocs.io/en/latest/install.html>`_

Spidev y MFRC522
~~~~~~~~~~~~~~~~~~~~~~~~~~~

La librería ``spidev`` ayuda a manejar las interacciones con SPI y es un componente clave en este tutorial, ya que la necesitamos para que la Raspberry Pi interactúe con el RFID RC522.

Ejecuta el siguiente comando para instalar ``spidev`` en tu Raspberry Pi a través de ``pip``.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install spidev


Continúa instalando la librería MFRC522.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install mfrc522

La librería MFRC522 contiene dos archivos: ``MFRC522.py`` y ``SimpleMFRC522.py``.

Entre ellos, ``MFRC522.py`` es la implementación de la interfaz RFID RC522, esta librería maneja todo el trabajo pesado de la comunicación con RFID a través de la interfaz SPI de la Pi.

``SimpleMFRC522.py`` toma el archivo ``MFRC522.py`` y lo simplifica considerablemente, permitiéndote trabajar con solo unas pocas funciones en lugar de muchas.