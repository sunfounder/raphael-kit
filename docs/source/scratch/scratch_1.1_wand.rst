.. _1.1_scratch:

1.1 Baguette magique
========================

Aujourd'hui, nous allons utiliser une LED, un Raspberry Pi et Scratch pour créer un jeu amusant. Lorsque nous agiterons la baguette magique, la LED clignotera.

.. image:: img/1.1_header.png

Composants nécessaires
---------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.1_list.png

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
    *   - :ref:`cpn_led`
        - |link_led_buy|

Construire le circuit
------------------------

.. image:: img/1.1_image49.png

Ajouter l'extension GPIO
---------------------------

Cliquez sur le bouton **Ajouter une extension** dans le coin inférieur gauche, puis ajoutez l'extension **Raspberry Pi GPIO**, une extension que nous utilisons pour tous nos projets Scratch.

.. image:: img/1.1_scratchled1.png
    :align: center

.. image:: img/1.1_scratchled2.png
    :align: center

.. image:: img/1.1_scratchled3.png
    :align: center

Charger le code et voir ce qui se passe
------------------------------------------

Chargez le fichier de code depuis votre ordinateur (``~/raphael-kit/scratch/code``) vers Scratch 3.

.. image:: img/1.1_scratch_step1.png

.. image:: img/1.1_scratch_step2.png

Après avoir cliqué sur la baguette magique dans la zone de scène, vous verrez la LED clignoter pendant deux secondes.

.. image:: img/1.1_step3.png


Astuces sur les sprites
---------------------------

Cliquez sur **Télécharger Sprite**.

.. image:: img/1.1_upload_sprite.png

Téléchargez **Wand.png** depuis le chemin ``~/raphael-kit/scratch/picture`` vers Scratch 3.

.. image:: img/1.1_upload.png

Enfin, supprimez **Sprite1**.

.. image:: img/1.1_delete.png

Astuces sur les codes
-------------------------

.. image:: img/1.1_LED1.png
  :width: 300

Ceci est un bloc d'événement dont la condition de déclenchement est de cliquer sur le drapeau vert sur la scène. Un événement de déclenchement est nécessaire au début de tous les codes, et vous pouvez sélectionner d'autres événements de déclenchement dans la catégorie **Événements** de la **palette de blocs**.

.. image:: img/1.1_events.png
  :width: 300

Par exemple, nous pouvons maintenant changer l'événement de déclenchement pour un clic sur le sprite.

.. image:: img/1.1_LED2.png
  :width: 300

Ceci est un bloc avec un nombre défini de cycles. Lorsque nous remplissons le nombre 10, les événements dans le bloc seront exécutés 10 fois.

.. image:: img/1.1_LED4.png
  :width: 300

Ce bloc est utilisé pour suspendre le programme pendant une période en secondes.

.. image:: img/1.1_LED3.png
  :width: 500

Étant donné que la méthode de nommage BCM est utilisée dans Scratch, ce code configure GPIO17 (BCM17) à 0V (niveau bas). Comme la cathode de la LED est connectée à GPIO17, la LED s'allumera. Au contraire, si vous configurez GPIO (BCM17) sur haut, la LED s'éteindra.
