.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

Vidéo 37 : Système d'alarme de détection de mouvement avec écran LCD et clavier
=======================================================================================

Ce tutoriel présente la création d'un système d'alarme utilisant un Raspberry Pi, intégrant une saisie via un clavier et un affichage LCD.
Il fournit des instructions pas à pas pour le câblage des composants, la configuration des bibliothèques,
et la mise en œuvre des fonctionnalités telles que l'activation, la désactivation et le changement de mot de passe.
La vidéo met l'accent sur la portabilité et le déploiement dans le monde réel, au-delà de l'utilisation sur bureau.

1. **Portabilité et déploiement** : Transférer les projets Raspberry Pi au-delà du bureau pour des applications réelles.
2. **Installation du clavier et de l'écran LCD** : Câblage d'un clavier et d'un écran LCD aux broches GPIO du Raspberry Pi pour l'entrée et la sortie.
3. **Multitâche avec le threading** : Utilisation du threading pour gérer les entrées du clavier tout en exécutant d'autres tâches.
4. **Intégration de bibliothèques** : Importation et utilisation de bibliothèques pour les fonctionnalités du clavier et de l'écran LCD.
5. **Flux du programme** : Mise en œuvre de trois modes pour le système d'alarme - armé, désarmé et changement de mot de passe - et utilisation du threading pour surveiller en continu l'entrée du clavier.
6. **Gestion des erreurs** : Fourniture de mécanismes de gestion des erreurs, tels que permettre aux utilisateurs de tuer le programme avec une entrée astérisque.
7. **Configuration de la structure du programme** : Démonstration de la configuration des threads, de la définition de la boucle principale et de la gestion des entrées du clavier.
8. **Gestion des entrées du clavier** : Explication de la façon de traiter les commandes du clavier pour armer, désarmer, changer les mots de passe et déclencher des actions d'alarme.
9. **Fonctionnalité de l'alarme** : Mise en œuvre de la détection de mouvement à l'aide d'un capteur PIR pour déclencher des alertes d'intrus sur l'écran LCD.
10. **Interaction utilisateur** : Fourniture de retours à l'utilisateur via l'écran LCD pour le statut du système, les alertes et les invites de mot de passe.
11. **Gestion des erreurs et nettoyage** : Assure une terminaison correcte du programme avec gestion des erreurs, nettoyage des GPIO et effacement de l'écran LCD.
12. **Défi pour les spectateurs** : Encourage les spectateurs à améliorer le système d'alarme avec des fonctionnalités supplémentaires telles que des alarmes sonores ou une intégration Bluetooth dans le cadre d'un concours pour les droits de vantardise.

**Vidéo**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/y0PEhuLAjNY?si=LI-oSA53Obuf8wn2" title="Lecteur vidéo YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
