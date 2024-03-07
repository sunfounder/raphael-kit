.. _1.10_scratch:

1.10 Drumming in the Air
==========================

Today we will learn to use the Raspberry Pi camera, Scratch has an expansion module for Video Sensing which turns on the camera in Scratch and detects the movement of objects on the stage. 


.. image:: img/1.10_header.png

Required Components
------------------------------

In this project, we need the following components. 

.. image:: img/1.10_list.png

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

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-
    *   - :ref:`cpn_camera_module`
        - |link_camera_buy|

Build the Circuit
-------------------------

.. image:: img/1.10_fritzing_speaker.png

.. image:: img/1.10_camera.png

.. note::
  
  You need to refer to :ref:`cpn_camera_module` to connect the camera module and enable the Raspberry Pi camera interface.


Load the Code and See What Happens
----------------------------------------

Load the code file (``1.10_drumming_in_the_air.sb3``) to Scratch 3.

Click on the green flag to start the game, place your hand in front of the camera module and Scratch 3 will make instrument sounds when your hand is shown touching an instrument on the stage area.

.. note::

  For a better gaming experience, please try to play on a white background to avoid interference with the camera from other objects.

Tips on Sprite
----------------

First delete the default sprites, then find the **Drum-cymbal** sprite and **Drum-snare** sprite and add them.

.. image:: img/1.10_camera1.png

Click the **Add Extension** icon at the bottom left of Scratch and add the **Music** and **Video Sensing** extensions to it.

.. image:: img/1.10_scratch.png

.. image:: img/1.10_scratch2.png

Tips on Codes
--------------

.. image:: img/1.10_camera3.png

When the green flag is clicked, it keeps cycling to detect if our hand is moving over the **Drum-cymbal** sprite by more than 60. if so, it is assumed that our hand touched the sprite, at which point the Open Hi-Hat instrument sound is played.

.. note::

  The movement magnitude refers to the change in coordinates on the stage area, which is calculated with respect to the amount of change in the coordinates of the detection target on the stage area.

.. image:: img/1.10_camera4.png

Similarly, if the movement of our hand on the **Drum-snare** sprite is detected to be greater than 60, our hand is considered to have touched the sprite and the sound of the snare drum instrument is played.

