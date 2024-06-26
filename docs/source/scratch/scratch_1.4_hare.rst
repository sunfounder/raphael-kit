.. _1.4_scratch:

1.4 Lièvre
==============

Aujourd'hui, nous allons utiliser un bouton, un Raspberry Pi et Scratch pour créer un lièvre avec diverses transformations !

Lorsque nous appuyons sur le premier bouton, le lièvre dans la zone de scène changera de couleur de corps ; lorsque nous appuyons sur le deuxième bouton, le lièvre changera de taille ; lorsque nous appuyons sur le troisième bouton, le lièvre fera un pas en avant.

.. image:: img/1.4_header.png

Composants Nécessaires
---------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.4_list.png

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
    *   - :ref:`cpn_button`
        - |link_button_buy|

Construire le Circuit
-------------------------

.. image:: img/1.4_scratch_button.png

Charger le Code et Voir ce Qui Se Passe
------------------------------------------

Chargez le fichier de code (``1.4_hare.sb3``) dans Scratch 3.

Vous pouvez maintenant essayer d'appuyer sur chacun des 3 boutons pour voir comment le Lièvre sur la scène va changer.


Astuces sur le Sprite
------------------------

Cliquez sur le bouton **Choisir un Sprite** dans le coin inférieur droit de la zone de sprite, entrez **Lièvre** dans la boîte de recherche, puis cliquez pour l'ajouter.

.. image:: img/1.4_button1.png

Supprimez Sprite1.

.. image:: img/1.4_button2.png

Astuces sur les Codes
-------------------------

.. image:: img/1.4_button3.png
  :width: 400

Ceci est un bloc d'événement qui est déclenché lorsque le niveau de GPIO17 est haut, ce qui signifie que le bouton est pressé à ce moment-là.

.. image:: img/1.4_button4.png
  :width: 400

Ceci est un bloc pour changer la couleur du **Lièvre**, la plage de la valeur est de 0 à 199, au-delà de 199, cela recommencera à 0.

.. image:: img/1.4_button5.png
  :width: 250

Ceci est un bloc utilisé pour changer la taille du sprite, plus la valeur est élevée, plus le sprite est grand.

.. note::
  Le sprite n'est pas non plus infiniment grand, et sa taille maximale est liée à la taille de l'image originale.

.. image:: img/1.4_button6.png
  :width: 200

Ceci est un bloc qui change les costumes du sprite, et lorsque le costume du **Lièvre** continue de changer, il effectue une série d'actions cohérentes. Par exemple, dans ce projet, faire avancer le **Lièvre** d'un pas.
