.. _1.1_scratch:

1.1 Zauberstab
=================

Heute werden wir LED, Raspberry Pi und Scratch nutzen, um ein unterhaltsames Spiel zu erstellen. Wenn wir den Zauberstab schwingen, blinkt die LED.

.. image:: img/1.1_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten.

.. image:: img/1.1_list.png

Es ist definitiv praktisch, ein gesamtes Set zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

Sie können sie auch einzeln über die untenstehenden Links kaufen.

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
    *   - :ref:`resistor`
        - |link_resistor_buy|
    *   - :ref:`led`
        - |link_led_buy|

Schaltung aufbauen
-----------------------

.. image:: img/1.1_image49.png

GPIO Erweiterung hinzufügen
-------------------------------

Klicken Sie unten links auf die Schaltfläche **Add Extension** und fügen Sie dann die **Raspberry Pi GPIO** hinzu, eine Erweiterung, die wir für all unsere Scratch-Projekte verwenden.

.. image:: img/1.1_scratchled1.png
    :align: center

.. image:: img/1.1_scratchled2.png
    :align: center

.. image:: img/1.1_scratchled3.png
    :align: center

Laden Sie den Code und sehen Sie, was passiert
---------------------------------------------------

Laden Sie die Code-Datei von Ihrem Computer (``~/raphael-kit/scratch/code``) in Scratch 3.

.. image:: img/1.1_scratch_step1.png

.. image:: img/1.1_scratch_step2.png

Nachdem Sie auf den Zauberstab im Bühnenbereich geklickt haben, wird die LED für zwei Sekunden blinken.

.. image:: img/1.1_step3.png

Tipps zu Sprite
---------------------

Klicken Sie auf **Upload Sprite**.

.. image:: img/1.1_upload_sprite.png

Laden Sie **Wand.png** aus dem Pfad ``~/raphael-kit/scratch/picture`` in Scratch 3 hoch.

.. image:: img/1.1_upload.png

Löschen Sie abschließend den **Sprite1**.

.. image:: img/1.1_delete.png

Tipps zu Codes
--------------

.. image:: img/1.1_LED1.png
  :width: 300

Dies ist ein Ereignisblock, dessen Auslösebedingung ein Klick auf die grüne Flagge auf der Bühne ist. Ein Auslöseereignis wird am Anfang aller Codes benötigt, und Sie können andere Auslöseereignisse in der **Events** Kategorie der **block palette** auswählen.

.. image:: img/1.1_events.png
  :width: 300

Zum Beispiel können wir das Auslöseereignis jetzt auf einen Klick auf das Sprite ändern.

.. image:: img/1.1_LED2.png
  :width: 300

Dies ist ein Block mit einer festgelegten Anzahl von Zyklen. Wenn wir die Zahl 10 eingeben, werden die Ereignisse im Block 10 Mal ausgeführt.

.. image:: img/1.1_LED4.png
  :width: 300

Mit diesem Block wird das Programm für eine bestimmte Zeit in Sekunden angehalten.

.. image:: img/1.1_LED3.png
  :width: 500

Da in Scratch die BCM-Namensgebung verwendet wird, stellt dieser Code GPIO17(BCM17) auf 0V (niedriges Niveau) ein. Da die Kathode der LED an GPIO17 angeschlossen ist, leuchtet die LED auf. Umgekehrt, wenn Sie GPIO(BCM17) als hoch setzen, schaltet sich die LED aus.
