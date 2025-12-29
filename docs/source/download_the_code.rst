.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !


Télécharger le code
==================

Tous les programmes d’exemple utilisés dans ce kit sont stockés dans notre dépôt GitHub officiel.  
Utilisez la commande suivante pour télécharger l’intégralité du projet sur votre Raspberry Pi.

Cloner le dépôt
---------------

#. Connectez-vous à votre Raspberry Pi et exécutez :

   .. raw:: html
   
       <run></run>
   
   .. code-block:: bash
   
      cd ~/
      git clone https://github.com/sunfounder/raphael-kit.git --depth 1

#. Entrez dans le répertoire du projet :

   .. raw:: html
   
       <run></run>
   
   .. code-block:: bash
   
      cd ~/raphael-kit/

#. Listez les fichiers :

   .. raw:: html
   
       <run></run>
   
   .. code-block:: bash
   
      ls

#. Vous verrez une structure similaire à celle-ci :

   .. code-block:: text
   
      raphael-kit/
      ├── c/
      ├── iot/
      ├── music/
      ├── nodejs/
      ├── python-pi5/
      ├── python/
      ├── scratch/
      └── README.md


Présentation de la structure du projet
--------------------------------------

Voici une brève introduction de chaque dossier :

* **c/**  

  Exemples et bibliothèques en langage C pour les utilisateurs qui préfèrent programmer en C sur Raspberry Pi.

* **iot/**  

  Exemples liés à l’IoT, incluant la connectivité avec la plateforme Blynk, des démonstrations de capteurs et des modules de communication.

* **music/** 

  Contient des ressources audio telles que ``doorbell.wav`` et ``my_music.mp3`` utilisées dans les projets ultérieurs.

* **nodejs/**

  Exemples Node.js pour les utilisateurs développant des projets basés sur JavaScript sur Raspberry Pi.

* **python/**  

  Programmes d’exemple en Python écrits avec la bibliothèque ``RPi.GPIO``, adaptés à la plupart des cartes Raspberry Pi.

* **python-pi5/**  

  Exemples Python écrits avec la bibliothèque ``GPIO Zero``, spécifiquement optimisés pour le **Raspberry Pi 5**.

* **scratch/** 

  Exemples de programmation Scratch conçus pour les débutants apprenant la programmation graphique.

* **README.md**  

  Informations de base sur le dépôt et instructions générales.

Vous pouvez maintenant entrer dans le dossier correspondant à votre langage de programmation ou type de projet préféré et commencer à exécuter les exemples.
