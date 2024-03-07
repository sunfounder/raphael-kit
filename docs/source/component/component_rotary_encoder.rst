.. _cpn_rotary_encoder:

Rotary Encoder Module
=============================

.. image:: img/rotary_encoder_pic.png
    :width: 300
    :align: center

A rotary encoder is a position sensor that converts the rotation of a knob into an output signal, indicating the direction in which the knob is turned.

Rotary encoders are digital versions of potentiometers, offering greater versatility. They can rotate continuously, while potentiometers have limited rotation. Potentiometers indicate exact knob position, while rotary encoders show changes in position.

There are mainly two types of rotary encoders: absolute and incremental (relative) encoders. An incremental one is used in this kit.

Incremental encoders produce two-phase square waves, with a 90-degree phase difference commonly referred to as the A and B channels.

As illustrated below, when channel A transitions from a high level to a low level, if channel B is at a high level, it indicates that the rotary encoder is rotating clockwise (CW); if at that moment channel B is at a low level, it means the rotation is counterclockwise (CCW). Therefore, by reading the value of channel B when channel A is at a low level, we can determine the direction in which the rotary encoder rotates.



.. image:: img/image206.png
    :width: 600
    :align: center
	
**Example**

* :ref:`2.1.6_c` (C Project)
* :ref:`2.1.6_py` (Python Project)
