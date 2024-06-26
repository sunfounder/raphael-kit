 
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