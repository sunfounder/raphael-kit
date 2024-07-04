.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _quick_guide_on_scratch:

Guide rapide sur Scratch
=============================

.. note::

    Lors de la programmation avec Scratch 3, vous pourriez avoir besoin d'un écran pour une meilleure expérience, consultez : `Connectez votre Raspberry Pi <https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/3>`_. Bien sûr, si vous n'avez pas d'écran, vous pouvez également accéder au bureau du Raspberry Pi à distance. Pour un tutoriel détaillé, veuillez consulter :ref:`remote_desktop`.

De plus, Scratch 3 nécessite au moins 1 Go de RAM pour fonctionner, et nous recommandons un Raspberry Pi 4 avec au moins 2 Go de RAM. Bien que vous puissiez exécuter Scratch 3 sur un Raspberry Pi 2, 3, 3B+ ou un Raspberry 4 avec 1 Go de RAM, les performances sur ces modèles sont réduites et, selon les autres logiciels que vous exécutez en même temps, Scratch 3 peut ne pas démarrer par manque de mémoire.

Installer Scratch 3
-----------------------
Lors de l'installation de Raspberry Pi OS (:ref:`install_os`), vous devez choisir la version avec bureau, soit uniquement avec bureau, soit avec bureau et logiciels recommandés.

Si vous installez la version avec les logiciels recommandés, vous pouvez voir Scratch 3 dans le menu système sous **Programmation**.

Si vous avez installé la version uniquement avec le bureau, vous devrez installer Scratch 3 manuellement, comme décrit ci-dessous.

Ouvrez le menu, cliquez sur **Préférences** -> **Logiciels recommandés**.

.. image:: img/quick_scratch1.png

Trouvez Scratch 3 et cochez-le, puis cliquez sur **Appliquer** et attendez la fin de l'installation.

.. image:: img/quick_scratch2.png

Une fois l'installation terminée, vous devriez le voir sous **Programmation** dans le menu système.

.. image:: img/quick_scratch3.png


À propos de l'interface de Scratch 3
------------------------------------

Scratch 3 est conçu pour être amusant, éducatif et facile à apprendre. Il dispose d'outils pour créer des histoires interactives, des jeux, de l'art, des simulations et plus encore, en utilisant la programmation par blocs. Scratch dispose également de son propre éditeur de peinture et éditeur de son intégrés.

Le haut de Scratch 3 possède quelques options de base, la première de gauche à droite est l'option de langue, vous pouvez choisir différentes langues pour la programmation. La seconde est l'option **Fichier**, vous pouvez créer de nouveaux fichiers, lire des fichiers locaux et enregistrer les fichiers en cours avec cette option. La troisième est l'option **Édition**, qui vous permet de reprendre certaines opérations de suppression et d'activer le mode accélération (dans lequel le mouvement du sprite devient particulièrement rapide). La quatrième est l'option **Tutoriels**, qui vous permet de consulter des tutoriels pour certains projets. La cinquième est l'option de nommage de fichier, où vous pouvez renommer le projet.

.. image:: img/quick_scratch13.png

**Code**

Il a trois sections principales : une zone de scène, une palette de blocs et une zone de codage. Programmez en cliquant et en faisant glisser le bloc de la palette de blocs vers la zone de codage, et enfin, vos résultats de programmation seront affichés dans la zone de scène.

.. image:: img/quick_scratch4.png

Voici la zone des sprites de Scratch 3. Au-dessus de la zone se trouvent les paramètres de base des sprites, vous pouvez ajouter des sprites fournis avec Scratch 3 ou télécharger des sprites locaux.

.. image:: img/quick_scratch5.png

Voici la zone de fond d'écran de Scratch 3, principalement pour ajouter un fond d'écran approprié pour votre scène. Vous pouvez ajouter le fond d'écran fourni avec Scratch 3 ou télécharger un fond d'écran local.

.. image:: img/quick_scratch6.png

Ceci est un bouton **Ajouter une extension**.

.. image:: img/quick_scratch7.png

Dans Scratch 3, nous pouvons ajouter toutes sortes d'extensions utiles. Ici, nous prenons **Détection vidéo** comme exemple et cliquons dessus.

.. image:: img/quick_scratch8.png

Vous le verrez dans la palette de blocs et vous pourrez utiliser les fonctions associées à cette extension. Si vous avez une caméra connectée, vous verrez l'écran de la caméra dans la zone de scène.

.. image:: img/quick_scratch9.png

**Costumes**

Cliquez sur l'option **Costumes** dans le coin supérieur gauche pour accéder à la palette de costumes. Différents costumes permettent aux sprites d'avoir des mouvements statiques différents, et lorsque ces mouvements statiques sont assemblés, ils forment un mouvement dynamique cohérent.

.. image:: img/quick_scratch10.png

**Sons**

Vous pourriez avoir besoin d'utiliser des extraits de musique pour rendre vos expériences plus intéressantes. Cliquez sur l'option **Sons** dans le coin supérieur gauche et vous pouvez éditer le son actuel ou en sélectionner/télécharger un nouveau.

.. image:: img/quick_scratch11.png



