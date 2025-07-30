.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _set_up_your_raspberry_pi:

Einrichtung deines Raspberry Pi
=====================================

Einrichtung mit Bildschirm
---------------------------

Die Verwendung eines Bildschirms vereinfacht die Arbeit mit deinem Raspberry Pi.

**Erforderliche Komponenten**

* Raspberry Pi  
* Netzteil  
* Micro-SD-Karte  
* Bildschirm-Netzteil  
* HDMI-Kabel  
* Bildschirm  
* Maus  
* Tastatur  

**Schritte**:

#. Schließe die Maus und die Tastatur an den Raspberry Pi an.

#. Verbinde den Bildschirm mit dem HDMI-Anschluss des Raspberry Pi über das HDMI-Kabel. Stelle sicher, dass der Bildschirm an eine Stromquelle angeschlossen und eingeschaltet ist.

#. Versorge den Raspberry Pi mit Strom über das Netzteil. Nach einigen Sekunden sollte der Desktop des Raspberry Pi OS auf dem Bildschirm erscheinen.

    .. image:: img/bullseye_desktop.png
        :align: center

Einrichtung ohne Bildschirm
------------------------------

Wenn du keinen Monitor hast, ist die Remote-Anmeldung eine praktikable Option.

**Erforderliche Komponenten**

* Raspberry Pi  
* Netzteil  
* Micro-SD-Karte  

Mit SSH kannst du auf die Bash-Shell des Raspberry Pi zugreifen, die die Standard-Linux-Shell ist. Bash bietet eine Befehlszeilenschnittstelle zum Ausführen verschiedener Aufgaben.

Für diejenigen, die eine grafische Benutzeroberfläche (GUI) bevorzugen, ist die Remote-Desktop-Funktion eine bequeme Alternative zum Verwalten von Dateien und Operationen.

Für detaillierte Einrichtungstutorials basierend auf deinem Betriebssystem siehe die folgenden Abschnitte:

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop
