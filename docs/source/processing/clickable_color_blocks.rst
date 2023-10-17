.. _clickable_color_blocks:

Clickable Color Blocks
=======================

We've already tried drawing a clickable dot to control the LED, so let's take it a step further and draw 3 colored squares to adjust the RGB colors!

.. image:: img/colorful_square.png

**Required Components**

In this project, we need the following components.

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
    *   - :ref:`rgb_led`
        - |link_rgb_led_buy|

**Wiring**

.. image:: img/image61.png

**Sketch**

.. code-block:: arduino

    import processing.io.*; // use the GPIO library

    int[] pins = { 17, 18, 27 };

    void setup() {
        for (int i = 0; i < pins.length; i++) {
            GPIO.pinMode(pins[i], GPIO.OUTPUT);
        }
        size(300, 100);
        background(255);
    }

    void draw() {
        fill(255, 0, 0);
        rect(0, 0, width/3, height);

        fill(0,255,0);
        rect(width/3, 0, 2*width/3, height);

        fill(0,0,255);
        rect(2*width/3, 0, width, height);
    }

    void mouseClicked() {
        for (int i = 0; i < pins.length; i++) {
            GPIO.digitalWrite(pins[i],GPIO.LOW);
        }
        if (mouseX<width/3){
            GPIO.digitalWrite(pins[0],GPIO.HIGH);
        }else if (mouseX>width/3&&mouseX<2*width/3){
            GPIO.digitalWrite(pins[1],GPIO.HIGH);
        }else if (mouseX>2*width/3){
            GPIO.digitalWrite(pins[2],GPIO.HIGH);
        }        
    }


**How it works?**

This project has a lot in common with :ref:`clickable_dot`, except that it refines the conditions for determining mouse click event.

First draw three color blocks in ``draw()``, then get which color block was clicked based on the value of mouseX (the X-axis coordinate of the mouse), and finally make RGB light up the corresponding color.

**What more?**

Based on the addition of light, we can make RGB LED display seven colors - adding red to green produces yellow; adding all three primary colors together produces white.
Now you can try it out for yourself.