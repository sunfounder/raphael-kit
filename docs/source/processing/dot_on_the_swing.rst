.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _dot_on_the_swing:

Punkt auf der Schaukel
==============================

In diesem Projekt werden 3 Tasten verbunden: eine, um die Größe des Punktes zu ändern, eine, um die Position zu ändern und die letzte, um die Farbe zu ändern. Wenn Sie alle 3 Tasten gleichzeitig drücken, erhalten Sie einen schwingenden Punkt mit variabler Farbe.

.. image:: img/dancing_dot.png

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

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
    *   - :ref:`cpn_button`
        - |link_button_buy|

**Verdrahtung**

.. image:: img/circuit_dancing_dot.png

**Skizze**

.. code-block:: arduino

    import processing.io.*;

    // Define an instance of the Dot object
    Dot myDot;

    // Define the pins that will be reading button presses
    int[] pins = { 18, 23, 24 };

    void setup() {
        size(400, 400);
        // Change the color mode of the sketch to HSB
        colorMode(HSB, 360, 100, 100);
        noStroke();

        for (int i = 0; i < pins.length; i++) {
            GPIO.pinMode(pins[i], GPIO.INPUT_PULLUP);
        }

        // Create a Dot in the middle of the screen 
        myDot = new Dot(width / 2, height / 2, 100, 255);
    }

    void draw() {
        background(0); 

        // Modify attributes of the Dot depending on which buttons are pressed
        if (GPIO.digitalRead(pins[0]) == GPIO.LOW) {myDot.setSize();} 
        if (GPIO.digitalRead(pins[1]) == GPIO.LOW) {myDot.setPosition();} 
        if (GPIO.digitalRead(pins[2]) == GPIO.LOW) {myDot.setColor();} 

        // Update the Dot state
        myDot.update();
        // And draw it to the screen
        myDot.show();
    }

    class Dot { 

        float initX;
        float initY;
        float currentX;
        float currentY;
        int positionRange = 60;

        float initSize;
        float currentSize;
        int sizeRange = 50;

        int initColor;
        int currentColor;
        int ColorRange = 80;

        float timer = 0.0;
        float speed = 0.06;

        Dot(float x, float y, float s, int c) {
            initX = x;
            initY = y;
            currentX = x;
            currentY = y;

            initSize = s;
            currentSize = s;

            initColor = c;
            currentColor = c;
        }

        void setSize() {
            currentSize = initSize + sizeRange * sin( timer );
        }

        void setPosition() {
            currentY = initY + positionRange * cos( timer *2);
        }

        void setColor() {
            currentColor = int(initColor + ColorRange * sin( timer ));
        }

        void update() {
            timer += speed;
        }

        void show() {
            fill(currentColor, 100, 100); 
            ellipse(currentX, currentY, currentSize, currentSize);
        }
    }

**Wie funktioniert das?**

Anstatt den Punkt direkt zu zeichnen, erstellen wir hier eine ``Dot``-Klasse.
Danach wird das Objekt (in diesem Fall ``myDot``) deklariert.

Dies ist eine einfache Möglichkeit, Punkte mit mehreren identischen Eigenschaften zu zeichnen.
Wenn wir beispielsweise in diesem Projekt dem Punkt drei Funktionen hinzufügen - Größe ändern, Position ändern und Farbe ändern - dann hat jeder von uns deklarierte Punkt dieselbe Funktion.
Wir können denselben Knopf verwenden, um sie alle das Gleiche tun zu lassen, oder wir können verschiedene Tasten verwenden, um jeden Punkt separat zu steuern.

Die Verwendung von **Klassen** macht Ihren Skizzenentwurf schön, leistungsstark und flexibel.

`Klasse (Programmierung) – Wikipedia <https://en.wikipedia.org/wiki/Class_(computer_programming)>`_

Schauen wir uns nun die ``Dot``-Klasse genauer an.

.. code-block:: arduino

    Dot(float x, float y, float s, int c)

Bei der Deklaration müssen vier Parameter übergeben werden: der X- und der Y-Koordinatenwert der Position, die Größe und die Farbe (hier im `HSB-Farbmodus <https://en.wikipedia.org/wiki/HSL_and_HSV>`_ eingestellt).

Jeder Parameter wird 2 Wertesätzen zugewiesen (Anfangswert und aktueller Wert).

.. code-block:: arduino

    float initX;
    float initY;
    float currentX;
    float currentY;
    int positionRange = 60;

    float initSize;
    float currentSize;
    int sizeRange = 50;

    int initColor;
    int currentColor;
    int ColorRange = 80;

Zusätzlich zum Anfangswert und zum aktuellen Wert gibt es auch einen Satz von Bereichswerten. Es ist nicht schwer zu verstehen, dass der Anfangswert dazu dient, den Anfangszustand des Punktes zu bestimmen (durch die eingehenden Parameter), während sich der aktuelle Wert innerhalb des Bereichs ändert, um den Punkt zu bewegen.

Daher werden, mit Ausnahme des X-Koordinatenwerts, die aktuellen Werte der anderen drei Parameter wie folgt berechnet:

.. code-block:: arduino

    void setSize() {
        currentSize = initSize + sizeRange * sin( timer );
    }

    void setPosition() {
        currentY = initY + positionRange * cos( timer *2);
    }

    void setColor() {
        currentColor = int(initColor + ColorRange * sin( timer ));
    }

Wenn Sie mit trigonometrischen Funktionen vertraut sind, sollte es nicht schwierig sein, `Sinus und Kosinus <https://en.wikipedia.org/wiki/Sine>`_ zu verstehen, wodurch eine glatte periodische Änderung (von -1 bis 1) des aktuellen Wertes des Punktes erzeugt wird.

Wir müssen auch einen Ausgangswert, ``timer``, für die periodische Variation hinzufügen. Er fügt den festen Wert in der Methode ``update()`` hinzu und wird in ``draw()`` aufgerufen.

.. code-block:: arduino

    void update() {
        timer += speed;
    }

Schließlich wird der Punkt gemäß dem aktuellen Wert mit der Methode ``show()`` angezeigt, die ebenfalls in ``draw()`` aufgerufen wird.

.. code-block:: arduino

    void show() {
        fill(currentColor, 100, 100); 
        ellipse(currentX, currentY, currentSize, currentSize);
    }

**Was gibt es noch?**

Wenn Sie den Einsatz von Klassen gemeistert haben, können Sie bereits mehrere Punkte mit den gleichen Eigenschaften zeichnen. Warum also nicht etwas Cooleres ausprobieren?
Wie wäre es beispielsweise, ein stabiles Doppelsternsystem zu zeichnen oder ein "DUET"-Spiel zu erstellen?
