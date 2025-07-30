.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke [|link_sf_facebook|] und tritt noch heute bei!

.. _install_os:

Installation des Betriebssystems
==============================================

**Erforderliche Komponenten**

* Raspberry Pi  
* Ein Personal Computer  
* Eine Micro-SD-Karte  

**Installationsschritte**

#. Besuche die Raspberry-Pi-Software-Download-Seite unter `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Wähle die Imager-Version, die mit deinem Betriebssystem kompatibel ist. Lade die Datei herunter und öffne sie, um die Installation zu starten.

    .. image:: img/os_install_imager.png

#. Während der Installation kann je nach Betriebssystem eine Sicherheitsabfrage erscheinen. Unter Windows kann beispielsweise eine Warnmeldung angezeigt werden. Wähle in diesem Fall **Weitere Informationen** und dann **Trotzdem ausführen**. Folge den Bildschirmanweisungen, um die Installation des Raspberry Pi Imagers abzuschließen.

    .. image:: img/os_info.png

#. Stecke deine SD-Karte in den SD-Kartensteckplatz deines Computers oder Laptops.

#. Starte die Raspberry Pi Imager-Anwendung, indem du auf das Symbol klickst oder ``rpi-imager`` im Terminal eingibst.

    .. image:: img/os_open_imager.png

#. Klicke auf **CHOOSE DEVICE** und wähle dein spezifisches Raspberry-Pi-Modell aus der Liste aus.

    .. image:: img/os_choose_device.png

#. Klicke anschließend auf **Choose OS** und wähle ein Betriebssystem für die Installation aus.

    .. image:: img/os_choose_os.png

#. Klicke auf **Choose Storage** und wähle das passende Speichermedium für die Installation aus.

    .. note::

        Stelle sicher, dass du das richtige Speichermedium auswählst. Um Verwechslungen zu vermeiden, trenne andere Speichergeräte, wenn mehrere angeschlossen sind.

    .. image:: img/os_choose_sd.png

#. Klicke auf **NEXT** und anschließend auf **EDIT SETTINGS**, um deine Betriebssystemeinstellungen anzupassen. Wenn du einen Monitor für deinen Raspberry Pi hast, kannst du die nächsten Schritte überspringen und **Yes** klicken, um mit der Installation zu beginnen. Weitere Einstellungen kannst du später direkt am Monitor vornehmen.

    .. image:: img/os_enter_setting.png

#. Vergib einen **Hostnamen** für deinen Raspberry Pi.

    .. note::

        Der Hostname ist der Netzwerkname deines Raspberry Pi. Du kannst auf deinen Pi über ``<hostname>.local`` oder ``<hostname>.lan`` zugreifen.

    .. image:: img/os_set_hostname.png

#. Erstelle einen **Benutzernamen** und ein **Passwort** für das Administrator-Konto des Raspberry Pi.

    .. note::

        Die Vergabe eines eindeutigen Benutzernamens und Passworts ist wichtig, um deinen Raspberry Pi zu sichern, da er kein Standardpasswort besitzt.

    .. image:: img/os_set_username.png

#. Konfiguriere das WLAN, indem du die **SSID** und das **Passwort** deines Netzwerks angibst.

    .. note::

        Stelle das ``Wireless LAN country`` auf den zweibuchstabigen `ISO/IEC alpha2 code <https://de.wikipedia.org/wiki/ISO-3166-1-Kodierliste#Offiziell_zugewiesene_Codes>`_ deines Landes ein.

    .. image:: img/os_set_wifi.png

#. Klicke auf **SERVICES** und aktiviere **SSH** für sicheren, passwortbasierten Fernzugriff. Vergiss nicht, deine Einstellungen zu speichern.

    .. image:: img/os_enable_ssh.png

#. Bestätige deine ausgewählten Einstellungen mit einem Klick auf **Yes**.

    .. image:: img/os_click_yes.png

#. Wenn sich auf der SD-Karte bereits Daten befinden, sichere diese, um Datenverlust zu vermeiden. Klicke auf **Yes**, wenn keine Sicherung erforderlich ist.

    .. image:: img/os_continue.png

#. Der Installationsprozess des Betriebssystems auf die SD-Karte beginnt. Nach Abschluss wird ein Bestätigungsdialog angezeigt.

    .. image:: img/os_finish.png
        :align: center
