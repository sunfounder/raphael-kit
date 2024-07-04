.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _cpn_rotary_encoder:

Module Encodeur Rotatif
=============================

.. image:: img/rotary_encoder_pic.png
    :width: 300
    :align: center

Un encodeur rotatif est un capteur de position qui convertit la rotation d'un bouton en un signal de sortie, indiquant la direction dans laquelle le bouton est tourné.

Les encodeurs rotatifs sont des versions numériques des potentiomètres, offrant une plus grande polyvalence. Ils peuvent tourner en continu, tandis que les potentiomètres ont une rotation limitée. Les potentiomètres indiquent la position exacte du bouton, tandis que les encodeurs rotatifs montrent les changements de position.

Il existe principalement deux types d'encodeurs rotatifs : les encodeurs absolus et les encodeurs incrémentaux (relatifs). Un encodeur incrémental est utilisé dans ce kit.

Les encodeurs incrémentaux produisent des ondes carrées à deux phases, avec une différence de phase de 90 degrés, couramment appelée canaux A et B.

Comme illustré ci-dessous, lorsque le canal A passe d'un niveau haut à un niveau bas, si le canal B est à un niveau haut, cela indique que l'encodeur rotatif tourne dans le sens horaire (CW); si à ce moment-là le canal B est à un niveau bas, cela signifie que la rotation est antihoraire (CCW). Par conséquent, en lisant la valeur du canal B lorsque le canal A est à un niveau bas, nous pouvons déterminer la direction de rotation de l'encodeur rotatif.

.. image:: img/image206.png
    :width: 600
    :align: center
	
**Exemple**

* :ref:`2.1.6_c` (Projet en C)
* :ref:`2.1.6_py` (Projet en Python)

