FAQ
======================

.. _faq_soc:

Si "gpiozero" no funciona.
-------------------------------------------------- ---------------------

El tutorial de Raspberry Pi 5 GPIO Python se basa en la biblioteca gpiozero y se probó exhaustivamente durante el proceso de diseño.

Sin embargo, los cambios recientes en el kernel de Linux en el sistema operativo Raspberry Pi [1] han cambiado la forma en que se manejan las llamadas al sistema GPIO, lo que hace que la biblioteca Python original no pueda acceder a GPIO en Raspberry Pi 5.

Nuestros desarrolladores informaron este problema a la biblioteca gpiozero, y los desarrolladores de gpiozero están al tanto de este problema y están trabajando activamente en las actualizaciones [2].


* [1] https://github.com/raspberrypi/linux/pull/6144
* [2] https://github.com/gpiozero/gpiozero/issues/1166

mientras tanto,
Encontré una solución temporal. Cuando ejecuto el siguiente comando, GPIO funciona bien.

.. code-block::

    sudo ln -s gpiochip0 /dev/gpiochip4

Esta solución funcionará hasta que la biblioteca gpiozero lance un parche adecuado.