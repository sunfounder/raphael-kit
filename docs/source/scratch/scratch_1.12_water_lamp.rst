.. _1.12_scratch:

1.12 Wasserlampe
================

Heute werden wir die LED-Balkenanzeige, Raspberry Pi und Scratch verwenden, um eine Wasserlampe zu erstellen.

Die LED-Balkenanzeige wird in der Reihenfolge der Pfeilrichtung auf der Bühne aufleuchten.

.. image:: img/1.12_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten.

.. image:: img/1.12_list.png

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
    *   - :ref:`cpn_bar_graph`
        - \-

Schaltung aufbauen
-----------------------

.. image:: img/1.12_image66.png

Laden Sie den Code und sehen Sie, was passiert
-------------------------------------------------

Laden Sie die Code-Datei (``1.12_water_lamp.sb3``) von Ihrem Computer in Scratch 3.

Durch Klicken auf **Arrow1** leuchten die LEDs auf dem LED-Balken nacheinander von links nach rechts (jeweils eine) und gehen dann aus. Klicken Sie auf **Arrow2** und die LEDs leuchten in umgekehrter Reihenfolge.

Tipps zu Sprites
----------------

Löschen Sie das Standard-Sprite und wählen Sie das Sprite **Arrow1**.

.. image:: img/1.12_graph1.png

Hier benötigen wir 2 **Arrow1** Sprites, was mit der Duplizieren-Taste gemacht werden kann.

.. image:: img/1.12_scratch_duplicate.png

Klicken Sie auf das Sprite **Arrow 2** und ändern Sie die Pfeilrichtung, indem Sie Kostüm 2 auswählen.

.. image:: img/1.12_graph2.png

Jetzt erstellen wir eine Variable.

.. image:: img/1.12_graph3.png

Benennen Sie sie als **num**.

.. image:: img/1.12_graph4.png

Verfolgen Sie die gleiche Methode, um eine Liste namens **led** zu erstellen.

.. image:: img/1.12_graph6.png

Nach dem Hinzufügen sollten Sie die Variable **num** und die Liste **led** im Bühnenbereich sehen.

Klicken Sie auf **+**, um 10 Listenelemente hinzuzufügen und geben Sie die Pin-Nummern in der Reihenfolge (17,18,27,22,23,24,25,2,3,8) ein.

.. image:: img/1.12_graph7.png

Tipps zu Codes
--------------

.. image:: img/1.12_graph10.png
  :width: 300

Dies ist ein Ereignisblock, der ausgelöst wird, wenn das aktuelle Sprite angeklickt wird.

.. image:: img/1.12_graph8.png
  :width: 300

Der Anfangswert der Variable **num** bestimmt, welche LED zuerst leuchtet.

.. image:: img/1.12_graph9.png

Setzen Sie den Pin, der **num** in der Led-Liste entspricht, auf niedrig, um die LED zu beleuchten, und setzen Sie dann den Pin, der **num-1** entspricht, auf hoch, um die vorherige LED auszuschalten.
