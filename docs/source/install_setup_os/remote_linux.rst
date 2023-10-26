.. _remote_linux:

Linux-/Unix-Benutzer
==========================

#. Navigieren Sie zu **Applications**->\ **Utilities**, suchen Sie das **Terminal** und öffnen Sie es.

    .. image:: img/image21.png
        :align: center

#. Überprüfen Sie, ob Ihr Raspberry Pi im selben Netzwerk ist, indem Sie ``ping <hostname>.local`` eingeben.

    .. code-block:: shell

        ping raspberrypi.local

    .. image:: img/mac-ping.png
        :width: 550
        :align: center

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

    .. image:: img/mac-ssh-login.png
        :width: 550
        :align: center

#. Geben Sie das zuvor festgelegte Passwort ein (Meines ist ``raspberry``).

#. Nun ist der Raspberry Pi verbunden, und wir können zum nächsten Schritt übergehen.

    .. image:: img/mac-ssh-terminal.png
        :width: 550
        :align: center
