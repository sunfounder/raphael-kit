Audio Configuration
=========================

Change Audio Output
----------------------------

If your speaker have no sound, it may be because the Raspberry Pi has selected the wrong audio output, the correct one should be **Headphones**. You can change the audio output by following these steps.


Enter the following command.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo raspi-config

Select **1 System Options**.

.. image:: media/audio1.jpg

Then **S2 Audio**.

.. image:: media/audio2.jpg

After selecting **1 Headphones**, press ``Enter`` to confirm and select ``Finish`` to exit.

.. image:: media/audio3.jpg

Adjust Volume 
---------------

If you feel that the volume of the speakers is too low, you can adjust it by entering the following command.

.. image:: media/faq1.png

The default page is shown below.

.. image:: media/faq2.png

Press ``F6`` to select **Headphones** mode.

.. image:: media/faq3.png

Then press the arrow keys up and down to adjust the volume level, and press ``ESC`` to exit.

.. image:: media/faq4.png