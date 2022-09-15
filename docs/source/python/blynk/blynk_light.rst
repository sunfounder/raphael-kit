Smart Light
===========

In this project, we use Blynk's Silder to control the brightness of the LED, turning it on and off with Switch.

.. note:: Before starting this project, we recommend that you complete :ref:`bk_start`. The following will give you a clear understanding of Blynk.


**1. Wiring**

.. image:: img/wiring_led1.png

**2. Create Widget and Datastream**

1. Click on the menu icon in the upper right corner and select edit dashboard.

    .. image:: img/sp220913_180231.png

2. Add a Switch widget and a Slider widget to the Dashboard.

    .. image:: img/sp220914_160427.png

3. Create a Datastream for the Switch widget (I used V3). It will be used to control the turning on and off of the LED.

    .. image:: img/sp220914_155911.png

4. Create a Datastream for the Slider widget (I used V2), its value range is 0 to 100, it will be used to control the brightness of the LED.

    .. image:: img/sp220914_160234.png

#. When finished, click Save And Apply at the top right.

    .. image:: img/sp220913_182300.png


**3. Run the Code**

1. Edit the code

.. raw:: html

   <run></run>

.. code-block:: 

    cd /home/pi/blynk-raspberrypi-python
    sudo nano blynk_light.py

2. Find the line below and past your ``BLYNK_AUTH_TOKEN``.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Run the code.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_light.py

4. Go to Blynk, operate widget on Dashboard. now you click switch widget will turn on/off LED. slide Slider widget will change LED brightness.

#. If you want to use Blynk on mobile devices, please refer to :ref:`blynk_mobile`.