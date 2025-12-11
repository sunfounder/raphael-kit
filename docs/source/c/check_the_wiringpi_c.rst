.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!


.. _install_wiringpi:

Install and Check the WiringPi
=======================================

``wiringPi`` is a C language GPIO library applied to the Raspberry Pi. It complies with GUN Lv3. The functions in wiringPi are
similar to those in the wiring system of Arduino. They enable the users
familiar with Arduino to use wiringPi more easily.

``wiringPi`` includes lots of GPIO commands which enable you to control all
kinds of interfaces on Raspberry Pi. 

Please run the following command to install ``wiringPi`` library.



.. raw:: html

   <run></run>

.. code-block::

    sudo apt-get update
    git clone https://github.com/WiringPi/WiringPi
    cd WiringPi 
    ./build

You can test whether the wiringPi
library is installed successfully or not by the following instruction.

.. raw:: html

   <run></run>

.. code-block::

    gpio -v

.. image:: ../img/image30.png


Check the GPIO with the following command:

.. raw:: html

   <run></run>

.. code-block::

    gpio readall

.. image:: ../img/image31.png


For more details about wiringPi, you can refer to `WiringPi <https://github.com/WiringPi/WiringPi>`_.


