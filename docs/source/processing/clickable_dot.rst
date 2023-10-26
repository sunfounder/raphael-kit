.. _clickable_dot:

Klickbarer Punkt
==================

Wir haben bereits Bewegungsgrafiken gezeichnet, auf Mausereignisse reagiert und LEDs gesteuert. Also könnten wir diese Funktionen kombinieren und einen klickbaren Punkt zeichnen, um die LED zu steuern!

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

    *   - :ref:`gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`breadboard`
        - |link_breadboard_buy|
    *   - :ref:`wires`
        - |link_wires_buy|
    *   - :ref:`led`
        - |link_led_buy|

**Verdrahtung**

.. image:: img/image49.png

**Skizze**

.. code-block:: arduino

    import processing.io.*; 
    boolean state = false;
    int ledPin = 17;

    void setup() {
        GPIO.pinMode(ledPin, GPIO.OUTPUT);
        background(255);
    }

    void draw() {
        if (state == true) { 
            GPIO.digitalWrite(ledPin, GPIO.LOW);
            fill(255, 0, 0);
        }else { 
            GPIO.digitalWrite(ledPin, GPIO.HIGH);
            fill(155);
        }
        ellipse(width/2, height/2, width*0.75, height*0.75);
    }

    void mouseClicked() {
        //  toggles state:
        if (2*dist(mouseX,mouseY,width/2, height/2)<=width*0.75)
            {state = !state;}
    }

**Wie funktioniert das?**

Dieses Projekt hat viele Gemeinsamkeiten mit :ref:`blinking_dot`. Der Unterschied besteht darin, dass der Umschaltzustand im Mausevent platziert ist. Dies führt dazu, dass die LED nicht automatisch blinkt, sondern mit einem Mausklick ein- und ausgeschaltet wird.

Im ``mouseClicked()``-Ereignis wird die ``dist()``-Funktion verwendet, um die Position der Maus zum Zeitpunkt des Klicks zu bestimmen. Der Punkt wird nur dann als angeklickt betrachtet, wenn der Abstand zwischen der Maus und dem Zentrum des Punktes kleiner als der Radius ist.
