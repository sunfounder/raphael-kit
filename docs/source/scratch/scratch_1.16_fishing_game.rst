.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _1.16_scratch:

1.16 Fishing Game
========================

Today, we will make a fishing game.

Observe the water on the stage area and if you find a fish on the hook, remember to tilt the switch to catch it.

.. image:: img/1.16_header.png

Required Components
------------------------------

In this project, we need the following components. 

.. image:: img/1.16_component.png

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
    *   - :ref:`cpn_tilt_switch`
        - \-

Build the Circuit
---------------------

.. image:: img/1.16_fritzing.png

Load the Code and See What Happens
---------------------------------------

Load the code file (``1.16_fishing_game.sb3``) to Scratch 3.

You will see a child is fishing, after a period of time when the water surface movement, you can shake the tilt switch to catch the fish.
Remember, if you do not keep shaking the switch, the fish will escape.

Tips on Sprite
----------------

Select Sprite1, click **Costumes** in the upper left corner; upload 6 pictures (**fish1** to **fish6**) from the ``~/raphael-kit/scratch/picture`` path via the **Upload Costume** button; delete the default 2 costumes and rename the sprite to **fish**.

.. image:: img/1.16_upload_fish.png


Tips on Codes
--------------

.. image:: img/1.16_fish2.png
  :width: 400

Set the initial costume of the **fish** sprite to **fish1** and assign the value of **fish_status** to 0 (when **fish_status=0**, it means the fish is not hooked, when **fish_status=1**, it means the fish is hooked).

.. image:: img/1.16_fish3.png
  :width: 400

When **fish_status=0**, i.e. the fish is not hooked yet, start the fishing game. Wait for a random time from 0 to 10 seconds, then assign **fish_status** to 1, which means the fish is hooked, and broadcast a message "The fish is biting".

.. note::

  The purpose of the broadcast block is to send a message to other code blocks or other sprites. The message can be either a request or a command.

.. image:: img/1.16_fish4.png
  :width: 400

When the message "The fish is biting" is received, let the fish sprite switch between the **fish2** and **fish3** costumes so that we can see the fish biting.

.. image:: img/1.16_fish5.png
  :width: 400

After switching the costume, if the game is not over, it means that the fish is off the hook and gone, so that we will switch the **fish** sprite costume to **fish6** (fish slipped state).

.. image:: img/1.16_fish6.png
  :width: 400

When gpio17 is high (the tilt switch is tilted), it means the fishing rod is pulled up. At this time, the value of fish_status is judged. If it is 1, it means that the fishing rod was pulled up when the fish was hooked and switched to fish4 costume (fish was caught). On the contrary, it means that the fishing rod pulled up when the fish is not hooked is switched to the fish5 costume (nothing is caught).

