.. _install_os:

Betriebssysteminstallation (Allgemein)
======================================

**Schritt 1**

Das Raspberry Pi-Team hat ein grafisches SD-Karten-Beschreibungsprogramm entwickelt, das
unter Mac OS, Ubuntu 18.04 und Windows funktioniert. Dies ist für die meisten
Benutzer die einfachste Option, da es das Image herunterlädt und es automatisch auf die
SD-Karte installiert.

Besuchen Sie die Download-Seite: https://www.raspberrypi.org/software/. Klicken Sie auf
den Link für den **Raspberry Pi Imager**, der zu Ihrem Betriebssystem passt. Nachdem der Download abgeschlossen ist, klicken Sie darauf, um den Installer zu starten.

.. image:: img/image11.png
    :align: center

**Schritt 2**

Wenn Sie den Installer starten, kann Ihr Betriebssystem versuchen, 
dies zu blockieren. Zum Beispiel erhalte ich unter Windows folgende
Meldung:

Sollte diese Meldung erscheinen, klicken Sie auf **More info** und dann auf **Run anyway**. Folgen Sie dann den Anweisungen, um den Raspberry Pi Imager zu installieren.

.. image:: img/image12.png
    :align: center

**Schritt 3**

Stecken Sie Ihre SD-Karte in den SD-Kartenslot Ihres Computers oder Laptops.

**Schritt 4**

Im Raspberry Pi Imager wählen Sie das Betriebssystem, das Sie installieren möchten, 
sowie die SD-Karte, auf die es installiert werden soll.

.. image:: img/image13.png
    :align: center

.. note::

    * Beim ersten Mal muss eine Internetverbindung bestehen.
    * Das Betriebssystem wird dann für die zukünftige Offline-Nutzung gespeichert (``lastdownload.cache``, ``C:/Users/IhrName/AppData/Local/Raspberry Pi/Imager/cache``). Wenn Sie die Software das nächste Mal öffnen, wird "Veröffentlicht: Datum, im Cache auf Ihrem Computer" angezeigt.

.. Laden Sie das `raspios_armhf-2020-05-28 <https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2021-05-28/2021-05-07-raspios-buster-armhf.zip>`_-Bild herunter und wählen Sie es im Raspberry Pi Imager aus.

.. .. image:: img/otherOS.png
..     :align: center

.. .. warning::
..     Raspberry Pi OS has major changes after the 2021-05-28 version, which may cause some functions to be unavailable. Please do not use the latest version for now.


.. .. mark

**Schritt 5**

Wählen Sie die verwendete SD-Karte aus.

.. image:: img/image14.png
    :align: center

**Schritt 6**

Drücken Sie **Ctrl+Shift+X** oder klicken Sie auf das **setting**-Symbol, um die Seite **Advanced options** zu öffnen, um SSH zu aktivieren und Benutzernamen und Passwort festzulegen.

    .. note::
        * Da der Raspberry Pi kein Standardpasswort hat, müssen Sie dieses selbst festlegen. Auch der Benutzername kann geändert werden.
        * Für den Fernzugriff müssen Sie SSH auch manuell aktivieren.

.. image:: img/image15.png
    :align: center

Scrollen Sie anschließend nach unten, um die WLAN-Konfiguration abzuschließen und klicken Sie auf **SAVE**.

.. note::

    ``wifi country`` sollte auf den zweistelligen `ISO/IEC alpha2 code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ für das Land eingestellt werden, in dem Sie Ihren Raspberry Pi verwenden.

.. image:: img/image16.png
    :align: center

**Schritt 7**

Klicken Sie auf die Schaltfläche **WRITE**.

.. image:: img/image17.png
    :align: center

**Schritt 8**

Falls sich derzeit Dateien auf Ihrer SD-Karte befinden, möchten Sie diese Dateien möglicherweise zuerst sichern, um sie nicht dauerhaft zu verlieren. Wenn keine Datei gesichert werden muss, klicken Sie auf **Yes**.

.. image:: img/image18.png
    :align: center

**Schritt 9**

Nach einer gewissen Wartezeit wird das folgende Fenster angezeigt, das das erfolgreiche Schreiben bestätigt.

.. image:: img/image19.png
    :align: center
