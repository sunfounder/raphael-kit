.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _1.10_scratch_pi5:

1.10 Jouer du Tambour dans l'Air
===================================

Aujourd'hui, nous allons apprendre à utiliser la caméra Raspberry Pi. Scratch dispose d'un module d'extension pour la détection vidéo qui active la caméra dans Scratch et détecte le mouvement des objets sur la scène.

.. image:: img/1.10_header.png

Composants Nécessaires
--------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.10_list.png

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
    *   - :ref:`cpn_audio_speaker`
        - \-
    *   - :ref:`cpn_camera_module`
        - |link_camera_buy|

Construire le Circuit
------------------------

.. image:: img/1.10_fritzing_speaker.png

.. image:: img/1.10_camera.png

.. note::

    Vous devez vous référer à :ref:`cpn_camera_module` pour connecter le module caméra et activer l'interface caméra du Raspberry Pi.

Charger le Code et Voir ce Qui Se Passe
------------------------------------------

Chargez le fichier de code (``1.10_drumming_in_the_air.sb3``) dans Scratch 3.

Cliquez sur le drapeau vert pour commencer le jeu, placez votre main devant le module caméra et Scratch 3 émettra des sons d'instruments lorsque votre main touchera un instrument sur la scène.

.. note::

    Pour une meilleure expérience de jeu, essayez de jouer sur un fond blanc pour éviter les interférences de la caméra avec d'autres objets.

Astuces sur le Sprite
-------------------------

Supprimez d'abord les sprites par défaut, puis trouvez le sprite **Drum-cymbal** et le sprite **Drum-snare** et ajoutez-les.

.. image:: img/1.10_camera1.png

Cliquez sur l'icône **Ajouter une extension** en bas à gauche de Scratch et ajoutez les extensions **Musique** et **Détection Vidéo**.

.. image:: img/1.10_scratch.png

.. image:: img/1.10_scratch2.png

Astuces sur les Codes
----------------------

.. image:: img/1.10_camera3.png

Lorsque le drapeau vert est cliqué, il continue à détecter si notre main se déplace sur le sprite **Drum-cymbal** de plus de 60. Si c'est le cas, on suppose que notre main a touché le sprite, à ce moment-là le son de l'instrument Open Hi-Hat est joué.

.. note::

    L'amplitude du mouvement fait référence au changement de coordonnées sur la zone de scène, qui est calculé par rapport au changement des coordonnées de la cible de détection sur la zone de scène.

.. image:: img/1.10_camera4.png

De même, si le mouvement de notre main sur le sprite **Drum-snare** est détecté à plus de 60, notre main est considérée comme ayant touché le sprite et le son de l'instrument caisse claire est joué.
