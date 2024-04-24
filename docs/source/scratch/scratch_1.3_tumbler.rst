.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _1.3_scratch:

1.3 Kipp-Schalter-Spielzeug
================================

In diesem Projekt werden wir ein Spielzeug bauen, das durch einen Kippschalter gesteuert wird.

.. image:: img/1.3_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten.

.. image:: img/1.3_component.png

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

Sie können diese auch einzeln über die folgenden Links erwerben.

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
    *   - :ref:`cpn_tilt_switch` 
        - \-

Schaltung aufbauen
---------------------

.. image:: img/1.3_fritzing.png

Laden Sie den Code und sehen Sie, was passiert
------------------------------------------------

Laden Sie die Code-Datei (``1.3_tumbler.sb3``) in Scratch 3.

Wenn der Kippschalter senkrecht steht, steht auch das Spielzeug. Wenn Sie ihn kippen, fällt das Spielzeug. Stellen Sie ihn wieder senkrecht auf, und das Spielzeug richtet sich wieder auf.

Tipps zu Sprite
------------------

Wählen Sie Sprite1 und klicken Sie oben links auf **Kostüme**; laden Sie **tumbler1.png** und **tumbler2.png** aus dem Pfad ``~/raphael-kit/scratch/picture`` über die Schaltfläche **Kostüm hochladen**; löschen Sie die beiden standardmäßigen Kostüme und benennen Sie das Sprite in **tumbler** um.

.. image:: img/1.3_add_tumbler.png

Tipps zu Codes
----------------

.. image:: img/1.3_title2.png
  :width: 400

Wenn die grüne Flagge angeklickt wird, wird der Anfangszustand von gpio17 auf niedrig gesetzt.

.. image:: img/1.3_title4.png
  :width: 400

Wenn pin17 niedrig ist (der Kippschalter steht senkrecht), wechseln wir das Kostüm des tumbler Sprites zu tumbler1 (aufrechter Zustand).

.. image:: img/1.3_title3.png
  :width: 400

Wenn pin17 hoch ist (Kippschalter ist gekippt), wechseln wir das Kostüm des tumbler Sprites zu tumbler2 (gekippter Zustand).
