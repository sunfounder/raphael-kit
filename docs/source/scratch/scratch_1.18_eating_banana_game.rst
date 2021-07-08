1.18 Eating Banana Game
~~~~~~~~~~~~~~~~~~~~~~~~

Description
---------------

Scratch has a Video Sensing expansion module, which can turn on the camera in Scratch and detect the movement of objects on the camera screen.

Today, we will use the camera to make a eating banana game. In the stipulated time, help the Monkey eat more bananas.

To play the game against a white background, click on the green flag to start. Move colored objects in front of the camera to control the Monkey sprite.

.. image:: media/1.18_header.png

Required Components
-----------------------

.. image:: media/1.18_photo1.png

Build the Circuit
--------------------

.. image:: media/1.10_camera.png

.. note::

    You need to refer to :ref:`Camera Module Installation` to connect the camera module and enable the Raspberry Pi camera interface.

Load the Code and See What Happens
---------------------------------------

Load the code file (``1.18_eating_banana_game.sb3``) to Scratch 3.

Tips on Codes
----------------

Arrange monkeys and bananas

First, we delete the original sprite, then add Monkey sprite and Bananas sprite, and change their sizes to 50.

Let Bananas appear randomly.

.. image:: media/1.18_code1.png

Bananas disappears after encountering the Monkey, which means it was eaten by the Monkey and reappears randomly.

.. image:: media/1.18_code2.png

Let the Monkey appear in the center of the stage and initialize the camera data (transparency is set to 20).

.. image:: media/1.18_code3.png

If the camera detects an object moving, let the Monkey move towards the object.

.. image:: media/1.18_code4.png

Now, click on the green flag at the top of the stage area to start the game.

Let the Monkey eat bananas, it is very hungry! Try to play this game on a white background to prevent interference from other objects.

Challenge
-------------

I believe that you will be smart enough to program and implement this game soon. Next, we will add some challenges to enrich our game content.

· When Monkey eats banana, we add 1 to the score. Within 30s, see who has the highest score!

· When Monkey eats a banana, it emits a suitable sound effect.