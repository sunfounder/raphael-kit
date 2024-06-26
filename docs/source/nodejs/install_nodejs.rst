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