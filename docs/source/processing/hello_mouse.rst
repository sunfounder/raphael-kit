 
.. _hello_mouse:

Bonjour Souris
====================

Dans ce projet, votre souris continuera de tirer des lignes vers un point ; déplacez la souris et vous dessinerez une ligne unique d'étoiles. Appuyez sur la souris pour redémarrer le dessin.

.. image:: img/hello_mouse1.png

**Croquis**

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

    void mousePressed() {
        pointX=mouseX;
        pointY=mouseY;
        background(192, 16, 18);
    }

**Comment ça fonctionne ?**

Le projet précédent dessinait une seule image sans aucune animation ni interaction.

Si nous voulons créer un croquis interactif, nous devons ajouter les fonctions ``setup()`` et ``draw()`` (ce sont des fonctions intégrées qui sont appelées automatiquement) pour construire le cadre.

* ``setup()`` : Exécuté une seule fois au démarrage du croquis.
* ``draw()`` : Exécuté de manière répétée, où nous ajoutons généralement le croquis pour dessiner l'animation.

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

Ce croquis ci-dessus fonctionne déjà sans problème en tant que croquis interactif.

Ensuite, vous pouvez ajouter un événement de clic de souris. Cet événement peut être implémenté avec la fonction ``mousePressed()``, où nous ajoutons des instructions pour actualiser le point cible et effacer l'écran.

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

    void mousePressed() {
        pointX=mouseX;
        pointY=mouseY;
        background(192, 16, 18);
    }

Pour plus d'informations, veuillez vous référer à `Processing Reference <https://processing.org/reference/>`_.
