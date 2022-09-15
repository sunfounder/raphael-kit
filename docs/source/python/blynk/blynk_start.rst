.. _bk_start:

Get Start with Blynk
=========================

You will learn how to use Blynk in this project.

In the event that you trigger widgets on Blynk, your Raspberry Pi will print out their values.

Follow the steps below, and note that you must do them in order and not skip any chapters.

.. note:: Before starting this project, you have to :ref:`bk_config`. 


1. Configuring the Blynk
--------------------------



1. Go to the `BLYNK <https://blynk.io/>`_ and click **START FREE**. 

    .. image:: img/sp220607_142551.png

#. Fill in your email address to register an account.

    .. image:: img/sp220607_142807.png

#. Go to your email address to complete your account registration.

    .. image:: img/sp220607_142936.png

#. Afterwards, **Blynk Tour** will appear and you can read it to learn the basic information about the Blynk.

    .. image:: img/sp220607_143244.png

#. Next we need to create a template and device, click **Cancel**.

    .. image:: img/sp220607_143608.png

#. Go to Template from the navigation bar.

    .. image:: img/sp220913_170029.png

#. Create New Template

    .. image:: img/sp220913_170206.png


#. Fill in **NAME**, feel free to do so; **HARDWARE** should be **Raspberry Pi**. Then **Done**.

    .. image:: img/sp220913_170402.png


#. You will be redirected to the Info page, just click on save in the top right corner.

    .. image:: img/sp220913_171202.png

#. Go to **Search** page from the navigation bar.

    .. image:: img/sp220913_172727.png

#. Create New Device.

    .. image:: img/sp220913_173259.png

#. From template.

    .. image:: img/sp220913_173350.png

#. Select **TEMPLATE** as the one you just set, **DEVICE NAME** can be customized. Then click Create.

    .. image:: img/sp220913_173507.png


#. You should now see a page like this one, which means that your initial Blynk setup is complete.

    .. image:: img/sp220913_173950.png


2. Edit Dashboard
--------------------------------


1. Click on the menu icon in the upper right corner and select edit dashboard.

    .. image:: img/sp220913_180231.png

#. Then drag any CONTROL Widgets you want onto the Dashboard. I dragged a Switch and a Slider.

    .. image:: img/sp220913_180725.png

#. Tap the setting icon on the widget.

    .. image:: img/sp220913_180806.png

#. Create Datastream, select Virtual Pin。

    .. image:: img/sp220913_180906.png

#. Complete the datastream setup. Here is the datastream created for Switch, so **DATA TYPE** select ``Interger``, **MIN** and **MAX** set to ``0`` and ``1``. Create and then Save.

    .. image:: img/sp220913_181113.png

#. Use the same steps to create a Datastream for the slider widget, and again, modify **DATA TYPE**, **MIN** and **MAX** to what you need.

    .. image:: img/sp220913_182042.png

#. When finished, click Save And Apply at the top right.

    .. image:: img/sp220913_182300.png


3. Install the Blynk library
------------------------------

Run the following command to install.

.. raw:: html

   <run></run>

.. code-block::

    cd /home/pi
    git clone https://github.com/vshymanskyy/blynk-library-python.git
    cd blynk-library-python
    sudo python3 setup.py

4. Download the Example
-----------------------


We have provided some examples, please run the following command to download them.

.. raw:: html

   <run></run>

.. code-block:: 

    cd /home/pi
    git clone https://github.com/sunfounder/blynk-raspberrypi-python.git


5. Run the Code
-----------------



1. Go to Blynk's Device Info page, you will see some information under **FIRMWARE CONFIGURATION**, you need to copy **BLYNK_AUTH_TOKEN** down.

    .. image:: img/sp220913_182456.png

2. Edit the code.

.. raw:: html

    <run></run>

.. code-block:: 

    cd /home/pi/blynk-raspberrypi-python
    sudo nano blynk_start.py

3. Find the line below and past your ``BLYNK_AUTH_TOKEN``.

.. code-block:: 

    BLYNK_AUTH = 'YourAuthToken'

4. Run the code.

.. raw:: html

    <run></run>

.. code-block:: 

    sudo python3 blynk_start.py

5. Go to Blynk, and operate the widget on Dashboard.

    .. image:: img/sp220913_183529.png

6. Now you will be able to see your actions on the terminal.

.. code-block:: 

    ..
       ___  __          __
      / _ )/ /_ _____  / /__
     / _  / / // / _ \/  '_/
    /____/_/\_, /_//_/_/\_\
            /___/ for Python v1.0.0 (linux)

    Connecting to blynk.cloud:443...
    Blynk ready. Ping: 142 ms
    V0 value: ['1']
    V0 value: ['0']
    V1 value: ['3']
    V1 value: ['8']
    V0 value: ['1']







