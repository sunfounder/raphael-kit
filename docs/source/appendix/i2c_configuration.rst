.. _i2c_config:

Configuration I2C
====================

**Étape 1** : Activez le port I2C de votre Raspberry Pi (Si vous l'avez
déjà activé, passez cette étape ; si vous ne savez pas si cela a été fait,
veuillez continuer).

.. raw:: html

   <run></run>
 
.. code-block:: 

    sudo raspi-config

**3 Options d'interfaçage**

.. image:: img/image282.png
    :align: center

**P5 I2C**

.. image:: img/image283.png
    :align: center

**<Yes>, then <Ok> -> <Finish>**

.. image:: img/image284.png
    :align: center

**Étape 2** : Vérifiez si les modules i2c sont chargés et actifs.

.. raw:: html

   <run></run>
 
.. code-block:: 

    lsmod | grep i2c

Ensuite, les codes suivants apparaîtront (les numéros peuvent être différents), s'ils n'apparaissent pas, veuillez redémarrer le Raspberry Pi avec ``sudo reboot``.

.. code-block:: 

    i2c_dev                     6276    0
    i2c_bcm2708                 4121    0

**Étape 3** : Installez i2c-tools.

.. raw:: html

   <run></run>
 
.. code-block:: 

    sudo apt-get install i2c-tools

**Étape 4** : Vérifiez l'adresse du périphérique I2C.

.. raw:: html

   <run></run>
  
.. code-block:: 

    i2cdetect -y 1      # Pour Raspberry Pi 2 et versions ultérieures

.. raw:: html

   <run></run>
 
.. code-block:: 

    i2cdetect -y 0      # Pour Raspberry Pi 1


.. code-block:: 

    pi@raspberrypi ~ $ i2cdetect -y 1
        0  1  2  3   4  5  6  7  8  9   a  b  c  d  e  f
    00:           -- -- -- -- -- -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    40: -- -- -- -- -- -- -- -- 48 -- -- -- -- -- -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- -- --

Si un périphérique I2C est connecté, l'adresse du périphérique sera affichée.

**Étape 5 :**

**Pour les utilisateurs de langage C :** Installez libi2c-dev.

.. raw:: html

   <run></run>
 
.. code-block:: 

    sudo apt-get install libi2c-dev 

**Pour les utilisateurs de Python :**

1. Activation de l'environnement virtuel.

.. note::
    
    * Avant l'activation, vous devez vous assurer que vous avez créé un environnement virtuel, veuillez consulter : :ref:`create_virtual`.

    * Chaque fois que vous redémarrez le Raspberry Pi, ou que vous ouvrez un nouveau terminal, vous devrez exécuter la commande suivante à nouveau pour activer l'environnement virtuel.

.. raw:: html

    <run></run>

.. code-block:: shell

    source myenv/bin/activate

Une fois l'environnement virtuel activé, vous verrez le nom de l'environnement avant l'invite de commande, indiquant que vous travaillez dans l'environnement virtuel.


2. Installez smbus pour I2C.

.. raw:: html

    <run></run>
 
.. code-block:: 

    sudo pip3 install smbus2


3. Sortie de l'environnement virtuel.

Lorsque vous avez terminé votre travail et souhaitez quitter l'environnement virtuel, exécutez simplement :

.. raw:: html

    <run></run>

.. code-block:: shell

    deactivate

Cela vous ramènera à l'environnement Python global du système.
