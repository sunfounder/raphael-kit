.. _metronome:

Métronome
=======================

Nous allons ici fabriquer un métronome. Le métronome est divisé en 5 niveaux : plus le niveau est élevé, plus l'appel du buzzer est urgent.

.. image:: img/metronome.png

**Composants nécessaires**

Dans ce projet, nous avons besoin des composants suivants.

Il est certainement pratique d'acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ÉLÉMENTS DANS CE KIT
        - LIEN
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUCTION DES COMPOSANTS
        - LIEN D'ACHAT

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_buzzer`
        - |link_passive_buzzer_buy|
    *   - :ref:`cpn_transistor`
        - |link_transistor_buy|

**Câblage**

.. image:: img/image106.png

.. note::

    Un buzzer actif est utilisé ici, et il a un autocollant blanc dessus.
    
**Croquis**

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

**Comment ça marche ?**

.. Comme dans le projet précédent, nous avons créé une classe ``Slider`` et l'avons utilisée comme **WIDGET**.

.. Cependant, ``dragPoint()`` a été légèrement modifié pour que le widget ait une fonctionnalité discontinue lors du glissement et soit plus adapté au réglage des niveaux.

.. .. code-block:: Arduino

..     int dragPoint(float mx, float my){
..         if(mx >= slotPointAX && mx <= slotPointBX && my >= slotPointAY && my <= slotPointBY){
..             value = int(map(mx, slotPointAX, slotPointBX, minRange, maxRange));
..             linePoint = map(value, minRange, maxRange, slotPointAX, slotPointBX);
..         }
..         return value;
..     }

Ici, nous avons créé une classe ``Slider`` et l'avons utilisée comme **WIDGET**.

.. code-block:: arduino

    Slider(ax, ay, bx, by, min, max, v)

Lors de la déclaration, elle nécessite de passer 7 paramètres.

Les quatre premiers paramètres déterminent la taille du widget, suivis par les coordonnées (x1, y1) du point de départ en haut à gauche et (x2, y2) en bas à droite.

Les trois derniers paramètres déterminent sa plage de valeurs (de min à max) et la valeur initiale.

Elle possède deux méthodes, l'effet de ``dragPoint()`` est de rendre le curseur glissable et de retourner la valeur de position actuelle du curseur.

.. code-block:: arduino

    int dragPoint(float mx, float my){
        if(mx>=slotPointAX && mx<=slotPointBX && my>=slotPointAY && my<=slotPointBY){
            value = int(map(mx,slotPointAX,slotPointBX,minRange,maxRange));
            linePoint = map(value,minRange,maxRange,slotPointAX,slotPointBX);
        }
        return value;
    }

Une autre méthode, ``show()``, est utilisée pour afficher le curseur. En même temps, la valeur de la plage et la valeur actuelle sont affichées à la position correspondante.

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