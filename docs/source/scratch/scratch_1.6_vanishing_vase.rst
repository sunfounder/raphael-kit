.. _1.6_scratch:

1.6 Vase Disparu
========================

Maintenant, faisons un petit tour de magie : ne rien faire, et le vase disparaît mystérieusement.

.. image:: img/1.6_header.png

Composants Nécessaires
-------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.6_component.png

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
    *   - :ref:`cpn_reed_switch`
        - |link_reed_switch_buy|

Construire le Circuit
------------------------

.. image:: img/1.6_fritzing.png

Charger le Code et Voir ce Qui Se Passe
------------------------------------------

Chargez le fichier de code (``1.6_vanishing_vase.sb3``) dans Scratch 3.

Lorsque vous utilisez un aimant près du module de l'interrupteur à lames, un vase apparaît sur la scène. Enlevez l'aimant et le vase disparaît.

Astuces sur le Sprite
----------------------

Sélectionnez Sprite1 et cliquez sur **Costumes** en haut à gauche ; téléchargez **desk1.png** et **desk2.png** depuis le chemin ``~/raphael-kit/scratch/picture`` via le bouton **Télécharger Costume** ; supprimez les 2 costumes par défaut et renommez le sprite en **desk**.

.. image:: img/1.6_vase.png

Astuces sur les Codes
----------------------

.. image:: img/1.6_reed2.png
  :width: 400

Lorsque l'aimant est proche du module de l'interrupteur à lames, gpio17 est bas, et le costume du sprite **desk** est changé en **desk1** (le vase est toujours sur le bureau).

.. image:: img/1.6_reed3.png
  :width: 400

Après avoir retiré l'aimant, gpio17 est haut, à ce moment-là le costume du sprite **desk** est changé en **desk2** (seulement le bureau).
