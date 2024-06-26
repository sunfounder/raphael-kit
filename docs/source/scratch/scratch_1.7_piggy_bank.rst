.. _1.7_scratch:

1.7 Tirelire
=========================

Dans ce projet, nous allons utiliser un module de capteur de vitesse, un Raspberry Pi et Scratch pour fabriquer une tirelire.

Placez une feuille de papier au milieu du module de capteur de vitesse et vous verrez une pièce tomber dans la tirelire sur la scène.

.. image:: img/1.7_header.png

Composants Nécessaires
--------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.7_component.png

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
    *   - :ref:`cpn_speed_sensor`
        - \-

Construire le Circuit
------------------------

.. image:: img/1.7_fritzing.png

Charger le Code et Voir ce Qui Se Passe
------------------------------------------

Chargez le fichier de code (``1.7_piggy_bank.sb3``) dans Scratch 3.

Les deux bornes au milieu du capteur de vitesse, l'une émet de la lumière, l'autre reçoit de la lumière ; si vous mettez une feuille de papier au milieu pour isoler la transmission de la lumière, le capteur de vitesse émettra un niveau haut. À ce moment, Scratch reçoit le niveau haut, puis change les costumes du sprite et vous verrez une pièce tomber dans la tirelire sur la scène.

Astuces sur le Sprite
------------------------

Sélectionnez Sprite1 et cliquez sur **Costumes** en haut à gauche ; téléchargez **piggybank1.png**, **piggybank2.png** et **piggybank3.png** depuis le chemin ``~/raphael-kit/scratch/picture`` via le bouton **Télécharger Costume** ; supprimez les 2 costumes par défaut, et renommez le sprite en **piggybank**.

.. image:: img/1.7_photoInterrupter1.png

Astuces sur les Codes
------------------------

.. image:: img/1.7_code2.png

Lorsque pin17 est bas (aucune pièce n'est introduite), changez le costume du sprite en **piggybank1**.

.. image:: img/1.7_code3.png

Lorsque pin17 est haut (une pièce est introduite), changez le costume du sprite en **piggybank2**, puis après 0,5s en **piggybank3**, de sorte que nous puissions voir une pièce tomber dans la tirelire sur la scène.
