.. note::

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! 
    Plongez plus profondément dans l’univers Raspberry Pi, Arduino et ESP32 avec d’autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d’experts** : Résolvez les problèmes après‑vente et les défis techniques avec l’aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Obtenez un accès anticipé aux annonces de nouveaux produits et aux avant‑premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions et concours festifs** : Participez à des concours et promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez‑nous dès aujourd’hui !

.. _bk_start_py:

Démarrage avec Blynk
=====================

Vous allez apprendre à utiliser **Blynk** dans ce projet.

Lorsque vous déclenchez des widgets sur Blynk, votre Raspberry Pi affichera leurs valeurs.

Suivez les étapes ci‑dessous, en respectant l’ordre sans sauter de chapitres.

1. Configuration de Blynk
-------------------------

1. Allez sur `BLYNK <https://blynk.io/>`_ et cliquez sur **START FREE**. 

    .. image:: img/sp220607_142551.png

#. Renseignez votre adresse e‑mail pour enregistrer un compte.

    .. image:: img/sp220607_142807.png

#. Allez dans votre messagerie pour compléter l’enregistrement de votre compte.

    .. image:: img/sp220607_142936.png

#. Ensuite, **Blynk Tour** apparaîtra ; vous pouvez le lire pour apprendre les informations de base sur Blynk.

    .. image:: img/sp220607_143244.png

#. Nous devons maintenant créer un modèle et un appareil, cliquez sur **Cancel**.

    .. image:: img/sp220607_143608.png

#. Allez dans **Developer Zone** depuis la barre de navigation.

    .. image:: img/develop_zone.png

#. Créez un nouveau modèle (**New Template**).

    .. image:: img/new_template.png

#. Renseignez **NAME** (nom libre), et sélectionnez **HARDWARE** sur **Raspberry Pi**. Puis cliquez sur **Done**.

    .. image:: img/sp220913_170402.png

#. Vous serez redirigé vers la page **Info**, cliquez simplement sur **Save** en haut à droite.

    .. image:: img/sp220913_171202.png

#. Allez sur la page **Devices** depuis la barre de navigation.

    .. image:: img/devices.jpg

#. Créez un nouvel appareil (**New Device**).

    .. image:: img/new_devices.png

#. Choisissez **From template**.

    .. image:: img/create_new_device.png

#. Sélectionnez **TEMPLATE** comme celui que vous venez de définir, personnalisez **DEVICE NAME**, puis cliquez sur **Create**.

    .. image:: img/sp220913_173507.png

#. Vous devriez maintenant voir une page similaire à celle‑ci, ce qui signifie que votre configuration initiale de Blynk est terminée.

    .. image:: img/my_device.png


2. Éditer le tableau de bord (Dashboard)
-----------------------------------------

1. Cliquez sur **Edit Dashboard**.

    .. image:: img/edit_dashboard.png

#. Glissez les widgets de contrôle (**CONTROL Widgets**) que vous souhaitez sur le tableau de bord. Par exemple, un **Switch** et un **Slider**.

    .. image:: img/sp220913_180725.png

#. Appuyez sur l’icône des paramètres du widget.

    .. image:: img/sp220913_180806.png

#. Créez un flux de données (**Datastream**), sélectionnez **Virtual Pin**.

    .. image:: img/sp220913_180906.png

#. Terminez la configuration du flux de données.  
   Exemple pour un Switch : sélectionnez **DATA TYPE** sur ``Integer``, définissez **MIN** et **MAX** sur ``0`` et ``1``.  
   Cliquez sur **Create**, puis sur **Save**.

    .. image:: img/sp220913_181113.png

#. Répétez les mêmes étapes pour créer un flux de données pour le **Slider**, en définissant **DATA TYPE**, **MIN** et **MAX** selon vos besoins.

    .. image:: img/sp220913_182042.png

#. Une fois terminé, cliquez sur **Save And Apply** en haut à droite.

    .. image:: img/sp220913_182300.png


3. Installer la bibliothèque Blynk
-----------------------------------

Exécutez la commande suivante pour installer la bibliothèque.

.. raw:: html

   <run></run>

.. code-block::

    cd ~
    git clone https://github.com/vshymanskyy/blynk-library-python.git
    cd blynk-library-python
    sudo python3 setup.py


4. Télécharger les exemples
----------------------------

Nous avons fourni quelques exemples. Exécutez la commande suivante pour les télécharger.

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~
    git clone https://github.com/sunfounder/blynk-raspberrypi-python.git


5. Exécuter le code
--------------------

1. Accédez à la page **Device Info** sur Blynk, et copiez le **BLYNK_AUTH_TOKEN** situé sous **FIRMWARE CONFIGURATION**.

    .. image:: img/sp220913_182456.png

2. Éditez le code.

.. raw:: html

    <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_start.py

3. Recherchez la ligne ci‑dessous et collez votre ``BLYNK_AUTH_TOKEN``.

.. code-block:: 

    BLYNK_AUTH = 'YourAuthToken'

4. Exécutez le code.

.. raw:: html

    <run></run>

.. code-block:: 

    sudo python3 blynk_start.py

5. Allez sur Blynk et manipulez les widgets du tableau de bord.

    .. image:: img/sp220913_183529.png

6. Vous verrez maintenant vos actions s’afficher dans le terminal.

.. code-block:: 

    ..
       ___  __          __
      / _ )/ /_ _____  / /__
     / _  / / // / _ \/  '_/
    /____/_/\_, /_//_/_/\_\
            /___/ for Python v1.0.0 (linux)

    Connecting to blynk.cloud:443...
    Blynk ready. Ping: 142 ms
    V0 value: ['1']
    V0 value: ['0']
    V1 value: ['3']
    V1 value: ['8']
    V0 value: ['1']
