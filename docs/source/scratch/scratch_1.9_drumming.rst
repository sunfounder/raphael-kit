.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _1.9_scratch:

1.9 Drumming
================

In this project, we play the drum with a touch switch module.

.. image:: img/1.9_header.png

Required Components
------------------------------

In this project, we need the following components. 

.. image:: img/1.9_component.png

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

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_touch_switch`
        - |link_touch_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-

Build the Circuit
---------------------

.. image:: img/1.9_fritzing.png


Load the Code and See What Happens
---------------------------------------

Load the code file (``1.9_drumming.sb3``) to Scratch 3.

When you tap on the touch switch module, you will hear the sound of drums coming from the speaker.


Tips on Sprite
----------------

Delete the default sprite, then find the **Drum-snare** sprite and add it, and change the size to 200.

.. image:: img/1.9_touch1.png

Scratch has a **Music** extension to play instruments and drums, now add it via the **Add Extension** button.

.. image:: img/1.9_touch2.png

Tips on Codes
--------------

.. image:: img/1.9_touch3.png
  :width: 400

When pin17 is low (not tapped on the touch switch module), switch the **Drum-snare** sprite costume to **drum-snare-a**.

.. image:: img/1.9_touch4.png
  :width: 600

When you tap on the touch switch module, gpio17 is low. At this point, the **Drum-snare** sprite costume is switched to **drum-snare-b** and the drum sound played on speaker.