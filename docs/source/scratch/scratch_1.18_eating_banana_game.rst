.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _1.18_scratch:

1.18 Eating Banana Game
================================

Description
---------------

Scratch has a Video Sensing expansion module, which can turn on the camera in Scratch and detect the movement of objects on the camera screen.

Today, we will use the camera to make a eating banana game. In the stipulated time, help the Monkey eat more bananas.

To play the game against a white background, click on the green flag to start. Move colored objects in front of the camera to control the Monkey sprite.

.. image:: img/1.18_header.png

Required Components
------------------------------

In this project, we need the following components. 

.. image:: img/1.18_photo1.png

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

    *   - :ref:`cpn_camera_module`
        - |link_camera_buy|


Build the Circuit
--------------------

.. image:: img/1.10_camera.png

.. note::

    You need to refer to :ref:`cpn_camera_module` to connect the camera module and enable the Raspberry Pi camera interface.

Load the Code and See What Happens
---------------------------------------

Load the code file (``1.18_eating_banana_game.sb3``) to Scratch 3.

Tips on Codes
----------------

Arrange monkeys and bananas

First, we delete the original sprite, then add Monkey sprite and Bananas sprite, and change their sizes to 50.

Let Bananas appear randomly.

.. image:: img/1.18_code1.png

Bananas disappears after encountering the Monkey, which means it was eaten by the Monkey and reappears randomly.

.. image:: img/1.18_code2.png

Let the Monkey appear in the center of the stage and initialize the camera data (transparency is set to 20).

.. image:: img/1.18_code3.png

If the camera detects an object moving, let the Monkey move towards the object.

.. image:: img/1.18_code4.png

Now, click on the green flag at the top of the stage area to start the game.

Let the Monkey eat bananas, it is very hungry! Try to play this game on a white background to prevent interference from other objects.

Challenge
-------------

I believe that you will be smart enough to program and implement this game soon. Next, we will add some challenges to enrich our game content.

· When Monkey eats banana, we add 1 to the score. Within 30s, see who has the highest score!

· When Monkey eats a banana, it emits a suitable sound effect.