 
.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _install_the_libraries:

Installer les bibliothèques
==============================

Pour les utilisateurs C
---------------------------

BCM2835
~~~~~~~~~~~~~~~
Il s'agit d'une bibliothèque en C pour Raspberry Pi (RPi). Elle permet d'accéder aux fonctions GPIO et autres E/S sur la puce Broadcom BCM 2835, utilisée dans le Raspberry Pi, permettant ainsi l'accès aux broches GPIO sur la prise IDE à 26 broches de la carte RPi pour contrôler et interfacer divers dispositifs externes.

Elle fournit des fonctions pour lire les entrées numériques et définir les sorties numériques, utiliser SPI et I2C, et accéder aux minuteries du système. La détection d'événements sur les broches est prise en charge par le sondage (les interruptions ne sont pas prises en charge).

Fonctionne sur toutes les versions jusqu'à et y compris le RPI 4. Fonctionne avec toutes les versions de Debian jusqu'à et y compris Debian Buster 10.

Ouvrez un terminal et téléchargez la bibliothèque ``bcm2835`` vers le chemin ``~``.

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~
    wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.69.tar.gz

Décompressez le paquet.

.. raw:: html

   <run></run>

.. code-block:: 

    tar zxvf bcm2835-1.69.tar.gz

Installez la bibliothèque BCM2835 avec les commandes suivantes.

.. raw:: html

   <run></run>

.. code-block:: 

    cd bcm2835-1.69
    ./configure
    make
    sudo make check
    sudo make install

* Référence : `bcm2835 <http://www.airspayce.com/mikem/bcm2835/>`_  


Pour les utilisateurs Python
--------------------------------

.. _create_virtual:

Créer un environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lorsque vous utilisez Raspberry Pi ou des appareils similaires, il est recommandé d'installer les paquets avec ``pip`` dans un environnement virtuel. Cela offre une isolation des dépendances, augmente la sécurité du système, maintient la propreté du système, facilite la migration et le partage des projets, simplifiant ainsi la gestion des dépendances. Ces avantages font des environnements virtuels un outil extrêmement important et utile dans le développement Python.

Voici les étapes pour créer un environnement virtuel :

**1. Créer un environnement virtuel**

Tout d'abord, vous devez vous assurer que votre système a Python installé. Python version 3.3 et ultérieure est livré avec le module ``venv`` pour créer des environnements virtuels, éliminant ainsi le besoin d'une installation séparée. Si vous utilisez Python 2 ou une version antérieure à Python 3.3, vous devrez installer ``virtualenv``.

* Pour Python 3 :

Python 3.3 et les versions ultérieures peuvent utiliser directement le module ``venv`` :

.. raw:: html

    <run></run>

.. code-block:: shell

    python3 -m venv myenv

Cela créera un environnement virtuel nommé ``myenv`` dans le répertoire actuel.

* Pour Python 2 :

Si vous utilisez encore Python 2, vous devez d'abord installer ``virtualenv`` :

.. raw:: html

    <run></run>

.. code-block:: shell

    pip install virtualenv

Ensuite, créez un environnement virtuel :

.. raw:: html

    <run></run>

.. code-block:: shell

    virtualenv myenv

Cela crée également un environnement virtuel nommé ``myenv`` dans le répertoire actuel.

**2. Activation de l'environnement virtuel**

Après avoir créé l'environnement virtuel, vous devez l'activer pour l'utiliser.

.. note::

    Chaque fois que vous redémarrez le Raspberry Pi ou ouvrez un nouveau terminal, vous devrez exécuter la commande suivante à nouveau pour activer l'environnement virtuel.

.. raw:: html

    <run></run>

.. code-block:: shell

    source myenv/bin/activate

Une fois l'environnement virtuel activé, vous verrez le nom de l'environnement avant l'invite de commande, indiquant que vous travaillez dans l'environnement virtuel.


**3. Installation des dépendances**

Avec l'environnement virtuel activé, vous pouvez utiliser pip pour installer les dépendances requises. Par exemple :

.. raw:: html

    <run></run>

.. code-block:: shell

    pip install requests

Cela installera la bibliothèque requests dans l'environnement virtuel actuel, plutôt que dans l'environnement global. Cette étape ne doit être effectuée qu'une seule fois.


**4. Sortie de l'environnement virtuel**

Lorsque vous avez terminé votre travail et souhaitez quitter l'environnement virtuel, exécutez simplement :

.. raw:: html

    <run></run>

.. code-block:: shell

    deactivate

Cela vous ramènera à l'environnement Python global du système.

**5. Suppression de l'environnement virtuel**

Si vous n'avez plus besoin d'un environnement virtuel particulier, vous pouvez simplement supprimer le répertoire contenant l'environnement virtuel :

.. raw:: html

    <run></run>

.. code-block:: shell

    rm -rf myenv


Luma.LED_Matrix
~~~~~~~~~~~~~~~~~~~~~~~

Il s'agit d'une bibliothèque Python 3 pour interfacer des affichages de matrice LED avec le pilote MAX7219 (utilisant SPI), WS2812 (NeoPixels, y compris Pimoroni Unicorn pHat/Hat et Unicorn Hat HD) et APA102 (DotStar) sur le Raspberry Pi et d'autres ordinateurs monocartes basés sur Linux.

Installez d'abord les dépendances pour la bibliothèque avec :

.. raw:: html

   <run></run>

.. code-block:: 

    sudo usermod -a -G spi,gpio pi
    sudo apt install build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5

.. note:: warning

    Les versions par défaut de pip et setuptools fournies avec apt sur Raspbian sont vraiment anciennes, et peuvent empêcher l'installation correcte de certains composants. Assurez-vous qu'ils sont à jour en les mettant à niveau d'abord :

    .. raw:: html

       <run></run>

    .. code-block:: 

        sudo -H pip install --upgrade --ignore-installed pip setuptools

Procédez à l'installation de la dernière version de la bibliothèque luma.led_matrix directement depuis PyPI :

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 -m pip install --upgrade luma.led_matrix


* Référence : `Luma.LED_Matrix <https://luma-led-matrix.readthedocs.io/en/latest/install.html>`_

Spidev et MFRC522
~~~~~~~~~~~~~~~~~~~~~~~~~~~

La bibliothèque ``spidev`` aide à gérer les interactions avec le SPI et est un composant clé de ce tutoriel car nous en avons besoin pour que le Raspberry Pi interagisse avec le RFID RC522.

Exécutez la commande suivante pour installer ``spidev`` sur votre Raspberry Pi via ``pip``.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install spidev


Continuez à installer la bibliothèque MFRC522.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install mfrc522

La bibliothèque MFRC522 contient deux fichiers : ``MFRC522.py`` et ``SimpleMFRC522.py``. 

Parmi eux, ``MFRC522.py`` est la réalisation de l'interface RFID RC522, cette bibliothèque gère tout le travail complexe de communication avec le RFID via l'interface SPI du Pi.

``SimpleMFRC522.py`` prend le fichier ``MFRC522.py`` et le simplifie grandement en vous permettant de gérer seulement quelques fonctions au lieu de plusieurs fonctions.
