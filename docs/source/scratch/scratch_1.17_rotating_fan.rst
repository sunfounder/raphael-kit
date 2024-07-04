.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _1.17_scratch:

1.17 Ventilateur Rotatif
=============================

Dans ce projet, nous allons créer un sprite d'étoile tournant et un ventilateur.

.. image:: img/1.17_header.png

Composants Nécessaires
---------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.17_list.png

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
    *   - :ref:`cpn_power_module`
        - \-
    *   - :ref:`cpn_l293d`
        - \-
    *   - :ref:`cpn_motor`
        - |link_motor_buy|

Construire le Circuit
-------------------------

.. image:: img/1.17_image117.png

Charger le Code et Voir ce Qui Se Passe
-------------------------------------------

Chargez le fichier de code (``1.17_rotating_fan.sb3``) sur Scratch 3.

Après avoir cliqué sur le drapeau vert dans la scène, cliquez sur le sprite étoile, puis l'étoile et le moteur tourneront dans le sens des aiguilles d'une montre ; vous pouvez changer le sens de rotation en cliquant sur les deux sprites **flèche**. Lorsque vous cliquez à nouveau sur le sprite **étoile**, celui-ci et le moteur arrêteront de tourner.


Astuces sur les Sprites
-----------------------------

Supprimez le sprite par défaut, puis sélectionnez le sprite **Étoile** et le sprite **Flèche1**, et copiez Flèche1 une fois.

.. image:: img/1.17_motor1.png

Dans l'option **Costumes**, changez le sprite Flèche2 en un costume de direction différente.

.. image:: img/1.17_motor2.png

Ajustez la taille et la position du sprite de manière appropriée.

.. image:: img/1.17_motor3.png


Astuces sur les Codes
--------------------------

**Diagramme de Flux**

.. image:: img/1.17_scratch.png

Dans ce code, vous verrez 2 blocs roses, tourner à gauche et tourner à droite, qui sont nos blocs personnalisés (fonctions).

.. image:: img/1.17_new_block.png

**Comment Créer un Bloc ?**

Apprenons à créer un bloc (fonction). Le bloc (fonction) peut être utilisé pour simplifier votre programme, en particulier si vous effectuez la même opération plusieurs fois. Mettre ces opérations dans un nouveau bloc déclaré peut être très pratique pour vous.

Tout d'abord, trouvez **Mes Blocs** dans la palette de blocs, puis sélectionnez **Créer un Bloc**.

.. image:: img/1.17_motor4.png

Entrez le nom du nouveau bloc.

.. image:: img/1.17_motor5.png

Après avoir écrit la fonction du nouveau bloc dans la zone de codage, enregistrez-la, puis vous pourrez trouver le bloc dans la palette de blocs.

.. image:: img/1.17_motor6.png

**tourner à gauche**

Voici le code à l'intérieur du bloc tourner à gauche pour faire tourner le moteur dans le sens inverse des aiguilles d'une montre.

.. image:: img/1.17_motor12.png
  :width: 400

**tourner à droite**

Voici le code à l'intérieur du bloc tourner à droite pour faire tourner le moteur dans le sens des aiguilles d'une montre.

.. image:: img/1.17_motor11.png
  :width: 400



