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
==========================

Pour les utilisateurs C
------------------------

BCM2835
~~~~~~~~~~~~~~~
Il s’agit d’une bibliothèque C pour Raspberry Pi (RPi). Elle fournit un accès aux GPIO et à d’autres fonctions d’E/S du circuit Broadcom BCM2835, tel qu’utilisé dans le Raspberry Pi, permettant l’accès aux broches GPIO du connecteur IDE à 26 broches de la carte RPi afin de contrôler et d’interfacer divers dispositifs externes.

Elle fournit des fonctions pour lire des entrées numériques et définir des sorties numériques, utiliser SPI et I2C, ainsi que pour accéder aux temporisateurs système. La détection d’événements sur les broches est prise en charge par interrogation (les interruptions ne sont pas prises en charge).

Fonctionne sur toutes les versions jusqu’à et y compris le RPi 4. Compatible avec toutes les versions de Debian jusqu’à et y compris Debian Buster 10.


Ouvrez un terminal et téléchargez la bibliothèque ``bcm2835`` dans le répertoire ``~``.

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

Installez la bibliothèque BCM2835 à l’aide des commandes suivantes.

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
-----------------------------

.. _create_virtual:

Création d’un environnement virtuel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lors de l’utilisation d’un Raspberry Pi ou de dispositifs similaires, il est recommandé d’installer les paquets avec ``pip`` dans un environnement virtuel. Cela permet l’isolation des dépendances, améliore la sécurité du système, maintient la propreté du système et facilite la migration et le partage des projets, simplifiant ainsi la gestion des dépendances. Ces avantages font des environnements virtuels un outil extrêmement important et utile dans le développement Python.

Voici les étapes pour créer un environnement virtuel :

**1. Créer un environnement virtuel**

Tout d’abord, vous devez vous assurer que Python est installé sur votre système. Les versions Python 3.3 et ultérieures incluent le module ``venv`` pour créer des environnements virtuels, éliminant le besoin d’une installation séparée. Si vous utilisez Python 2 ou une version antérieure à Python 3.3, vous devrez installer ``virtualenv``.

* Pour Python 3 :

Les versions Python 3.3 et ultérieures peuvent utiliser directement le module ``venv`` :

.. raw:: html

    <run></run>

.. code-block:: shell

    python3 -m venv myenv

Cela créera un environnement virtuel nommé ``myenv`` dans le répertoire courant.

* Pour Python 2 :

Si vous utilisez encore Python 2, vous devez d’abord installer ``virtualenv`` :

.. raw:: html

    <run></run>

.. code-block:: shell

    pip install virtualenv

Ensuite, créez un environnement virtuel :

.. raw:: html

    <run></run>

.. code-block:: shell

    virtualenv myenv

Cela crée également un environnement virtuel nommé ``myenv`` dans le répertoire courant.

**2. Activer l’environnement virtuel**

Après avoir créé l’environnement virtuel, vous devez l’activer pour l’utiliser.

.. note::

    Chaque fois que vous redémarrez le Raspberry Pi ou ouvrez un nouveau terminal, vous devrez exécuter à nouveau la commande suivante pour activer l’environnement virtuel.

.. raw:: html

    <run></run>

.. code-block:: shell

    source myenv/bin/activate

Une fois l’environnement virtuel activé, vous verrez le nom de l’environnement apparaître avant l’invite de commande, indiquant que vous travaillez dans l’environnement virtuel.


**3. Quitter l’environnement virtuel**

Lorsque vous avez terminé votre travail et souhaitez quitter l’environnement virtuel, exécutez simplement :

.. raw:: html

    <run></run>

.. code-block:: shell

    deactivate

Cela vous ramènera à l’environnement Python global du système.

**4. Supprimer l’environnement virtuel**

Si vous n’avez plus besoin d’un environnement virtuel particulier, vous pouvez simplement supprimer le répertoire contenant l’environnement virtuel :

.. raw:: html

    <run></run>

.. code-block:: shell

    rm -rf myenv

.. _install_luma_led_matrix:

Luma.LED_Matrix
~~~~~~~~~~~~~~~~~~~~~~~

Il s’agit d’une bibliothèque Python 3 permettant d’interfacer des matrices de LED utilisant le pilote MAX7219 (via SPI), des WS2812 (NeoPixels, y compris Pimoroni Unicorn pHat/Hat et Unicorn Hat HD) et des APA102 (DotStar) sur le Raspberry Pi et d’autres ordinateurs monocarte fonctionnant sous Linux.

#. Ajoutez l’utilisateur aux groupes ``spi`` et ``gpio`` afin de garantir que l’utilisateur courant (remplacez « pi » par votre propre nom d’utilisateur) dispose des autorisations nécessaires pour accéder aux interfaces SPI et GPIO.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell

        sudo usermod -a -G spi,gpio pi

   Après l’exécution de cette commande, il est recommandé de redémarrer le système ou de se déconnecter puis se reconnecter afin que les modifications d’appartenance aux groupes prennent effet.

#. Installez les dépendances nécessaires : utilisez ``apt`` pour installer les outils de compilation et les bibliothèques de développement associées. Ces bibliothèques sont indispensables pour compiler et installer certains paquets Python.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell

        sudo apt update
        sudo apt install -y build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff-dev

#. Créez un environnement virtuel. Ici, ``~/my_env`` correspond au chemin de l’environnement virtuel et peut être personnalisé.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       python3 -m venv ~/my_env


#. Après avoir créé l’environnement virtuel, activez-le pour l’utiliser.

   .. note::
   
       Chaque fois que vous redémarrez le Raspberry Pi ou ouvrez un nouveau terminal, vous devrez exécuter à nouveau la commande suivante pour activer l’environnement virtuel.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       source ~/my_env/bin/activate

   Une fois l’environnement virtuel activé, vous verrez le nom de l’environnement apparaître avant l’invite de commande, indiquant que vous travaillez dans l’environnement virtuel.

#. À l’intérieur de l’environnement virtuel, mettez à niveau ``pip`` et ``setuptools`` afin de garantir l’installation des versions les plus récentes des paquets.

   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell

      pip install --upgrade pip setuptools


#. Ensuite, installez ``luma.led_matrix`` :

   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell
   
     pip install luma.led_matrix

#. Après l’installation, vous pouvez vérifier que ``luma.led_matrix`` est correctement installé en exécutant la commande suivante. En cas de succès, le numéro de version de ``luma.led_matrix`` sera affiché.

   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell

        python3 -c "import luma.led_matrix; print(luma.led_matrix.__version__)"

#. Lorsque vous avez terminé votre travail et souhaitez quitter l’environnement virtuel, exécutez simplement :

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       deactivate


* Référence : `Luma.LED_Matrix <https://luma-led-matrix.readthedocs.io/en/latest/install.html>`_

.. .. _install_mfrc522:

.. MFRC522
.. ~~~~~~~~~~~~~~~~~

.. Exécutez la commande suivante pour installer la bibliothèque MFRC522.

.. .. raw:: html

..    <run></run>

.. .. code-block::

..     sudo pip3 install mfrc522

.. La bibliothèque MFRC522 contient deux fichiers : ``MFRC522.py`` et ``SimpleMFRC522.py``. 

.. Parmi eux, ``MFRC522.py`` implémente l’interface RFID RC522 ; cette bibliothèque gère tout le travail complexe de communication avec le RFID via l’interface SPI du Raspberry Pi.

.. ``SimpleMFRC522.py`` s’appuie sur le fichier ``MFRC522.py`` et le simplifie considérablement en vous permettant de n’utiliser que quelques fonctions au lieu d’un ensemble plus complexe de fonctions.
