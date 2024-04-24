.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _1.4_scratch:

1.4 Hase
==============

Heute werden wir mit Hilfe von Button, Raspberry Pi und Scratch einen Hasen erstellen, der verschiedene Veränderungen zeigt!

Wenn wir den ersten Button drücken, ändert der Hase in der Bühnenzone seine Körperfarbe; beim Drücken des zweiten Buttons ändert der Hase seine Körpergröße; und beim Drücken des dritten Buttons macht der Hase einen Schritt nach vorne.

.. image:: img/1.4_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten.

.. image:: img/1.4_list.png

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
    *   - :ref:`cpn_button`
        - |link_button_buy|

Schaltung aufbauen
---------------------

.. image:: img/1.4_scratch_button.png

Laden Sie den Code und sehen Sie, was passiert
------------------------------------------------

Laden Sie die Code-Datei (``1.4_hare.sb3``) in Scratch 3.

Jetzt können Sie versuchen, jeden der 3 Buttons zu drücken und zu sehen, wie sich der Hase auf der Bühne verändert.

Tipps zu Sprite
-------------------

Klicken Sie auf die Schaltfläche **Choose a Sprite** in der unteren rechten Ecke des Sprite-Bereichs, geben Sie **Hare** in das Suchfeld ein und klicken Sie dann, um es hinzuzufügen.

.. image:: img/1.4_button1.png

Löschen Sie Sprite1.

.. image:: img/1.4_button2.png

Tipps zu Codes
-----------------

.. image:: img/1.4_button3.png
  :width: 400

Dies ist ein Ereignisblock, der ausgelöst wird, wenn das Level von GPIO17 hoch ist, was bedeutet, dass der Button in diesem Moment gedrückt wird.

.. image:: img/1.4_button4.png
  :width: 400

Dieser Block ändert die Farbe von **Hare**. Der Wertebereich liegt zwischen 0 und 199; über 199 beginnt er wieder bei 0.

.. image:: img/1.4_button5.png
  :width: 250

Mit diesem Block wird die Größe des Sprites geändert; je höher der Wert, desto größer der Sprite.

.. note::
  Der Sprite ist auch nicht unendlich groß, und seine maximale Größe hängt von der ursprünglichen Bildgröße ab.

.. image:: img/1.4_button6.png
  :width: 200

Dieser Block wechselt die Kostüme des Sprites. Wenn das Kostüm von **Hare** kontinuierlich wechselt, führt es eine Reihe kohärenter Aktionen aus. Zum Beispiel, in diesem Projekt, lässt es **Hare** einen Schritt nach vorne machen.
