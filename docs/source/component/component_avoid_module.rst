.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _cpn_avoid_module:

Module d'évitement d'obstacles
===========================================

.. image:: img/2.2.5IR_Obstacle.png
   :width: 400
   :align: center

Le module d'évitement d'obstacles IR a une forte adaptabilité à la lumière ambiante. 
Il est équipé d'une paire de tubes émetteurs et récepteurs infrarouges.

Le tube émetteur émet une fréquence infrarouge. Lorsque la direction de détection rencontre un 
obstacle, le rayonnement infrarouge est reçu par le tube récepteur. Après traitement par le 
circuit comparateur, l'indicateur vert s'allume et un signal de niveau bas est émis.

La distance de détection peut être ajustée par un potentiomètre, avec une plage de distance effective de 2 à 30 cm.

.. image:: img/IR_module.png
    :width: 600
    :align: center

**Exemple**

* :ref:`2.2.5_c` (Projet C)
* :ref:`2.2.5_py` (Projet Python)
* :ref:`1.11_scratch` (Projet Scratch)
