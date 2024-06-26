.. _cpn_mfrc522:

Module MFRC522
=====================

**RFID**

La radio-identification (RFID) désigne les technologies qui impliquent l'utilisation de la 
communication sans fil entre un objet (ou tag) et un dispositif d'interrogation (ou lecteur) 
pour suivre et identifier automatiquement ces objets. La portée de transmission du tag est 
limitée à plusieurs mètres du lecteur. Une ligne de vue directe entre le lecteur et le tag n'est 
pas nécessaire.

La plupart des tags contiennent au moins un circuit intégré (IC) et une antenne. Le microprocesseur 
stocke les informations et est responsable de la gestion de la communication en radiofréquence (RF) 
avec le lecteur. Les tags passifs n'ont pas de source d'énergie indépendante et dépendent d'un signal 
électromagnétique externe, fourni par le lecteur, pour alimenter leurs opérations. Les tags actifs 
contiennent une source d'énergie indépendante, comme une batterie. Ainsi, ils peuvent avoir des 
capacités de traitement, de transmission et de portée accrues.

.. image:: img/image230.png

**MFRC522**

Le MFRC522 est un type de puce de lecture et d'écriture intégrée. Il est couramment utilisé dans 
les radios à 13,56 MHz. Lancé par la société NXP, c'est une puce de carte sans contact à faible 
tension, faible coût et petite taille, un excellent choix pour les instruments intelligents et les 
appareils portables.

Le MF RC522 utilise un concept avancé de modulation et de démodulation qui est pleinement présenté 
dans tous les types de méthodes et protocoles de communication sans contact passif à 13,56 MHz. 
De plus, il prend en charge l'algorithme de cryptage rapide CRYPTO1 pour vérifier les produits 
MIFARE. Le MFRC522 prend également en charge la série de communications sans contact haute vitesse 
MIFARE, avec un taux de transmission de données bidirectionnel allant jusqu'à 424 kbit/s. 
En tant que nouveau membre de la série de lecteurs de cartes hautement intégrés à 13,56 MHz, 
le MF RC522 est très similaire aux MF RC500 et MF RC530 existants mais présente également de 
grandes différences. Il communique avec l'ordinateur hôte via la manière série qui nécessite 
moins de câblage. Vous pouvez choisir entre les modes SPI, I2C et UART série (similaire à RS232), 
ce qui permet de réduire les connexions, d'économiser de l'espace sur la carte PCB (plus petite 
taille) et de réduire les coûts.

**Exemple**

* :ref:`2.2.10_c` (Projet C)
* :ref:`2.2.10_py` (Projet Python)
* :ref:`4.1.19_py` (Projet Python)
