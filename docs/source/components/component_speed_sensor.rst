.. _speed_sensor:

Speed Sensor Module
========================

.. image:: img/speed_sensor1.png
    :width: 300
    :align: center

The speed sensor consists of two parts: a transmitter and a receiver. The transmitter emits light, which then enters the receiver.

If the light beam between the emitter and receiver is interrupted by an obstacle, the receiver will not detect the incident light, then the D0 pin will output low level.

.. note::
    The A0 pin on this module is empty and there is no circuit.

.. image:: img/speed_sensor2.png

**Example**

* :ref:`2.2.6_c` (C Project)
* :ref:`2.2.6_py` (Python Project)
* :ref:`1.7_scratch` (Scratch Project)