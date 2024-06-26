.. _1.3_scratch:

1.3 Culbuto
==================

Dans ce projet, nous allons créer un jouet culbuto contrôlé par un interrupteur à bascule.

.. image:: img/1.3_header.png

Composants Nécessaires
--------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.3_component.png

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
------------------------

.. image:: img/1.3_fritzing.png

Charger le Code et Voir ce Qui Se Passe
------------------------------------------

Chargez le fichier de code (``1.3_tumbler.sb3``) dans Scratch 3.

Lorsque l'interrupteur à bascule est en position verticale, le culbuto est debout. Si vous le penchez, le culbuto tombera également. Remettez-le à la verticale, et le culbuto se relèvera.

Astuces sur le Sprite
------------------------
Sélectionnez Sprite1 et cliquez sur **Costumes** dans le coin supérieur gauche ; téléchargez **tumbler1.png** et **tumbler2.png** depuis le chemin ``~/raphael-kit/scratch/picture`` via le bouton **Télécharger un Costume** ; supprimez les 2 costumes par défaut et renommez le sprite en **culbuto**.

.. image:: img/1.3_add_tumbler.png

Astuces sur les Codes
-------------------------

.. image:: img/1.3_title2.png
  :width: 400

Lorsque le drapeau vert est cliqué, l'état initial de gpio17 est réglé sur bas.

.. image:: img/1.3_title4.png
  :width: 400

Lorsque le pin17 est bas (l'interrupteur à bascule est en position verticale), nous changeons le costume du sprite culbuto en tumbler1 (état vertical).

.. image:: img/1.3_title3.png
  :width: 400

Lorsque le pin17 est haut (l'interrupteur à bascule est incliné), nous changeons le costume du sprite culbuto en tumbler2 (état incliné).
