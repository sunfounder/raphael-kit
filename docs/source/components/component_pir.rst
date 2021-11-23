PIR Motion Sensor Module
============================

.. image:: img/pir_pic.png
    :width: 300
    :align: center

The PIR sensor detects infrared heat radiation that can be used to detect the presence of organisms that emit infrared heat radiation.

The PIR sensor is split into two slots that are connected to a differential amplifier. Whenever a stationary object is in front of the sensor, the two slots receive the same amount of radiation and the output is zero. Whenever a moving object is in front of the sensor, one of the slots receives more radiation than the other , which makes the output fluctuate high or low. This change in output voltage is a result of detection of motion.

.. image:: img/PIR_working_principle.jpg
    :width: 800

After the sensing module is wired, there is a one-minute initialization. During the initialization, module will output for 0~3 times at intervals. Then the module will be in the standby mode. Please keep the interference of light source and other sources away from the surface of the module so as to avoid the misoperation caused by the interfering signal. Even you'd better use the module without too much wind, because the wind can also interfere with the sensor.

.. image:: img/pir_back.png
    :width: 600
    :align: center

**Distance Adjustment**

Turning the knob of the distance adjustment potentiometer clockwise, the range of sensing distance increases, and the maximum sensing distance range is about 0-7 meters. If turn it anticlockwise, the range of sensing distance is reduced, and the minimum sensing distance range is about 0-3 meters.

**Delay adjustment**

Rotate the knob of the delay adjustment potentiometer clockwise, you can also see the sensing delay increasing. The maximum of the sensing delay can reach up to 300s. On the contrary, if rotate it anticlockwise, you can shorten the delay with a minimum of 5s. 

**Two Trigger Modes**

Choosing different modes by using the jumper cap.

* **H**: Repeatable trigger mode, after sensing the human body, the module outputs high level. During the subsequent delay period, if somebody enters the sensing range, the output will keep being the high level.

* **L**: Non-repeatable trigger mode, outputs high level when it senses the human body. After the delay, the output will change from high level into low level automatically. 

**Example**

* :ref:`2.2.7_c` (C Project)
* :ref:`2.2.7_py` (Python Project)
* :ref:`4.1.4 Automatic Capture Camera` (Python Project)
* :ref:`1.5 Wake up the Owl` (Scratch Project)

