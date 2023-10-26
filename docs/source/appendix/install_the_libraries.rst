.. _install_the_libraries:

Bibliotheken installieren
==========================

Für C-Nutzer
--------------

BCM2835
~~~~~~~~~~~~~~~
Dies ist eine C-Bibliothek für den Raspberry Pi (RPi). Sie ermöglicht den Zugriff auf GPIO und andere IO-Funktionen auf dem Broadcom BCM 2835-Chip, wie er im RaspberryPi verwendet wird. Damit kann auf die GPIO-Pins am 26-poligen IDE-Stecker auf der RPi-Platine zugegriffen werden, um verschiedene externe Geräte zu steuern und mit ihnen zu kommunizieren.

Die Bibliothek bietet Funktionen zum Lesen digitaler Eingänge, zum Setzen digitaler Ausgänge, zum Verwenden von SPI und I2C und zum Zugreifen auf die Systemtimer. Pin-Ereigniserkennung wird durch Polling unterstützt (Interrupts werden nicht unterstützt).

Funktioniert auf allen Versionen bis einschließlich RPI 4. Kompatibel mit allen Debian-Versionen bis einschließlich Debian Buster 10.

Öffnen Sie ein Terminal und laden Sie die ``bcm2835``-Bibliothek in den ``~``-Pfad herunter.

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~
    wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.69.tar.gz

Entpacken Sie das Paket.

.. raw:: html

   <run></run>

.. code-block:: 

    tar zxvf bcm2835-1.69.tar.gz

Installieren Sie die BCM2835-Bibliothek mit den folgenden Befehlen.

.. raw:: html

   <run></run>

.. code-block:: 

    cd bcm2835-1.69
    ./configure
    make
    sudo make check
    sudo make install

* Referenz: `bcm2835 <http://www.airspayce.com/mikem/bcm2835/>`_  


Für Python-Nutzer
----------------------

Luma.LED_Matrix
~~~~~~~~~~~~~~~~~~~~~~~

Dies ist eine Python 3-Bibliothek für die Ansteuerung von LED-Matrix-Displays mit dem MAX7219-Treiber (über SPI), WS2812 (NeoPixels, einschließlich Pimoroni Unicorn pHat/Hat und Unicorn Hat HD) und APA102 (DotStar) auf dem Raspberry Pi und anderen Linux-basierten Einplatinencomputern.

Zuerst die Abhängigkeiten für die Bibliothek installieren:

.. raw:: html

   <run></run>

.. code-block:: 

    sudo usermod -a -G spi,gpio pi
    sudo apt install build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5

.. note:: warning

    Das standardmäßig mit apt auf Raspbian gebündelte pip und setuptools sind sehr alt und können dazu führen, dass Komponenten nicht ordnungsgemäß installiert werden. Stellen Sie sicher, dass sie aktuell sind, indem Sie sie zuerst aktualisieren:

    .. raw:: html

       <run></run>

    .. code-block:: 

        sudo -H pip install --upgrade --ignore-installed pip setuptools

Fahren Sie fort und installieren Sie die neueste Version der luma.led_matrix-Bibliothek direkt von PyPI:

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 -m pip install --upgrade luma.led_matrix

* Referenz: `Luma.LED_Matrix <https://luma-led-matrix.readthedocs.io/en/latest/install.html>`_

Spidev und MFRC522
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Die ``spidev``-Bibliothek unterstützt die Interaktion mit SPI und ist eine Schlüsselkomponente dieses Tutorials, da wir sie für die Interaktion des Raspberry Pi mit dem RFID RC522 benötigen.

Führen Sie den folgenden Befehl aus, um ``spidev`` über ``pip`` auf Ihrem Raspberry Pi zu installieren.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install spidev

Fahren Sie mit der Installation der MFRC522-Bibliothek fort.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install mfrc522

Die MFRC522-Bibliothek enthält zwei Dateien: ``MFRC522.py`` und ``SimpleMFRC522.py``. 

``MFRC522.py`` ist die Implementierung der RFID RC522-Schnittstelle. Diese Bibliothek übernimmt die gesamte Arbeit bei der Kommunikation mit RFID über die SPI-Schnittstelle des Pi.

``SimpleMFRC522.py`` vereinfacht die ``MFRC522.py``-Datei erheblich, indem sie Ihnen ermöglicht, nur mit einigen wenigen Funktionen statt vielen zu arbeiten.
