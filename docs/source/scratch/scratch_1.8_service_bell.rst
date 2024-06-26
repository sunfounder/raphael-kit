.. _1.8_scratch:

1.8 Service Bell
=====================

Aujourd'hui, nous allons utiliser un micro-interrupteur, des haut-parleurs, un module amplificateur audio, un Raspberry Pi et Scratch pour fabriquer une sonnette de service.

Appuyez sur le micro-interrupteur pour faire sonner la sonnette de service.

.. image:: img/1.8_header.png

Composants Nécessaires
--------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.8_component.png

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
    *   - :ref:`cpn_micro_switch`
        - \-
    *   - :ref:`cpn_capacitor`
        - |link_capacitor_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-

Construire le Circuit
------------------------

.. image:: img/1.8_fritzing.png

Charger le Code et Voir ce Qui Se Passe
-------------------------------------------

Chargez le fichier de code (``1.8_service_bell.sb3``) dans Scratch 3.

Appuyez sur le micro-interrupteur et la sonnette de service sonnera une fois.

.. note::

  Si votre Raspberry Pi est connecté à un écran avec des haut-parleurs, cela peut empêcher le son de sortir de ce haut-parleur externe, veuillez vous référer à :ref:`change_audio_output` pour la solution.

  De plus, si vous souhaitez ajuster le niveau du volume, veuillez vous référer à :ref:`adjust_volume`.

Astuces sur le Sprite
------------------------

Sélectionnez Sprite1 et cliquez sur **Costumes** en haut à gauche ; téléchargez **bell1.png** et **bell2.png** depuis le chemin ``~/raphael-kit/scratch/picture`` via le bouton **Télécharger Costume** ; supprimez les 2 costumes par défaut, et renommez le sprite en **bell**.

.. image:: img/1.8_travel1.png

Dans l'option **Sons**, téléchargez le fichier ``bell.wav`` depuis le chemin ``~/raphael-kit/scratch/sound`` vers Scratch 3.

.. image:: img/1.8_travel2.png

Astuces sur les Codes
-------------------------

.. image:: img/1.8_travel3.png
  :width: 400

Lorsque pin17 est haut (le micro-interrupteur n'est pas pressé), changez le costume du sprite **bell** en **bell1** (état relâché).

.. image:: img/1.8_travel4.png
  :width: 400

Appuyez sur le micro-interrupteur, gpio17 est à niveau bas. À ce moment-là, changez le costume du sprite **bell** en **bell2** (état pressé) et jouez un effet sonore via le haut-parleur.
