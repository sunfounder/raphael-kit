 
.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _blynk_temp_py:

Enregistreur de Température
=================================

Dans ce projet, vous pouvez voir la température actuelle et le graphique des variations de température sur Blynk.

.. note:: Avant de commencer ce projet, nous vous recommandons de compléter :ref:`bk_start_py`. Cela vous donnera une compréhension claire de Blynk.

**Composants Nécessaires**

Pour ce projet, nous avons besoin des composants suivants. 

Il est certainement pratique d'acheter un kit complet, voici le lien : 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom	
        - ÉLÉMENTS DANS CE KIT
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
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_humiture_sensor`
        - |link_humiture_buy|


**1. Câblage**

.. image:: img/wiring_blynk_temp.png


**2. Créer un Widget et un Flux de Données**

1. Cliquez sur l'icône du menu en haut à droite et sélectionnez éditer le tableau de bord.

    .. image:: img/sp220913_180231.png

2. Ajoutez un widget Gauge et un widget Chart au tableau de bord.

    .. image:: img/sp220914_175437.png

3. Créez un Flux de Données pour le widget Gauge (j'ai utilisé V5). Il sera utilisé pour afficher la température. Réglez **DATA TYPE** sur ``Double``, **DECIMALS** sur ``#. #`` (deux décimales valides).

    .. image:: img/sp220914_182300.png

4. Ajoutez le Flux de Données V5 que vous venez de créer au widget Chart.

    .. image:: img/sp220914_183039.png

#. Lorsque vous avez terminé, cliquez sur Save And Apply en haut à droite.

    .. image:: img/sp220913_182300.png


**3. Exécuter le Code**

1. Modifiez le code

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_temp.py

2. Trouvez la ligne ci-dessous et collez votre ``BLYNK_AUTH_TOKEN``.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Exécutez le code.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_temp.py

4. Allez sur Blynk. Maintenant, vous pouvez voir la température et le graphique des variations de température sur le tableau de bord.

    .. image:: img/sp220915_101137.png


#. Si vous souhaitez utiliser Blynk sur des appareils mobiles, veuillez vous référer à :ref:`blynk_mobile`.
