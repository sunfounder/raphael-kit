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
Dies ist eine C-Bibliothek für den Raspberry Pi (RPi). Sie bietet Zugriff auf GPIO- und andere I/O-Funktionen des Broadcom BCM2835-Chips, wie er im Raspberry Pi verwendet wird, und ermöglicht die Ansteuerung der GPIO-Pins auf dem 26-poligen IDE-Stecker des RPi-Boards. Damit können Sie verschiedene externe Geräte steuern und auslesen.

Die Bibliothek bietet Funktionen zum Lesen digitaler Eingänge und Setzen digitaler Ausgänge, zur Verwendung von SPI und I²C sowie zum Zugriff auf System-Timer. Ereigniserkennung an Pins wird per Polling unterstützt (Interrupts werden nicht unterstützt).

Funktioniert auf allen Versionen bis einschließlich Raspberry Pi 4. Unterstützt Debian-Versionen bis einschließlich Debian Buster 10.

Öffnen Sie ein Terminal und laden Sie die ``bcm2835``-Bibliothek in das ``~``-Verzeichnis herunter.

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

Installieren Sie die BCM2835-Bibliothek mit folgenden Befehlen:

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

Virtuelle Umgebung erstellen
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Beim Arbeiten mit Raspberry Pi oder ähnlichen Geräten wird empfohlen, Python-Pakete über ``pip`` in einer virtuellen Umgebung zu installieren.  
Dies bietet Vorteile wie Abhängigkeitsisolierung, höhere Systemsicherheit, saubere Systemumgebung und einfachere Projektübertragung – weshalb virtuelle Umgebungen ein äußerst wichtiges Werkzeug in der Python-Entwicklung sind.

Nachfolgend finden Sie die Schritte zum Erstellen einer virtuellen Umgebung:

**1. Virtuelle Umgebung erstellen**

Stellen Sie sicher, dass Python installiert ist. Python 3.3 und höher enthalten das ``venv``-Modul, daher ist keine zusätzliche Installation erforderlich. Nutzer von Python 2 müssen ``virtualenv`` installieren.

* Für Python 3:

Python 3.3+ kann ``venv`` direkt nutzen:

.. raw:: html

    <run></run>

.. code-block:: shell

    python3 -m venv myenv

Dies erstellt die virtuelle Umgebung ``myenv`` im aktuellen Verzeichnis.

* Für Python 2:

Falls Sie noch Python 2 nutzen, installieren Sie zuerst ``virtualenv``:

.. raw:: html

    <run></run>

.. code-block:: shell

    pip install virtualenv

Dann erstellen Sie die Umgebung:

.. raw:: html

    <run></run>

.. code-block:: shell

    virtualenv myenv

**2. Virtuelle Umgebung aktivieren**

Nach dem Erstellen müssen Sie die Umgebung aktivieren:

.. note::
    Nach jedem Neustart des Raspberry Pi oder Öffnen eines neuen Terminals müssen Sie die Umgebung erneut aktivieren.

.. raw:: html

    <run></run>

.. code-block:: shell

    source myenv/bin/activate

Wenn die Umgebung aktiv ist, erscheint ihr Name links vor der Eingabeaufforderung.

**3. Virtuelle Umgebung verlassen**

.. raw:: html

    <run></run>

.. code-block:: shell

    deactivate

**4. Virtuelle Umgebung löschen**

.. raw:: html

    <run></run>

.. code-block:: shell

    rm -rf myenv


.. _install_luma_led_matrix:

Luma.LED_Matrix
~~~~~~~~~~~~~~~~~~~~~~~

Dies ist eine Python-3-Bibliothek zur Ansteuerung von LED-Matrix-Displays über MAX7219 (SPI), WS2812 (NeoPixel), APA102 (DotStar) und ähnliche Module auf Raspberry Pi und anderen Linux-Boards.

#. Fügen Sie Ihren Benutzer zu den Gruppen ``spi`` und ``gpio`` hinzu (ersetzen Sie „pi“ durch Ihren Benutzernamen):

   .. raw:: html

       <run></run>

   .. code-block:: shell

        sudo usermod -a -G spi,gpio pi

   Danach sollten Sie neu starten oder sich ab- und wieder anmelden.

#. Installieren Sie die nötigen Abhängigkeiten:

   .. raw:: html

       <run></run>

   .. code-block:: shell

        sudo apt update
        sudo apt install -y build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff-dev

#. Erstellen Sie eine virtuelle Umgebung (Beispiel: ``~/my_env``):

   .. raw:: html

       <run></run>

   .. code-block:: shell

       python3 -m venv ~/my_env

#. Aktivieren Sie die Umgebung:

   .. note::
       Nach jedem Neustart oder neuem Terminal muss dieser Befehl erneut ausgeführt werden.

   .. raw:: html

       <run></run>

   .. code-block:: shell

       source ~/my_env/bin/activate

#. Aktualisieren Sie ``pip`` und ``setuptools``:

   .. raw:: html

      <run></run>

   .. code-block:: shell

      pip install --upgrade pip setuptools

#. Installieren Sie ``luma.led_matrix``:

   .. raw:: html

      <run></run>

   .. code-block:: shell

      pip install luma.led_matrix

#. Testen Sie die Installation:

   .. raw:: html

      <run></run>

   .. code-block:: shell

        python3 -c "import luma.led_matrix; print(luma.led_matrix.__version__)"

#. Umgebung verlassen:

   .. raw:: html
    
       <run></run>

   .. code-block:: shell

       deactivate

* Referenz: `Luma.LED_Matrix <https://luma-led-matrix.readthedocs.io/en/latest/install.html>`_


.. .. _install_mfrc522:

.. MFRC522
.. ~~~~~~~~~~~~~~~~~

.. Führen Sie folgenden Befehl aus, um die MFRC522-Bibliothek zu installieren:

.. .. raw:: html

..    <run></run>

.. .. code-block:: 

..     sudo pip3 install mfrc522

.. Die MFRC522-Bibliothek besteht aus zwei Dateien: ``MFRC522.py`` und ``SimpleMFRC522.py``.  

.. * ``MFRC522.py`` implementiert die Kommunikation mit dem RFID-Modul RC522 über SPI.  
.. * ``SimpleMFRC522.py`` vereinfacht die Nutzung erheblich, da nur wenige Funktionen verwendet werden müssen.

