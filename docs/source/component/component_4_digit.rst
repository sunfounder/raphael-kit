.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_4_digit:

4-Digit 7-Segment Display
==================================

4-Digit 7-segment display consists of four 7- segment displays working
together.

.. image:: img/4-digit-sche.png

The 4-digtal 7-segment display works independently. It uses the
principle of human visual persistence to quickly display the characters
of each 7-segment in a loop to form continuous strings.

For example, when "1234" is displayed on the display, "1" is displayed
on the first 7-segment, and "234" is not displayed. After a period of
time, the second 7-segment shows "2", the 1st 3th 4th of 7-segment does
not show, and so on, the four digital display show in turn. This process
is very short (typically 5ms), and because of the optical afterglow
effect and the principle of visual residue, we can see four characters
at the same time.

.. image:: img/image78.png


**Display Codes**

To help you get to know how 7-segment displays(Common Anode) display
Numbers, we have drawn the following table. Numbers are the number 0-F
displayed on the 7-segment display; (DP) GFEDCBA refers to the
corresponding LED set to 0 or 1, For example, 11000000 means that DP and
G are set to 1, while others are set to 0. Therefore, the number 0 is
displayed on the 7-segment display, while HEX Code corresponds to
hexadecimal number.

.. image:: img/common_anode.png

**Example**

* :ref:`1.1.5_c` (C Project)
* :ref:`3.1.1_c` (C Project)
* :ref:`3.1.6_c` (C Project)
* :ref:`3.1.12_c` (C Project)
* :ref:`1.1.5_py` (Python Project)
* :ref:`4.1.3_py` (Pyhton Project)
* :ref:`4.1.7_py` (Pyhton Project)
* :ref:`4.1.12_py` (Pyhton Project)
* :ref:`4.1.18_py` (Pyhton Project)

