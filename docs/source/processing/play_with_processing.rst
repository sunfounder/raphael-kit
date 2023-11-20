.. _play_with_processing:

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

    Before you can use Processing, you need to access the Raspberry Pi desktop remotely (:ref:`windows_remote_desktop`) or connect a display for the Raspberry Pi.

.. Run the following command in Terminal to install Processing.

.. .. raw:: html

..    <run></run>

.. .. code-block:: 

..     curl https://processing.org/download/install-arm.sh | sudo sh

.. Once the installation is complete, type ``processing`` to open it.


.. .. image:: img/processing1.png


.. For a detailed tutorial, please refer to `Pi Processing <https://pi.processing.org/>`_.

#. First visit https://processing.org/download and select the ``Linux（Raspberry Pi 32-bit）`` or ``Linux（Raspberry Pi 64-bit）`` version. Using this method, you can always download the latest version.

    Or you can use the following command to download the Processing from the Terminal.

    .. code-block:: 

        wget https://github.com/benfry/processing4/releases/download/processing-1293-4.3/processing-4.3-linux-arm32.tgz

    .. code-block:: 

        wget https://github.com/benfry/processing4/releases/download/processing-1293-4.3/processing-4.3-linux-arm64.tgz


#. A ``.tar.gz`` file will be downloaded, which most Linux users should be familiar with. Extract the file you just downloaded from its location.

    .. code-block:: 

        tar xvfz processing-xxxx.tgz

    Replace xxxx with the rest of the file's name, which is the version number. This will create a folder named processing-xxxx or something similar. 

#. Then go to that directory:

    .. code-block:: 

        cd processing-xxxx

#. And run it:

.. code-block:: 

    ./processing

#. With any luck, the main Processing window will now be visible.

    .. image:: img/processing2.png


Install Hardware I/O
--------------------

In order to use the Raspberry Pi's GPIO, you need to manually add a `Hardware I/O library <https://processing.org/reference/libraries/io/index.html>`_.

Click ``Sketch`` -> ``Import Library`` -> ``Add Library...`` 

.. image:: img/import-00.png

Find Hardware I/O , select it, and then click Install. When done, a checkmark icon will appear.

.. image:: img/import-02.png


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
