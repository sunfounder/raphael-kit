.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _1.16_scratch_pi5:

1.16 Jeu de Pêche
======================

Aujourd'hui, nous allons créer un jeu de pêche.

Observez l'eau dans la zone de scène et si vous trouvez un poisson sur l'hameçon, n'oubliez pas d'incliner l'interrupteur pour l'attraper.

.. image:: img/1.16_header.png

Composants Nécessaires
--------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.16_component.png

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
    *   - :ref:`cpn_tilt_switch`
        - \-

Construire le Circuit
-------------------------

.. image:: img/1.16_fritzing.png

Charger le Code et Voir ce Qui Se Passe
-------------------------------------------

Chargez le fichier de code (``1.16_fishing_game.sb3``) sur Scratch 3.

Vous verrez un enfant en train de pêcher. Après un certain temps, lorsque l'eau bouge, vous pouvez secouer l'interrupteur à bascule pour attraper le poisson. Souvenez-vous, si vous ne continuez pas à secouer l'interrupteur, le poisson s'échappera.

Astuces sur les Sprites
---------------------------

Sélectionnez Sprite1, cliquez sur **Costumes** dans le coin supérieur gauche ; téléchargez 6 images (**fish1** à **fish6**) depuis le chemin ``~/raphael-kit/scratch/picture`` via le bouton **Télécharger Costume** ; supprimez les 2 costumes par défaut et renommez le sprite en **fish**.

.. image:: img/1.16_upload_fish.png

Astuces sur les Codes
--------------------------

.. image:: img/1.16_fish2.png
  :width: 400

Réglez le costume initial du sprite **fish** à **fish1** et attribuez la valeur de **fish_status** à 0 (lorsque **fish_status=0**, cela signifie que le poisson n'est pas accroché, lorsque **fish_status=1**, cela signifie que le poisson est accroché).

.. image:: img/1.16_fish3.png
  :width: 400

Lorsque **fish_status=0**, c'est-à-dire que le poisson n'est pas encore accroché, commencez le jeu de pêche. Attendez un temps aléatoire de 0 à 10 secondes, puis attribuez **fish_status** à 1, ce qui signifie que le poisson est accroché, et diffusez un message "Le poisson mord".

.. note::

  Le but du bloc de diffusion est d'envoyer un message à d'autres blocs de code ou à d'autres sprites. Le message peut être soit une demande, soit une commande.

.. image:: img/1.16_fish4.png
  :width: 400

Lorsque le message "Le poisson mord" est reçu, faites en sorte que le sprite poisson alterne entre les costumes **fish2** et **fish3** pour que nous puissions voir le poisson mordre.

.. image:: img/1.16_fish5.png
  :width: 400

Après avoir changé de costume, si le jeu n'est pas terminé, cela signifie que le poisson s'est décroché et est parti, nous changeons donc le costume du sprite **fish** en **fish6** (état du poisson échappé).

.. image:: img/1.16_fish6.png
  :width: 400

Lorsque gpio17 est haut (l'interrupteur à bascule est incliné), cela signifie que la canne à pêche est tirée vers le haut. À ce moment-là, la valeur de **fish_status** est évaluée. Si elle est à 1, cela signifie que la canne à pêche a été tirée vers le haut lorsque le poisson était accroché, et le costume est changé en **fish4** (poisson attrapé). Sinon, cela signifie que la canne à pêche a été tirée vers le haut sans poisson accroché et le costume est changé en **fish5** (rien n'est attrapé).
