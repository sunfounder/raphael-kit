Aufblasen des Punkts
===========================

Als Nächstes bauen wir einen Schaltkreis, der es dem Knopf ermöglicht, die Größe des Punktes zu steuern.
Wenn wir den Knopf drücken, wird der Punkt schnell größer; wenn wir den Knopf loslassen, wird der Punkt allmählich kleiner, sodass der Punkt wie ein aufblasbarer Ballon wirkt.

.. image:: img/dot_size.png

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

    *   - :ref:`gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`breadboard`
        - |link_breadboard_buy|
    *   - :ref:`wires`
        - |link_wires_buy|
    *   - :ref:`button`
        - |link_button_buy|

**Verdrahtung**

.. image:: img/button_pressed.png

**Skizze**

.. code-block:: arduino

    import processing.io.*;
    int buttonPin = 18; 

    float diameter;

    void setup() {
        size(200, 200);
        frameRate(64); //set frame rate
        GPIO.pinMode(buttonPin, GPIO.INPUT_PULLUP); 
        diameter = width*0.5;
    }

    void draw() {
        if (GPIO.digitalRead(buttonPin)==GPIO.LOW) {
            if(diameter<width*0.8) {diameter=diameter+5;}
        } else {
            if(diameter>=width*0.2) {diameter--;}
        } 
        background(192, 16, 18);
        ellipse(width/2, height/2,diameter, diameter);
    }

**Wie funktioniert das?**

Dieses Projekt verwendet die Eingabefunktion im Vergleich zu den vorherigen 2 Projekten, die die Ausgabefunktion des GPIO genutzt haben.

Die Funktion ``GPIO.pinMode()`` wird verwendet, um ``buttonPin`` auf den Pull-up-Eingangsmodus einzustellen, was dazu führt, dass der Pin im Standardzustand automatisch hoch geht.

Dann verwenden Sie die Funktion ``GPIO.digitalRead()`` um den Wert von ``buttonPin`` zu lesen. Wenn der Wert LOW ist, bedeutet das, dass der Knopf gedrückt ist, zu diesem Zeitpunkt sollte der Durchmesser des Punktes um 5 erhöhen; wenn der Knopf losgelassen wird, dann wird der Durchmesser des Punktes um 1 verringern.
