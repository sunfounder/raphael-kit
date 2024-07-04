.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _cpn_7_segment:

Affichage à 7 segments
==============================

.. image:: img/7-seg.jpg

Un affichage à 7 segments est un composant en forme de 8 qui regroupe 7 LED. Chaque LED est appelée un segment - lorsqu'elle est alimentée, un segment forme une partie du chiffre à afficher.

Il existe deux types de connexion de broches : Cathode Commune (CC) et Anode Commune (CA). Comme son nom l'indique, un affichage CC a toutes les cathodes des 7 LED connectées tandis qu'un affichage CA a toutes les anodes des 7 segments connectées.

Dans ce kit, nous utilisons l'affichage à 7 segments à cathode commune, voici le symbole électronique.

.. image:: img/segment_cathode.png
    :width: 800

Chaque LED de l'affichage est attribuée à un segment positionnel avec une de ses broches de connexion sortant du boîtier en plastique rectangulaire. Ces broches LED sont étiquetées de "a" à "g" représentant chaque LED individuelle. Les autres broches LED sont connectées ensemble formant une broche commune. Ainsi, en polarisant dans le sens direct les broches appropriées des segments LED dans un ordre particulier, certains segments s'allumeront et d'autres resteront éteints, affichant ainsi le caractère correspondant sur l'affichage.

**Codes d'affichage**

Pour vous aider à comprendre comment les affichages à 7 segments (Cathode Commune) affichent les chiffres, nous avons dressé le tableau suivant. Les chiffres correspondent aux nombres de 0 à F affichés sur l'affichage à 7 segments ; (DP) GFEDCBA se réfère à l'ensemble de LED correspondant à 0 ou 1. Par exemple, 00111111 signifie que DP et G sont réglés sur 0, tandis que les autres sont réglés sur 1. Ainsi, le chiffre 0 est affiché sur l'affichage à 7 segments, et le code HEX correspond au nombre hexadécimal.

.. image:: img/segment_code.png

**Exemple**

* :ref:`1.1.4_c` (Projet C)
* :ref:`1.1.4_py` (Projet Python)

