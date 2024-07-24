.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _1.10_scratch_pi5:

1.10 Trommeln in der Luft
==========================

Heute werden wir lernen, wie man die Raspberry Pi Kamera verwendet. Scratch verfügt über ein Erweiterungsmodul für Videoerkennung, welches die Kamera in Scratch aktiviert und die Bewegung von Objekten auf der Bühne erkennt.

.. image:: img/1.10_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten. 

.. image:: img/1.10_list.png

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
    *   - :ref:`cpn_audio_speaker`
        - \-
    *   - :ref:`cpn_camera_module`
        - |link_camera_buy|

Schaltung aufbauen
-------------------------

.. image:: img/1.10_fritzing_speaker.png

.. image:: img/1.10_camera.png

.. note::
  
  Sie sollten sich auf :ref:`cpn_camera_module` beziehen, um das Kameramodul anzuschließen und die Raspberry Pi Kamera-Schnittstelle zu aktivieren.

Laden Sie den Code und sehen Sie, was passiert
----------------------------------------------------

Laden Sie die Code-Datei (``1.10_drumming_in_the_air.sb3``) in Scratch 3.

Klicken Sie auf die grüne Flagge, um das Spiel zu starten. Halten Sie Ihre Hand vor das Kameramodul, und Scratch 3 wird Instrumentenklänge abspielen, wenn Ihre Hand ein Instrument auf der Bühnenfläche berührt.

.. note::

  Für ein besseres Spielerlebnis versuchen Sie, vor einem weißen Hintergrund zu spielen, um Störungen durch andere Objekte zu vermeiden.

Tipps zu Sprite
----------------

Löschen Sie zuerst die Standard-Sprites. Suchen Sie dann das **Drum-cymbal**-Sprite und das **Drum-snare**-Sprite und fügen Sie sie hinzu.

.. image:: img/1.10_camera1.png

Klicken Sie auf das Symbol **Add Extensio** unten links in Scratch und fügen Sie die Erweiterungen **Music** und **Video Sensing** hinzu.

.. image:: img/1.10_scratch.png

.. image:: img/1.10_scratch2.png

Tipps zu Codes
-----------------

.. image:: img/1.10_camera3.png

Wenn auf die grüne Flagge geklickt wird, wird ständig überprüft, ob unsere Hand sich um mehr als 60 über das **Drum-cymbal**-Sprite bewegt. Ist dies der Fall, wird davon ausgegangen, dass unsere Hand das Sprite berührt hat, und der Klang des Open Hi-Hat Instruments wird abgespielt.

.. note::

  Die Bewegungsmagnitude bezieht sich auf die Änderung der Koordinaten im Bühnenbereich, die in Bezug auf die Änderung der Koordinaten des Erkennungsziels im Bühnenbereich berechnet wird.

.. image:: img/1.10_camera4.png

Ebenso, wenn die Bewegung unserer Hand über das **Drum-snare**-Sprite als größer als 60 erkannt wird, wird angenommen, dass unsere Hand das Sprite berührt hat, und der Klang des Snare Drum Instruments wird abgespielt.
