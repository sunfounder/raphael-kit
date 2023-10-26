.. _install_wiringpi:

Installieren und Überprüfen von WiringPi
===========================================

``wiringPi`` ist eine GPIO-Bibliothek in C für den Raspberry Pi. Sie entspricht GUN Lv3. Die Funktionen in wiringPi ähneln denen im Wiring-System von Arduino. Dies ermöglicht Nutzern, die mit Arduino vertraut sind, die Verwendung von wiringPi leichter zu gestalten.

``wiringPi`` beinhaltet zahlreiche GPIO-Befehle, mit denen Sie alle Arten von Schnittstellen am Raspberry Pi steuern können.

Bitte führen Sie den folgenden Befehl aus, um die ``wiringPi``-Bibliothek zu installieren.

.. raw:: html

   <run></run>

.. code-block::

    sudo apt-get update
    git clone https://github.com/WiringPi/WiringPi
    cd WiringPi 
    ./build

Sie können testen, ob die wiringPi-Bibliothek erfolgreich installiert wurde, indem Sie den folgenden Befehl ausführen.

.. raw:: html

   <run></run>

.. code-block::

    gpio -v

.. image:: ../img/image30.png

Überprüfen Sie die GPIO mit dem folgenden Befehl:

.. raw:: html

   <run></run>

.. code-block::

    gpio readall

.. image:: ../img/image31.png

Für weitere Details über wiringPi können Sie sich auf `WiringPi <https://github.com/WiringPi/WiringPi>`_ beziehen.



