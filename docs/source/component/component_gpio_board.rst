.. _cpn_gpio_extension_board:

Carte d'extension GPIO
==========================

Avant de commencer à apprendre les commandes, vous devez d'abord en savoir plus sur les broches du 
Raspberry Pi, ce qui est essentiel pour l'étude suivante.

Nous pouvons facilement connecter les broches du Raspberry Pi à une breadboard à l'aide de la carte 
d'extension GPIO pour éviter les dommages au GPIO causés par des branchements fréquents. Voici 
notre carte d'extension GPIO à 40 broches et le câble GPIO pour le Raspberry Pi modèle B+, modèle 2 B, 
modèle 3 et modèle 4 B.

.. image:: img/image32.png
    :align: center

**Numéro de broche**

Les broches du Raspberry Pi ont trois façons de les nommer : wiringPi, BCM et Board.

Parmi ces méthodes de nommage, la carte d'extension GPIO à 40 broches utilise la méthode de nommage BCM. Mais pour certaines broches spéciales, telles que le port I2C et le port SPI, elles utilisent le nom qui leur est propre.

Le tableau suivant nous montre les méthodes de nommage de WiringPi, Board et le nom intrinsèque de chaque broche sur la carte d'extension GPIO. Par exemple, pour le GPIO17, la méthode de nommage Board est 11, la méthode de nommage wiringPi est 0, et la méthode de nommage intrinsèque est GPIO0.

.. note::

    1) En langage C, ce qui est utilisé est la méthode de nommage WiringPi.
    
    2) En langage Python, les méthodes de nommage appliquées sont **Board** et **BCM**, et la fonction ``GPIO.setmode()`` est utilisée pour les définir.

    3) En Scratch 3 et Processing, la méthode de nommage appliquée est **BCM**.

.. image:: img/gpio_board.png