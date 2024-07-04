.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

Vidéo 10 : Création d'une LED Dimmable avec Deux Boutons-Poussoirs
=======================================================================================

Ce tutoriel couvre la construction de circuits de LED dimmables utilisant les broches GPIO du Raspberry Pi,
en se concentrant sur la réalisation d'un contrôle fluide de la luminosité. Paul McQuarter démontre le processus étape par étape,
de la configuration du circuit à la mise en œuvre du codage. Dans la section Raspberry Pi, il explique comment construire le circuit en utilisant les broches GPIO et des boutons-poussoirs pour le contrôle,
accompagné de codage Python pour le contrôle PWM (Modulation de Largeur d'Impulsion).
La vidéo explore les subtilités du PWM,
en mettant l'accent sur les changements non linéaires du cycle de travail pour des transitions de luminosité plus douces et en abordant les problèmes de synchronisation entre la fréquence du PWM et le taux de balayage de la caméra.
La vidéo introduit le concept d'utilisation de l'échelle exponentielle pour obtenir un contrôle précis et fluide de la luminosité.
Elle plonge dans des concepts mathématiques comme les logarithmes et les exposants, illustrant leur application dans le codage pour le contrôle de la luminosité des LED.
Des conseils de dépannage sont fournis pour déboguer et affiner le code afin d'assurer des performances optimales.


1. **Configuration du circuit** : Explication et démonstration de la construction de circuits de LED dimmables avec les broches GPIO du Raspberry Pi, utilisant des boutons-poussoirs pour le contrôle.
2. **Codage Python** : Parcours du code Python pour la mise en œuvre du contrôle PWM et de l'échelle exponentielle pour le contrôle de la luminosité des LED, respectivement.
3. **Principes du PWM** : Compréhension du cycle de travail du PWM et son application dans le contrôle de la luminosité des LED.
4. **Échelle exponentielle** : Utilisation de l'échelle exponentielle dans le codage pour obtenir un contrôle de la luminosité doux et linéaire.
5. **Concept logarithmique** : Application des logarithmes pour déterminer la constante requise pour un nombre spécifique de pressions sur les boutons pour l'ajustement de la luminosité.
6. **Ajustement non linéaire de la luminosité** : Exploration des changements non linéaires du cycle de travail pour des transitions de luminosité plus douces.
7. **Problèmes de synchronisation** : Traitement des problèmes de synchronisation entre la fréquence du PWM et le taux de balayage de la caméra.
8. **Dépannage et affinement** : Techniques pour déboguer le code et affiner la fonctionnalité de gradation des LED pour des performances optimales.

**Vidéo**

.. raw:: html
    
    <iframe width="700" height="500" src="https://www.youtube.com/embed/2QAn1e8U5ho?si=1aWOugdV2_4pIO9N" title="Lecteur vidéo YouTube" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

