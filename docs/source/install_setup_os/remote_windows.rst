.. _remote_windows:

Windows-Benutzer
=======================

Wenn Sie ein Windows-Benutzer sind, können Sie die Windows PowerShell verwenden, um sich aus der Ferne am Raspberry Pi anzumelden.

#. Drücken Sie die Tastenkombination ``windows`` + ``R`` auf Ihrer Tastatur, um das Programm **Run** zu öffnen. Geben Sie dann **powershell** in das Eingabefeld ein.

    .. image:: img/sp221221_135900.png
        :align: center

#. Überprüfen Sie, ob Ihr Raspberry Pi im selben Netzwerk ist, indem Sie ``ping <hostname>.local`` eingeben.

    .. code-block:: shell

        ping raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    * Wenn das Terminal die Meldung ``Ping request could not find host <hostname>.local`` ausgibt, ist es möglich, dass der Raspberry Pi keine Netzwerkverbindung hat. Überprüfen Sie das Netzwerk.
    * Wenn Sie ``<hostname>.local`` wirklich nicht anpingen können, versuchen Sie :ref:`get_ip` zu verwenden und stattdessen ``ping <IP-Adresse>`` auszuführen (z. B. ``ping 192.168.6.116``).
    * Wenn mehrere Meldungen wie "Antwort von <IP-Adresse>: Bytes=32 Zeit<1ms TTL=64" erscheinen, bedeutet dies, dass Ihr Computer auf den Raspberry Pi zugreifen kann.

#. Geben Sie ``ssh <username>@<hostname>.local`` (oder ``ssh <username>@<IP address>``) ein.

    .. code-block:: shell

        ssh pi@raspberrypi.local

#. Die folgende Nachricht könnte erscheinen.

    .. code-block::

        The authenticity of host 'raspberrypi.local (192.168.6.116)' can't be established.
        ECDSA key fingerprint is SHA256:7ggckKZ2EEgS76a557cddfxFNDOBBuzcJsgaqA/igz4.
        Are you sure you want to continue connecting (yes/no/[fingerprint])? 

    Geben Sie "yes" ein.

#. Geben Sie das zuvor festgelegte Passwort ein (Meines ist ``raspberry``).

    .. note::
        Beim Eingeben des Passworts werden die Zeichen nicht im Fenster angezeigt, was normal ist. Wichtig ist, dass Sie das richtige Passwort eingeben.

#. Nun ist der Raspberry Pi verbunden, und wir sind bereit für den nächsten Schritt.

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center

.. _windows_remote_desktop:

Remote-Desktop
------------------

Wenn Sie nicht zufrieden sind, den Befehlsfenster zum Zugriff auf Ihren Raspberry Pi zu verwenden, können Sie auch die Remote-Desktop-Funktion nutzen, um Dateien auf Ihrem Raspberry Pi über eine GUI zu verwalten.

Hier verwenden wir den `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_.

**VNC-Dienst aktivieren**

Der VNC-Dienst ist im System installiert. Standardmäßig ist VNC deaktiviert. Sie müssen ihn in der Konfiguration aktivieren.

#. Geben Sie den folgenden Befehl ein:

    .. raw:: html

        <run></run>

    .. code-block:: shell 

        sudo raspi-config

#. Wählen Sie **3** **Interfacing Options** mit der Abwärtspfeiltaste Ihrer Tastatur aus und drücken Sie die **Enter**.

    .. image:: img/image282.png
        :align: center

#. Danach **VNC**.

    .. image:: img/image288.png
        :align: center

#. Verwenden Sie die Pfeiltasten auf der Tastatur, um **<Yes>** -> **<OK>** -> **<Finish>** auszuwählen und die Einrichtung abzuschließen.

    .. image:: img/mac_vnc8.png
        :align: center

**In VNC anmelden**

#. Sie müssen den `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ auf Ihrem persönlichen Computer herunterladen und installieren.

#. Öffnen Sie ihn nach Abschluss der Installation. Geben Sie dann den Hostnamen oder die IP-Adresse ein und drücken Sie Enter.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Nachdem Sie Ihren Raspberry Pi-Namen und Ihr Passwort eingegeben haben, klicken Sie auf **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Nun können Sie den Desktop des Raspberry Pi sehen.

    .. image:: img/login1.png
        :align: center
