1.8 Service Bell
===================

Today, we will use Micro Switch, speakers, audio amplifier module, Raspberry Pi and scratch to make a service bell.

Tap the Micro Switch to make the service bell sound.

.. image:: media/1.8_header.png

Required Components
-----------------------

.. image:: media/1.8_component.png

* :ref:`GPIO Extension Board`
* :ref:`Breadboard`
* :ref:`Resistor`
* :ref:`Micro Switch`
* :ref:`Capacitor`
* :ref:`Audio Module and Speaker`

Build the Circuit
---------------------

.. image:: media/1.8_fritzing.png


Load the Code and See What Happens
-----------------------------------------

Load the code file (``1.8_service_bell.sb3``) to Scratch 3.

Press the micro switch and the service bell will ring once.

.. note::
  
  If your Raspberry Pi is connected to a screen with speakers, it may cause no sound from this external speaker, please refer to :ref:`Change Audio Output` for the solution.

  Also, if you want to adjust the volume level, please refer to :ref:`Adjust Volume`.

Tips on Sprite
----------------

Select Sprite1 and click **Costumes** in the top left corner; upload **bell1.png** and **bell2.png** from the ``home/pi/raphael-kit/scratch/picture`` path via the **Upload Costume** button; delete the default 2 costumes, and rename the sprite to **bell**.

.. image:: media/1.8_travel1.png

In the **Sounds** option, upload the ``bell.wav`` from the ``home/pi/raphael-kit/scratch/sound`` path to Scratch 3.

.. image:: media/1.8_travel2.png

Tips on Codes
--------------

.. image:: media/1.8_travel3.png
  :width: 400

When pin17 is high (the Micro switch is not pressed), switch the costume of the **bell** sprite to **bell1** (released state).

.. image:: media/1.8_travel4.png
  :width: 400

Press the micro switch, gpio17 is low level. At this time, switch the costume of the **bell** sprite to **bell2** (press state), and play a sound effect through the speaker.
