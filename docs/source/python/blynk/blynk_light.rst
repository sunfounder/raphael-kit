 
.. _blynk_light_py:

Lumière intelligente
=========================

Dans ce projet, nous utilisons le curseur de Blynk pour contrôler la luminosité de la LED, en l'allumant et l'éteignant avec un interrupteur.

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
    *   - :ref:`cpn_led`
        - |link_led_buy|

**1. Câblage**

.. image:: img/wiring_led1.png

**2. Créer le widget et le flux de données**

1. Cliquez sur l'icône de menu en haut à droite et sélectionnez "Edit Dashboard".

    .. image:: img/sp220913_180231.png

2. Ajoutez un widget Interrupteur et un widget Curseur au tableau de bord.

    .. image:: img/sp220914_160427.png

3. Créez un flux de données pour le widget Interrupteur (j'ai utilisé V3). Il sera utilisé pour contrôler l'allumage et l'extinction de la LED.

    .. image:: img/sp220914_155911.png

4. Créez un flux de données pour le widget Curseur (j'ai utilisé V2), sa plage de valeurs est de 0 à 100, il sera utilisé pour contrôler la luminosité de la LED.

    .. image:: img/sp220914_160234.png

#. Une fois terminé, cliquez sur "Save And Apply" en haut à droite.

    .. image:: img/sp220913_182300.png


**3. Exécuter le code**

1. Modifiez le code

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_light.py

2. Trouvez la ligne ci-dessous et collez votre ``BLYNK_AUTH_TOKEN``.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Exécutez le code.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_light.py

4. Allez sur Blynk, utilisez le widget sur le tableau de bord. Maintenant, en cliquant sur le widget interrupteur, vous allumerez/éteindrez la LED. En glissant le curseur, vous changerez la luminosité de la LED.

#. Si vous souhaitez utiliser Blynk sur des appareils mobiles, veuillez vous référer à :ref:`blynk_mobile`.
