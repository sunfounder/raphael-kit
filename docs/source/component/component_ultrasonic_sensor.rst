.. _cpn_ultrasonic_sensor:

Module Ultrasonique
===========================

.. image:: img/ultrasonic_pic.png
    :width: 400
    :align: center

Le module de télémétrie ultrasonique offre une fonction de mesure sans contact de 2 cm à 400 cm, avec une précision de mesure pouvant atteindre 3 mm. 
Il peut assurer que le signal reste stable dans un rayon de 5 m, le signal s'affaiblissant progressivement après 5 m jusqu'à disparaître à 7 m.

Le module comprend des émetteurs ultrasoniques, un récepteur et un circuit de contrôle. Les principes de base sont les suivants :

#. Utilisez une bascule IO pour traiter un signal de niveau haut d'au moins 10 μs.

#. Le module envoie automatiquement huit impulsions de 40 kHz et détecte si un signal de retour est présent.

#. Si le signal revient, en passant par le niveau haut, la durée de sortie de l'IO haut correspond au temps écoulé entre l'émission de l'onde ultrasonique et son retour. La distance mesurée est alors calculée comme suit : distance = (temps haut x vitesse du son (340 m/s) / 2).

Le diagramme de chronométrage est présenté ci-dessous.

.. image:: img/ultrasonic228.png

Il suffit de fournir une courte impulsion de 10 μs à l'entrée du déclencheur pour démarrer la télémétrie, puis le module
enverra une rafale de 8 cycles d'ultrasons à 40 kHz et élèvera son
écho. Vous pouvez calculer la portée grâce à l'intervalle de temps entre
l'envoi du signal de déclenchement et la réception du signal d'écho.

Formule : μs / 58 = centimètres ou μs / 148 = pouces ; ou : la portée = temps du niveau haut \* vitesse (340 m/s) / 2 ; il est recommandé d'utiliser
un cycle de mesure supérieur à 60 ms afin de prévenir les collisions de
signal entre le signal de déclenchement et le signal d'écho.

**Exemple**

* :ref:`2.2.8_c` (Projet C)
* :ref:`3.1.3_c` (Projet C)
* :ref:`2.2.8_py` (Projet Python)
* :ref:`4.1.9_py` (Projet Python)

