.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _1.8_scratch:

1.8 Serviceklingel
===================

Heute verwenden wir Mikroschalter, Lautsprecher, Audioverstärkermodul, Raspberry Pi und Scratch, um eine Serviceklingel zu bauen.

Betätigen Sie den Mikroschalter, um den Klang der Serviceklingel auszulösen.

.. image:: img/1.8_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten.

.. image:: img/1.8_component.png

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
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_micro_switch`
        - \-
    *   - :ref:`cpn_capacitor`
        - |link_capacitor_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-

Schaltung aufbauen
---------------------

.. image:: img/1.8_fritzing.png

Laden Sie den Code und sehen Sie, was passiert
---------------------------------------------------

Laden Sie die Code-Datei (``1.8_service_bell.sb3``) in Scratch 3.

Drücken Sie den Mikroschalter, und die Serviceklingel wird einmal klingeln.

.. note::
  
  Wenn Ihr Raspberry Pi an einen Bildschirm mit Lautsprechern angeschlossen ist, kann dies dazu führen, dass dieser externe Lautsprecher keinen Ton ausgibt. Bitte beziehen Sie sich auf :ref:`change_audio_output` für eine Lösung.

  Wenn Sie außerdem die Lautstärke anpassen möchten, konsultieren Sie bitte :ref:`adjust_volume`.

Tipps zu Sprite
---------------------

Wählen Sie Sprite1 und klicken Sie in der oberen linken Ecke auf **Costumes**. Laden Sie **bell1.png** und **bell2.png** über den Pfad ``~/raphael-kit/scratch/picture`` mit der Schaltfläche **Upload Costume** hoch. Löschen Sie die beiden Standardkostüme und benennen Sie das Sprite in **bell** um.

.. image:: img/1.8_travel1.png

Im **Sounds**-Bereich laden Sie die Datei ``bell.wav`` aus dem Pfad ``~/raphael-kit/scratch/sound`` in Scratch 3 hoch.

.. image:: img/1.8_travel2.png

Tipps zu Codes
--------------

.. image:: img/1.8_travel3.png
  :width: 400

Wenn pin17 hoch ist (der Mikroschalter ist nicht betätigt), wechseln Sie das Kostüm des Sprites **bell** zu **bell1** (entspannter Zustand).

.. image:: img/1.8_travel4.png
  :width: 400

Drücken Sie den Mikroschalter, gpio17 ist auf niedrigem Level. Zu diesem Zeitpunkt wechseln Sie das Kostüm des Sprites **bell** zu **bell2** (gedrückter Zustand) und spielen Sie einen Soundeffekt über den Lautsprecher ab.
