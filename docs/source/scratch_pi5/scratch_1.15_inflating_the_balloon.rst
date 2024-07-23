.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _1.15_scratch:

1.15 Das Aufblasen des Ballons
=================================

Hier spielen wir ein Ballonaufblas-Spiel.

Um mit dem Aufblasen des Ballons zu beginnen, schieben Sie den Schieberegler nach links. Der Ballon wird dann immer größer. Wenn der Ballon zu groß ist, wird er platzen; wenn er zu klein ist, wird er nicht in die Luft steigen. Sie müssen den richtigen Zeitpunkt abwägen, um den Schalter nach rechts zu schieben und das Pumpen zu stoppen.

.. image:: img/1.15_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten. 

.. image:: img/1.15_component.png

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

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_slide_switch`
        - |link_slide_switch_buy|
    *   - :ref:`cpn_capacitor`
        - |link_capacitor_buy|

Schaltung aufbauen
---------------------

.. image:: img/1.15_scratch_fritzing.png

Laden Sie den Code und sehen Sie, was passiert
-------------------------------------------------

Laden Sie die Code-Datei (``1.15_inflating_the_balloon.sb3``) in Scratch 3.

Durch das Schieben des Sliders nach links beginnen Sie mit dem Aufblasen des Ballons. In dieser Phase wird der Ballon stetig größer. Wenn der Ballon zu groß ist, wird er platzen; wenn er zu klein ist, wird er nicht abheben. Sie müssen den richtigen Zeitpunkt abwägen, um den Schalter nach rechts zu schieben und das Pumpen zu stoppen.

Tipps zu Sprite
----------------

Löschen Sie den vorherigen Sprite1 und fügen Sie den **Balloon1**-Sprite hinzu.

.. image:: img/1.15_slide1.png

Für dieses Projekt wird ein Ballonexplosions-Soundeffekt verwendet. Sehen Sie sich an, wie er hinzugefügt wurde.

Klicken Sie auf die **Sound**-Option oben und dann auf **Upload Sound**, um ``boom.wav`` aus dem Pfad ``~/raphael-kit/scratch/sound`` in Scratch 3 hochzuladen.

.. image:: img/1.15_slide2.png

Tipps zu Codes
--------------

.. image:: img/1.15_slide3.png
  :width: 500

Dies ist ein Ereignisblock. Die Auslösebedingung ist, dass gpio17 hoch ist, das heißt, der Schalter ist nach links verschoben.

.. image:: img/1.15_slide4.png
  :width: 400

Legen Sie den Größenschwellenwert des Ballon1-Sprites auf 120 fest.

.. image:: img/1.15_slide7.png
  :width: 400

Verschieben Sie die Koordinaten des Ballon1-Sprites auf (0,0), was das Zentrum des Bühnenbereichs ist.

.. image:: img/1.15_slide8.png
  :width: 300

Stellen Sie die Größe des Ballon1-Sprites auf 50 ein und zeigen Sie ihn im Bühnenbereich.

.. image:: img/1.15_slide5.png

Richten Sie eine Schleife ein, um den Ballon aufzublasen. Diese Schleife stoppt, wenn der Schiebeschalter nach rechts verschoben wird.

Innerhalb dieser Schleife wird die Ballongröße alle 0,1s um 1 erhöht. Wenn sie größer als ``maxSize`` ist, wird der Ballon platzen, und der Boom-Sound wird abgespielt und der Code beendet.

.. image:: img/1.15_slide6.png
  :width: 600

Nachdem die letzte Schleife beendet ist (Slider wird nach rechts verschoben), bestimmen Sie die Position des Ballon1-Sprites basierend auf seiner Größe. Wenn die Größe des Ballon1-Sprites größer als 90 ist, hebt er ab (verschiebt die Koordinaten auf (0, 90), ansonsten landet er (verschiebt die Koordinaten auf (0, -149).

