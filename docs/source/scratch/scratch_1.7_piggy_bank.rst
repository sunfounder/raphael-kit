1.7 Piggy Bank
=========================

In this project we will use Speed sensor module, Raspberry Pi and Scratch to make a Piggy Bank.

Place a piece of paper in the middle of the Speed sensor module and you will see a coin fall into the Piggy Bank on the stage.


.. image:: img/1.7_header.png

**Required Components**
------------------------------

In this project, we need the following components. 

.. image:: img/1.7_component.png

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

    *   - :ref:`GPIO Extension Board`
        - |link_gpio_board_buy|
    *   - :ref:`Breadboard`
        - |link_breadboard_buy|
    *   - :ref:`Jumper Wires`
        - |link_wires_buy|
    *   - :ref:`Speed Sensor Module`
        - \-

Build the Circuit
---------------------

.. image:: img/1.7_fritzing.png

Load the Code and See What Happens
---------------------------------------

Load the code file (``1.7_piggy_bank.sb3``) to Scratch 3.

The 2 terminals in the middle of the speed sensor, one is to send light, one is to receive light; if you put a piece of paper in the middle to isolate the light transmission, thus the speed sensor will output a high level. At this point Scratch receives the high level, then switch the costumes of the sprite and you will see a coin fall into the Piggy Bank on the stage.

Tips on Sprite
----------------

Select Sprite1 and click **Costumes** in the top left corner; upload **piggybank1.png**, **piggybank2.png** and **piggybank3.png** from the ``~/raphael-kit/scratch/picture`` path via the **Upload Costume** button; delete the default 2 costumes, and rename the sprite to **piggybank**.

.. image:: img/1.7_photoInterrupter1.png

Tips on Codes
--------------

.. image:: img/1.7_code2.png

When pin17 is low (no coins are put in), switch the sprite's costume to **piggybank1**.

.. image:: img/1.7_code3.png

When pin17 is high (a coin is put in), switch the sprite's costume to **piggybank2**, and after 0.5s switch to **piggybank3**, so that we can see a coin falling into the Piggy Bank on the stage.



