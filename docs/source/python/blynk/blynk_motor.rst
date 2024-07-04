 
.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _blynk_motor_py:

Ventilateur intelligent
============================

Dans ce projet, vous pouvez voir la température depuis Blynk et allumer le ventilateur à distance.

.. note:: Avant de commencer ce projet, nous vous recommandons de compléter :ref:`bk_start_py`. Cela vous donnera une compréhension claire de Blynk.

**Composants requis**

Pour ce projet, nous avons besoin des composants suivants. 

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

Vous pouvez également les acheter séparément via les liens ci-dessous.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUCTION AUX COMPOSANTS
        - LIEN D'ACHAT

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_power_module`
        - \-
    *   - :ref:`cpn_l293d`
        - \-
    *   - :ref:`cpn_adc0834`
        - \-
    *   - :ref:`cpn_thermistor`
        - |link_thermistor_buy|
    *   - :ref:`cpn_motor`
        - |link_motor_buy|

**1. Câblage**

.. image:: img/wiring_blynk_motor.png


**2. Créer un Widget et un Flux de Données**

1. Cliquez sur l'icône de menu en haut à droite et sélectionnez "Modifier le tableau de bord".

    .. image:: img/sp220913_180231.png

2. Ajoutez un widget Switch et un widget Label au tableau de bord.

    .. image:: img/sp220914_175437.png

3. Créez un flux de données (j'ai utilisé V3) pour le widget Switch. Il sera utilisé pour allumer le moteur.

    .. image:: img/sp220914_155911.png

4. Créez un flux de données pour le widget Label (j'ai utilisé V0). Il sera utilisé pour afficher la température. Réglez le **TYPE DE DONNÉES** sur String.

    .. image:: img/sp220914_175616.png

#. Une fois terminé, cliquez sur "Enregistrer et Appliquer" en haut à droite.

    .. image:: img/sp220913_182300.png


**3. Exécuter le Code**

1. Éditez le code

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_motor.py

2. Trouvez la ligne ci-dessous et collez votre ``BLYNK_AUTH_TOKEN``.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Exécutez le code.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_motor.py

4. Allez sur Blynk, dans le tableau de bord, vous pouvez vérifier la température via le widget Label ; vous pouvez allumer/éteindre le ventilateur via le widget Switch.


#. Si vous souhaitez utiliser Blynk sur des appareils mobiles, veuillez vous référer à :ref:`blynk_mobile`.
