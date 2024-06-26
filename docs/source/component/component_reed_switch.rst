.. _cpn_reed_switch:

Module Interrupteur à Lame Relevable
==========================================

.. image:: img/reed_switch.png
    :width: 300
    :align: center

* Utilisation d'un interrupteur à lame normalement ouvert.
* Sortie du comparateur, signal propre, bonne forme d'onde, capacité de pilotage puissante, plus de 15mA.
* Tension de fonctionnement : 3.3V-5V.
* Forme de sortie : sortie de commutateur numérique (0 et 1).
* Avec des trous de boulons fixes pour une installation facile.
* Taille de la carte PCB : 3.2cm x 1.4cm.
* Utilisation d'un comparateur LM393 à large tension.

Le module interrupteur à lame se compose d'un interrupteur à lame, d'un potentiomètre, d'un comparateur LM393, d'une LED, etc. Le circuit interne est illustré ci-dessous. Lorsque l'aimant est proche du module, il s'allume et le module sort un niveau bas ; lorsqu'il n'y a pas de magnétisme, il s'éteint et sort un niveau haut. La distance d'induction entre l'interrupteur à lame et l'aimant doit être inférieure à 1,5 cm ; au-delà, il ne sera pas sensible ou ne déclenchera pas. Vous pouvez également ajuster la sensibilité via le potentiomètre sur le module.
    
.. image:: img/reedswitch_sche.jpg
    :width: 600
    :align: center

L'interrupteur à lame, également connu sous le nom d'interrupteur magnétique ou interrupteur à lames.

Il contient deux lames métalliques internes, scellées dans un tube en verre rempli de gaz inerte. Normalement, les deux lames se chevauchent mais sont séparées par un écart, et le circuit est ouvert. Lorsqu'un objet magnétique s'approche, les deux lames produisent une attraction magnétique mutuelle, se rapprochent et le circuit se ferme. Par conséquent, l'interrupteur à lame peut être utilisé comme capteur magnétique.
        
.. image:: img/HowItWorksReed.jpg

**Exemple**

* :ref:`2.2.4_c` (Projet C)
* :ref:`2.2.4_py` (Projet Python)
* :ref:`4.1.6_py` (Projet Python)
* :ref:`1.6_scratch` (Projet Scratch)

