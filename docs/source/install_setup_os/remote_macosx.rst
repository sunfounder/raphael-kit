.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _remote_macosx:

Mac OS X Benutzer
==================

Für Mac-Benutzer ist es komfortabler, über VNC direkt auf den Raspberry Pi Desktop zuzugreifen, als über die Kommandozeile. Sie können darauf über den Finder zugreifen, indem Sie das festgelegte Kontopasswort eingeben, nachdem Sie VNC auf der Raspberry Pi-Seite aktiviert haben.

Beachten Sie, dass diese Methode die Kommunikation zwischen dem Mac und dem Raspberry Pi nicht verschlüsselt. Die Kommunikation erfolgt innerhalb Ihres Heim- oder Geschäftsnetzwerks, sodass es selbst wenn sie ungeschützt ist, kein Problem darstellt. Wenn Sie jedoch Bedenken haben, können Sie eine VNC-Anwendung wie `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ installieren.

Alternativ wäre es praktisch, wenn Sie einen temporären Monitor (TV), Maus und Tastatur verwenden könnten, um den Raspberry Pi Desktop direkt zu öffnen und VNC einzurichten. Wenn nicht, ist das auch kein Problem. Sie können den SSH-Befehl verwenden, um die Bash-Shell des Raspberry Pi zu öffnen und dann den Befehl zum Einrichten des VNC zu verwenden.

* :ref:`have_temp_monitor`
* :ref:`no_temp_monitor`

.. _have_temp_monitor:

Haben Sie einen temporären Monitor (oder TV)?
-----------------------------------------------------

#. Verbinden Sie einen Monitor (oder TV), Maus und Tastatur mit dem Raspberry Pi und schalten Sie ihn ein. Wählen Sie das Menü entsprechend den Nummern in der Abbildung aus.

    .. image:: img/mac_vnc1.png
        :align: center

#. Der folgende Bildschirm wird angezeigt. Stellen Sie **VNC** auf der Registerkarte **Enabled** auf **Interfaces** und klicken Sie auf **OK**.

    .. image:: img/mac_vnc2.png
        :align: center

#. Ein VNC-Symbol erscheint oben rechts auf dem Bildschirm und der VNC-Server startet.

    .. image:: img/login1.png
        :align: center

#. Öffnen Sie das VNC-Server-Fenster, indem Sie auf das **VNC**-Symbol klicken, klicken Sie dann auf die **Menu**-Schaltfläche in der oberen rechten Ecke und wählen Sie **Options**.

    .. image:: img/mac_vnc4.png
        :align: center

#. Ihnen wird der folgende Bildschirm angezeigt, auf dem Sie die Optionen ändern können.

    .. image:: img/mac_vnc5.png
        :align: center

    Stellen Sie **Encryption** auf **Prefer off** und **Authentication** auf **VNC password**.

#. Wenn Sie auf die Schaltfläche **OK** klicken, wird der Passworteingabebildschirm angezeigt. Sie können dasselbe Passwort wie das Raspberry Pi-Passwort oder ein anderes Passwort verwenden, geben Sie es also ein und klicken Sie auf **OK**. 

    .. image:: img/mac_vnc16.png
        :align: center

    Sie können nun von Ihrem Mac aus verbinden. Es ist in Ordnung, den Monitor zu trennen.

**Von hier an erfolgt die Bedienung auf der Mac-Seite.**

#. Wählen Sie jetzt **Connect to Server** aus dem Finder-Menü, das Sie mit einem Rechtsklick öffnen können.

    .. image:: img/mac_vnc10.png
        :align: center

#. Geben Sie ``vnc://<Benutzername>@<Hostname>.local`` ein (oder ``vnc://<Benutzername>@<IP-Adresse>``). Nach der Eingabe klicken Sie auf **Connect**.

        .. image:: img/mac_vnc11.png
            :align: center

#. Sie werden nach einem Passwort gefragt, bitte geben Sie es ein.

        .. image:: img/mac_vnc12.png
            :align: center

#. Der Desktop des Raspberry Pi wird angezeigt und Sie können ihn so bedienen, als wären Sie direkt darauf.

        .. image:: img/mac_vnc13.png
            :align: center

.. _no_temp_monitor:

Keinen temporären Monitor (oder TV) zur Verfügung?
--------------------------------------------------------

* Sie können den SSH-Befehl verwenden, um die Bash-Shell des Raspberry Pi zu öffnen.
* Bash ist die standardmäßige Shell für Linux.
* Die Shell selbst ist ein Befehl (Anweisung), wenn der Benutzer Unix/Linux verwendet.
* Das Meiste, was Sie tun müssen, kann über die Shell erledigt werden.
* Nachdem Sie die Raspberry Pi-Seite eingerichtet haben, können Sie über den **Finder** vom Mac aus auf den Desktop des Raspberry Pi zugreifen.

#. Geben Sie ``ssh <Benutzername>@<Hostname>.local`` ein, um eine Verbindung zum Raspberry Pi herzustellen.

    .. code-block:: shell

        ssh pi@raspberrypi.local

    .. image:: img/mac_vnc14.png


#. Die folgende Meldung wird nur bei der ersten Anmeldung angezeigt, geben Sie also **yes** ein.

    .. code-block::

        Die Authentizität des Hosts 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' kann nicht festgestellt werden.
        ED25519 Schlüssel-Fingerabdruck ist SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Dieser Schlüssel ist unter keinen anderen Namen bekannt.
        Sind Sie sicher, dass Sie die Verbindung fortsetzen möchten (ja/nein/[Fingerabdruck])?

#. Geben Sie das Passwort für den Raspberry Pi ein. Das eingegebene Passwort wird nicht angezeigt, seien Sie also vorsichtig und vermeiden Sie Fehler.

    .. code-block::

        pi@raspberrypi.local's Passwort: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        Die Programme, die mit dem Debian GNU/Linux-System geliefert werden, sind freie Software;
        die genauen Vertriebsbedingungen für jedes Programm sind in den
        einzelnen Dateien in /usr/share/doc/*/copyright beschrieben.

        Debian GNU/Linux wird OHNE JEGLICHE GARANTIE geliefert, soweit gesetzlich zulässig.
        Letzter Login: Do. 22. Sep. 12:18:22 2022
        pi@raspberrypi:~ $ 


#. Richten Sie Ihren Raspberry Pi so ein, dass Sie sich nach erfolgreichem Login von Ihrem Mac aus über VNC anmelden können. Der erste Schritt besteht darin, Ihr Betriebssystem mit den folgenden Befehlen zu aktualisieren.

    .. code-block:: shell

        sudo apt update
        sudo apt upgrade

    ``Do you want to continue? [Y/n]``, Geben Sie bei Aufforderung ``Y`` ein.

    Das Update kann einige Zeit in Anspruch nehmen. (Dies hängt von der Anzahl der Aktualisierungen zu diesem Zeitpunkt ab.)

#. Geben Sie den folgenden Befehl ein, um den **VNC Server** zu aktivieren.

    .. code-block:: shell

        sudo raspi-config

#. Der folgende Bildschirm wird angezeigt. Wählen Sie mit den Pfeiltasten auf der Tastatur **3 Interface Options** und drücken Sie die **Enter**.

    .. image:: img/image282.png
        :align: center

#. Wählen Sie dann **VNC** aus.

    .. image:: img/image288.png
        :align: center

#. Verwenden Sie die Pfeiltasten auf der Tastatur, um **<Yes>** -> **<OK>** -> **<Finish>** auszuwählen und die Einrichtung abzuschließen.

    .. image:: img/mac_vnc8.png
        :align: center


#. Jetzt, da der VNC-Server gestartet ist, ändern Sie die Einstellungen für die Verbindung von einem Mac.

    Um Parameter für alle Programme für alle Benutzerkonten auf dem Computer festzulegen, erstellen Sie ``/etc/vnc/config.d/common.custom``.

    .. code-block:: shell

        sudo nano /etc/vnc/config.d/common.custom

    Nachdem Sie ``Authentication=VncAuthenter`` eingegeben haben, drücken Sie ``Ctrl+X`` -> ``Y`` -> ``Enter``, um zu speichern und zu beenden.

    .. image:: img/mac_vnc15.png
        :align: center

#. Legen Sie außerdem ein Passwort für die Anmeldung über VNC von einem Mac fest. Sie können dasselbe Passwort wie das Raspberry-Pi-Passwort oder ein anderes Passwort verwenden.

    .. code-block:: shell

        sudo vncpasswd -service

#. Sobald die Einrichtung abgeschlossen ist, starten Sie den Raspberry Pi neu, um die Änderungen anzuwenden.

    .. code-block:: shell

        sudo sudo reboot

#. Wählen Sie nun **Connect to Server** aus dem Menü **Finder**, das Sie mit einem Rechtsklick öffnen können.

    .. image:: img/mac_vnc10.png
        :align: center

#. Geben Sie ``vnc://<Benutzername>@<Hostname>.local`` (oder ``vnc://<Benutzername>@<IP-Adresse>``) ein. Klicken Sie nach der Eingabe auf **Connect**.

        .. image:: img/mac_vnc11.png
            :align: center

#. Sie werden nach einem Passwort gefragt, bitte geben Sie es ein.

        .. image:: img/mac_vnc12.png
            :align: center

#. Der Desktop des Raspberry Pi wird angezeigt und Sie können ihn vom Mac aus wie gewohnt bedienen.

        .. image:: img/mac_vnc13.png
            :align: center

