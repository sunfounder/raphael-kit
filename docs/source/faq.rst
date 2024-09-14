FAQ 
===============================


.. _faq_soc:

If ``gpiozero`` doesn't work.
-------------------------------------------------------------------------

Our Raspberry Pi 5 GPIO Python tutorial is based on the gpiozero library, 
and it has been thoroughly tested during the design process. 

However, recent modifications to the Linux kernel on the Raspberry Pi OS [1] have changed the way GPIO system calls are handled, 
which has caused the original Python library to be unable to access GPIO on the Raspberry Pi 5. 
Our developers have reported this issue to the gpiozero library, 
and the gpiozero developers are aware of the issue and are actively working on an update [2]. 

* [1] https://github.com/raspberrypi/linux/pull/6144
* [2] https://github.com/gpiozero/gpiozero/issues/1166

In the meantime, 
we have found a temporary solution: by running the command below, the GPIO will function normally. 

.. code-block::

    sudo ln -s gpiochip0 /dev/gpiochip4

This solution will remain effective until the gpiozero library releases an appropriate fix.

