.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _1.17_scratch_pi5:

1.17 Drehender Ventilator
============================

In diesem Projekt werden wir einen rotierenden Stern-Sprite und einen Ventilator erstellen.

.. image:: img/1.17_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir folgende Komponenten.

.. image:: img/1.17_list.png

Es ist definitiv praktisch, ein ganzes Set zu kaufen. Hier ist der Link:

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
    *   - :ref:`cpn_power_module`
        - \-
    *   - :ref:`cpn_l293d`
        - \-
    *   - :ref:`cpn_motor`
        - |link_motor_buy|

Schaltung aufbauen
---------------------

.. image:: img/1.17_image117.png

Laden Sie den Code und sehen Sie, was passiert
------------------------------------------------

Laden Sie die Code-Datei (``1.17_rotating_fan.sb3``) in Scratch 3.

Nachdem Sie auf die grüne Flagge auf der Bühne geklickt haben, klicken Sie auf den Stern-Sprite. Dann werden dieser und der Motor im Uhrzeigersinn drehen. Sie können die Drehrichtung ändern, indem Sie auf die beiden **arrow**-Sprites klicken. Wenn Sie erneut auf den **star**-Sprite klicken, hören er und der Motor auf zu drehen.

Tipps zu Sprite
----------------

Löschen Sie den Standard-Sprite und wählen Sie dann den **star**-Sprite und den **Arrow1**-Sprite aus und kopieren Sie Pfeil1 einmal.

.. image:: img/1.17_motor1.png

Unter der Option **Costumes** ändern Sie das Pfeil2-Sprite zu einem Kostüm in anderer Richtung.

.. image:: img/1.17_motor2.png

Passen Sie die Größe und Position des Sprites entsprechend an.

.. image:: img/1.17_motor3.png

Tipps zu Codes
--------------

**Flussdiagramm**

.. image:: img/1.17_scratch.png

In diesem Code sehen Sie 2 rosa Blöcke, links drehen und rechts drehen. Das sind unsere benutzerdefinierten Blöcke (Funktionen).

.. image:: img/1.17_new_block.png

**Wie erstellt man einen Block?**

Lernen Sie, wie Sie einen Block (Funktion) erstellen. Der Block (Funktion) kann verwendet werden, um Ihr Programm zu vereinfachen, insbesondere wenn Sie die gleiche Operation mehrmals ausführen. Das Platzieren dieser Operationen in einem neu deklarierten Block kann sehr praktisch für Sie sein.

Suchen Sie zuerst **My Blocks** in der Blockpalette und wählen Sie dann **Make a Block**.

.. image:: img/1.17_motor4.png

Geben Sie den Namen des neuen Blocks ein.

.. image:: img/1.17_motor5.png

Nachdem Sie die Funktion des neuen Blocks im Codierungsbereich geschrieben haben, speichern Sie ihn, und dann können Sie den Block in der Blockpalette finden.

.. image:: img/1.17_motor6.png

**links drehen**

Dies ist der Code im Block "links drehen", um den Motor gegen den Uhrzeigersinn zu drehen.

.. image:: img/1.17_motor12.png
  :width: 400

**rechts drehen**

Dies ist der Code im Block "rechts drehen", um den Motor im Uhrzeigersinn zu drehen.

.. image:: img/1.17_motor11.png
  :width: 400
