.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _metronome:

Metronom
====================

Hier werden wir ein Metronom bauen. Das Metronom ist in 5 Stufen unterteilt; je höher die Stufe, desto dringender der Signalton des Buzzers.

.. image:: img/metronome.png

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten:

Es ist sicherlich praktisch, ein gesamtes Kit zu kaufen. Hier ist der Link dazu:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

Sie können die Teile auch einzeln über die untenstehenden Links kaufen.

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
    *   - :ref:`cpn_Buzzer`
        - |link_passive_buzzer_buy|
    *   - :ref:`cpn_transistor`
        - |link_transistor_buy|

**Verdrahtung**

.. image:: img/image106.png

.. note::

    Hier wird ein aktiver Buzzer verwendet, der einen weißen Aufkleber darauf hat.
    
**Skizze**

.. code-block:: Arduino

    import processing.io.*;

    int level = 0;
    int buzzerPin = 17;
    int levelRange=5;
    Slider mySlider;

    void setup() {
        size(400, 200);
        frameRate(50);
        mySlider = new Slider(width * 0.2,height * 0.4,width * 0.8,height * 0.6,0,levelRange,level);
        GPIO.pinMode(buzzerPin, GPIO.OUTPUT);
    }

    void draw() {

        background(255);
        mySlider.show();
        if(level==0){
            GPIO.digitalWrite(buzzerPin, GPIO.HIGH);
        }else if((frameCount/5) % (levelRange-level+1) ==0){
            GPIO.digitalWrite(buzzerPin, GPIO.LOW);
        }else{
            GPIO.digitalWrite(buzzerPin, GPIO.HIGH);
        }
    }

    void mouseDragged(){
        level = mySlider.dragPoint(mouseX,mouseY);
    }

    class Slider{
        float slotPointAX;
        float slotPointBX;
        float slotPointAY;
        float slotPointBY;
        float linePoint;
        float depth;
        int maxRange;
        int minRange;
        int value;

        Slider(float ax, float ay, float bx, float by, int min, int max, int v){
            slotPointAX = ax;
            slotPointAY = ay;
            slotPointBX = bx;
            slotPointBY = by;
            maxRange = max;
            minRange = min;
            value = v;
            linePoint = slotPointAX;// + map(value, minRange, maxRange, slotPointAX, slotPointBX);
            depth = (slotPointBY - slotPointAY)*0.75;
        }

        void show(){
            rectMode(CORNERS);
            fill(200);
            stroke(255,0,0);
            rect(slotPointAX, slotPointAY, slotPointBX, slotPointBY);
            fill(255,0,0);
            rect(slotPointAX, slotPointAY, linePoint, slotPointBY);
            fill(200);
            textSize(depth);
            text(minRange, slotPointAX, slotPointBY+depth);
            text(maxRange, slotPointBX, slotPointBY+depth);
            text(value, linePoint, slotPointAY);
        }

        int dragPoint(float mx, float my){
            if(mx>=slotPointAX && mx<=slotPointBX && my>=slotPointAY && my<=slotPointBY){
                value = int(map(mx,slotPointAX,slotPointBX,minRange,maxRange));
                linePoint = map(value,minRange,maxRange,slotPointAX,slotPointBX);
            }
            return value;
        }
    }

**Wie funktioniert das?**

.. Wie im vorherigen Projekt haben wir eine ``Slider`` Klasse erstellt und sie als **WIDGET** agieren lassen.

.. Allerdings wurde ``dragPoint()`` leicht modifiziert, sodass das Widget beim Verschieben eine diskontinuierliche Eigenschaft hat und besser zur Pegelanpassung geeignet ist.

.. .. code-block:: Arduino

..     int dragPoint(float mx, float my){
..         if(mx>=slotPointAX && mx<=slotPointBX && my>=slotPointAY && my<=slotPointBY){
..             value = int(map(mx,slotPointAX,slotPointBX,minRange,maxRange));
..             linePoint = map(value,minRange,maxRange,slotPointAX,slotPointBX);
..         }
..         return value;
..     }

Hier haben wir eine ``Slider`` Klasse erstellt und sie als **WIDGET** agieren lassen.

.. code-block:: arduino

    Slider(ax, ay, bx, by, min, max, v)

Bei der Deklaration müssen 7 Parameter übergeben werden.

Die ersten vier Parameter bestimmen die Größe des Widgets, gefolgt von den Koordinaten (x1, y1) des Startpunkts in der oberen linken Ecke und (x2, y2) in der unteren rechten Ecke.

Die letzten drei Parameter bestimmen seinen numerischen Bereich (von min bis max) und den Anfangswert.

Es hat zwei Methoden, die Wirkung von ``dragPoint()`` ist es, den Schieberegler verschiebbar zu machen und den aktuellen Positionswert des Schiebereglers zurückzugeben.

.. code-block:: arduino

    int dragPoint(float mx, float my){
        if(mx>=slotPointAX && mx<=slotPointBX && my>=slotPointAY && my<=slotPointBY){
            value = int(map(mx,slotPointAX,slotPointBX,minRange,maxRange));
            linePoint = map(value,minRange,maxRange,slotPointAX,slotPointBX);
        }
        return value;
    }

Eine weitere Methode ``show()`` dient dazu, den Slider anzuzeigen. Gleichzeitig werden der Bereichswert und der aktuelle Wert an der entsprechenden Stelle angezeigt.

.. code-block:: arduino

    void show(){
        rectMode(CORNERS);
        fill(200);
        stroke(255,0,0);
        rect(slotPointAX, slotPointAY, slotPointBX, slotPointBY);
        fill(255,0,0);
        rect(slotPointAX, slotPointAY, linePoint, slotPointBY);
        fill(200);
        textSize(depth);
        text(minRange, slotPointAX, slotPointBY+depth);
        text(maxRange, slotPointBX, slotPointBY+depth);
        text(value, linePoint, slotPointAY);
    }