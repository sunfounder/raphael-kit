.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Sneak Peeks.
    - **Sonderrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _login_windows:

PuTTY
=========================

Wenn Sie Windows-Benutzer sind, können Sie einige SSH-Anwendungen verwenden. Hier empfehlen wir `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_.

**Schritt 1**

Laden Sie PuTTY herunter.

**Schritt 2**

Öffnen Sie PuTTY und klicken Sie auf **Session** in der baumähnlichen Struktur auf der linken Seite. Geben Sie die IP-Adresse des Raspberry Pi in das Textfeld unter **Host Name (or IP address)** ein und **22** unter **Port** (standardmäßig ist dies 22).

.. image:: img/image25.png
    :align: center

**Schritt 3**

Klicken Sie auf **Open**. Beachten Sie, dass beim ersten Anmelden am Raspberry Pi mit der IP-Adresse eine Sicherheitswarnung angezeigt wird. Klicken Sie einfach auf **Yes**.

**Schritt 4**

Wenn im PuTTY-Fenster \"**login as:**\" angezeigt wird, geben Sie \"**pi**\" (den Benutzernamen des Raspberry Pi) ein und als **Passwort**: \"raspberry\" (das Standardpasswort, falls Sie es nicht geändert haben).

.. note::

    Wenn Sie das Passwort eingeben, werden die Zeichen im Fenster nicht angezeigt, was normal ist. Sie müssen lediglich das richtige Passwort eingeben.
    
    Wenn neben PuTTY „inactive“ angezeigt wird, bedeutet dies, dass die Verbindung unterbrochen wurde und neu hergestellt werden muss.
    
.. image:: img/image26.png
    :align: center

**Schritt 5**

Nun ist der Raspberry Pi verbunden und es ist Zeit, die nächsten Schritte durchzuführen.
