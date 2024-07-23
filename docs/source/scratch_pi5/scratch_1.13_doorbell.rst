.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _1.13_scratch:

1.13 Türklingel
==================

Heute bauen wir eine Türklingel. Klicken Sie auf das Sprite „button3“ auf der Bühne, dann ertönt das Summen; klicken Sie erneut, dann hört das Summen auf.

.. image:: img/1.13_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten.

.. image:: img/1.13_list.png

Es ist definitiv praktisch, ein gesamtes Set zu kaufen. Hier ist der Link:

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
    *   - :ref:`cpn_buzzer`
        - \-
    *   - :ref:`cpn_transistor`
        - |link_transistor_buy|

Schaltkreis aufbauen
---------------------

.. image:: img/1.13_image106.png

Laden Sie den Code und sehen Sie, was passiert
------------------------------------------------

Laden Sie die Code-Datei (``1.13_doorbell.sb3``) in Scratch 3.

Klicken Sie auf die grüne Fahne auf der Bühne. Wenn wir auf das Sprite „Button 3“ klicken, wird es blau und der Summer ertönt; klicken wir erneut, kehrt das **Button3** Sprite zu Grau zurück und der Summer hört auf zu summen.

Tipps zu Sprites
----------------

Löschen Sie das Standard-Sprite und wählen Sie dann das Sprite **Button 3** aus.

.. image:: img/1.13_scratch_button3.png

Stellen Sie anschließend die Größe auf 200 ein.

.. image:: img/1.13_scratch_button3_size.png

Tipps zu Codes
--------------

.. image:: img/1.13_buzzer4.png
  :width: 400

Dieser Block ermöglicht das Wechseln des Sprites-Kostüms.

.. image:: img/1.13_buzzer5.png
  :width: 400

Setzen Sie gpio17 auf niedrig, damit der Summer ertönt; setzen Sie ihn auf hoch und der Summer wird nicht ertönen.

Der **status** Schalter wird hier verwendet, und wir werden ein Flussdiagramm verwenden, um Ihnen zu helfen, den gesamten Code zu verstehen.

Wenn auf die grüne Fahne geklickt wird, wird **status** zuerst auf 0 gesetzt und wartet zu diesem Zeitpunkt darauf, dass das Sprite angeklickt wird; wenn das **button3** Sprite angeklickt wird, wechselt es zum Kostüm **button-b** (blau) und **status** wird auf 1 gesetzt. Wenn das Hauptprogramm den **status** als 1 empfängt, lässt es den Summer in 0,1s-Intervallen ertönen.
Wenn **button3** erneut angeklickt wird, wechselt es zum Kostüm **button-a** (grau) und **status** wird wieder auf 0 gesetzt.

.. image:: img/1.13_scratch_code.png
