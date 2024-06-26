 
.. _bk_start_py:

Commencer avec Blynk
===========================

Vous apprendrez à utiliser Blynk dans ce projet.

Lorsque vous déclenchez des widgets sur Blynk, votre Raspberry Pi imprimera leurs valeurs.

Suivez les étapes ci-dessous, et notez que vous devez les faire dans l'ordre sans sauter de chapitres.

1. Configuration de Blynk
----------------------------

1. Allez sur `BLYNK <https://blynk.io/>`_ et cliquez sur **START FREE**. 

    .. image:: img/sp220607_142551.png

2. Remplissez votre adresse e-mail pour créer un compte.

    .. image:: img/sp220607_142807.png

3. Consultez votre adresse e-mail pour finaliser l'enregistrement de votre compte.

    .. image:: img/sp220607_142936.png

4. Ensuite, **Blynk Tour** apparaîtra et vous pourrez le lire pour apprendre les informations de base sur Blynk.

    .. image:: img/sp220607_143244.png

5. Ensuite, nous devons créer un modèle et un appareil, cliquez sur **Cancel**.

    .. image:: img/sp220607_143608.png

6. Allez dans Template depuis la barre de navigation.

    .. image:: img/sp220913_170029.png

7. Créez un nouveau modèle

    .. image:: img/sp220913_170206.png

8. Remplissez le **NOM**, à votre convenance ; **HARDWARE** doit être **Raspberry Pi**. Puis cliquez sur **Done**.

    .. image:: img/sp220913_170402.png

9. Vous serez redirigé vers la page Info, cliquez simplement sur enregistrer en haut à droite.

    .. image:: img/sp220913_171202.png

10. Allez sur la page **Search** depuis la barre de navigation.

    .. image:: img/sp220913_172727.png

11. Créez un nouvel appareil.

    .. image:: img/sp220913_173259.png

12. À partir du modèle.

    .. image:: img/sp220913_173350.png

13. Sélectionnez **TEMPLATE** comme celui que vous venez de définir, **DEVICE NAME** peut être personnalisé. Puis cliquez sur **Create**.

    .. image:: img/sp220913_173507.png

14. Vous devriez maintenant voir une page comme celle-ci, ce qui signifie que votre configuration initiale de Blynk est terminée.

    .. image:: img/sp220913_173950.png

2. Modifier le tableau de bord
-----------------------------------

1. Cliquez sur l'icône du menu en haut à droite et sélectionnez "modifier le tableau de bord".

    .. image:: img/sp220913_180231.png

2. Faites glisser les Widgets de CONTRÔLE que vous souhaitez sur le tableau de bord. J'ai glissé un interrupteur et un curseur.

    .. image:: img/sp220913_180725.png

3. Appuyez sur l'icône de réglage du widget.

    .. image:: img/sp220913_180806.png

4. Créez un flux de données (Datastream), sélectionnez "Virtual Pin".

    .. image:: img/sp220913_180906.png

5. Complétez la configuration du flux de données. Ici, un flux de données a été créé pour l'interrupteur, donc **TYPE DE DONNÉES** sélectionnez ``Interger``, **MIN** et **MAX** réglez sur ``0`` et ``1``. Créez et enregistrez.

    .. image:: img/sp220913_181113.png

6. Utilisez les mêmes étapes pour créer un flux de données pour le widget curseur, et modifiez à nouveau **TYPE DE DONNÉES**, **MIN** et **MAX** selon vos besoins.

    .. image:: img/sp220913_182042.png

7. Lorsque vous avez terminé, cliquez sur "Enregistrer et appliquer" en haut à droite.

    .. image:: img/sp220913_182300.png

3. Installer la bibliothèque Blynk
--------------------------------------

Exécutez la commande suivante pour installer.

.. raw:: html

   <run></run>

.. code-block::

    cd ~
    git clone https://github.com/vshymanskyy/blynk-library-python.git
    cd blynk-library-python
    sudo python3 setup.py

4. Télécharger l'exemple
---------------------------

Nous avons fourni quelques exemples, veuillez exécuter la commande suivante pour les télécharger.

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~
    git clone https://github.com/sunfounder/blynk-raspberrypi-python.git

5. Exécuter le code
----------------------

1. Allez sur la page d'informations de l'appareil Blynk, vous verrez des informations sous **CONFIGURATION DU MICROLOGICIEL**, vous devez copier **BLYNK_AUTH_TOKEN**.

    .. image:: img/sp220913_182456.png

2. Modifiez le code.

.. raw:: html

    <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_start.py

3. Trouvez la ligne ci-dessous et collez votre ``BLYNK_AUTH_TOKEN``.

.. code-block:: 

    BLYNK_AUTH = 'YourAuthToken'

4. Exécutez le code.

.. raw:: html

    <run></run>

.. code-block:: 

    sudo python3 blynk_start.py

5. Allez sur Blynk, et utilisez le widget sur le tableau de bord.

    .. image:: img/sp220913_183529.png

6. Maintenant, vous pourrez voir vos actions sur le terminal.

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







