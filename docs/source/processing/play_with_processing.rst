.. _play_with_processing:

Jouer avec Processing (non compatible avec Pi 5)
===================================================

Qu'est-ce que Processing ?
---------------------------------

Processing est un environnement de programmation simple qui a été créé pour faciliter le développement d'applications visuellement orientées, en mettant l'accent sur l'animation et en fournissant aux utilisateurs un retour instantané grâce à l'interaction. 
Les développeurs voulaient un moyen de « dessiner » des idées en code. 
Au fil de la dernière décennie, les capacités de Processing se sont étendues, et il est désormais utilisé pour des travaux de production avancés en plus de son rôle initial de croquis. 
Initialement construit comme une extension de Java spécifiquement destinée aux artistes et designers, Processing a évolué pour devenir un outil de conception et de prototypage complet utilisé pour des installations à grande échelle, des graphiques animés et des visualisations de données complexes.

Processing est basé sur Java, mais comme les éléments de programme dans Processing sont assez simples, vous pouvez apprendre à l'utiliser même si vous ne connaissez pas Java. Si vous êtes familier avec Java, il est préférable d'oublier que Processing a quoi que ce soit à voir avec Java pendant un certain temps, jusqu'à ce que vous compreniez comment l'API fonctionne.

Ce texte est tiré du tutoriel, `Aperçu de Processing <https://processing.org/tutorials/overview/>`_.

Installer Processing
------------------------

.. note:: 

    Avant de pouvoir utiliser Processing, vous devez accéder au bureau de Raspberry Pi à distance (:ref:`remote_desktop`) ou connecter un écran au Raspberry Pi.

.. Exécutez la commande suivante dans le Terminal pour installer Processing.

.. .. raw:: html

..    <run></run>

.. .. code-block:: 

..     curl https://processing.org/download/install-arm.sh | sudo sh

.. Une fois l'installation terminée, tapez ``processing`` pour l'ouvrir.

.. .. image:: img/processing1.png

.. Pour un tutoriel détaillé, veuillez vous référer à `Pi Processing <https://pi.processing.org/>`_.


#. Visitez d'abord https://processing.org/download et sélectionnez la version ``Linux（Raspberry Pi 32-bit）`` ou ``Linux（Raspberry Pi 64-bit）``. En utilisant cette méthode, vous pouvez toujours télécharger la dernière version.

    Ou vous pouvez utiliser la commande suivante pour télécharger Processing depuis le Terminal.

    .. code-block:: 

        wget https://github.com/benfry/processing4/releases/download/processing-1293-4.3/processing-4.3-linux-arm32.tgz

    .. code-block:: 

        wget https://github.com/benfry/processing4/releases/download/processing-1293-4.3/processing-4.3-linux-arm64.tgz

#. Un fichier ``.tar.gz`` sera téléchargé, ce qui est bien connu des utilisateurs de Linux. Extrayez le fichier que vous venez de télécharger à partir de son emplacement.

    .. code-block:: 

        tar xvfz processing-xxxx.tgz

    Remplacez xxxx par le reste du nom du fichier, qui est le numéro de version. Cela créera un dossier nommé processing-xxxx ou quelque chose de similaire.

#. Ensuite, allez dans ce répertoire :

    .. code-block:: 

        cd processing-xxxx

#. Et exécutez-le :

.. code-block:: 

    ./processing

#. Avec un peu de chance, la fenêtre principale de Processing sera maintenant visible.

    .. image:: img/processing2.png


Installer Hardware I/O
----------------------

Pour utiliser le GPIO du Raspberry Pi, vous devez ajouter manuellement une `bibliothèque Hardware I/O <https://processing.org/reference/libraries/io/index.html>`_.

Cliquez sur ``Sketch`` -> ``Import Library`` -> ``Add Library...`` 

.. image:: img/import-00.png

Trouvez Hardware I/O, sélectionnez-le, puis cliquez sur Installer. Une fois terminé, une icône de coche apparaîtra.

.. image:: img/import-02.png

Projets
------------

.. toctree::
    draw_a_matchmaker
    hello_mouse
    blinking_dot
    clickable_dot
    clickable_color_blocks
    inflating_the_dot
    dot_on_the_swing
    metronome
    show_number
    drag_number
