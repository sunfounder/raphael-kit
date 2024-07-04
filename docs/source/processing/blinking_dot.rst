 
.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _point_clignotant:

Point Clignotant
===========================

Dans ce projet, nous allons dessiner un point dans Processing, qui clignote en synchronisation avec la LED. Veuillez construire le circuit comme indiqué sur le schéma et exécuter le sketch.

.. image:: img/blinking_dot.png
.. image:: img/clickable_dot_on.png

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
    *   - :ref:`cpn_led`
        - |link_led_buy|

**Câblage**

.. image:: img/image49.png

**Sketch**

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

**Comment ça marche ?**

Au début du sketch, vous devez intégrer la bibliothèque de fonctions GPIO de Processing avec ``import processing.io.*;``, indispensable pour les expériences de circuit.

La **fréquence d'images** est la fréquence à laquelle les bitmaps apparaissent sur la carte, exprimée en hertz (Hz). En d'autres termes, c'est aussi la fréquence à laquelle la fonction ``draw()`` est appelée. Dans ``setup()``, définir la **fréquence d'images** à 2 appellera ``draw()`` toutes les 0,5s.

Chaque appel de la fonction ``draw()`` inverse la valeur de ``state`` et la détermine ensuite. Si la valeur est ``true``, la LED s'allume et le pinceau se remplit de rouge ; sinon, la LED s'éteint et le pinceau se remplit de gris.

Après avoir terminé le jugement, utilisez la fonction ``ellipse()`` pour dessiner un cercle. Il convient de noter que ``width`` et ``height`` sont des variables système utilisées pour stocker la largeur et la hauteur de la fenêtre d'affichage.

Il y a deux autres points à noter. Lors de l'utilisation des GPIO, vous devez utiliser la fonction ``GPIO.pinMode()`` pour définir l'état INPUT/OUTPUT de la broche, puis utiliser la fonction ``GPIO.digitalWrite()`` pour attribuer une valeur (HIGH/LOW) à la broche.

.. note::

    Veuillez essayer d'éviter d'utiliser ``delay()`` dans ``draw()`` car cela affectera le rafraîchissement de la fenêtre d'affichage.
