.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _audio_configuration:

Audio Configuration
=========================

.. _change_audio_output:

Change Audio Output
----------------------------

If your speaker have no sound, it may be because the Raspberry Pi has selected the wrong audio output, the correct one should be **Headphones**. You can change the audio output by following these steps.


Enter the following command.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo raspi-config

Select **1 System Options**.

.. image:: img/audio1.jpg

Then **S2 Audio**.

.. image:: img/audio2.jpg

After selecting **1 Headphones**, press ``Enter`` to confirm and select ``Finish`` to exit.

.. image:: img/audio3.jpg

.. _adjust_volume:

Adjust Volume 
---------------

If you feel that the volume of the speakers is too low, you can adjust it by entering the following command.

.. raw:: html

   <run></run>

.. code-block:: 

    alsamixer

.. image:: img/faq1.png

The default page is shown below.

.. image:: img/faq2.png

Press ``F6`` to select **Headphones** mode.

.. image:: img/faq3.png

Then press the arrow keys up and down to adjust the volume level, and press ``ESC`` to exit.

.. image:: img/faq4.png