.. _cpn_led:

LED
==========

.. image:: img/LED.png
    :width: 400

Une diode électroluminescente (LED) est un type de composant qui peut convertir l'énergie électrique en énergie lumineuse via des jonctions PN. En fonction de la longueur d'onde, elle peut être catégorisée en diode laser, diode électroluminescente infrarouge et diode électroluminescente visible, généralement connue sous le nom de LED.

La diode a une conductivité unidirectionnelle, donc le flux de courant suivra la direction indiquée par la flèche dans le symbole du circuit. Vous ne pouvez fournir une alimentation positive qu'à l'anode et une alimentation négative à la cathode. Ainsi, la LED s'allumera.

.. image:: img/led_symbol.png

Une LED a deux broches. La plus longue est l'anode et la plus courte est la cathode. Faites attention à ne pas les connecter à l'envers. Il y a une chute de tension directe fixe dans la LED, elle ne peut donc pas être connectée directement au circuit car la tension d'alimentation peut dépasser cette chute et provoquer la brûlure de la LED. La tension directe des LED rouge, jaune et verte est de 1,8 V et celle de la LED blanche est de 2,6 V. La plupart des LED peuvent supporter un courant maximum de 20 mA, nous devons donc connecter une résistance de limitation de courant en série.

La formule de la valeur de la résistance est la suivante :

    R = (Vsupply – VD)/I

**R** représente la valeur de la résistance de limitation de courant, **Vsupply** la tension d'alimentation, **VD** la chute de tension et **I** le courant de fonctionnement de la LED.

Voici une introduction détaillée pour la LED : `LED - Wikipédia <https://en.wikipedia.org/wiki/Light-emitting_diode>`_.

**Exemple**

* :ref:`1.1.1_c` (Projet C)
* :ref:`3.1.6_c` (Projet C)
* :ref:`1.1.1_py` (Projet Python)
* :ref:`4.1.12_py` (Projet Python)
* :ref:`1.1_scratch` (Projet Scratch)

