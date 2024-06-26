.. _cpn_74hc595:

74HC595
===========

.. image:: img/74HC595.png

Le 74HC595 est composé d'un registre à décalage de 8 bits et d'un registre de stockage avec des sorties parallèles à trois états. Il convertit l'entrée série en sortie parallèle afin d'économiser les ports d'E/S d'un MCU.
Lorsque MR (broche 10) est au niveau haut et OE (broche 13) est au niveau bas, les données sont entrées sur le front montant de SHcp et passent au registre de mémoire via le front montant de SHcp. Si les deux horloges sont connectées ensemble, le registre à décalage est toujours une impulsion en avance sur le registre de mémoire. Il y a une broche d'entrée de décalage série (Ds), une broche de sortie série (Q) et un bouton de réinitialisation asynchrone (niveau bas) dans le registre de mémoire. Le registre de mémoire produit un bus avec une sortie parallèle de 8 bits et en trois états. Lorsque OE est activé (niveau bas), les données du registre de mémoire sont envoyées sur le bus.

* `Fiche technique du 74HC595 <https://www.ti.com/lit/ds/symlink/cd74hc595.pdf?ts=1617341564801>`_

.. image:: img/74hc595_pin.png
    :width: 600

Broches du 74HC595 et leurs fonctions :

* **Q0-Q7** : Broches de sortie de données parallèles de 8 bits, capables de contrôler directement 8 LED ou 8 broches d'un affichage à 7 segments.
* **Q7’** : Broche de sortie en série, connectée à DS d'un autre 74HC595 pour connecter plusieurs 74HC595 en série.
* **MR** : Broche de réinitialisation, active au niveau bas ;
* **SHcp** : Entrée de séquence temporelle du registre à décalage. Sur le front montant, les données du registre à décalage se déplacent successivement d'un bit, c'est-à-dire que les données de Q1 passent à Q2, et ainsi de suite. Sur le front descendant, les données du registre à décalage restent inchangées.
* **STcp** : Entrée de séquence temporelle du registre de stockage. Sur le front montant, les données du registre à décalage passent dans le registre de mémoire.
* **CE** : Broche d'activation de sortie, active au niveau bas.
* **DS** : Broche d'entrée de données série.
* **VCC** : Tension d'alimentation positive.
* **GND** : Masse.

**Exemple**

* :ref:`1.1.4_c` (Projet C)
* :ref:`1.1.5_c` (Projet C)
* :ref:`3.1.1_c` (Projet C)
* :ref:`3.1.6_c` (Projet C)
* :ref:`3.1.12_c` (Projet C)
* :ref:`1.1.4_py` (Projet Python)
* :ref:`1.1.5_py` (Projet Python)
* :ref:`4.1.7_py` (Projet Python)
* :ref:`4.1.12_py` (Projet Python)
* :ref:`4.1.18_py` (Projet Python)
