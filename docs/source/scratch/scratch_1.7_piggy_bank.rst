1.7 Piggy Bank
=========================

In this project we will use Speed sensor module, Raspberry Pi and Scratch to make a Piggy Bank.

Place a piece of paper in the middle of the Speed sensor module and you will see a coin fall into the Piggy Bank on the stage.


.. image:: img/1.7_header.png

Required Components
-----------------------

.. image:: img/1.7_component.png

* :ref:`GPIO Extension Board`
* :ref:`Breadboard`
* :ref:`Speed Sensor Module`

Build the Circuit
---------------------

.. image:: img/1.7_fritzing.png

Load the Code and See What Happens
---------------------------------------

Load the code file (``1.7_piggy_bank.sb3``) to Scratch 3.

The 2 terminals in the middle of the speed sensor, one is to send light, one is to receive light; if you put a piece of paper in the middle to isolate the light transmission, thus the speed sensor will output a high level. At this point Scratch receives the high level, then switch the costumes of the sprite and you will see a coin fall into the Piggy Bank on the stage.

Tips on Sprite
----------------

Select Sprite1 and click **Costumes** in the top left corner; upload **piggybank1.png**, **piggybank2.png** and **piggybank3.png** from the ``home/pi/raphael-kit/scratch/picture`` path via the **Upload Costume** button; delete the default 2 costumes, and rename the sprite to **piggybank**.

.. image:: img/1.7_photoInterrupter1.png

Tips on Codes
--------------

.. image:: img/1.7_code2.png

When pin17 is low (no coins are put in), switch the sprite's costume to **piggybank1**.

.. image:: img/1.7_code3.png

When pin17 is high (a coin is put in), switch the sprite's costume to **piggybank2**, and after 0.5s switch to **piggybank3**, so that we can see a coin falling into the Piggy Bank on the stage.



