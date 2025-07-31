.. _spi_configuration:

SPI Configurtion
-----------------------

**Paso 1**: Habilita el puerto SPI de tu Raspberry Pi (si ya lo has habilitado, omite este paso; si no sabes si lo has hecho, continúa).

.. raw:: html

   <run></run>

.. code-block:: 

    sudo raspi-config

**3 Interfacing options**

.. image:: img/image282.png
   :align: center

**I3 SPI**

.. image:: img/i3spi.png
   :align: center

**<YES>, luego haz clic en <OK> y <Finish>.**

.. image:: img/image286.png
   :align: center 

**Paso 2:** Verifica que los módulos spi estén cargados y activos.

.. raw:: html

   <run></run>

.. code-block:: 

    ls /dev/sp*

Luego aparecerán los siguientes códigos (el número puede ser diferente).

.. code-block:: 

    /dev/spidev0.0  /dev/spidev0.1

**Paso 3:** Instala el módulo Python ``spidev`` .

* Ejecute el siguiente comando para instalarlo usando ``pip``:

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install spidev

Esta biblioteca proporciona la interfaz Python para comunicarse con dispositivos SPI utilizando /dev/spidevX.Y.