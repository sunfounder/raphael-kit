
.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _filezilla:

Logiciel Filezilla
==========================

.. image:: img/filezilla_icon.png

Le protocole de transfert de fichiers (FTP) est un protocole de communication standard utilisé pour le transfert de fichiers informatiques d'un serveur à un client sur un réseau informatique.

Filezilla est un logiciel open source qui prend en charge non seulement le FTP, mais aussi le FTP sur TLS (FTPS) et le SFTP. Nous pouvons utiliser Filezilla pour télécharger des fichiers locaux (tels que des images et des fichiers audio) vers le Raspberry Pi, ou télécharger des fichiers du Raspberry Pi vers le local.

**Étape 1** : Télécharger Filezilla.

Téléchargez le client depuis `Filezilla’s official website <https://filezilla-project.org/>`_, Filezilla dispose d'un très bon tutoriel, veuillez consulter : `Documentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_.

**Étape 2** : Connectez-vous au Raspberry Pi

Après une installation rapide, ouvrez-le et `connect it to an FTP server <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Il existe 3 manières de se connecter, ici nous utilisons la barre **Connexion rapide**. Entrez le **nom d'hôte/IP**, le **nom d'utilisateur**, le **mot de passe** et le **port (22)**, puis cliquez sur **Connexion rapide** ou appuyez sur **Entrée** pour vous connecter au serveur.

.. image:: img/filezilla_connect.png

.. note::

    La connexion rapide est un bon moyen de tester vos informations de connexion. Si vous souhaitez créer une entrée permanente, vous pouvez sélectionner **Fichier** -> **Copier la connexion actuelle vers le gestionnaire de sites** après une connexion rapide réussie, entrez le nom et cliquez sur **OK**. La prochaine fois, vous pourrez vous connecter en sélectionnant le site précédemment enregistré dans **Fichier** -> **Gestionnaire de sites**.
    
    .. image:: img/ftp_site.png

**Étape 3** : Télécharger/téléverser des fichiers.

Vous pouvez téléverser des fichiers locaux vers le Raspberry Pi en les glissant et en les déposant, ou télécharger les fichiers du Raspberry Pi vers votre ordinateur local.

.. image:: img/upload_ftp.png

