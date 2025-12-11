.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _1.11_scratch_pi5:

1.11 Repelling locusts
========================


Today, we will use IR obstacle avoidance module, Raspberry Pi and Scratch to make a locust repelling game.

Place your hand in front of the obstacle avoidance module and you will see the locusts being chased away.

.. image:: img/1.11_header.png

Required Components
------------------------------

In this project, we need the following components. 

.. image:: img/1.11_component.png

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
    *   - :ref:`cpn_avoid_module`
        - |link_obstacle_avoidance_buy|

Build the Circuit
----------------------

.. image:: img/1.11_fritzing.png
    :width: 700
    :align: center

Load the Code and See What Happens
----------------------------------------

Load the code file (``1.11_repelling_locusts.sb3``) to Scratch 3.

Place your hand in front of the obstacle avoidance module and you will see the locusts being chased away.


Tips on Sprite
----------------

Select Sprite1 and click **Costumes** in the top left corner; upload **locust1.png**, **locust1.png** and **locust3.png** from the ``~/raphael-kit/scratch/picture`` path via the **Upload Costume** button; delete the default 2 costumes, and rename the sprite to **locust**.

.. image:: img/1.11_ir1.png

Tips on Codes
--------------

.. image:: img/1.11_ir2.png
  :width: 400

When the IR obstacle avoidance module does not detect an obstacle (no hand is placed in front of the probe), the gpio is high.

.. image:: img/1.11_ir3.png
  :width: 400

When gpio17 is high (no obstacles go in front of the IR obstacle avoidance module), switch the locust sprite's costume to locust1 (locusts gather in wheat). Conversely when gpio17 is low (put your hand in front of the IR obstacle avoidance module), switch the locust sprite's costume to locust2 (expel locusts), then switch the locust sprite's costume to locust3 (locusts are completely expelled) after 0.5s.

