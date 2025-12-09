.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _1.6_scratch_pi5:

1.6 Verschwindende Vase
========================

Lassen Sie uns jetzt einen kleinen Zaubertrick vollführen: Nichts tun und plötzlich verschwindet die Vase.

.. image:: img/1.6_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten.

.. image:: img/1.6_component.png

Es ist sicherlich praktisch, ein ganzes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

Sie können diese auch einzeln über die untenstehenden Links erwerben.

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
    *   - :ref:`cpn_reed_switch`
        - |link_reed_switch_buy|

Schaltung aufbauen
---------------------

.. image:: img/1.6_fritzing.png

Laden Sie den Code und sehen Sie, was passiert
---------------------------------------------------

Laden Sie die Code-Datei (``1.6_vanishing_vase.sb3``) in Scratch 3.

Wenn Sie einen Magneten in die Nähe des Reed-Schalter-Moduls bringen, erscheint eine Vase auf der Bühne. Entfernen Sie den Magneten, verschwindet die Vase.

Tipps zu Sprite
-------------------

Wählen Sie Sprite1 aus und klicken Sie in der oberen linken Ecke auf **Costumes**; laden Sie **desk1.png** und **desk2.png** über den Pfad ``~/raphael-kit/scratch/picture`` mit der Schaltfläche **Upload Costume** hoch; löschen Sie die beiden Standardkostüme und benennen Sie das Sprite in **desk** um.

.. image:: img/1.6_vase.png

Tipps zu Codes
----------------

.. image:: img/1.6_reed2.png
  :width: 400

Wenn der Magnet dem Reed-Schalter-Modul nahe ist, ist gpio17 niedrig, und das Kostüm des **desk**-Sprites wird auf **desk1** gewechselt (die Vase steht noch auf dem Tisch).

.. image:: img/1.6_reed3.png
  :width: 400

Nach dem Entfernen des Magneten ist gpio17 hoch. Zu diesem Zeitpunkt wird das Kostüm des **desk**-Sprites auf **desk2** gewechselt (nur ein Tisch).
