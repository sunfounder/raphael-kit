Install the Libraries
==========================

For C User
--------------

BCM2835
~~~~~~~~~~~~~~~
This is a C library for Raspberry Pi (RPi). It provides access to GPIO and other IO functions on the Broadcom BCM 2835 chip, as used in the RaspberryPi, allowing access to the GPIO pins on the 26 pin IDE plug on the RPi board so you can control and interface with various external devices.

It provides functions for reading digital inputs and setting digital outputs, using SPI and I2C, and for accessing the system timers. Pin event detection is supported by polling (interrupts are not supported).

Works on all versions upt to and including RPI 4. Works with all versions of Debian up to and including Debian Buster 10.


Open a terminal and download the ``bcm2835`` library to the ``/home/pi`` path.

.. code-block:: shell

    cd /home/pi
    wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.69.tar.gz

Unzip the package.

.. code-block:: shell

    tar zxvf bcm2835-1.69.tar.gz

Install the BCM2835 library with the following commands.

.. code-block:: shell

    cd bcm2835-1.69
    ./configure
    make
    sudo make check
    sudo make install

* Reference: `bcm2835 <http://www.airspayce.com/mikem/bcm2835/>`_  


For Python User
----------------------

Luma.LED_Matrix
~~~~~~~~~~~~~~~~~~~~~~~

This is a Python 3 library interfacing LED matrix displays with the MAX7219 driver (using SPI), WS2812 (NeoPixels, inc Pimoroni Unicorn pHat/Hat and Unicorn Hat HD) and APA102 (DotStar) on the Raspberry Pi and other Linux-based single board computers.

Install the dependencies for library first with:

.. code-block:: shell

    sudo usermod -a -G spi,gpio pi
    sudo apt install build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5

.. note:: warning

    The default pip and setuptools bundled with apt on Raspbian are really old, and can cause components to not be installed properly. Make sure they are up to date by upgrading them first:

    .. code-block:: shell

        sudo -H pip install --upgrade --ignore-installed pip setuptools

Proceed to install latest version of the luma.led_matrix library directly from PyPI:

.. code-block:: shell

    sudo python3 -m pip install --upgrade luma.led_matrix


* Reference: `Luma.LED_Matrix <https://luma-led-matrix.readthedocs.io/en/latest/install.html>`_

Spidev and MFRC522
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``spidev`` library helps handle interactions with the SPI and is a key component to this tutorial as we need it for the Raspberry Pi to interact with the RFID RC522.

Run the following command to install ``spidev`` to your Raspberry Pi via ``pip``.

.. code-block:: shell

    sudo pip3 install spidev


Continue to install the MFRC522 library.

.. code-block:: shell

    sudo pip3 install mfrc522

The MFRC522 library contains two files: ``MFRC522.py`` and ``SimpleMFRC522.py``. 

Among them ``MFRC522.py`` is the realization of RFID RC522 interface, this library handles all the heavy work of communicating with RFID through Pi's SPI interface.

``SimpleMFRC522.py`` takes the ``MFRC522.py`` file and greatly simplifies it by allowing you to deal with only a few functions instead of a few functions.