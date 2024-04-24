.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _blinking_dot:

Blinkender Punkt
===========================

In diesem Projekt werden wir einen Punkt in Processing zeichnen, der synchron mit der LED blinkt. Bitte bauen Sie den Schaltkreis gemäß dem Diagramm auf und führen Sie die Skizze aus.

.. image:: img/blinking_dot.png
.. image:: img/clickable_dot_on.png

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link: 

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
    *   - :ref:`cpn_led`
        - |link_led_buy|

**Verdrahtung**

.. image:: img/image49.png

**Skizze**

.. code-block:: Arduino

    import processing.io.*;
    int ledPin = 17; 
    boolean state = true; 

    void setup() {
        size(100, 100);
        frameRate(2); //set frame rate
        GPIO.pinMode(ledPin, GPIO.OUTPUT); //set the ledPin to output mode 
    }

    void draw() {
        state = !state;
        if (state==true) {
            GPIO.digitalWrite(ledPin, GPIO.LOW); //led on 
            fill(255, 0, 0); //set the fill color of led on
        } else {
            GPIO.digitalWrite(ledPin, GPIO.HIGH); //led off
            fill(155); //set the fill color of led off
        } 
        ellipse(width/2, height/2, width*0.75, height*0.75);
    }

**Wie funktioniert das?**

Zu Beginn der Skizze müssen Sie die GPIO-Funktionsbibliothek von Processing mit ``import processing.io.*;`` einbinden, die für Schaltungsexperimente unerlässlich ist.

Die **Bildrate** ist die Häufigkeit, mit der Bitmaps auf dem Board erscheinen, ausgedrückt in Hertz (Hz). Anders ausgedrückt, ist es auch die Frequenz, mit der die ``draw()`` Funktion aufgerufen wird. In ``setup()`` ruft die Einstellung der **Bildrate** auf 2 ``draw()`` alle 0,5s auf.

Bei jedem Aufruf der ``draw()`` Funktion wird das Inverse von ``state`` genommen und anschließend bestimmt. Wenn der Wert ``true`` ist, leuchtet die LED und der Pinsel wird rot gefüllt; wenn nicht, wird die LED ausgeschaltet und der Pinsel mit Grau gefüllt.

Nach Abschluss der Beurteilung verwenden Sie die ``ellipse()`` Funktion, um einen Kreis zu zeichnen. Es sollte beachtet werden, dass ``width`` und ``height`` Systemvariablen sind, die zur Speicherung der Breite und Höhe des Anzeigefensters verwendet werden.

Es gibt zwei weitere Punkte zu beachten. Bei der Verwendung von GPIOs müssen Sie die ``GPIO.pinMode()`` Funktion verwenden, um den INPUT/OUTPUT-Zustand des Pins einzustellen, und dann die ``GPIO.digitalWrite()`` Funktion verwenden, um einen Wert (HIGH/LOW) dem Pin zuzuweisen.

.. note::

    Bitte versuchen Sie, ``delay()`` in ``draw()`` zu vermeiden, da dies die Aktualisierung des Anzeigefensters beeinflusst.