.. _1.7_scratch:

1.7 Sparschwein
=========================

In diesem Projekt verwenden wir das Geschwindigkeitssensor-Modul, Raspberry Pi und Scratch, um ein Sparschwein zu erstellen.

Legen Sie ein Stück Papier in die Mitte des Geschwindigkeitssensors und Sie werden sehen, wie eine Münze auf der Bühne in das Sparschwein fällt.

.. image:: img/1.7_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten.

.. image:: img/1.7_component.png

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

    *   - :ref:`gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`breadboard`
        - |link_breadboard_buy|
    *   - :ref:`wires`
        - |link_wires_buy|
    *   - :ref:`speed_sensor`
        - \-

Schaltung aufbauen
---------------------

.. image:: img/1.7_fritzing.png

Laden Sie den Code und sehen Sie, was passiert
---------------------------------------------------

Laden Sie die Code-Datei (``1.7_piggy_bank.sb3``) in Scratch 3.

Die 2 Kontakte in der Mitte des Geschwindigkeitssensors dienen dazu, Licht zu senden bzw. zu empfangen. Wenn Sie ein Stück Papier in die Mitte legen, um die Lichtübertragung zu isolieren, gibt der Geschwindigkeitssensor ein hohes Signal aus. Zu diesem Zeitpunkt erhält Scratch das hohe Signal, wechselt dann die Kostüme des Sprites und Sie sehen, wie eine Münze auf der Bühne in das Sparschwein fällt.

Tipps zu Sprite
-------------------

Wählen Sie Sprite1 und klicken Sie in der oberen linken Ecke auf **Costumes**. Laden Sie **piggybank1.png**, **piggybank2.png** und **piggybank3.png** über den Pfad ``~/raphael-kit/scratch/picture`` mit der Schaltfläche **Upload Costume** hoch. Löschen Sie die beiden Standardkostüme und benennen Sie das Sprite in **piggybank** um.

.. image:: img/1.7_photoInterrupter1.png

Tipps zu Codes
----------------

.. image:: img/1.7_code2.png

Wenn pin17 niedrig ist (keine Münzen eingeworfen werden), wechseln Sie das Kostüm des Sprites zu **piggybank1**.

.. image:: img/1.7_code3.png

Wenn pin17 hoch ist (eine Münze wird eingeworfen), wechseln Sie das Kostüm des Sprites zu **piggybank2** und nach 0,5s zu **piggybank3**, sodass wir sehen können, wie eine Münze auf der Bühne in das Sparschwein fällt.
