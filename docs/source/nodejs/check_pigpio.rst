.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

 
Vérifier pigpio
==========================

pigpio est un module utilisé pour contrôler les canaux GPIO du Raspberry Pi. Ce package fournit des méthodes pour gérer les GPIO sur le Raspberry Pi. Pour des exemples et de la documentation, veuillez visiter : https://www.npmjs.com/package/pigpio.

Entrez la commande suivante pour installer la bibliothèque pigpio.

.. raw:: html

    <run></run>

.. code-block::

    npm install pigpio

Pour vérifier si la bibliothèque est installée avec succès, changez de répertoire et entrez dans nodejs :

.. raw:: html

    <run></run>

.. code-block::

    cd ~/raphael-kit/nodejs
    nodejs

.. image:: img/pigpio1.png

Ensuite, entrez require('pigpio') :

.. raw:: html

    <run></run>

.. code-block::

    require('pigpio')

.. image:: img/pigpio2.png   

Si l'écran ci-dessus apparaît, l'installation de la bibliothèque est réussie.

Si vous souhaitez quitter l'interface de ligne de commande node, veuillez appuyer deux fois sur Ctrl+C.

.. image:: img/pigpio3.png