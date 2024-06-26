.. _install_wiringpi:

Installer et vérifier WiringPi
=======================================

``wiringPi`` est une bibliothèque GPIO en langage C appliquée au Raspberry Pi. Elle est conforme 
à la licence GUN Lv3. Les fonctions de wiringPi sont similaires à celles du système de câblage 
d'Arduino. Elles permettent aux utilisateurs familiers avec Arduino d'utiliser wiringPi plus 
facilement.

``wiringPi`` comprend de nombreuses commandes GPIO qui vous permettent de contrôler toutes sortes 
d'interfaces sur le Raspberry Pi.

Veuillez exécuter la commande suivante pour installer la bibliothèque ``wiringPi`` :

.. raw:: html

   <run></run>

.. code-block::

    sudo apt-get update
    git clone https://github.com/WiringPi/WiringPi
    cd WiringPi 
    ./build

Vous pouvez tester si la bibliothèque wiringPi est installée avec succès en utilisant l'instruction suivante :

.. raw:: html

   <run></run>

.. code-block::

    gpio -v

.. image:: ../img/image30.png

Vérifiez le GPIO avec la commande suivante :

.. raw:: html

   <run></run>

.. code-block::

    gpio readall

.. image:: ../img/image31.png

Pour plus de détails sur wiringPi, vous pouvez vous référer à `WiringPi <https://github.com/WiringPi/WiringPi>`_.
