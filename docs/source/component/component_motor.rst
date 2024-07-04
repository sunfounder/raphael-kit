.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _cpn_motor:

Moteur à courant continu
================================

.. image:: img/image114.jpeg
    :align: center

Ceci est un moteur à courant continu de 3V. Lorsque vous appliquez un niveau élevé et un niveau faible à chacune des 2 bornes, il se mettra à tourner.

* **Dimensions** : 25*20*15MM
* **Tension de fonctionnement** : 1-6V
* **Courant à vide** (3V) : 70mA
* **Vitesse à vide** (3V) : 13000RPM
* **Courant de blocage** (3V) : 800mA
* **Diamètre de l'arbre** : 2mm

Le moteur à courant continu (DC) est un actionneur continu qui convertit l'énergie électrique en énergie mécanique. Les moteurs à courant continu permettent de faire fonctionner des pompes rotatives, des ventilateurs, des compresseurs, des turbines et d'autres dispositifs en produisant une rotation angulaire continue.

Un moteur à courant continu se compose de deux parties : la partie fixe du moteur appelée **stator** et la partie interne du moteur appelée **rotor** (ou **armature** d'un moteur à courant continu) qui tourne pour produire le mouvement.
La clé pour générer du mouvement est de positionner l'armature dans le champ magnétique de l'aimant permanent (dont le champ s'étend du pôle nord au pôle sud). L'interaction du champ magnétique et des particules chargées en mouvement (le fil porteur de courant génère le champ magnétique) produit le couple qui fait tourner l'armature.

.. image:: img/motor_sche.png
    :align: center

Le courant circule de la borne positive de la batterie à travers le circuit, passant par les balais en cuivre jusqu'au collecteur, puis jusqu'à l'armature.
Mais en raison des deux fentes dans le collecteur, ce flux s'inverse à mi-chemin de chaque rotation complète.
Cette inversion continue convertit essentiellement l'alimentation en courant continu de la batterie en courant alternatif, permettant à l'armature de subir un couple dans la bonne direction au bon moment pour maintenir la rotation.

**Exemple**

* :ref:`1.3.1_c` (Projet C)
* :ref:`3.1.4_c` (Projet C)
* :ref:`1.3.1_py` (Projet Python)
* :ref:`4.1.10_py` (Projet Python)
* :ref:`1.17_scratch` (Projet Scratch)
