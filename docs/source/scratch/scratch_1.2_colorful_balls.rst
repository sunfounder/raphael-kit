.. _1.2_scratch:

1.2 Colorful Balls
=====================


Clicking on different colored balls on the stage area will cause the RGB LED to light up in different colors.

.. image:: img/1.2_header.png

Required Components
------------------------------

In this project, we need the following components. 

.. image:: img/1.2_list.png

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

    *   - :ref:`gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`breadboard`
        - |link_breadboard_buy|
    *   - :ref:`wires`
        - |link_wires_buy|
    *   - :ref:`resistor`
        - |link_resistor_buy|
    *   - :ref:`rgb_led`
        - |link_rgb_led_buy|

Build the Circuit
---------------------

.. image:: img/1.2_image61.png


Load the Code and See What Happens
-----------------------------------------

After loading the code file (``1.2_colorful_balls.sb3``) into Scratch 3, the RGB LED will light up yellow, blue, red, green or purple respectively when you click on the corresponding ball.

Tips on Sprites
----------------

Delete the default sprite, then choose the **Ball** sprite.

.. image:: img/1.2_ball.png

And duplicate it 5 times.

.. image:: img/1.2_duplicate_ball.png

Choose different costumes for these 5 **Ball** sprites and move them to the corresponding positions.

.. image:: img/1.2_rgb1.png

Tips on Codes
--------------
Before understanding the code, we need to understand the `RGB color model <https://en.wikipedia.org/wiki/RGB_color_model>`_.

The RGB color model is an additive color model in which red, green, and blue light are added together in various ways to reproduce a broad array of colors. 

Additive color mixing: adding red to green yields yellow; adding green to blue yields cyan; adding blue to red yields magenta; adding all three primary colors together yields white.

.. image:: img/1.2_rgb_addition.png
  :width: 400

An RGB LED is a combination of 3 LEDs(red LED, green LED, blue LED ) in just one package, you can produce almost any color by combining those three colors.
It has 4 pins, one of which is GND, and the other 3 pins control 3 LEDs respectively.

So the code to make the RGB LED light yellow is as follows.

.. image:: img/1.2_rgb3.png


When the Ball sprite (yellow ball) is clicked, we set gpio17 high (red LED on), gpio18 high (green LED on) and gpio27 low (blue LED off) so that the RGB LED will light yellow.

You can Write codes to other sprites in the same way to make the RGB LEDs light up in the corresponding colors.


