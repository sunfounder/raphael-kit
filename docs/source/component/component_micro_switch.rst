.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _cpn_micro_switch:

Micro-interrupteur
=====================

.. image:: img/micro_pic.png
    :width: 200
    :align: center

La construction d'un micro-interrupteur est vraiment simple. Les principales parties de l'interrupteur sont :

.. image:: img/micro_switch2.png
    :align: center

* 1. Poussoir (Actionneur)
* 2. Couvercle
* 3. Pièce mobile
* 4. Support
* 5. Boîtier
* 6. Borne NO : normalement ouvert
* 7. Borne NC : normalement fermé
* 8. Contact
* 9. Bras mobile

Après qu'un micro-interrupteur ait établi un contact physique avec un objet, ses contacts changent de position. Le principe de fonctionnement de base est le suivant.

Lorsque le poussoir est en position relâchée ou de repos.

* Le circuit normalement fermé peut laisser passer le courant.
* Le circuit normalement ouvert est isolé électriquement.

Lorsque le poussoir est enfoncé ou commuté.

* Le circuit normalement fermé est ouvert.
* Le circuit normalement ouvert est fermé.

.. image:: img/micro_switch1.png

**Exemple**

* :ref:`2.1.2_c` (Projet C)
* :ref:`2.1.2_py` (Projet Python)
* :ref:`1.8_scratch` (Projet Scratch)
