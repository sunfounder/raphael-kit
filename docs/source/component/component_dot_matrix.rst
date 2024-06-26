.. _cpn_dot_matrix:

Module Matrice LED
==============================

.. image:: img/max7219_module.jpg
    :width: 400
    :align: center

Il s'agit d'un module matrice de points 8x8 à cathode commune piloté par le MAX7219. La tension de fonctionnement du module est de 5V, sa taille est de 50mmx32mmx15mm. Le côté gauche est le port d'entrée, le côté droit est le port de sortie, et il prend en charge la cascade de plusieurs modules.

* **VCC** : Tension d'alimentation positive. Connecter au +5V.
* **GND** : Masse (les deux broches GND doivent être connectées)
* **DIN** : Entrée de données série. Les données sont chargées dans le registre à décalage interne de 16 bits sur le front montant de CLK.
* **CS** : Entrée de sélection de la puce. Les données série sont chargées dans le registre à décalage lorsque CS est bas. Les 16 derniers bits de données série sont verrouillés sur le front montant de CS.
* **CLK** : Entrée d'horloge série. Taux maximum de 10MHz. Sur le front montant de CLK, les données sont décalées dans le registre à décalage interne. Sur le front descendant de CLK, les données sont sorties de DOUT. Sur le MAX7221, l'entrée CLK est active uniquement lorsque CS est bas.

**MAX7219**

Le MAX7219 est un pilote d'affichage à cathode commune compact, à entrée/sortie série, qui interface les microprocesseurs (µP) avec des affichages LED numériques à 7 segments de jusqu'à 8 chiffres, des affichages à barres ou 64 LED individuelles. Inclus sur la puce sont un décodeur BCD code-B, un circuit de balayage multiplex, des pilotes de segment et de chiffre, et une RAM statique 8x8 qui stocke chaque chiffre.

Une seule résistance externe est nécessaire pour régler le courant de segment pour toutes les LED. Le MAX7221 est compatible avec SPI™, QSPI™ et MICROWIRE™, et dispose de pilotes de segment à vitesse de balayage limitée pour réduire les EMI.

Une interface série pratique à 4 fils se connecte à tous les µP courants. Les chiffres individuels peuvent être adressés et mis à jour sans réécrire l'affichage entier. Les MAX7219/MAX7221 permettent également à l'utilisateur de sélectionner le décodage code-B ou sans décodage pour chaque chiffre.

.. image:: img/max7219_sche.png

* `MAX7219 Datasheet <https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf>`_

**Exemple**

* :ref:`1.1.6_c` (Projet C)
* :ref:`3.1.12_c` (Projet C)
* :ref:`1.1.6_py` (Projet Python)
* :ref:`4.1.19_py` (Projet Python)

