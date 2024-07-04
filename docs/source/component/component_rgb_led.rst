.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _cpn_rgb_led:

LED RVB
=================

.. image:: img/rgb_led.png
    :width: 100
    
Les LED RVB émettent de la lumière dans différentes couleurs. Une LED RVB regroupe trois LED de couleurs rouge, verte et bleue dans une enveloppe en plastique transparente ou semi-transparente. Elle peut afficher diverses couleurs en modifiant la tension d'entrée des trois broches et en les superposant, ce qui, selon les statistiques, peut créer 16 777 216 couleurs différentes. 

.. image:: img/rgb_light.png
    :width: 600

Les LED RVB peuvent être classées en anode commune et cathode commune. Dans ce kit, la seconde est utilisée. La **cathode commune**, ou CC, signifie connecter les cathodes des trois LED. Après l'avoir connectée à la masse (GND) et branché les trois broches, la LED affichera la couleur correspondante. 

Son symbole de circuit est illustré ci-dessous.

.. image:: img/rgb_symbol.png
    :width: 300

Une LED RVB a 4 broches : la plus longue est la masse (GND); les autres sont Rouge, Vert et Bleu. Touchez son enveloppe en plastique et vous trouverez une encoche. La broche la plus proche de l'encoche est la première broche, marquée Rouge, puis GND, Vert et Bleu dans cet ordre. 

.. image:: img/rgb_pin.jpg
    :width: 200

**Exemple**

* :ref:`1.1.2_c` (Projet en C)
* :ref:`1.1.2_py` (Projet en Python)
* :ref:`1.2_scratch` (Projet en Scratch)

