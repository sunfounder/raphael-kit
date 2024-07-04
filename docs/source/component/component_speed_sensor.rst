.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _cpn_speed_sensor:

Module de capteur de vitesse
=================================

.. image:: img/speed_sensor1.png
    :width: 300
    :align: center

Le capteur de vitesse se compose de deux parties : un émetteur et un récepteur. L'émetteur émet de la lumière, qui entre ensuite dans le récepteur.

Si le faisceau lumineux entre l'émetteur et le récepteur est interrompu par un obstacle, le récepteur ne détectera pas la lumière incidente, alors la broche D0 sortira un niveau bas.

.. note::
    La broche A0 de ce module est vide et il n'y a pas de circuit.

.. image:: img/speed_sensor2.png

**Exemple**

* :ref:`2.2.6_c` (Projet C)
* :ref:`2.2.6_py` (Projet Python)
* :ref:`1.7_scratch` (Projet Scratch)
