.. _cpn_adc0834:

ADC0834
==============

L'ADC0834 est un convertisseur analogique-numérique à approximation successive de 8 bits, équipé d'un multiplexeur multicanal configurable en entrée et d'une entrée/sortie série. L'entrée/sortie série est configurée pour interfacer avec des registres à décalage standard ou des microprocesseurs.

.. image:: img/image309.png

**Séquence de fonctionnement**

Une conversion est initiée en mettant CS à un niveau bas, ce qui active tous les circuits logiques.
CS doit être maintenu bas pendant tout le processus de conversion. Une horloge est ensuite reçue du
 processeur. À chaque transition du bas vers le haut de l'entrée d'horloge, les données sur DI sont
  horodatées dans le registre de décalage de l'adresse du multiplexeur. Le premier niveau haut 
  sur l'entrée est le bit de départ. Un mot d'attribution de 3 à 4 bits suit le bit de départ. 
  À chaque transition successive du bas vers le haut de l'entrée d'horloge, le bit de départ et 
  le mot d'attribution sont décalés dans le registre de décalage. Lorsque le bit de départ est 
  décalé dans la position de départ du registre du multiplexeur, le canal d'entrée est sélectionné 
  et la conversion commence. La sortie de l'état SAR (SARS) devient haute pour indiquer qu'une 
  conversion est en cours, et DI vers le registre de décalage du multiplexeur est désactivé pour 
  la durée de la conversion.

Un intervalle d'une période d'horloge est automatiquement inséré pour permettre au canal multiplexé 
sélectionné de se stabiliser. La sortie de données DO sort de l'état haute impédance et fournit un 
niveau bas initial pour cette période d'horloge de temps de stabilisation du multiplexeur. 
Le comparateur SAR compare les sorties successives de l'échelle résistive avec le signal analogique
entrant. La sortie du comparateur indique si l'entrée analogique est supérieure ou inférieure à 
la sortie de l'échelle résistive. À mesure que la conversion progresse, les données de conversion 
sont simultanément sorties par la broche de sortie DO, avec le bit de poids fort (MSB) en premier.

Après huit périodes d'horloge, la conversion est terminée et la sortie SARS devient basse. Enfin, 
les données sont sorties avec le bit de poids faible en premier après le flux de données avec le 
MSB en premier.

.. image:: img/image175.png

**TABLE DE LOGIQUE DE CONTRÔLE D'ADRESSE MUX DE L'ADC0834**

.. image:: img/image176.png

* `Fiche technique de la série ADC0831 <https://www.ti.com/lit/ds/symlink/adc0831-n.pdf>`_

**Exemple**

* :ref:`2.1.7_c` (Projet C)
* :ref:`2.2.1_c` (Projet C)
* :ref:`2.2.2_c` (Projet C)
* :ref:`3.1.4_c` (Projet C)
* :ref:`3.1.5_c` (Projet C)
* :ref:`3.1.7_c` (Projet C)
* :ref:`2.1.7_py` (Projet Python)
* :ref:`2.2.1_py` (Projet Python)
* :ref:`2.2.2_py` (Projet Python)
* :ref:`4.1.10_py` (Projet Python)
* :ref:`4.1.11_py` (Projet Python)
* :ref:`4.1.13_py` (Projet Python)
