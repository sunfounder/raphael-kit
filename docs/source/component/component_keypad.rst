.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _cpn_keypad:

Clavier
========================

Un clavier est une matrice rectangulaire de 12 ou 16 boutons OFF-(ON). 
Leurs contacts sont accessibles via un connecteur adapté à une connexion avec un câble ruban ou une insertion dans un circuit imprimé. 
Dans certains claviers, chaque bouton se connecte à un contact séparé dans le connecteur, tandis que tous les boutons partagent une masse commune.

.. image:: img/keypad314.png

Le plus souvent, les boutons sont codés en matrice, ce qui signifie que chacun d'eux relie une paire unique de conducteurs dans une matrice. 
Cette configuration est adaptée à l'interrogation par un microcontrôleur, qui peut être programmé pour envoyer une impulsion de sortie à chacun des quatre fils horizontaux à tour de rôle. 
Pendant chaque impulsion, il vérifie les quatre fils verticaux restants en séquence pour déterminer lequel, le cas échéant, transporte un signal. 
Des résistances de pull-up ou pull-down doivent être ajoutées aux fils d'entrée pour éviter que les entrées du microcontrôleur ne se comportent de manière imprévisible en l'absence de signal.

**Exemple**

* :ref:`2.1.8_c` (Projet C)
* :ref:`3.1.8_c` (Projet C)
* :ref:`3.1.11_c` (Projet C)
* :ref:`2.1.8_py` (Projet Python)
* :ref:`4.1.14_py` (Projet Python)
* :ref:`4.1.17_py` (Projet Python)
