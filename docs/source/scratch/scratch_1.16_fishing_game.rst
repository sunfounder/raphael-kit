.. _1.16_scratch:

1.16 Angelspiel
========================

Heute erstellen wir ein Angelspiel.

Beobachten Sie das Wasser im Bühnenbereich und wenn Sie einen Fisch am Haken sehen, denken Sie daran, den Schalter zu kippen, um ihn zu fangen.

.. image:: img/1.16_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten. 

.. image:: img/1.16_component.png

Es ist definitiv praktisch, ein ganzes Set zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ELEMENTE IN DIESEM KIT
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

.. image:: img/1.16_fritzing.png

Laden Sie den Code und sehen Sie, was passiert
-------------------------------------------------

Laden Sie die Code-Datei (``1.16_fishing_game.sb3``) in Scratch 3.

Sie sehen ein Kind, das angelt. Nach einer Weile, wenn sich die Wasseroberfläche bewegt, können Sie den Kippschalter schütteln, um den Fisch zu fangen. Denken Sie daran, wenn Sie den Schalter nicht weiter schütteln, wird der Fisch entkommen.

Tipps zu Sprite
----------------

Wählen Sie Sprite1, klicken Sie oben links auf **Costumes**; laden Sie 6 Bilder (**fish1** bis **fish6**) aus dem Pfad ``~/raphael-kit/scratch/bild`` über die Schaltfläche **Upload Costume** hoch; löschen Sie die beiden Standardkostüme und benennen Sie das Sprite in **fish** um.

.. image:: img/1.16_upload_fish.png

Tipps zu Codes
--------------

.. image:: img/1.16_fish2.png
  :width: 400

Legen Sie das Anfangskostüm des **fish** Sprites auf **fish1** fest und weisen Sie dem Wert von **fish_status** 0 zu (wenn **fish_status=0**, bedeutet das, der Fisch ist nicht am Haken, bei **fish_status=1** ist der Fisch am Haken).

.. image:: img/1.16_fish3.png
  :width: 400

Wenn **fish_status=0**, also der Fisch noch nicht am Haken ist, beginnen Sie das Angelspiel. Warten Sie eine zufällige Zeit von 0 bis 10 Sekunden, dann setzen Sie **fish_status** auf 1, was bedeutet, dass der Fisch am Haken ist, und senden Sie eine Nachricht "Der Fisch beißt".

.. note::

  Der Zweck des Sendeblocks ist es, eine Nachricht an andere Codeblöcke oder andere Sprites zu senden. Die Nachricht kann entweder eine Anfrage oder ein Befehl sein.

.. image:: img/1.16_fish4.png
  :width: 400

Wenn die Nachricht "Der Fisch beißt" empfangen wird, lassen Sie das Fischsprite zwischen den Kostümen **fish2** und **fish3** wechseln, damit wir den Fisch sehen können, der beißt.

.. image:: img/1.16_fish5.png
  :width: 400

Nach dem Wechseln des Kostüms, wenn das Spiel nicht beendet ist, bedeutet das, dass der Fisch vom Haken gerutscht ist und weg ist, so dass wir das Kostüm des **fisch** Sprites auf **fish6** (Fisch rutschte Zustand) wechseln.

.. image:: img/1.16_fish6.png
  :width: 400

Wenn gpio17 hoch ist (der Kippschalter ist gekippt), bedeutet das, dass die Angel hochgezogen wird. Zu diesem Zeitpunkt wird der Wert von fish_status überprüft. Wenn er 1 ist, bedeutet das, dass die Angel hochgezogen wurde, als der Fisch am Haken war und auf das Kostüm fish4 (Fisch wurde gefangen) gewechselt wurde. Im Gegenteil, es bedeutet, dass die Angel hochgezogen wurde, als der Fisch nicht am Haken war, wird auf das Kostüm fish5 (nichts gefangen) gewechselt.

