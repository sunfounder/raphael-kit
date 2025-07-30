.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten Community auf Facebook! Tauchen Sie mit anderen Enthusiasten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Vorschauen.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!


Für alle Modelle (empfohlen)
===============================

Die Veröffentlichung des Raspberry Pi 5 hat uns ein leistungsstärkeres Modell gebracht, aber auch einige Änderungen mit sich gebracht, insbesondere im Hinblick auf die GPIO. Obwohl das Standard-40-Pin-Interface beibehalten wurde, hat sich die Funktionalität aufgrund der Verbindung mit dem neu integrierten RP1-Southbridge-Chip verschoben. Dieser benutzerdefinierte RP1-Chip verwaltet nun die Peripheriegeräte auf dem Pi 5 und hat zu verschiedenen Kompatibilitätsproblemen geführt. Derzeit ist nur die GPIO Zero-Bibliothek, die offiziell von der Raspberry Pi-Organisation gewartet wird, vollständig kompatibel. Wir haben eine Reihe von Kursen entwickelt, die sich speziell auf diese Bibliothek konzentrieren.

.. toctree::
    :maxdepth: 1
    
    python_pi5/play_with_python_pi5
    c_pi5/play_with_c
    scratch_pi5/play_with_scratch

Bei Kompatibilitätsproblemen mit anderen Programmiersprachen finden Sie unten detaillierte Informationen:


**Processing**

Bei der Verwendung von Processing 4 auf dem Raspberry Pi 5 treten bei der GPIO-Programmierung Herausforderungen auf. Fehler wie "Invalid argument" und "GPIO pin 17 scheint auf Ihrer Plattform nicht verfügbar zu sein" treten während der Ausführung von GPIO-bezogenem Code auf (wie im beigefügten Bild dargestellt). Weitere Details finden Sie unter: https://github.com/benfry/processing4/issues/807

.. image:: img/pi5_processing.png

**Node.js**

Node.js verwendet die pigpio-Bibliothek, die derzeit den Raspberry Pi 5 nicht unterstützt. Weitere Einblicke finden Sie unter: https://github.com/joan2937/pigpio/issues/589

.. image:: img/pi5_nodejs.png
    :width: 700

Auf einem 64-Bit-System treten bei der Einfuhr der Raspberry Pi GPIO-Bibliothek Probleme auf, die zu einer Unempfindlichkeit führen. Weitere Informationen finden Sie unter: https://github.com/raspberrypi/bookworm-feedback/issues/91.
