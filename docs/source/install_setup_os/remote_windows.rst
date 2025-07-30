.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

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

.. _remote_desktop:

Für Windows-Benutzer
=======================

Für Benutzer von Windows 10 oder höher kann die Remote-Anmeldung bei einem Raspberry Pi mit den folgenden Schritten erfolgen:

#. Suche in der Windows-Suchleiste nach ``powershell``. Klicke mit der rechten Maustaste auf ``Windows PowerShell`` und wähle **Als Administrator ausführen**.

    .. image:: img/powershell_ssh.png
        :align: center

#. Ermittele die IP-Adresse deines Raspberry Pi, indem du in PowerShell ``ping -4 <hostname>.local`` eingibst.

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    Die IP-Adresse des Raspberry Pi wird angezeigt, sobald er mit dem Netzwerk verbunden ist.

    * Wenn das Terminal anzeigt ``Ping request could not find host pi.local. Please check the name and try again.``, überprüfe, ob der eingegebene Hostname korrekt ist.
    * Wenn die IP-Adresse immer noch nicht abrufbar ist, überprüfe deine Netzwerk- oder WLAN-Einstellungen auf dem Raspberry Pi.

#. Sobald die IP-Adresse bestätigt wurde, melde dich mit ``ssh <benutzername>@<hostname>.local`` oder ``ssh <benutzername>@<IP-Adresse>`` beim Raspberry Pi an.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Wenn ein Fehler auftritt wie ``The term 'ssh' is not recognized as the name of a cmdlet...``, sind möglicherweise keine SSH-Tools auf deinem System installiert. In diesem Fall musst du OpenSSH manuell installieren, wie in :ref:`openssh_powershell` beschrieben, oder ein Drittanbieter-Tool verwenden, wie in :ref:`login_windows` beschrieben.

#. Beim ersten Login erscheint eine Sicherheitsmeldung. Gib ``yes`` ein, um fortzufahren.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Gib das zuvor festgelegte Passwort ein. Beachte, dass die Passwortzeichen aus Sicherheitsgründen nicht angezeigt werden.

    .. note::
        Es ist normal, dass beim Tippen des Passworts keine Zeichen angezeigt werden. Achte einfach darauf, das richtige Passwort einzugeben.

#. Sobald die Verbindung hergestellt ist, ist dein Raspberry Pi bereit für Remote-Operationen.

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center


