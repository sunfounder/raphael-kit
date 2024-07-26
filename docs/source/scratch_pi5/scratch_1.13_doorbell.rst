.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _1.13_scratch_pi5:

1.13 Sonnette
================

Aujourd'hui, nous allons fabriquer une sonnette. Cliquez sur le sprite bouton3 sur la scène, le buzzer sonnera; cliquez à nouveau, le buzzer cessera de sonner.

.. image:: img/1.13_header.png

Composants Nécessaires
--------------------------

Dans ce projet, nous avons besoin des composants suivants.

.. image:: img/1.13_list.png

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
        - \-
    *   - :ref:`cpn_transistor`
        - |link_transistor_buy|

Construire le Circuit
------------------------

.. image:: img/1.13_image106.png

Charger le Code et Voir ce Qui Se Passe
---------------------------------------

Chargez le fichier de code (``1.13_doorbell.sb3``) sur Scratch 3.

Cliquez sur le drapeau vert sur la scène. Lorsque nous cliquons sur le sprite Button 3, il deviendra bleu et le buzzer sonnera; lorsque nous cliquons à nouveau, le sprite **Button3** redevient gris et le buzzer cesse de sonner.


Astuces sur les Sprites
---------------------------

Supprimez le sprite par défaut, puis choisissez le sprite **Button 3**.

.. image:: img/1.13_scratch_button3.png

Puis réglez la taille sur 200.

.. image:: img/1.13_scratch_button3_size.png

Astuces sur les Codes
-------------------------

.. image:: img/1.13_buzzer4.png
  :width: 400

Ce bloc vous permet de changer le costume du sprite.

.. image:: img/1.13_buzzer5.png
  :width: 400


Réglez gpio17 sur bas pour faire sonner le buzzer; réglez-le sur haut et le buzzer ne sonnera pas.

L'interrupteur **status** est utilisé ici, et nous utiliserons un organigramme pour vous aider à comprendre l'ensemble du code.

Lorsque le drapeau vert est cliqué, le **status** sera d'abord réglé sur 0, et attendra que le sprite soit cliqué; si le sprite **button3** est cliqué, il changera de costume en **button-b** (bleu) et le **status** sera réglé sur 1. Lorsque le programme principal reçoit le **status** à 1, il fera sonner le buzzer à intervalle de 0.1s. Si **button3** est cliqué à nouveau, il changera de costume en **button-a** (gris) et le **status** sera de nouveau réglé sur 0.

.. image:: img/1.13_scratch_code.png

