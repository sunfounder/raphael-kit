.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _1.8_scratch_pi5:

1.8 Service Bell
===================

Today, we will use Micro Switch, speakers, audio amplifier module, Raspberry Pi and scratch to make a service bell.

Tap the Micro Switch to make the service bell sound.

.. image:: img/1.8_header.png

Required Components
------------------------------

In this project, we need the following components. 

.. image:: img/1.8_component.png

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

You can also buy them separately from the links below.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - COMPONENT INTRODUCTION
        - PURCHASE LINK

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_micro_switch`
        - \-
    *   - :ref:`cpn_capacitor`
        - |link_capacitor_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-

Build the Circuit
---------------------

.. image:: img/1.8_fritzing.png


Load the Code and See What Happens
-----------------------------------------

Load the code file (``1.8_service_bell.sb3``) to Scratch 3.

Press the micro switch and the service bell will ring once.

Tips on Sprite
----------------

Select Sprite1 and click **Costumes** in the top left corner; upload **bell1.png** and **bell2.png** from the ``~/raphael-kit/scratch/picture`` path via the **Upload Costume** button; delete the default 2 costumes, and rename the sprite to **bell**.

.. image:: img/1.8_travel1.png

In the **Sounds** option, upload the ``bell.wav`` from the ``~/raphael-kit/scratch/sound`` path to Scratch 3.

.. image:: img/1.8_travel2.png

Tips on Codes
--------------

.. image:: img/1.8_travel3.png
  :width: 400

When pin17 is high (the Micro switch is not pressed), switch the costume of the **bell** sprite to **bell1** (released state).

.. image:: img/1.8_travel4.png
  :width: 400

Press the micro switch, gpio17 is low level. At this time, switch the costume of the **bell** sprite to **bell2** (press state), and play a sound effect through the speaker.
