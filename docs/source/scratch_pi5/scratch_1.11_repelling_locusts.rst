.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _1.11_scratch_pi5:

1.11 Repousser les criquets
===============================

Aujourd'hui, nous allons utiliser un module de détection d'obstacles infrarouge, un Raspberry Pi et Scratch pour créer un jeu de répulsion des criquets.

Placez votre main devant le module de détection d'obstacles et vous verrez les criquets être chassés.

.. image:: img/1.11_header.png

Composants Nécessaires
--------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.11_component.png

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
    *   - :ref:`cpn_avoid_module`
        - |link_obstacle_avoidance_buy|

Construire le Circuit
------------------------

.. image:: img/1.11_fritzing.png
    :width: 700
    :align: center

Charger le Code et Voir ce Qui Se Passe
------------------------------------------

Chargez le fichier de code (``1.11_repelling_locusts.sb3``) dans Scratch 3.

Placez votre main devant le module de détection d'obstacles et vous verrez les criquets être chassés.


Astuces sur le Sprite
-----------------------

Sélectionnez Sprite1 et cliquez sur **Costumes** en haut à gauche; téléchargez **locust1.png**, **locust2.png** et **locust3.png** depuis le chemin ``~/raphael-kit/scratch/picture`` via le bouton **Upload Costume**; supprimez les 2 costumes par défaut et renommez le sprite en **locust**.

.. image:: img/1.11_ir1.png

Astuces sur les Codes
-------------------------

.. image:: img/1.11_ir2.png
  :width: 400

Lorsque le module de détection d'obstacles infrarouge ne détecte aucun obstacle (aucune main devant la sonde), le gpio est haut.

.. image:: img/1.11_ir3.png
  :width: 400

Lorsque gpio17 est haut (aucun obstacle devant le module de détection d'obstacles IR), changez le costume du sprite locust en locust1 (les criquets se rassemblent dans le blé). À l'inverse, lorsque gpio17 est bas (placez votre main devant le module de détection d'obstacles IR), changez le costume du sprite locust en locust2 (expulsion des criquets), puis changez le costume du sprite locust en locust3 (les criquets sont complètement expulsés) après 0,5 s.
