.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _cpn_4_digit:

Affichage à 7 segments 4 chiffres
==================================

L'affichage à 7 segments 4 chiffres se compose de quatre affichages à 7 segments fonctionnant 
ensemble.

.. image:: img/4-digit-sche.png

L'affichage à 7 segments 4 chiffres fonctionne indépendamment. Il utilise le principe de la 
persistance visuelle humaine pour afficher rapidement les caractères de chaque segment en boucle
afin de former des chaînes continues.

Par exemple, lorsque "1234" est affiché, "1" apparaît sur le premier segment, tandis que "234" 
ne s'affiche pas. Après un certain temps, le deuxième segment affiche "2", et les 1er, 3e et 4e 
segments n'affichent rien. Ainsi, les quatre chiffres s'affichent à tour de rôle. Ce processus 
est très court (environ 5ms) et, grâce à l'effet de rémanence optique et au principe de 
persistance visuelle, nous pouvons voir les quatre caractères en même temps.

.. image:: img/image78.png

**Codes d'affichage**

Pour vous aider à comprendre comment les affichages à 7 segments (anode commune) affichent les 
chiffres, nous avons dressé le tableau suivant. Les nombres correspondent aux chiffres de 0 à F 
affichés sur l'affichage à 7 segments ; (DP) GFEDCBA se réfère à l'ensemble de LED correspondant 
à 0 ou 1. Par exemple, 11000000 signifie que DP et G sont réglés sur 1, tandis que les autres sont 
réglés sur 0. Ainsi, le chiffre 0 est affiché sur l'affichage à 7 segments, et le code HEX 
correspond au nombre hexadécimal.

.. image:: img/common_anode.png

**Exemple**

* :ref:`1.1.5_c` (Projet C)
* :ref:`3.1.1_c` (Projet C)
* :ref:`3.1.6_c` (Projet C)
* :ref:`3.1.12_c` (Projet C)
* :ref:`1.1.5_py` (Projet Python)
* :ref:`4.1.3_py` (Projet Python)
* :ref:`4.1.7_py` (Projet Python)
* :ref:`4.1.12_py` (Projet Python)
* :ref:`4.1.18_py` (Projet Python)

