.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _1.9_scratch_pi5:

1.9 Trommeln
================

In diesem Projekt spielen wir die Trommel mit einem Tastschaltermodul.

.. image:: img/1.9_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten.

.. image:: img/1.9_component.png

Es ist definitiv praktisch, ein komplettes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

Sie können diese auch einzeln über die untenstehenden Links kaufen.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - KOMPONENTENBESCHREIBUNG
        - KAUF-LINK

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_touch_switch`
        - |link_touch_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-

Schaltung aufbauen
---------------------

.. image:: img/1.9_fritzing.png

Laden Sie den Code und sehen Sie, was passiert
---------------------------------------------------

Laden Sie die Code-Datei (``1.9_drumming.sb3``) in Scratch 3.

Wenn Sie das Tastschaltermodul berühren, hören Sie den Trommelklang, der aus dem Lautsprecher kommt.

Tipps zu Sprite
-------------------

Löschen Sie das Standard-Sprite, suchen Sie dann das **Drum-snare**-Sprite, fügen Sie es hinzu und ändern Sie die Größe auf 200.

.. image:: img/1.9_touch1.png

Scratch verfügt über eine **Music**-Erweiterung zum Abspielen von Instrumenten und Trommeln. Fügen Sie diese nun über die Schaltfläche **Add Extension** hinzu.

.. image:: img/1.9_touch2.png

Tipps zu Codes
-----------------

.. image:: img/1.9_touch3.png
  :width: 400

Wenn pin17 niedrig ist (nicht auf das Tastschaltermodul getippt wurde), wechseln Sie das Kostüm des **Drum-snare**-Sprites zu **drum-snare-a**.

.. image:: img/1.9_touch4.png
  :width: 600

Wenn Sie das Tastschaltermodul berühren, ist gpio17 niedrig. Zu diesem Zeitpunkt wird das Kostüm des **Drum-snare**-Sprites zu **drum-snare-b** gewechselt und der Trommelsound über den Lautsprecher abgespielt.
