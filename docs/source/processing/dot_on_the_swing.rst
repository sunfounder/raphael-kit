.. _point_sur_la_balançoire:

Point sur la Balançoire
================================

Dans ce projet, 3 boutons sont connectés : un pour changer la taille du point, un pour changer la position et le dernier pour changer la couleur. Si vous appuyez sur les 3 boutons en même temps, vous obtiendrez un point qui se balance et change de couleur.

.. image:: img/dancing_dot.png

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
    *   - :ref:`cpn_button`
        - |link_button_buy|

**Câblage**

.. image:: img/circuit_dancing_dot.png
**Croquis**

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
**Comment ça marche ?**

Au lieu de dessiner directement un point, nous créons ici une classe ``Dot``.
Ensuite, nous déclarons l'objet (dans ce cas, ``myDot``).

C'est une manière simple de dessiner des points avec plusieurs propriétés identiques. 
Par exemple, si nous ajoutons trois fonctions au point dans ce projet - changer la taille, 
changer la position et changer la couleur - alors chaque point que nous déclarons aura les 
mêmes fonctions. Nous pouvons utiliser le même bouton pour leur faire faire la même chose, 
ou nous pouvons utiliser différents boutons pour contrôler chaque point séparément.

Utiliser des **classes** rend votre croquis plus élégant, puissant et flexible.

`Class (programmation informatique) - Wikipédia <https://fr.wikipedia.org/wiki/Classe_(informatique)>`_

Ensuite, examinons de plus près la classe ``Dot``. 

.. code-block:: arduino

    Dot(float x, float y, float s, int c)

Dans la déclaration, elle doit recevoir quatre paramètres : les valeurs de coordonnées X et Y de la position, la taille, et la couleur (ici définie en `mode de couleur HSB <https://fr.wikipedia.org/wiki/Teinte_Saturation_Valeur>`_ ).

Chaque paramètre sera assigné à deux ensembles de valeurs (valeur initiale et valeur actuelle).

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

En plus de la valeur initiale et de la valeur actuelle, il y a aussi un ensemble de valeurs de plage. Il n'est pas difficile de comprendre que la valeur initiale est utilisée pour déterminer l'état initial du point (déterminé par les paramètres d'entrée), tandis que la valeur actuelle changera dans la plage pour faire bouger le point.

Par conséquent, à l'exception de la valeur de la coordonnée X, les valeurs actuelles des trois autres paramètres sont calculées comme suit :

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

Si vous êtes familier avec les fonctions trigonométriques, il ne devrait pas être difficile de 
comprendre `sinus et cosinus <https://fr.wikipedia.org/wiki/Sinus>`_, qui donnent un changement 
périodique lisse (de -1 à 1) de la valeur actuelle du point.

Nous devons également ajouter une variable, ``timer``, pour la variation périodique. Elle ajoute 
la valeur fixe dans la méthode ``update()`` et est appelée dans ``draw()``.

.. code-block:: arduino

    void update() {
        timer += speed;
    }

Enfin, le point est affiché en fonction de la valeur actuelle en utilisant la méthode ``show()``, qui est également appelée dans ``draw()``.

.. code-block:: arduino

    void show() {
        fill(currentColor, 100, 100); 
        ellipse(currentX, currentY, currentSize, currentSize);
    }

**Que faire de plus ?**

Ayant maîtrisé l'utilisation des classes, vous pouvez déjà dessiner plusieurs points avec les mêmes propriétés, alors pourquoi ne pas essayer de faire quelque chose de plus cool ?
Par exemple, que diriez-vous de dessiner un système binaire stable, ou de créer un jeu 'DUET' ?
