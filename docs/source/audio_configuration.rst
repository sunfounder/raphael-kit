Audio Configuration
=========================

Change Audio Output
----------------------------

If your speaker have no sound, it may be because the Raspberry Pi has selected the wrong audio output, the correct one should be **Headphones**. You can change the audio output by following these steps.


Enter the following command.

.. code-block:: shell

    sudo raspi-config

Select **1 System Options**.

.. image:: media/audio1.png

Then **S2 Audio**.

.. image:: media/audio2.png

After selecting **1 Headphones**, press ``Enter`` to confirm and select ``Finish`` to exit.

.. image:: media/audio3.png

Volume Adjust
---------------

If you feel that the volume of the speakers is too low, you can adjust it by entering the following command.

.. image:: media/faq1.png

The default page is shown below.

.. image:: media/faq2.png

Press ``F6`` to select **Headphones** mode.

.. image:: media/faq3.png

Then press the arrow keys up and down to adjust the volume level, and press ``ESC`` to exit.

.. image:: media/faq4.png