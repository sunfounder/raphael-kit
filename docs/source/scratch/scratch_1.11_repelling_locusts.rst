1.11 Repelling locusts
========================


Today, we will use IR obstacle avoidance module, Raspberry Pi and Scratch to make a locust repelling game.

Place your hand in front of the obstacle avoidance module and you will see the locusts being chased away.

.. image:: media/1.11_header.png

Required Components
-----------------------

.. image:: media/1.11_component.png

Build the Circuit
----------------------

.. image:: media/1.11_fritzing.png
    :width: 700
    :align: center

Load the Code and See What Happens
----------------------------------------

Load the code file (``1.11_repelling_locusts.sb3``) to Scratch 3.

Place your hand in front of the obstacle avoidance module and you will see the locusts being chased away.


Tips on Sprite
----------------

Select Sprite1 and click **Costumes** in the top left corner; upload **locust1.png**, **locust1.png** and **locust3.png** from the ``home/pi/raphael-kit/scratch/picture`` path via the **Upload Costume** button; delete the default 2 costumes, and rename the sprite to **locust**.

.. image:: media/1.11_ir1.png

Tips on Codes
--------------

.. image:: media//1.11_ir2.png
  :width: 400

When the IR obstacle avoidance module does not detect an obstacle (no hand is placed in front of the probe), the gpio is high.

.. image:: media//1.11_ir3.png
  :width: 400

When gpio17 is high (no obstacles go in front of the IR obstacle avoidance module), switch the locust sprite's costume to locust1 (locusts gather in wheat). Conversely when gpio17 is low (put your hand in front of the IR obstacle avoidance module), switch the locust sprite's costume to locust2 (expel locusts), then switch the locust sprite's costume to locust3 (locusts are completely expelled) after 0.5s.

