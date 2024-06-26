.. _1.15_scratch:

1.15 Gonfler le Ballon
=========================

Nous allons jouer à un jeu de gonflage de ballon.

En basculant l'interrupteur vers la gauche, vous commencez à gonfler le ballon, qui devient alors de plus en plus gros. Si le ballon devient trop grand, il éclatera ; s'il est trop petit, il ne flottera pas dans les airs. Vous devez juger le bon moment pour basculer l'interrupteur vers la droite pour arrêter de pomper.

.. image:: img/1.15_header.png

Composants Nécessaires
--------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.15_component.png

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
    *   - :ref:`cpn_slide_switch`
        - |link_slide_switch_buy|
    *   - :ref:`cpn_capacitor`
        - |link_capacitor_buy|

Construire le Circuit
------------------------

.. image:: img/1.15_scratch_fritzing.png

Charger le Code et Voir ce Qui Se Passe
------------------------------------------

Chargez le fichier de code (``1.15_inflating_the_balloon.sb3``) sur Scratch 3.

En basculant l'interrupteur vers la gauche, vous commencez à gonfler le ballon, qui devient alors de plus en plus gros. Si le ballon devient trop grand, il éclatera ; s'il est trop petit, il ne flottera pas dans les airs. Vous devez juger le bon moment pour basculer l'interrupteur vers la droite pour arrêter de pomper.

Astuces sur les Sprites
---------------------------

Supprimez le sprite précédent Sprite1, puis ajoutez le sprite **Balloon1**.

.. image:: img/1.15_slide1.png

Un effet sonore d'explosion de ballon est utilisé dans ce projet, voyons comment il a été ajouté.

Cliquez sur l'option **Son** en haut, puis cliquez sur **Télécharger Son** pour télécharger ``boom.wav`` à partir du chemin ``~/raphael-kit/scratch/sound`` vers Scratch 3.

.. image:: img/1.15_slide2.png

Astuces sur les Codes
--------------------------

.. image:: img/1.15_slide3.png
  :width: 500

Ceci est un bloc d'événement, et la condition de déclenchement est que gpio17 est haut, c'est-à-dire que l'interrupteur est basculé vers la gauche.

.. image:: img/1.15_slide4.png
  :width: 400

Réglez le seuil de taille du sprite Ballon1 à 120

.. image:: img/1.15_slide7.png
  :width: 400

Déplacez les coordonnées du sprite Balloon1 à (0,0), ce qui est le centre de la zone de scène.

.. image:: img/1.15_slide8.png
  :width: 300

Réglez la taille du sprite Balloon1 à 50 et affichez-le dans la zone de scène.

.. image:: img/1.15_slide5.png

Mettez en place une boucle pour gonfler le ballon, cette boucle s'arrête lorsque l'interrupteur à glissière est basculé vers la droite.

Dans cette boucle, la taille du ballon augmente de 1 toutes les 0,1s, et si elle dépasse ``maxSize``, le ballon éclatera, à ce moment-là, le son d'explosion retentira et le code sera terminé.

.. image:: img/1.15_slide6.png
  :width: 600

Après la sortie de la dernière boucle (interrupteur à glissière basculé vers la droite), déterminez la position du sprite Balloon1 en fonction de sa taille. Si la taille du sprite Balloon1 est supérieure à 90, décollez (déplacez les coordonnées à (0, 90), sinon atterrissez (déplacez les coordonnées à (0, -149)).
