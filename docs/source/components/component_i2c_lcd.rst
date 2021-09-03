I2C LCD1602
==============

.. image:: img/i2c_lcd1602.png
    :width: 800

* **GND**: Ground
* **VCC**: Voltage supply, 5V.
* **SDA**: Serial data line. Connect to VCC through a pullup resistor.
* **SCL**: Serial clock line. Connect to VCC through a pullup resistor.

As we all know, though LCD and some other displays greatly enrich the man-machine interaction, they share a common weakness. When they are connected to a controller, multiple IOs will be occupied of the controller which has no so many outer ports. Also it restricts other functions of the controller. 

Therefore, LCD1602 with an I2C module is developed to solve the problem. The I2C module has a built-in PCF8574 I2C chip that converts I2C serial data to parallel data for the LCD display.        

* `PCF8574 Datasheet <https://www.ti.com/lit/ds/symlink/pcf8574.pdf?ts=1627006546204&ref_url=https%253A%252F%252Fwww.google.com%252F>`_

Backlight can be enabled by jumper cap, unplugg the jumper cap to disable the backlight. The blue potentiometer on the back is used to adjust the contrast (the clarity of the displayed text), which is increased in the clockwise direction and decreased in the counterclockwise direction.

The default address is basically 0x27, in a few cases it may be 0x3F, which can be known by test (:ref:`I2C Configuration`).

Taking the default address of 0x27 as an example, the device address can be modified by shorting the A0/A1/A2 pads; in the default state, A0/A1/A2 is 1, and if the pad is shorted, A0/A1/A2 is 0.

.. image:: img/i2c_address.jpg
    :width: 600

**Example**

* :ref:`1.1.7 I2C LCD1602` (C Project)
* :ref:`3.1.3 Reversing Alarm` (C Project)
* :ref:`3.1.7 Overheat Monitor` (C Project)
* :ref:`3.1.8 Password Lock` (C Project)
* :ref:`3.1.11 GAME– Guess Number` (C Project)
* :ref:`1.1.7 I2C LCD1602` (Python Project)
* :ref:`4.1.9 Reversing Alarm` (Python Project)
* :ref:`4.1.13 Overheat Monitor` (Python Project)
* :ref:`4.1.14 Password Lock` (Python Project)
* :ref:`4.1.17_python` (Python Project)
