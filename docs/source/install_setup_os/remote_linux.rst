.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _remote_linux:

Linux-/Unix-Benutzer
==========================

#. Navigieren Sie zu **Applications**->\ **Utilities**, suchen Sie das **Terminal** und öffnen Sie es.

    .. image:: img/image21.png
        :align: center

#. Überprüfen Sie, ob Ihr Raspberry Pi im selben Netzwerk ist, indem Sie ``ping <hostname>.local`` eingeben.

    .. code-block:: shell

        ping raspberrypi.local

    * Wenn das Terminal ``ping: cannot resolve <hostname>.local`` anzeigt, könnte es sein, dass der Raspberry Pi keine Verbindung zum Netzwerk hat. Bitte überprüfen Sie das Netzwerk.
    * Wenn Sie ``<hostname>.local`` wirklich nicht anpingen können, versuchen Sie :ref:`get_ip` und geben Sie stattdessen ``ping <IP-Adresse>`` ein (z. B. ``ping 192.168.6.116``).
    * Wenn mehrere Meldungen wie ``64 Bytes von <IP-Adresse>: icmp_seq=0 ttl=64 time=0.464 ms`` erscheinen, bedeutet dies, dass Ihr Computer auf den Raspberry Pi zugreifen kann.

#. Geben Sie ``ssh <username>@<hostname>.local`` (oder ``ssh <username>@<IP-Adresse>``) ein.

    .. code-block:: shell

        ssh pi@raspberrypi.local

#. Die folgende Nachricht könnte erscheinen.

    .. code-block::

        The authenticity of host 'raspberrypi.local (192.168.6.116)' can't be established.
        ECDSA key fingerprint is SHA256:7ggckKZ2EEgS76a557cddfxFNDOBBuzcJsgaqA/igz4.
        Are you sure you want to continue connecting (yes/no/[fingerprint])? 

    Geben Sie "yes" ein.


#. Geben Sie das zuvor festgelegte Passwort ein (Meines ist ``raspberry``).

#. Nun ist der Raspberry Pi verbunden, und wir können zum nächsten Schritt übergehen.

