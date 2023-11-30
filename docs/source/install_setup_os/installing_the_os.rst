.. _install_os:

Installation des Betriebssystems (Allgemein)
=====================================================

**Schritt 1**

Das Raspberry Pi-Team bietet ein benutzerfreundliches, grafisches SD-Karten-Schreibprogramm, das mit Mac OS, Ubuntu 18.04 und Windows kompatibel ist. Dies ist die bequemste Option für die meisten Anwender, da es automatisch das Betriebssystem-Image herunterlädt und auf die SD-Karte installiert.

Besuchen Sie die Download-Seite: https://www.raspberrypi.org/software/. Wählen Sie den **Raspberry Pi Imager** für Ihr Betriebssystem aus. Nach dem Herunterladen öffnen Sie das Programm, um mit der Installation zu beginnen.

.. image:: img/image2.png
    :align: center

.. raw:: html

    <br/>

**Schritt 2**

Beim Starten des Installationsprogramms könnte Ihr Betriebssystem eine Sicherheitswarnung anzeigen. Windows könnte beispielsweise folgende Nachricht zeigen:

Wenn Sie darauf stoßen, wählen Sie **More info** und dann **Run anyway**. Befolgen Sie die Anweisungen auf dem Bildschirm, um den Raspberry Pi Imager zu installieren.

.. image:: img/image3.png
    :align: center

.. raw:: html

    <br/>

**Schritt 3**

Nach der Installation des Imagers öffnen Sie die Anwendung, indem Sie auf das Symbol **Raspberry Pi Imager** klicken oder `rpi-imager` ausführen.

.. image:: img/image4.png
    :align: center

.. raw:: html

    <br/>

**Schritt 4**

Klicken Sie auf **Choose device** und wählen Sie Ihr Raspberry Pi-Modell aus der Liste aus.

.. image:: img/image5.png
    :align: center

.. raw:: html

    <br/>

**Schritt 5**

Klicken Sie anschließend auf **Choose OS** und wählen Sie ein Betriebssystem zur Installation aus. 

.. image:: img/image6.png
    :align: center

.. raw:: html

    <br/>

**Schritt 6**

Verbinden Sie Ihr bevorzugtes Speichermedium, wie eine microSD-Karte, über einen externen oder eingebauten SD-Kartenleser. Klicken Sie dann auf Speicher wählen und wählen Sie Ihr Speichergerät aus.

.. note:: 

    * Stellen Sie sicher, dass Sie das richtige Speichergerät auswählen, falls mehrere angeschlossen sind. Geräte können oft an ihrer Größe erkannt werden. Trennen Sie andere, falls Sie unsicher sind.

.. image:: img/image7.png
    :align: center

.. raw:: html

    <br/>

**Schritt 7**

Drücken Sie die Schaltfläche **NEXT** und wählen Sie **EDIT SETTINGS**, um auf die Seite zur Betriebssystem-Anpassung zuzugreifen.

.. image:: img/image8.png
    :align: center

.. raw:: html

    <br/>

**Schritt 8**

Legen Sie den **hostname** fest.

.. note::
        * Die Hostname-Option definiert den Namen, unter dem Ihr Raspberry Pi sich im Netzwerk mittels mDNS bekannt macht. Sobald Sie Ihren Raspberry Pi mit Ihrem Netzwerk verbinden, können andere Geräte im Netzwerk mit Ihrem Computer über ``<hostname>.local`` oder ``<hostname>.lan`` kommunizieren.

.. image:: img/image9.png
    :align: center

.. raw:: html

    <br/>

Legen Sie den **username** und das **password** für das Administrator-Konto des Raspberry Pi fest.

.. note::
        * Da der Raspberry Pi kein Standardpasswort hat, ist es wichtig, Ihr eigenes zu erstellen. Der Benutzername kann ebenfalls angepasst werden.

.. image:: img/image10.png
    :align: center

.. raw:: html

    <br/>

Konfigurieren Sie das WLAN, indem Sie den **SSID** und das **Passwort** Ihres Netzwerks eingeben.

.. note::

    Stellen Sie das ``Wireless LAN Land`` auf den zweibuchstabigen `ISO/IEC alpha2-Code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ Ihres Landes ein.

.. image:: img/image11.png
    :align: center

.. raw:: html

    <br/>

**Schritt 9**

Klicken Sie auf **SERVICES**, um SSH zu aktivieren und die Passwort-basierte Anmeldung zu wählen. Klicken Sie dann auf **Save**.

.. image:: img/image12.png
    :align: center

.. raw:: html

    <br/>

**Schritt 10**

Klicken Sie auf die Schaltfläche **Yes**.

.. image:: img/image13.png
    :align: center

.. raw:: html

    <br/>

**Schritt 11**

Wenn Ihre SD-Karte Dateien enthält, sollten Sie in Erwägung ziehen, diese zu sichern, um dauerhaften Datenverlust zu vermeiden. Wenn keine Sicherung erforderlich ist, klicken Sie auf **Yes**.

.. image:: img/image14.png
    :align: center

.. raw:: html

    <br/>

**Schritt 12**

Das Ende des Schreibvorgangs wird nach einer Wartezeit durch das folgende Fenster angezeigt.

.. image:: img/image15.png
    :align: center

.. raw:: html

    <br/>

