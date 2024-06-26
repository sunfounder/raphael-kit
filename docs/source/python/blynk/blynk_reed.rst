 
.. _blynk_reed_py:

Capteur de Porte et Fenêtre
===============================

Quand vous êtes à l'extérieur, vous vous êtes probablement déjà demandé : "Est-ce que les portes et fenêtres de ma maison sont bien fermées ?"

Pour résoudre ce problème, dans ce projet, nous allons construire un capteur de porte et fenêtre avec un interrupteur Reed et des aimants.

Installez ce capteur et cet aimant de chaque côté de la porte ou de la fenêtre. Vous pourrez vérifier si vos portes et fenêtres sont fermées ou non depuis l'application Blynk sur votre téléphone.

.. note:: Avant de commencer ce projet, nous vous recommandons de compléter :ref:`bk_start_py`. Cela vous donnera une compréhension claire de Blynk.

**Composants Nécessaires**

Dans ce projet, nous avons besoin des composants suivants. 

Il est certainement pratique d'acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ARTICLES DANS CE KIT
        - LIEN
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

Vous pouvez également les acheter séparément à partir des liens ci-dessous.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUCTION DES COMPOSANTS
        - LIEN D'ACHAT

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_reed_switch`
        - |link_reed_switch_buy|



**1. Câblage**

.. image:: img/wiring_blynk_reed.png

**2. Créer un Flux de Données**

1. Cliquez sur l'icône de menu en haut à droite et sélectionnez "Modifier le tableau de bord".

    .. image:: img/sp220913_180231.png

2. Allez à la page des Flux de Données et créez un Nouveau Flux de Données.

    .. image:: img/sp220914_165911.png

3. Créez un Pin Virtuel V4.

    .. image:: img/sp220914_170113.png

#. Une fois terminé, cliquez sur "Enregistrer et Appliquer" en haut à droite.

    .. image:: img/sp220913_182300.png

**3. Exécuter le code**

1. Modifiez le code

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_reed.py

2. Trouvez la ligne ci-dessous et collez votre ``BLYNK_AUTH_TOKEN``.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Exécutez le code.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_reed.py

**4. Ouvrir l'application Blynk**

.. note::

    Comme les flux de données ne peuvent être créés que dans Blynk sur le web, vous devrez consulter différents projets pour créer des flux de données sur le web, puis suivre le tutoriel ci-dessous pour créer des widgets dans Blynk sur votre appareil mobile.

#. Ouvrez Google Play ou l'App Store sur votre appareil mobile et recherchez "Blynk IoT" (pas Blynk (legacy)) pour le télécharger.
#. Après avoir ouvert l'application, connectez-vous, ce compte doit être le même que celui utilisé sur le client web.
#. Ensuite, allez dans **Dashboard** (si vous n'en avez pas, créez-en un) et vous verrez que le **Dashboard** pour mobile et web sont indépendants l'un de l'autre.

    .. image:: img/APP_1.jpg


#. Cliquez sur l'icône **Modifier**.
#. Cliquez sur la zone vide. 
#. Choisissez le widget **LED**.

    .. image:: img/APP_2.jpg      


#. Maintenant, vous verrez apparaître un widget **LED** dans la zone vide, même s'il ressemble à une grille vide, cliquez dessus.
#. Les paramètres de la **LED** apparaîtront, sélectionnez les flux de données **V4** que vous venez de définir sur la page web. Notez que chaque widget correspond à un flux de données différent dans chaque projet.
#. Retournez à la page **Dashboard**. Maintenant, si vous voyez que le widget **LED** est rempli de couleur, votre porte ou fenêtre est ouverte ; si le widget **LED** n'est pas rempli de couleur, la porte ou fenêtre est fermée.

    .. image:: img/APP_3.jpg


