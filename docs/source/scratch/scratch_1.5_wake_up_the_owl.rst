.. _1.5_scratch:

1.5 Den Eulen wecken
====================

Heute spielen wir ein Spiel, in dem wir die Eule aufwecken.

Wenn sich jemand dem PIR-Sensormodul nähert, wird die Eule aus dem Schlaf erwachen.

.. image:: img/1.5_header.png

Benötigte Komponenten
------------------------------

In diesem Projekt benötigen wir die folgenden Komponenten.

.. image:: img/1.5_component.png

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

    *   - :ref:`gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`breadboard`
        - |link_breadboard_buy|
    *   - :ref:`wires`
        - |link_wires_buy|
    *   - :ref:`pir`
        - \-

Schaltung aufbauen
---------------------

.. image:: img/1.5_fritzing.png

Auf dem PIR-Modul gibt es zwei Potentiometer: eines zur Einstellung der Empfindlichkeit und das andere zur Einstellung der Erkennungsdistanz. Um das PIR-Modul optimal zu nutzen, sollten Sie beide Potentiometer bis zum Anschlag gegen den Uhrzeigersinn drehen.

.. image:: ../img/PIR_TTE.png
    :width: 400
    :align: center

Laden Sie den Code und sehen Sie, was passiert
-------------------------------------------------------

Laden Sie die Code-Datei (``1.5_wake_up_the_owl.sb3``) in Scratch 3.

Wenn Sie sich dem PIR-Sensormodul nähern, sehen Sie, wie die Eule im Bühnenbereich ihre Flügel ausbreitet und aufwacht. Entfernen Sie sich wieder, wird die Eule erneut einschlafen.

Tipps zu Sprite
-------------------

Wählen Sie Sprite1 aus und klicken Sie in der oberen linken Ecke auf **Costumes**; laden Sie **owl1.png** und **owl2.png** über den Pfad ``~/raphael-kit/scratch/picture`` mit der Schaltfläche **Upload Costume** hoch; löschen Sie die beiden Standardkostüme und benennen Sie das Sprite in **owl** um.

.. image:: img/1.5_pir1.png

Tipps zu Codes
--------------

.. image:: img/1.3_title2.png

Wenn die grüne Flagge angeklickt wird, wird der anfängliche Zustand von gpio17 auf niedrig gesetzt.

.. image:: img/1.5_owl1.png
  :width: 400

Wenn pin17 niedrig ist (sich niemand nähert), wechseln Sie das Kostüm des Eulen-Sprites zu owl1 (Schlafzustand).

.. image:: img/1.5_owl2.png
  :width: 400

Wenn pin17 hoch ist (sich jemand nähert), wechseln wir das Kostüm des Eulen-Sprites zu owl2 (Aufwachzustand).
