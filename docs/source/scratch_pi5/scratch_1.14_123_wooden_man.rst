.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _1.14_scratch_pi5:

1.14 123 Holzmensch
===========================

Heute spielen wir das Spiel "123 Holzmensch".

Klicken Sie auf die grüne Flagge, um das Spiel zu starten. Halten Sie die rechte Pfeiltaste auf der Tastatur gedrückt, damit die Figur nach rechts geht. Wenn das grüne Licht an ist, kann die Figur sich bewegen; aber wenn die rote LED leuchtet, müssen Sie die Figur stoppen; sonst wird der Summer dauerhaft klingeln.

.. image:: img/1.14_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir die folgenden Komponenten.

.. image:: img/1.14_component.png

Es ist definitiv praktisch, ein ganzes Set zu kaufen, hier ist der Link:

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

    *   - KOMPONENTEN ÜBERSICHT
        - KAUF LINK

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_Buzzer`
        - |link_passive_buzzer_buy|
    *   - :ref:`cpn_led`
        - |link_led_buy|
    *   - :ref:`cpn_transistor`
        - |link_transistor_buy|

Schaltkreis aufbauen
---------------------

.. image:: img/1.14_fritzing.png

Laden Sie den Code und sehen Sie, was passiert
-------------------------------------------------

Laden Sie die Code-Datei (``1.14_123_wooden_man.sb3``) in Scratch 3.

Wenn die grüne LED leuchtet, können Sie mit der rechten Pfeiltaste **Avery** steuern, um nach rechts zu gehen; wenn die rote LED leuchtet und Sie **Avery** weiter nach rechts bewegen, wird ein Alarm ausgelöst.

Tipps zu Sprite
---------------------

Löschen Sie die Standardfigur und wählen Sie dann die **Avery Walking** Figur aus.

.. image:: img/1.14_wooden1.png
  :width: 400

Tipps zu Codes
--------------

.. image:: img/1.14_wooden2.png
  :width: 400

Alle Pins auf hoch initialisieren.

.. image:: img/1.14_wooden3.png
  :width: 400

Wenn das Spiel startet, setzen Sie die Statusvariable auf 1, was bedeutet, dass die Figur **Avery Walking** beweglich ist. Dann setzen Sie gpio18 auf niedrig, was die grüne LED für 5s aufleuchten lässt.

.. image:: img/1.14_wooden4.png
  :width: 400

Setzen Sie gpio18 auf hoch und dann gpio27 auf niedrig, was bedeutet, dass Sie die grüne LED ausschalten und die gelbe LED für 0,5s einschalten.

.. image:: img/1.14_wooden5.png
  :width: 400

Setzen Sie die Statusvariable auf 0, was bedeutet, dass die Figur **Avery Walking** nicht bewegt wird. Setzen Sie dann gpio27 auf niedrig und gpio17 auf hoch, was die gelbe LED ausschaltet und dann die rote LED für 3s einschaltet. Schließlich setzen Sie gpio17 auf hoch, um die rote LED auszuschalten.

.. image:: img/1.14_wooden6.png
  :width: 400

Wenn wir die rechte Pfeiltaste auf der Tastatur drücken, müssen wir die **Avery Walking** Figur zum nächsten Kostüm wechseln, damit wir sehen können, wie Avery nach rechts geht. Dann müssen wir den Wert der **status** Variablen bestimmen. Wenn er 0 ist, bedeutet das, dass die Figur **Avery Walking** in diesem Moment nicht bewegt wird, und der Summer wird klingen, um Sie zu warnen, dass Sie die rechte Pfeiltaste nicht erneut drücken können.

