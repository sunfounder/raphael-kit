.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _play_with_processing:

Spielen Sie mit der Verarbeitung (nicht für Pi 5)
===========================================================

Was ist Processing?
---------------------------

Processing ist eine einfache Programmierumgebung, die entwickelt wurde, um die Erstellung von visuell orientierten Anwendungen mit Schwerpunkt auf Animation zu vereinfachen und den Benutzern durch Interaktion ein sofortiges Feedback zu bieten.
Die Entwickler wollten eine Möglichkeit, Ideen im Code zu "skizzieren".
Mit der Erweiterung seiner Fähigkeiten im Laufe des letzten Jahrzehnts wird Processing neben seiner Skizzierfunktion auch für fortgeschrittene produktionsreife Arbeiten verwendet.
Ursprünglich als domänenspezifische Erweiterung zu Java für Künstler und Designer erstellt, hat sich Processing zu einem vollwertigen Design- und Prototyping-Tool entwickelt, das für großangelegte Installationsarbeiten, Motion Graphics und komplexe Datenvisualisierung eingesetzt wird.

Processing basiert auf Java, aber da die Programmelemente in Processing recht einfach sind, können Sie es erlernen, auch wenn Sie kein Java kennen. Wenn Sie mit Java vertraut sind, ist es am besten, zu vergessen, dass Processing etwas mit Java zu tun hat, bis Sie den Dreh raus haben, wie die API funktioniert.

Dieser Text stammt aus dem Tutorial `Processing Übersicht <https://processing.org/tutorials/overview/>`_.

Processing installieren
------------------------------

.. note:: 

    Bevor Sie Processing nutzen können, müssen Sie auf den Raspberry Pi Desktop remote zugreifen (:ref:`remote_desktop`) oder einen Bildschirm für den Raspberry Pi anschließen.

.. Führen Sie den folgenden Befehl im Terminal aus, um Processing zu installieren.

.. .. raw:: html

..    <run></run>

.. .. code-block:: 

..     curl https://processing.org/download/install-arm.sh | sudo sh

.. Nachdem die Installation abgeschlossen ist, geben Sie ``processing`` ein, um es zu öffnen.

.. .. image:: img/processing1.png

.. Für ein detailliertes Tutorial, siehe `Pi Processing <https://pi.processing.org/>`_.

#. Zuerst besuchen Sie https://processing.org/download und wählen die ``Linux（Raspberry Pi 32-bit）`` oder ``Linux（Raspberry Pi 64-bit）`` Version. Mit dieser Methode können Sie immer die neueste Version herunterladen.

    Alternativ können Sie den folgenden Befehl verwenden, um Processing aus dem Terminal herunterzuladen.

    .. code-block:: 

        wget https://github.com/benfry/processing4/releases/download/processing-1293-4.3/processing-4.3-linux-arm32.tgz

    .. code-block:: 

        wget https://github.com/benfry/processing4/releases/download/processing-1293-4.3/processing-4.3-linux-arm64.tgz


#. Eine ``.tar.gz`` Datei wird heruntergeladen, mit der die meisten Linux-Benutzer vertraut sein sollten. Entpacken Sie die gerade heruntergeladene Datei.

    .. code-block:: 

        tar xvfz processing-xxxx.tgz

    Ersetzen Sie xxxx durch den Rest des Dateinamens, also die Versionsnummer. Dies wird einen Ordner namens processing-xxxx oder ähnliches erstellen. 

#. Wechseln Sie dann in dieses Verzeichnis:

    .. code-block:: 

        cd processing-xxxx

#. Und starten Sie es:

.. code-block:: 

    ./processing

#. Mit etwas Glück wird das Hauptfenster von Processing jetzt sichtbar sein.

    .. image:: img/processing2.png


Hardware I/O installieren
-------------------------------

Um den GPIO des Raspberry Pi zu nutzen, müssen Sie manuell eine `Hardware I/O-Bibliothek <https://processing.org/reference/libraries/io/index.html>`_ hinzufügen.

Klicken Sie auf ``Sketch`` -> ``Import Library`` -> ``Add Library...`` 

.. image:: img/import-00.png

Finden Sie Hardware I/O, wählen Sie es aus und klicken Sie dann auf Installieren. Wenn es fertig ist, erscheint ein Häkchen-Symbol.

.. image:: img/import-02.png


Projekte
---------------

.. toctree::
    draw_a_matchmaker
    hello_mouse
    blinking_dot
    clickable_dot
    clickable_color_blocks
    inflating_the_dot
    dot_on_the_swing
    metronome
    show_number
    drag_number
