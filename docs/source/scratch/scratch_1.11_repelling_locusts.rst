.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _1.11_scratch:

1.11 Heuschrecken vertreiben
====================================

Heute werden wir das IR-Hindernisvermeidungsmodul, Raspberry Pi und Scratch verwenden, um ein Heuschreckenabwehrspiel zu erstellen.

Halten Sie Ihre Hand vor das Hindernisvermeidungsmodul und Sie werden sehen, wie die Heuschrecken vertrieben werden.

.. image:: img/1.11_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten. 

.. image:: img/1.11_component.png

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
    *   - :ref:`cpn_infrared_avoidance`
        - |link_obstacle_avoidance_buy|

Schaltkreis aufbauen
----------------------

.. image:: img/1.11_fritzing.png
    :width: 700
    :align: center

Laden Sie den Code und sehen Sie, was passiert
---------------------------------------------------

Laden Sie die Code-Datei (``1.11_repelling_locusts.sb3``) in Scratch 3.

Halten Sie Ihre Hand vor das Hindernisvermeidungsmodul und Sie werden sehen, wie die Heuschrecken vertrieben werden.

Tipps zu Sprite
----------------

Wählen Sie Sprite1 und klicken Sie oben links auf **Costumes**; laden Sie **locust1.png**, **locust1.png** und **locust3.png** über den Pfad ``~/raphael-kit/scratch/picture`` mithilfe der Schaltfläche **Upload Costume** hoch; löschen Sie die 2 Standardkostüme und benennen Sie das Sprite in **locust** um.

.. image:: img/1.11_ir1.png

Tipps zu Codes
------------------

.. image:: img/1.11_ir2.png
  :width: 400

Wenn das IR-Hindernisvermeidungsmodul kein Hindernis erkennt (keine Hand wird vor der Sonde platziert), ist das GPIO hoch.

.. image:: img/1.11_ir3.png
  :width: 400

Wenn gpio17 hoch ist (keine Hindernisse kommen vor das IR-Hindernisvermeidungsmodul), wechseln Sie das Kostüm des Heuschrecken-Sprites zu locust1 (Heuschrecken sammeln sich im Weizen). Umgekehrt, wenn gpio17 niedrig ist (legen Sie Ihre Hand vor das IR-Hindernisvermeidungsmodul), wechseln Sie das Kostüm des Heuschrecken-Sprites zu locust2 (Heuschrecken vertreiben), und nach 0,5s wechseln Sie das Kostüm des Heuschrecken-Sprites zu locust3 (Heuschrecken sind vollständig vertrieben).
