1.6 Vanishing Vase
========================

Now let's do a little magic trick, do nothing, and then the vase somehow disappears.

.. image:: media/1.6_header.png

Required Components
-----------------------

.. image:: media/1.6_component.png

* :ref:`GPIO Extension Board`
* :ref:`Breadboard`
* :ref:`Reed Switch Module`

Build the Circuit
---------------------

.. image:: media/1.6_fritzing.png

Load the Code and See What Happens
---------------------------------------

Load the code file (``1.6_vanishing_vase.sb3``) to Scratch 3.

When you use a magnet near the reed switch module, a vase will appear on the stage, take away the magnet and the vase will disappear.

Tips on Sprite
----------------

Select Sprite1 and click **Costumes** in the top left corner; upload **desk1.png** and **desk2.png** from the ``home/pi/raphael-kit/scratch/picture`` path via the **Upload Costume** button; delete the default 2 costumes, and rename the sprite to **desk**.

.. image:: media/1.6_vase.png

Tips on Codes
--------------

.. image:: media/1.6_reed2.png
  :width: 400

When the magnet is close to the reed switch module, gpio17 is low, and the costume of the **desk** sprite is switched to **desk1** (the vase is still on the desk).

.. image:: media/1.6_reed3.png
  :width: 400

After taking away the magnet, gpio17 is high, at this time the costume of the **desk** sprite is switched to **desk2** (only one desk).
