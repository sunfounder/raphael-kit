.. _spi_configuration:

SPI Konfiguration
-----------------------

**Schritt 1**: Aktivieren Sie den SPI-Port Ihres Raspberry Pi (Falls Sie ihn bereits aktiviert haben, überspringen Sie diesen Schritt; wenn Sie nicht sicher sind, ob Sie dies getan haben oder nicht, fahren Sie bitte fort).

.. raw:: html

   <run></run>

.. code-block:: 

    sudo raspi-config

**3 Interfacing options**

.. image:: img/image282.png
   :align: center

**P4 SPI**

.. image:: img/image285.png
   :align: center

**<YES>, anschließend <OK> und <Finish> anklicken.**

.. image:: img/image286.png
   :align: center 

**Schritt 2:** Überprüfen Sie, ob die SPI-Module geladen und aktiv sind.

.. raw:: html

   <run></run>

.. code-block:: 

    ls /dev/sp*

Daraufhin sollten die folgenden Codes erscheinen (die Nummer könnte unterschiedlich sein).


.. code-block:: 

    /dev/spidev0.0  /dev/spidev0.1

**Schritt 3:** Installieren Sie das Python-Modul SPI-Py.

.. raw:: html

   <run></run>

.. code-block:: 

    git clone https://github.com/lthiery/SPI-Py.git
    cd SPI-Py
    sudo python3 setup.py install

.. note::
    Dieser Schritt ist für Python-Benutzer, wenn Sie C verwenden,
    überspringen Sie bitte diesen Schritt.

