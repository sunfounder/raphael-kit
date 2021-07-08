1.9 Drumming
================

In this project, we play the drum with a touch switch module.

.. image:: media/1.9_header.png

Required Components
-----------------------

.. image:: media/1.9_component.png

Build the Circuit
---------------------

.. image:: media/1.9_fritzing.png


Load the Code and See What Happens
---------------------------------------

Load the code file (``1.9_drumming.sb3``) to Scratch 3.

When you tap on the touch switch module, you will hear the sound of drums coming from the speaker.


Tips on Sprite
----------------

Delete the default sprite, then find the **Drum-snare** sprite and add it, and change the size to 200.

.. image:: media/1.9_touch1.png

Scratch has a **Music** extension to play instruments and drums, now add it via the **Add Extension** button.

.. image:: media/1.9_touch2.png

Tips on Codes
--------------

.. image:: media/1.9_touch3.png
  :width: 400

When pin17 is low (not tapped on the touch switch module), switch the **Drum-snare** sprite costume to **drum-snare-a**.

.. image:: media/1.9_touch4.png
  :width: 600

When you tap on the touch switch module, gpio17 is low. At this point, the **Drum-snare** sprite costume is switched to **drum-snare-b** and the drum sound played on speaker.