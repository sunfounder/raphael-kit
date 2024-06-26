 
.. _carrés_clicables:

Carrés de Couleur Clicables
======================================

Nous avons déjà essayé de dessiner un point cliquable pour contrôler la LED, allons donc plus loin et dessinons 3 carrés colorés pour ajuster les couleurs RGB !

.. image:: img/colorful_square.png

**Composants nécessaires**

Pour ce projet, nous avons besoin des composants suivants.

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

Vous pouvez également les acheter séparément à partir des liens ci-dessous.

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
    *   - :ref:`cpn_rgb_led`
        - |link_rgb_led_buy|
**Câblage**

.. image:: img/image61.png

**Esquisse**

.. code-block:: arduino

    import processing.io.*; // utiliser la bibliothèque GPIO

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


**Comment ça fonctionne ?**

Ce projet a beaucoup en commun avec :ref:`clickable_dot`, sauf qu'il affine les conditions pour déterminer l'événement de clic de souris.

Dessinez d'abord trois blocs de couleur dans ``draw()``, puis identifiez quel bloc de couleur a été cliqué en fonction de la valeur de mouseX (la coordonnée X de la souris), et enfin, allumez la couleur correspondante avec la LED RGB.

**Quoi de plus ?**

En combinant les lumières, nous pouvons faire afficher à la LED RGB sept couleurs - ajouter du rouge au vert produit du jaune ; ajouter les trois couleurs primaires ensemble produit du blanc.
Maintenant, essayez-le vous-même.
