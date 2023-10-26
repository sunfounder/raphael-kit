.. _clickable_color_blocks:

Klickbare Farbblöcke
=======================

Wir haben bereits versucht, einen klickbaren Punkt zu zeichnen, um die LED zu steuern. Gehen wir einen Schritt weiter und zeichnen 3 farbige Quadrate, um die RGB-Farben anzupassen!

.. image:: img/colorful_square.png

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

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

    *   - KOMPONENTENBESCHREIBUNG
        - KAUF-LINK

    *   - :ref:`gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`breadboard`
        - |link_breadboard_buy|
    *   - :ref:`wires`
        - |link_wires_buy|
    *   - :ref:`rgb_led`
        - |link_rgb_led_buy|

**Verdrahtung**

.. image:: img/image61.png

**Skizze**

.. code-block:: arduino

    import processing.io.*; // use the GPIO library

    int[] pins = { 17, 18, 27 };

    void setup() {
        for (int i = 0; i < pins.length; i++) {
            GPIO.pinMode(pins[i], GPIO.OUTPUT);
        }
        size(300, 100);
        background(255);
    }

    void draw() {
        fill(255, 0, 0);
        rect(0, 0, width/3, height);

        fill(0,255,0);
        rect(width/3, 0, 2*width/3, height);

        fill(0,0,255);
        rect(2*width/3, 0, width, height);
    }

    void mouseClicked() {
        for (int i = 0; i < pins.length; i++) {
            GPIO.digitalWrite(pins[i],GPIO.LOW);
        }
        if (mouseX<width/3){
            GPIO.digitalWrite(pins[0],GPIO.HIGH);
        }else if (mouseX>width/3&&mouseX<2*width/3){
            GPIO.digitalWrite(pins[1],GPIO.HIGH);
        }else if (mouseX>2*width/3){
            GPIO.digitalWrite(pins[2],GPIO.HIGH);
        }        
    }

**Wie funktioniert das?**

Dieses Projekt hat viele Gemeinsamkeiten mit :ref:`clickable_dot`, außer dass es die Bedingungen zur Bestimmung des Mausklick-Ereignisses verfeinert.

Zuerst werden in ``draw()`` drei Farbblöcke gezeichnet, dann wird basierend auf dem Wert von mouseX (der X-Koordinate der Maus) ermittelt, welcher Farbblock angeklickt wurde, und schließlich leuchtet RGB in der entsprechenden Farbe auf.

**Was noch?**

Basierend auf der Lichtzusatz können wir die RGB-LED sieben Farben anzeigen lassen - Rot zu Grün ergibt Gelb; alle drei Grundfarben zusammen ergeben Weiß.
Jetzt können Sie es selbst ausprobieren.
