.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

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

**3. Verlassen der virtuellen Umgebung**

Wenn Sie Ihre Arbeit abgeschlossen haben und die virtuelle Umgebung verlassen möchten, führen Sie einfach folgenden Befehl aus:

.. raw:: html

    <run></run>

.. code-block:: shell

    deactivate

Dadurch kehren Sie zur globalen Python-Umgebung des Systems zurück.

**4. Löschen der virtuellen Umgebung**

Wenn Sie eine bestimmte virtuelle Umgebung nicht mehr benötigen, können Sie einfach das Verzeichnis löschen, das die virtuelle Umgebung enthält:

.. raw:: html

    <run></run>

.. code-block:: shell

    rm -rf myenv

Luma.LED_Matrix
~~~~~~~~~~~~~~~~~~~~~~~

Dies ist eine Python 3-Bibliothek zur Ansteuerung von LED-Matrix-Displays unter Verwendung des MAX7219-Treibers (über SPI), WS2812 (NeoPixels, einschließlich Pimoroni Unicorn pHat/Hat und Unicorn Hat HD) und APA102 (DotStar) auf dem Raspberry Pi und anderen Linux-basierten Single-Board-Computern.

#. Fügen Sie den Benutzer zur Gruppe ``spi`` und ``gpio`` hinzu, um sicherzustellen, dass der aktuelle Benutzer (ersetzen Sie "pi" durch Ihren eigenen Benutzernamen) die Berechtigung hat, auf die SPI- und GPIO-Schnittstellen zuzugreifen.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell

        sudo usermod -a -G spi,gpio pi

   Nach Ausführung dieses Befehls wird empfohlen, das System neu zu starten oder sich ab- und wieder anzumelden, um die Gruppenmitgliedschaft anzuwenden.

#. Installieren Sie die erforderlichen Abhängigkeiten: Verwenden Sie ``apt``, um Build-Tools und zugehörige Entwicklungspakete zu installieren. Diese Bibliotheken sind notwendig, um bestimmte Python-Pakete zu kompilieren und zu installieren.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell

        sudo apt update
        sudo apt install -y build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff-dev

#. Erstellen Sie eine virtuelle Umgebung. Hier ist ``~/my_env`` der Pfad zur virtuellen Umgebung und kann angepasst werden.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       python3 -m venv ~/my_env

#. Nachdem die virtuelle Umgebung erstellt wurde, aktivieren Sie sie zur Nutzung.

   .. note::
   
       Jedes Mal, wenn Sie den Raspberry Pi neu starten oder ein neues Terminal öffnen, müssen Sie den folgenden Befehl erneut ausführen, um die virtuelle Umgebung zu aktivieren.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       source ~/my_env/bin/activate
   
   Sobald die virtuelle Umgebung aktiviert ist, sehen Sie den Namen der Umgebung vor der Befehlszeile, was anzeigt, dass Sie in der virtuellen Umgebung arbeiten.

#. Aktualisieren Sie innerhalb der virtuellen Umgebung ``pip`` und ``setuptools``, um sicherzustellen, dass die neuesten Versionen der Pakete installiert werden.
   
   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell

      pip install --upgrade pip setuptools

#. Installieren Sie dann ``luma.led_matrix``:

   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell
   
        pip install luma.led_matrix

#. Nach der Installation können Sie überprüfen, ob ``luma.led_matrix`` korrekt installiert wurde, indem Sie den folgenden Befehl ausführen. Bei erfolgreicher Installation wird die Versionsnummer von ``luma.led_matrix`` angezeigt.
   
   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell

        python3 -c "import luma.led_matrix; print(luma.led_matrix.__version__)"

#. Wenn Sie die Arbeit beendet haben und die virtuelle Umgebung verlassen möchten, führen Sie einfach den folgenden Befehl aus:

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       deactivate

* Referenz: `Luma.LED_Matrix <https://luma-led-matrix.readthedocs.io/en/latest/install.html>`_

MFRC522
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Führen Sie den folgenden Befehl aus, um die MFRC522-Bibliothek zu installieren.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install mfrc522

Die MFRC522-Bibliothek enthält zwei Dateien: ``MFRC522.py`` und ``SimpleMFRC522.py``. 

``MFRC522.py`` ist die Implementierung der RFID RC522-Schnittstelle. Diese Bibliothek übernimmt die gesamte Arbeit bei der Kommunikation mit RFID über die SPI-Schnittstelle des Pi.

``SimpleMFRC522.py`` vereinfacht die ``MFRC522.py``-Datei erheblich, indem sie Ihnen ermöglicht, nur mit einigen wenigen Funktionen statt vielen zu arbeiten.
