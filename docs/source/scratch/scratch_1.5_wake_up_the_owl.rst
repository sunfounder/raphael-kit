.. _1.5_scratch:

1.5 Réveiller le Hibou
=========================

Aujourd'hui, nous allons jouer à un jeu pour réveiller le hibou.

Lorsque quelqu'un s'approche du module de capteur PIR, le hibou se réveillera de son sommeil.

.. image:: img/1.5_header.png

Composants Nécessaires
---------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.5_component.png

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
    *   - :ref:`cpn_pir`
        - \-

Construire le Circuit
------------------------

.. image:: img/1.5_fritzing.png

Il y a deux potentiomètres sur le module PIR : l'un pour ajuster la sensibilité et l'autre pour ajuster la distance de détection. Pour que le module PIR fonctionne mieux, vous devez tourner les deux à fond dans le sens antihoraire.

.. image:: ../img/PIR_TTE.png
    :width: 400
    :align: center

Charger le Code et Voir ce Qui Se Passe
------------------------------------------

Chargez le fichier de code (``1.5_wake_up_the_owl.sb3``) dans Scratch 3.

Lorsque vous vous approchez du module de capteur PIR, vous verrez le hibou dans la zone de scène ouvrir ses ailes et se réveiller, et lorsque vous vous éloignez, le hibou se rendormira.


Astuces sur le Sprite
--------------------------

Sélectionnez Sprite1 et cliquez sur **Costumes** en haut à gauche ; téléchargez **owl1.png** et **owl2.png** depuis le chemin ``~/raphael-kit/scratch/picture`` via le bouton **Télécharger Costume** ; supprimez les 2 costumes par défaut et renommez le sprite en **hibou**.

.. image:: img/1.5_pir1.png

Astuces sur les Codes
------------------------

.. image:: img/1.3_title2.png

Lorsque le drapeau vert est cliqué, l'état initial de gpio17 est défini sur bas.

.. image:: img/1.5_owl1.png
  :width: 400

Lorsque pin17 est bas (personne ne s'approche), changez le costume du sprite hibou en owl1 (état de sommeil).

.. image:: img/1.5_owl2.png
  :width: 400

Lorsque pin17 est haut (quelqu'un s'approche), changez le costume du sprite hibou en owl2 (état réveillé).
