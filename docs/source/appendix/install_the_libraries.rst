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
.. _create_virtual:

Erstellen einer virtuellen Umgebung
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bei Verwendung von Raspberry Pi oder ähnlichen Geräten wird empfohlen, Pakete mit ``pip`` in einer virtuellen Umgebung zu installieren. Diese bietet eine Abhängigkeitsisolierung, erhöht die Systemsicherheit, gewährleistet die Sauberkeit des Systems und erleichtert Projektmigration und -freigabe, was die Abhängigkeitsverwaltung vereinfacht. Diese Vorteile machen virtuelle Umgebungen zu einem äußerst wichtigen und nützlichen Werkzeug in der Python-Entwicklung.

Im Folgenden finden Sie die Schritte zur Erstellung einer virtuellen Umgebung:

**1. Erstellen einer virtuellen Umgebung**

Zunächst müssen Sie sicherstellen, dass Ihr System Python installiert hat. Python-Version 3.3 und später werden mit dem ``venv``-Modul geliefert, um virtuelle Umgebungen zu erstellen, was die separate Installation überflüssig macht. Wenn Sie Python 2 oder eine Version vor Python 3.3 verwenden, müssen Sie ``virtualenv`` installieren.

* Für Python 3:

Python-Versionen 3.3 und später können direkt das ``venv``-Modul verwenden:

.. raw:: html

    <run></run>

.. code-block:: shell

    python3 -m venv myenv

Dies erstellt eine virtuelle Umgebung namens ``myenv`` im aktuellen Verzeichnis.

* Für Python 2:

Wenn Sie immer noch Python 2 verwenden, müssen Sie zuerst ``virtualenv`` installieren:

.. raw:: html

    <run></run>

.. code-block:: shell

    pip install virtualenv

Erstellen Sie dann eine virtuelle Umgebung:

.. raw:: html

    <run></run>

.. code-block:: shell

    virtualenv myenv

Dies erstellt ebenfalls eine virtuelle Umgebung namens ``myenv`` im aktuellen Verzeichnis.

**2. Aktivieren der virtuellen Umgebung**

Nachdem Sie die virtuelle Umgebung erstellt haben, müssen Sie sie für die Verwendung aktivieren.

.. note::

    Jedes Mal, wenn Sie den Raspberry Pi neu starten oder ein neues Terminal öffnen, müssen Sie erneut den folgenden Befehl ausführen, um die virtuelle Umgebung zu aktivieren.

.. raw:: html

    <run></run>

.. code-block:: shell

    source myenv/bin/activate

Sobald die virtuelle Umgebung aktiviert ist, sehen Sie den Umgebungsnamen vor dem Befehlszeilen-Prompt, was darauf hinweist, dass Sie innerhalb der virtuellen Umgebung arbeiten.


**3. Abhängigkeiten installieren**

Mit der aktivierten virtuellen Umgebung können Sie pip verwenden, um die erforderlichen Abhängigkeiten zu installieren. Zum Beispiel:

.. raw:: html

    <run></run>

.. code-block:: shell

    pip install requests

Dies installiert die Requests-Bibliothek in die aktuelle virtuelle Umgebung anstelle der globalen Umgebung. Dieser Schritt muss nur einmal ausgeführt werden.


**4. Verlassen der virtuellen Umgebung**

Wenn Sie Ihre Arbeit abgeschlossen haben und die virtuelle Umgebung verlassen möchten, führen Sie einfach folgenden Befehl aus:

.. raw:: html

    <run></run>

.. code-block:: shell

    deactivate

Dadurch kehren Sie zur globalen Python-Umgebung des Systems zurück.

**5. Löschen der virtuellen Umgebung**

Wenn Sie eine bestimmte virtuelle Umgebung nicht mehr benötigen, können Sie einfach das Verzeichnis löschen, das die virtuelle Umgebung enthält:

.. raw:: html

    <run></run>

.. code-block:: shell

    rm -rf myenv



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
