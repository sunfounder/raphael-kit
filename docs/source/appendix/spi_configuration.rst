.. _spi_configuration:

SPI Configuration
-----------------------

#. Enable the SPI interface on your Raspberry Pi. If you've already enabled it, you can skip this step. If you're unsure, follow the instructions below.

   * Open the Raspberry Pi configuration tool:

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         sudo raspi-config

   * **3 Interfacing options**

     .. image:: img/image282.png
        :align: center

   * **I3 SPI**

     .. image:: img/i3spi.png
        :align: center
     
   * **<YES>, then click <OK> and <Finish>.**

     .. image:: img/image286.png
        :align: center 

#. Verify that the SPI modules are active.

   * Run the following command:

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         ls /dev/sp*

   * You should see output similar to:


     .. code-block:: 
     
         /dev/spidev0.0  /dev/spidev0.1

   If these devices appear, the SPI interface is active and ready.

#. Install the ``spidev`` Python library.

   * Run the following command to install it using ``pip``:

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         sudo pip3 install spidev
     
   This library provides the Python interface to communicate with SPI devices using /dev/spidevX.Y.