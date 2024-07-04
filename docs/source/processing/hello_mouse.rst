 
.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

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
