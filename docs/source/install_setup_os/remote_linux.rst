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

Für Linux/Unix-Benutzer
==========================

#. Öffne das **Terminal** auf deinem Linux/Unix-System.

#. Stelle sicher, dass dein Raspberry Pi mit demselben Netzwerk verbunden ist. Überprüfe dies, indem du ``ping <hostname>.local`` eingibst. Zum Beispiel:

    .. code-block::

        ping raspberrypi.local

    Du solltest die IP-Adresse des Raspberry Pi sehen, wenn er mit dem Netzwerk verbunden ist.

    * Wenn das Terminal eine Meldung wie ``Ping request could not find host pi.local. Please check the name and try again.`` anzeigt, überprüfe den eingegebenen Hostnamen.
    * Wenn du die IP-Adresse nicht abrufen kannst, überprüfe deine Netzwerk- oder WLAN-Einstellungen auf dem Raspberry Pi.

#. Starte eine SSH-Verbindung, indem du ``ssh <benutzername>@<hostname>.local`` oder ``ssh <benutzername>@<IP-Adresse>`` eingibst. Zum Beispiel:

    .. code-block::

        ssh pi@raspberrypi.local

#. Beim ersten Login erscheint eine Sicherheitsabfrage. Tippe ``yes``, um fortzufahren.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Gib das zuvor festgelegte Passwort ein. Aus Sicherheitsgründen wird das Passwort beim Tippen nicht angezeigt.

    .. note::
        Es ist normal, dass die eingegebenen Zeichen des Passworts im Terminal nicht angezeigt werden. Stelle einfach sicher, dass du das richtige Passwort eingibst.

#. Sobald du dich erfolgreich angemeldet hast, ist dein Raspberry Pi verbunden und du kannst mit dem nächsten Schritt fortfahren.


