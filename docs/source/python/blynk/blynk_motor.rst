.. _blynk_motor_py:

Smart Fan
===========

In this project, you can see the temperature from Blynk and turn on the fan remotely.

.. note:: Before starting this project, we recommend that you complete :ref:`bk_start_py`. The following will give you a clear understanding of Blynk.

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
    *   - :ref:`resistor`
        - |link_resistor_buy|
    *   - :ref:`power_module`
        - \-
    *   - :ref:`l293d`
        - \-
    *   - :ref:`adc0834`
        - \-
    *   - :ref:`thermistor`
        - |link_thermistor_buy|
    *   - :ref:`motor`
        - |link_motor_buy|

**1. Wiring**

.. image:: img/wiring_blynk_motor.png


**2. Create Widget and Datastream**

1. Click on the menu icon in the upper right corner and select edit dashboard.

    .. image:: img/sp220913_180231.png

2. Add a Switch widget and a Label widget to the Dashboard.

    .. image:: img/sp220914_175437.png

3. Create a Datastream (I used V3) for the Switch widget. It will be used to turn on the Motor.

    .. image:: img/sp220914_155911.png

4. Create a Datastream for the Label widget(I used V0). It will be used to display the temperature. Set **DATA TYPE** to String.

    .. image:: img/sp220914_175616.png

#. When finished, click Save And Apply at the top right.

    .. image:: img/sp220913_182300.png


**3. Run the Code**

1. Edit the code

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_motor.py

2. Find the line below and past your ``BLYNK_AUTH_TOKEN``.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Run the code.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_motor.py

4. Go to Blynk, on the Dashboard you can check the temperature via Label widget; you can turn on/off the fan via Switch widget.

#. If you want to use Blynk on mobile devices, please refer to :ref:`blynk_mobile`.