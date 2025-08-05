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

.. _blynk_motor2_py_mcp3008:

Ventilateur intelligent (MCP3008)
==================================

Dans ce projet, vous pouvez consulter la température depuis **Blynk** et allumer le ventilateur à distance.

.. note:: Avant de commencer ce projet, nous vous recommandons de compléter :ref:`bk_start_py`.  
   Vous aurez ainsi une compréhension claire de **Blynk**.

**Composants requis**

Dans ce projet, nous avons besoin des composants suivants :

Il est définitivement plus pratique d’acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ÉLÉMENTS DANS CE KIT
        - LIEN
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

Vous pouvez également les acheter séparément via les liens ci‑dessous :

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUCTION DU COMPOSANT
        - LIEN D’ACHAT

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
    *   - :ref:`cpn_mcp3008`
        - \-
    *   - :ref:`cpn_thermistor`
        - |link_thermistor_buy|
    *   - :ref:`cpn_motor`
        - |link_motor_buy|

**1. Câblage**

.. image:: img/3.1.4_smart_fan_iot.png

**2. Créer un widget et un flux de données**

1. Cliquez sur l’icône du menu en haut à droite et sélectionnez **Edit Dashboard**.

    .. image:: img/sp220913_180231.png

2. Ajoutez un widget **Switch** et un widget **Label** au tableau de bord.

    .. image:: img/sp220914_175437.png

3. Créez un flux de données (j’ai utilisé **V3**) pour le widget Switch.  
   Il sera utilisé pour allumer le moteur.

    .. image:: img/sp220914_155911.png

4. Créez un flux de données pour le widget Label (j’ai utilisé **V0**).  
   Il sera utilisé pour afficher la température. Définissez **DATA TYPE** sur **String**.

    .. image:: img/sp220914_175616.png

#. Une fois terminé, cliquez sur **Save And Apply** en haut à droite.

    .. image:: img/sp220913_182300.png

**3. Exécuter le code**

1. Éditez le code :

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_motor(mcp3008).py

2. Trouvez la ligne ci‑dessous et collez votre ``BLYNK_AUTH_TOKEN``.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Exécutez le code :

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_motor(mcp3008).py

4. Allez sur **Blynk**, dans le tableau de bord vous pouvez vérifier la température via le widget Label ;  
   vous pouvez allumer/éteindre le ventilateur via le widget Switch.

#. Si vous souhaitez utiliser **Blynk** sur des appareils mobiles, veuillez consulter :ref:`blynk_mobile`.
