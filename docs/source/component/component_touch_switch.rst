
.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _cpn_touch_switch:

Module Interrupteur Tactile
==================================

.. image:: img/touch168.png
    :width: 300
    :align: center

Le module interrupteur tactile fonctionne en détectant un changement de capacité dû à l'influence d'un objet externe. La plaque tactile est recouverte d'un matériau isolant, et l'utilisateur n'entre pas en contact avec le circuit électrique.

Un interrupteur tactile capacitif comporte différentes couches : une plaque isolante supérieure suivie d'une plaque tactile, une autre couche isolante, puis une plaque de masse.

.. image:: img/touch169.jpeg

En pratique, un capteur capacitif peut être fabriqué sur un circuit imprimé double face en considérant un côté comme le capteur tactile et le côté opposé comme la plaque de masse du condensateur. Lorsque l'alimentation est appliquée à ces plaques, les deux plaques se chargent. En état d'équilibre, les plaques ont la même tension que la source d'alimentation.

Le circuit détecteur tactile possède un oscillateur dont la fréquence dépend de la capacité du pavé tactile. Lorsqu'un doigt s'approche du pavé tactile, la capacité supplémentaire provoque un changement de fréquence de cet oscillateur interne. Le circuit de détection suit la fréquence de l'oscillateur à des intervalles réguliers et, lorsque le décalage dépasse le seuil de changement, le circuit déclenche un événement de pression de touche.

**Exemple**

* :ref:`2.1.3_c` (Projet C)
* :ref:`2.1.3_py` (Projet Python)
* :ref:`1.9_scratch` (Projet Scratch)
