.. _cpn_l293d:

L293D
=================

Le L293D est un pilote de moteur à 4 canaux intégré par une puce avec haute tension et courant élevé.
Il est conçu pour se connecter aux niveaux logiques DTL et TTL standard, et pour piloter des charges inductives (telles que des bobines de relais, des moteurs à courant continu, des moteurs pas à pas) et des transistors de commutation de puissance, etc.
Les moteurs à courant continu (DC) sont des dispositifs qui convertissent l'énergie électrique en énergie mécanique. Ils sont largement utilisés dans les entraînements électriques en raison de leurs excellentes performances de régulation de la vitesse.

Voir la figure des broches ci-dessous. Le L293D a deux broches (Vcc1 et Vcc2) pour l'alimentation.
Vcc2 est utilisé pour alimenter le moteur, tandis que Vcc1 alimente la puce. Puisqu'un petit moteur à courant continu est utilisé ici, connectez les deux broches à +5V.

.. image:: img/l293d111.png

Voici la structure interne du L293D.
La broche EN est une broche d'activation et ne fonctionne qu'avec un niveau haut ; A représente l'entrée et Y la sortie.
Vous pouvez voir la relation entre eux en bas à droite.
Lorsque la broche EN est au niveau haut, si A est haut, Y émet un niveau haut ; si A est bas, Y émet un niveau bas. Lorsque la broche EN est au niveau bas, le L293D ne fonctionne pas.

.. image:: img/l293d334.png

* `L293D Datasheet <https://www.ti.com/lit/ds/symlink/l293d.pdf?ts=1627004062301&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FL293D>`_

**Exemple**

* :ref:`1.3.1_c` (Projet C)
* :ref:`3.1.4_c` (Projet C)
* :ref:`1.3.1_py` (Projet Python)
* :ref:`4.1.10_py` (Projet Python)
* :ref:`1.17_scratch` (Projet Scratch)
