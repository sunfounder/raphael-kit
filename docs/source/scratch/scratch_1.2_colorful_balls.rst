.. _1.2_scratch:

1.2 Bunte Bälle
=====================

Wenn Sie auf unterschiedlich gefärbte Bälle im Bühnenbereich klicken, leuchtet die RGB-LED in verschiedenen Farben auf.

.. image:: img/1.2_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten.

.. image:: img/1.2_list.png

Es ist definitiv praktisch, ein komplettes Set zu kaufen, hier ist der Link:

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

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_rgb_led`
        - |link_rgb_led_buy|

Schaltung aufbauen
---------------------

.. image:: img/1.2_image61.png

Laden Sie den Code und sehen Sie, was passiert
------------------------------------------------

Nach dem Laden der Code-Datei (``1.2_colorful_balls.sb3``) in Scratch 3 wird die RGB-LED jeweils gelb, blau, rot, grün oder lila leuchten, wenn Sie auf den entsprechenden Ball klicken.

Tipps zu Sprite
-------------------

Löschen Sie das Standard-Sprite und wählen Sie das **Ball**-Sprite aus.

.. image:: img/1.2_ball.png

Und duplizieren Sie es 5 Mal.

.. image:: img/1.2_duplicate_ball.png

Wählen Sie für diese 5 **Ball**-Sprites unterschiedliche Kostüme und verschieben Sie sie an die entsprechenden Positionen.

.. image:: img/1.2_rgb1.png

Tipps zu Codes
--------------

Bevor wir den Code verstehen, müssen wir das `RGB-Farbmodell <https://en.wikipedia.org/wiki/RGB_color_model>`_ kennen.

Das RGB-Farbmodell ist ein additives Farbmodell, bei dem rotes, grünes und blaues Licht auf verschiedene Weise hinzugefügt wird, um eine breite Palette von Farben zu reproduzieren.

Additives Farbmischen: Rot und Grün ergibt Gelb; Grün und Blau ergibt Cyan; Blau und Rot ergibt Magenta; Alle drei Primärfarben zusammen ergeben Weiß.

.. image:: img/1.2_rgb_addition.png
  :width: 400

Eine RGB-LED besteht aus 3 LEDs (rote LED, grüne LED, blaue LED) in einem Gehäuse. Mit diesen drei Farben können Sie fast jede Farbe erzeugen.
Sie hat 4 Pins, einer davon ist GND, und die anderen 3 Pins steuern jeweils eine der 3 LEDs.

Der Code, um die RGB-LED gelb leuchten zu lassen, lautet also:

.. image:: img/1.2_rgb3.png

Wenn auf das Ball-Sprite (gelber Ball) geklickt wird, setzen wir gpio17 auf high (rote LED an), gpio18 auf high (grüne LED an) und gpio27 auf low (blaue LED aus), damit die RGB-LED gelb leuchtet.

Sie können Codes für andere Sprites auf die gleiche Weise schreiben, damit die RGB-LEDs in den entsprechenden Farben leuchten.
