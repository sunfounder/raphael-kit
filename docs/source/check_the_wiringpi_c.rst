Check the WiringPi
=======================================

wiringPi is a C language GPIO library applied to the Raspberry Pi
platform and the Raspberry Pi OS installs it by default. It complies with GUN Lv3. The functions in wiringPi are
similar to those in the wiring system of Arduino. They enable the users
familiar with Arduino to use wiringPi more easily.

wiringPi includes lots of GPIO commands which enable you to control all
kinds of interfaces on Raspberry Pi. You can test whether the wiringPi
library is installed successfully or not by the following instructions.

.. raw:: html

   <run></run>

.. code-block::

    gpio -v

.. image:: media/image30.png


If you are using Raspberry Pi 4B, but the GPIO version is **2.50**, it will cause no response after the C language code is running, that is, GPIO pins do not work. At this time, you need to manually update to version **2.52**, the update steps are as follows :

.. raw:: html

   <run></run>

.. code-block::

    cd /tmp

    wget https://project-downloads.drogon.net/wiringpi-latest.deb

    sudo dpkg -i wiringpi-latest.deb

Check with:

.. raw:: html

   <run></run>

.. code-block::

    gpio -v

and make sure it’s version 2.52.

.. raw:: html

   <run></run>

.. code-block::

    gpio readall

.. image:: media/image31.png


For more details about wiringPi, you can refer to `WiringPi <http://wiringpi.com/download-and-install/>`_.


