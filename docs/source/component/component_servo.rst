.. _cpn_servo:

Servo
===========

.. image:: img/servo.png
    :align: center

Un servo est généralement composé des parties suivantes : boîtier, arbre, système d'engrenages, potentiomètre, moteur à courant continu et carte embarquée.

Voici comment cela fonctionne : Le microcontrôleur envoie des signaux PWM au servo, puis la carte embarquée dans le servo reçoit les signaux via la broche de signal et contrôle le moteur interne pour tourner. En conséquence, le moteur entraîne le système d'engrenages et motive ensuite l'arbre après la réduction de vitesse. L'arbre et le potentiomètre du servo sont connectés ensemble. Lorsque l'arbre tourne, il entraîne le potentiomètre, donc le potentiomètre envoie un signal de tension à la carte embarquée. Ensuite, la carte détermine la direction et la vitesse de rotation en fonction de la position actuelle, de sorte qu'elle puisse s'arrêter exactement à la position définie et s'y maintenir.

.. image:: img/servo_internal.png
    :align: center

L'angle est déterminé par la durée d'une impulsion appliquée au fil de commande. Cela s'appelle la modulation de largeur d'impulsion (PWM). Le servo s'attend à voir une impulsion toutes les 20 ms. La longueur de l'impulsion détermine jusqu'où le moteur tourne. Par exemple, une impulsion de 1,5 ms fera tourner le moteur à la position de 90 degrés (position neutre).
Lorsqu'une impulsion est envoyée à un servo qui est inférieure à 1,5 ms, le servo tourne vers une position et maintient son arbre de sortie à un certain nombre de degrés dans le sens antihoraire par rapport au point neutre. Lorsque l'impulsion est plus large que 1,5 ms, l'effet inverse se produit. La largeur minimale et maximale de l'impulsion qui commandera le servo à tourner vers une position valide est fonction de chaque servo. Généralement, l'impulsion minimale sera d'environ 0,5 ms de large et l'impulsion maximale sera de 2,5 ms de large.

.. image:: img/servo_duty.png
    :width: 600
    :align: center

**Exemple**

* :ref:`1.3.2_c` (Projet C)
* :ref:`3.1.2_c` (Projet C)
* :ref:`1.3.2_py` (Projet Python)
* :ref:`4.1.8_py` (Projet Python)
