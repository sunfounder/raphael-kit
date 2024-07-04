.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _1.2_scratch:

1.2 Boules Colorées
======================

Cliquer sur les boules de différentes couleurs dans la zone de scène fera s'allumer la LED RGB en différentes couleurs.

.. image:: img/1.2_header.png

Composants Nécessaires
--------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.2_list.png

Il est certainement pratique d'acheter un kit complet, voici le lien :

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom
        - ARTICLES DANS CE KIT
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
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_rgb_led`
        - |link_rgb_led_buy|

Construire le Circuit
------------------------

.. image:: img/1.2_image61.png

Charger le Code et Voir ce Qui Se Passe
-----------------------------------------

Après avoir chargé le fichier de code (``1.2_colorful_balls.sb3``) dans Scratch 3, la LED RGB s'allumera en jaune, bleu, rouge, vert ou violet lorsque vous cliquerez sur la boule correspondante.

Astuces sur les Sprites
--------------------------

Supprimez le sprite par défaut, puis choisissez le sprite **Boule**.

.. image:: img/1.2_ball.png

Et dupliquez-le 5 fois.

.. image:: img/1.2_duplicate_ball.png

Choisissez différents costumes pour ces 5 sprites **Boule** et déplacez-les aux positions correspondantes.

.. image:: img/1.2_rgb1.png

Astuces sur les Codes
--------------------------

Avant de comprendre le code, nous devons comprendre le `modèle de couleur RGB <https://fr.wikipedia.org/wiki/RVB_(couleur)>`_.

Le modèle de couleur RGB est un modèle de couleur additive dans lequel les lumières rouge, verte et bleue sont ajoutées de différentes manières pour reproduire une large gamme de couleurs.

Mélange de couleurs additives : ajouter du rouge au vert donne du jaune ; ajouter du vert au bleu donne du cyan ; ajouter du bleu au rouge donne du magenta ; ajouter les trois couleurs primaires ensemble donne du blanc.

.. image:: img/1.2_rgb_addition.png
  :width: 400

Une LED RGB est une combinaison de 3 LEDs (LED rouge, LED verte, LED bleue) dans un seul boîtier, vous pouvez produire presque n'importe quelle couleur en combinant ces trois couleurs.
Elle a 4 broches, dont une est la masse (GND), et les 3 autres broches contrôlent respectivement les 3 LEDs.

Ainsi, le code pour faire s'allumer la LED RGB en jaune est le suivant.

.. image:: img/1.2_rgb3.png

Lorsque le sprite Boule (boule jaune) est cliqué, nous définissons gpio17 haut (LED rouge allumée), gpio18 haut (LED verte allumée) et gpio27 bas (LED bleue éteinte) de sorte que la LED RGB s'allume en jaune.

Vous pouvez écrire des codes pour d'autres sprites de la même manière pour faire s'allumer les LEDs RGB dans les couleurs correspondantes.
