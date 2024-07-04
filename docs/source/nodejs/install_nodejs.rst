.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

Qu'est-ce que Node.js ?
================================

Node.js a été lancé en mai 2009 et développé par Ryan Dahl. Il s'agit d'un environnement d'exécution JavaScript basé sur le moteur V8 de Chrome. Il utilise un modèle d'E/S non bloquant et piloté par des événements pour permettre à JavaScript de s'exécuter sur une plateforme de développement côté serveur.

En termes simples, Node.js est du JavaScript s'exécutant sur le serveur. Si vous êtes familier avec JavaScript, vous apprendrez facilement Node.js.

Node.js utilise généralement la commande ``npm install xxx`` pour installer des packages tiers, ce qui nécessite l'installation de l'outil npm, similaire à l'outil pip en Python.

Installer ou mettre à jour Node.js et npm
-----------------------------------------

Exécutez les commandes suivantes pour installer et mettre à jour Node.js et npm.

.. raw:: html

    <run></run>

.. code-block::

    sudo apt-get update
    sudo apt-get install nodejs
    sudo apt-get install npm 
    sudo npm install npm -g

Ensuite, vérifiez la version actuelle de Node avec la commande suivante.

.. raw:: html

    <run></run>

.. code-block::

    node -v

La commande suivante vérifie la version actuelle de npm.

.. raw:: html

    <run></run>

.. code-block::

    npm -v