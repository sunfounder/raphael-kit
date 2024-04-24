.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_reed_switch:

Reed Switch Module
======================

.. image:: img/reed_switch.png
    :width: 300
    :align: center

* Using normally open type reed switch.
* Comparator output, clean signal, good waveform, strong driving ability, more than 15mA.
* Working voltage: 3.3V-5V
* Output form: digital switch output (0 and 1).
* With fixed bolt holes for easy installation.
* Small board PCB size: 3.2cm x 1.4cm.
* Use wide voltage LM393 comparator.

The reed switch module consists of a reed switch, potentiometer, LM393 comparator, LED, etc. The internal circuit is shown below, when the magnet is close to the module, it will be on, and the module will output low level; when there is no magnetism, it will be off, and output high level. Reed switch and magnet induction distance should be within 1.5cm, beyond will not be sensitive or no trigger phenomenon, you can also adjust the sensitivity through the potentiometer on the module.
    
.. image:: img/reedswitch_sche.jpg
    :width: 600
    :align: center

Reed switch, also known as a magnetic switch or reed switch.

It has two internal metal reeds, sealed in a glass tube, which is filled with inert gas. Normally the two reeds overlap each other, but are separated by a gap, and the circuit is broken. When there is a magnetic object close to the two reeds will produce a mutual attraction of the magnetic force, which will be sucked together, the circuit is connected. Therefore, the reed switch can be used to make a magnetic sensor.
        
.. image:: img/HowItWorksReed.jpg

**Example**

* :ref:`2.2.4_c` (C Project)
* :ref:`2.2.4_py` (Python Project)
* :ref:`4.1.6_py` (Python Project)
* :ref:`1.6_scratch` (Scratch Project)
