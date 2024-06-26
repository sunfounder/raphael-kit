.. _dot_cliquable:

Point Cliquable
======================

Nous avons essayé de dessiner des graphiques animés, de répondre à des événements de souris et de contrôler une LED. Nous pourrions donc combiner ces fonctions, dessiner un point cliquable pour contrôler la LED !  

.. image:: img/clickable_dot_on.png

**Composants Nécessaires**

Dans ce projet, nous avons besoin des composants suivants.

Il est définitivement pratique d'acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ARTICLES DANS CE KIT
        - LIEN
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

Vous pouvez également les acheter séparément à partir des liens ci-dessous.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUCTION DU COMPOSANT
        - LIEN D'ACHAT

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_led`
        - |link_led_buy|

**Câblage**

.. image:: img/image49.png

**Esquisse**

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

**Comment ça fonctionne ?**

Ce projet a beaucoup en commun avec :ref:`blinking_dot`, la différence est qu'il met l'état de bascule dans l'événement de la souris.
Cela fait que la LED ne clignote pas automatiquement, mais s'allume et s'éteint avec un clic de souris.

Et dans l'événement ``mouseClicked()``, la fonction ``dist()`` est utilisée pour déterminer la position de la souris au moment du clic, et le point est considéré comme cliqué uniquement si la distance entre la souris et le centre du point est inférieure au rayon.
