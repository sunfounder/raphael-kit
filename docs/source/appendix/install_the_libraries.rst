 
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

**3. Sortie de l'environnement virtuel**

Lorsque vous avez terminé votre travail et souhaitez quitter l'environnement virtuel, exécutez simplement :

.. raw:: html

    <run></run>

.. code-block:: shell

    deactivate

Cela vous ramènera à l'environnement Python global du système.

**4. Suppression de l'environnement virtuel**

Si vous n'avez plus besoin d'un environnement virtuel particulier, vous pouvez simplement supprimer le répertoire contenant l'environnement virtuel :

.. raw:: html

    <run></run>

.. code-block:: shell

    rm -rf myenv


Luma.LED_Matrix
~~~~~~~~~~~~~~~~~~~~~~~

Il s'agit d'une bibliothèque Python 3 pour interfacer des affichages à matrice de LED en utilisant le pilote MAX7219 (via SPI), WS2812 (NeoPixels, y compris Pimoroni Unicorn pHat/Hat et Unicorn Hat HD), et APA102 (DotStar) sur Raspberry Pi et d'autres ordinateurs monocartes basés sur Linux.

#. Ajoutez l’utilisateur aux groupes ``spi`` et ``gpio`` pour vous assurer que l’utilisateur actuel (remplacez "pi" par votre propre nom d’utilisateur) a la permission d’accéder aux interfaces SPI et GPIO.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell

        sudo usermod -a -G spi,gpio pi

   Après avoir exécuté cette commande, il est recommandé de redémarrer le système ou de se déconnecter puis de se reconnecter pour appliquer les changements d’appartenance aux groupes.

#. Installez les dépendances nécessaires : Utilisez ``apt`` pour installer les outils de construction et les bibliothèques de développement associées. Ces bibliothèques sont essentielles pour compiler et installer certains paquets Python.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
    
        sudo apt update
        sudo apt install -y build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff-dev

#. Créez un environnement virtuel. Ici, ``~/my_env`` est le chemin de l’environnement virtuel, et il peut être personnalisé.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       python3 -m venv ~/my_env

#. Après avoir créé l’environnement virtuel, activez-le pour l’utiliser.

   .. note::
   
       Chaque fois que vous redémarrez le Raspberry Pi ou ouvrez un nouveau terminal, vous devrez exécuter la commande suivante à nouveau pour activer l’environnement virtuel.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       source ~/my_env/bin/activate
   
   Une fois l’environnement virtuel activé, vous verrez le nom de l’environnement avant l’invite de commande, indiquant que vous travaillez dans l’environnement virtuel.

#. Dans l’environnement virtuel, mettez à jour ``pip`` et ``setuptools`` pour vous assurer que les versions les plus récentes des paquets sont installées.
   
   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell

        pip install --upgrade pip setuptools

#. Ensuite, installez ``luma.led_matrix``:
   
   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell
   
        pip install luma.led_matrix

#. Après l'installation, vous pouvez vérifier que ``luma.led_matrix`` est correctement installé en exécutant la commande suivante. Si l’installation est réussie, elle affichera le numéro de version de ``luma.led_matrix``.
   
   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell

        python3 -c "import luma.led_matrix; print(luma.led_matrix.__version__)"

#. Lorsque vous avez terminé votre travail et que vous souhaitez quitter l’environnement virtuel, il vous suffit d’exécuter :
   
   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       deactivate

* Référence : `Luma.LED_Matrix <https://luma-led-matrix.readthedocs.io/en/latest/install.html>`_

.. _mfrc522_lib:

MFRC522
~~~~~~~~~~~~~~~~~~~~~~~~~~~

La bibliothèque ``spidev`` aide à gérer les interactions avec le SPI et est un composant clé de ce tutoriel car nous en avons besoin pour que le Raspberry Pi interagisse avec le RFID RC522.

Exécutez la commande suivante pour installer la bibliothèque MFRC522.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install mfrc522

La bibliothèque MFRC522 contient deux fichiers : ``MFRC522.py`` et ``SimpleMFRC522.py``. 

Parmi eux, ``MFRC522.py`` est la réalisation de l'interface RFID RC522, cette bibliothèque gère tout le travail complexe de communication avec le RFID via l'interface SPI du Pi.

``SimpleMFRC522.py`` prend le fichier ``MFRC522.py`` et le simplifie grandement en vous permettant de gérer seulement quelques fonctions au lieu de plusieurs fonctions.
