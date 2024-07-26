.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _1.12_scratch_pi5:

1.12 Lampe à eau
====================

Aujourd'hui, nous allons utiliser une barre LED, un Raspberry Pi et Scratch pour créer une lampe à eau.

La barre LED s'allumera en suivant la direction des flèches sur la scène.

.. image:: img/1.12_header.png

Composants Nécessaires
--------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.12_list.png

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
    *   - :ref:`cpn_bar_graph`
        - \-

Construire le Circuit
-----------------------

.. image:: img/1.12_image66.png

Charger le Code et Voir ce Qui Se Passe
------------------------------------------

Chargez le fichier de code (``1.12_water_lamp.sb3``) depuis votre ordinateur vers Scratch 3.

En cliquant sur **Arrow1**, les LED de la barre s'allument une à une de la gauche vers la droite, puis s'éteignent. Cliquez sur **Arrow2** et les LED s'allument dans l'ordre inverse.

Astuces sur les Sprites
----------------------------

Supprimez le sprite par défaut et choisissez le sprite **Arrow1**.

.. image:: img/1.12_graph1.png

Nous aurons besoin de 2 sprites **Arrow1**, que vous pouvez dupliquer avec le bouton de duplication.

.. image:: img/1.12_scratch_duplicate.png

Cliquez sur le sprite **Arrow 2** et changez la direction de la flèche en sélectionnant le costume 2.

.. image:: img/1.12_graph2.png

Créons maintenant une variable.

.. image:: img/1.12_graph3.png

Nommez-la **num**.

.. image:: img/1.12_graph4.png

Suivez la même méthode pour créer une liste appelée **led**.

.. image:: img/1.12_graph6.png

Après l'ajout, vous devriez voir la variable **num** et la liste **led** sur la zone de la scène.

Cliquez sur **+** pour ajouter 10 éléments à la liste et entrez les numéros de broche dans l'ordre (17,18,27,22,23,24,25,2,3,8).

.. image:: img/1.12_graph7.png

Astuces sur les Codes
-------------------------

.. image:: img/1.12_graph10.png
  :width: 300

Ceci est un bloc d'événement qui est déclenché lorsque le sprite actuel est cliqué.

.. image:: img/1.12_graph8.png
  :width: 300

La valeur initiale de la variable **num** détermine quelle LED est allumée en premier.

.. image:: img/1.12_graph9.png

Réglez la broche correspondant à **num** dans la liste led sur bas pour allumer la LED, puis réglez la broche correspondant à **num-1** sur haut pour éteindre la LED précédente.
