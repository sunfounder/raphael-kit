.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _1.9_scratch:

1.9 Jouer du Tambour
=======================

Dans ce projet, nous jouons du tambour avec un module interrupteur tactile.

.. image:: img/1.9_header.png

Composants Nécessaires
--------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.9_component.png

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
    *   - :ref:`cpn_touch_switch`
        - |link_touch_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-

Construire le Circuit
---------------------

.. image:: img/1.9_fritzing.png

Charger le Code et Voir ce Qui Se Passe
-------------------------------------------

Chargez le fichier de code (``1.9_drumming.sb3``) dans Scratch 3.

Lorsque vous appuyez sur le module interrupteur tactile, vous entendrez le son des tambours venant du haut-parleur.

Astuces sur le Sprite
------------------------

Supprimez le sprite par défaut, puis trouvez le sprite **Drum-snare** et ajoutez-le, changez sa taille à 200.

.. image:: img/1.9_touch1.png

Scratch possède une extension **Musique** pour jouer des instruments et des tambours, ajoutez-la maintenant via le bouton **Ajouter une extension**.

.. image:: img/1.9_touch2.png

Astuces sur les Codes
--------------------------

.. image:: img/1.9_touch3.png
  :width: 400

Lorsque pin17 est bas (non appuyé sur le module interrupteur tactile), changez le costume du sprite **Drum-snare** en **drum-snare-a**.

.. image:: img/1.9_touch4.png
  :width: 600

Lorsque vous appuyez sur le module interrupteur tactile, gpio17 est bas. À ce moment-là, le costume du sprite **Drum-snare** est changé en **drum-snare-b** et le son du tambour est joué par le haut-parleur.
