.. _1.14_scratch:

1.14 123 Homme de bois
==========================

Aujourd'hui, nous allons jouer à un jeu de 123 homme de bois.

Cliquez sur le drapeau vert pour démarrer le jeu, maintenez la touche fléchée droite du clavier enfoncée pour faire avancer le sprite vers la droite. Si le voyant vert est allumé, le sprite peut se déplacer ; mais lorsque la LED rouge est allumée, vous devez arrêter le sprite, sinon le buzzer continuera de sonner.

.. image:: img/1.14_header.png

Composants Nécessaires
--------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.14_component.png

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
    *   - :ref:`cpn_buzzer`
        - |link_passive_buzzer_buy|
    *   - :ref:`cpn_led`
        - |link_led_buy|
    *   - :ref:`cpn_transistor`
        - |link_transistor_buy|

Construire le Circuit
------------------------

.. image:: img/1.14_fritzing.png


Charger le Code et Voir ce Qui Se Passe
------------------------------------------

Chargez le fichier de code (``1.14_123_wooden_man.sb3``) sur Scratch 3.

Lorsque la LED verte est allumée, vous pouvez utiliser la touche fléchée droite pour contrôler **Avery** pour marcher vers la droite ; lorsque la LED rouge est allumée, si vous continuez à faire avancer **Avery**, une alarme se déclenchera.

Astuces sur les Sprites
----------------------------

Supprimez le sprite par défaut, puis choisissez le sprite **Avery Walking**.

.. image:: img/1.14_wooden1.png
  :width: 400

Astuces sur les Codes
-------------------------

.. image:: img/1.14_wooden2.png
  :width: 400

Initialisez tous les pins sur haut.

.. image:: img/1.14_wooden3.png
  :width: 400

Lorsque le jeu commence, attribuez la variable de statut à 1, indiquant que le sprite Avery Walking est déplaçable, puis réglez gpio18 sur bas, ce qui allume la LED verte pendant 5s.

.. image:: img/1.14_wooden4.png
  :width: 400

Réglez gpio18 sur haut, puis réglez gpio27 sur bas, ce qui éteint la LED verte et allume la LED jaune pendant 0,5s.

.. image:: img/1.14_wooden5.png
  :width: 400

Attribuez la variable de statut à 0, ce qui signifie que le sprite Avery Walking ne se déplace pas ; puis réglez gpio27 sur bas et gpio17 sur haut, ce qui éteint la LED jaune et allume la LED rouge pendant 3s. Enfin, réglez gpio17 sur haut pour éteindre la LED rouge.

.. image:: img/1.14_wooden6.png
  :width: 400

Lorsque nous appuyons sur la touche fléchée droite du clavier, nous devons passer le sprite **Avery Walking** au costume suivant afin que nous puissions voir Avery marcher vers la droite. Ensuite, nous devons déterminer la valeur de la variable **status**. Si elle est à 0, cela signifie que le sprite Avery Walking ne bouge pas à ce moment-là et le buzzer sonnera pour vous avertir que vous ne pouvez pas appuyer à nouveau sur la touche fléchée droite.
