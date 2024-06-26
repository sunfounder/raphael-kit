.. _cpn_diode:

Diode
=================

Une diode est un composant électronique avec deux électrodes. Elle permet au courant de circuler dans une seule direction, ce que l'on appelle souvent la fonction de "redressement".
Ainsi, une diode peut être considérée comme une version électronique d'un clapet anti-retour.

En raison de sa conductivité unidirectionnelle, la diode est utilisée dans presque tous les circuits électroniques de complexité moyenne à élevée. C'est l'un des premiers dispositifs à semi-conducteurs et elle a de nombreuses applications.

Selon son utilisation, elle peut être divisée en diodes détectrices, diodes redresseuses, diodes limiteuses, diodes régulatrices de tension, etc.

Des diodes redresseuses et des diodes régulatrices de tension sont incluses dans ce kit.

**Diode Redresseuse**

.. image:: img/in4007_diode.png
.. image:: img/symbol_rectifier_diode.png
    :width: 200

Une diode redresseuse est une diode à semi-conducteur, utilisée pour redresser le courant alternatif (CA) en courant continu (CC) à l'aide de l'application de pont de redressement. L'alternative de la diode redresseuse par la barrière Schottky est principalement valorisée dans l'électronique numérique. Cette diode est capable de conduire des valeurs de courant allant de mA à quelques kA et des tensions allant jusqu'à quelques kV.

Les diodes redresseuses sont conçues avec du silicium et sont capables de conduire des valeurs élevées de courant électrique. Ces diodes sont également fabriquées à base de germanium ou d'arséniure de gallium. Les diodes Ge ont une tension de seuil plus faible que les diodes Si lorsqu'elles fonctionnent en polarisation directe, mais elles supportent moins bien les tensions inverses et les températures de jonction élevées.

* `1N400x general-purpose diode - Wikipedia <https://en.wikipedia.org/wiki/1N400x_general-purpose_diode>`_

**Diode Zener**

Une diode Zener est un type spécial de diode conçue pour permettre de manière fiable au courant de circuler "à l'envers" lorsqu'une tension de seuil inverse spécifique, appelée tension Zener, est atteinte.

Cette diode est un dispositif à semi-conducteur qui présente une très haute résistance jusqu'à la tension critique de claquage inverse. À ce point de claquage critique, la résistance inverse est réduite à une valeur très faible, et le courant augmente tandis que la tension reste constante dans cette région de faible résistance.

.. image:: img/zener_diode.png
.. image:: img/symbol-zener-diode.jpg

* `Zener diode - Wikipedia <https://en.wikipedia.org/wiki/Zener_diode>`_

**Exemple**

* :ref:`1.3.3_c` (Projet C)
* :ref:`1.3.3_py` (Projet Python)
