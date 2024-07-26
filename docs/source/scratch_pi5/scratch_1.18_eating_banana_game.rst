.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _1.18_scratch_pi5:

1.18 Jeu de la Banane
========================

Description
--------------

Scratch dispose d'un module d'extension de détection vidéo, qui peut activer la caméra dans Scratch et détecter les mouvements des objets à l'écran.

Aujourd'hui, nous allons utiliser la caméra pour créer un jeu de bananes. Dans le temps imparti, aidez le Singe à manger plus de bananes.

Pour jouer, placez-vous devant un fond blanc et cliquez sur le drapeau vert pour commencer. Déplacez des objets colorés devant la caméra pour contrôler le sprite du Singe.

.. image:: img/1.18_header.png

Composants Nécessaires
---------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.18_photo1.png

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

    *   - :ref:`cpn_camera_module`
        - |link_camera_buy|

Construire le Circuit
-------------------------

.. image:: img/1.10_camera.png

.. note::

    Vous devez vous référer à :ref:`cpn_camera_module` pour connecter le module caméra et activer l'interface caméra du Raspberry Pi.

Charger le Code et Voir ce Qui Se Passe
-------------------------------------------

Chargez le fichier de code (``1.18_eating_banana_game.sb3``) sur Scratch 3.

Astuces sur les Codes
-------------------------

Disposer les singes et les bananes

Tout d'abord, nous supprimons le sprite d'origine, puis ajoutons le sprite Singe et le sprite Bananes, et modifions leurs tailles à 50.

Faire apparaître les Bananes de manière aléatoire.

.. image:: img/1.18_code1.png

Les Bananes disparaissent après avoir rencontré le Singe, ce qui signifie qu'elles ont été mangées par le Singe et réapparaissent de manière aléatoire.

.. image:: img/1.18_code2.png

Faire apparaître le Singe au centre de la scène et initialiser les données de la caméra (la transparence est réglée à 20).

.. image:: img/1.18_code3.png

Si la caméra détecte un objet en mouvement, déplacer le Singe vers l'objet.

.. image:: img/1.18_code4.png

Maintenant, cliquez sur le drapeau vert en haut de la scène pour commencer le jeu.

Laissez le Singe manger des bananes, il a très faim ! Essayez de jouer à ce jeu sur un fond blanc pour éviter les interférences avec d'autres objets.

Défi
----------

Je suis sûr que vous serez assez intelligent pour programmer et réaliser ce jeu rapidement. Ensuite, nous ajouterons quelques défis pour enrichir le contenu de notre jeu.

· Lorsque le Singe mange une banane, ajoutez 1 au score. Dans les 30 secondes, voyez qui obtient le score le plus élevé !

· Lorsque le Singe mange une banane, il émet un effet sonore approprié.
