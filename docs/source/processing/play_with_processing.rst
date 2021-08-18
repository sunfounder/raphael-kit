Play with Processing
==========================

What is Processing？
---------------------------

Processing is a simple programming environment that was created to make it easier to develop visually oriented applications with an emphasis on animation and providing users with instant feedback through interaction. 
The developers wanted a means to “sketch” ideas in code. 
As its capabilities have expanded over the past decade, Processing has come to be used for more advanced production-level work in addition to its sketching role. 
Originally built as a domain-specific extension to Java targeted towards artists and designers, Processing has evolved into a full-blown design and prototyping tool used for large-scale installation work, motion graphics, and complex data visualization.

Processing is based on Java, but because program elements in Processing are fairly simple, you can learn to use it even if you don't know any Java. If you're familiar with Java, it's best to forget that Processing has anything to do with Java for a while, until you get the hang of how the API works.


This text is from the tutorial, `Processing Overview <https://processing.org/tutorials/overview/>`_.

Install the Processing
------------------------------

.. note::

    When programming with Processing, you may need a screen for a better experience, refer to: `Connect your Raspberry Pi <https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/3>`_. Of course, if you don't have a screen, you can also access the Raspberry Pi desktop remotely, for a detailed tutorial please refer to :ref:`Remote Desktop`.


Run the following command in Terminal to install Processing.

.. raw:: html

   <run></run>

.. code-block:: 

    curl https://processing.org/download/install-arm.sh | sudo sh


If you think the above method is too slow, you can also download the image directly from the `Processing for Pi <https://pi.processing.org/download/>`_ page.

.. image:: img/processing.png

Once the installation is complete, type ``processing`` to open it.


.. image:: img/processing1.png


For a detailed tutorial, please refer to `Pi Processing <https://pi.processing.org/>`_.

Projects
---------------

.. toctree::
    draw_a_matchmaker
    hello_mouse
    blinking_dot
    clickable_dot
    clickable_color_blocks
    inflating_the_dot
    dot_on_the_swing
    metronome
    show_number
    drag_number
