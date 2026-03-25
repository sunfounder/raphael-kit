.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

Vidéo 21 : Utilisation d'un capteur ultrasonique HC-SR04 pour l'écholocalisation
=======================================================================================

Ce tutoriel couvre le processus de création d'un capteur de distance ultrasonique avec un Raspberry Pi en utilisant le capteur HC-SR04.
Cette vidéo explique les principes de l'écholocalisation, présente les composants nécessaires, démontre la configuration du câblage,
et guide pas à pas à travers le processus de codage.
Elle souligne l'importance d'une temporisation précise dans l'exécution du code pour des mesures de distance exactes et promeut de bonnes pratiques d'ingénierie.

1. **Introduction à l'Écholocalisation** : Utiliser le son pour détecter la position des objets, inspiré par les chauves-souris et les baleines.
2. **Vue d'ensemble des composants** : Présentation du capteur ultrasonique HC-SR04 et de sa connexion au Raspberry Pi.
3. **Configuration du câblage** : Connexion du capteur HC-SR04 aux broches GPIO du Raspberry Pi pour l'alimentation, la masse, la gâchette et l'écho.
4. **Processus de codage** : Parcours du code Python pour générer des impulsions ultrasoniques, activer le capteur et mesurer le temps de retour de l'écho.
5. **Considérations de temporisation** : Importance d'une temporisation précise pour une mesure de distance exacte.
6. **Bonnes pratiques d'ingénierie** : Insister sur la planification et la compréhension du code avant la mise en œuvre.
7. **Attente pour la broche d'écho** : Utilisation d'une boucle while pour attendre que la broche d'écho soit activée.
8. **Enregistrement de l'heure de début** : Capture du temps système lorsque la broche d'écho est activée pour marquer le début de la mesure.
9. **Mesure du temps de parcours du ping** : Calcul du temps de parcours du ping en déterminant la différence de temps entre le moment où la broche d'écho est activée et désactivée.
10. **Conversion des unités** : Multiplication du temps de parcours du ping par un million pour une lisibilité.
11. **Ajout de délai** : Introduction d'un délai après chaque mesure pour éviter les échos multiples.
12. **Calcul de la distance** : Utilisation de la vitesse du son et du temps de parcours du ping pour calculer la distance jusqu'à la cible.


**Vidéo**

.. raw:: html

    <iframe width="100%" 
    style="aspect-ratio: 16/9; max-width: 100%;"
    src="https://www.youtube.com/embed/SoAGLXoQ5XI?si=OPMqLtQ53hKNHs4j" 
    title="YouTube video player" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    allowfullscreen>
    </iframe>
