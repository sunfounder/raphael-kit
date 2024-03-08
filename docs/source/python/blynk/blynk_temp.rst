.. _blynk_temp_py:

Temperaturaufzeichner
=====================

In diesem Projekt können Sie die aktuelle Temperatur und das Temperaturänderungs-Liniendiagramm von Blynk sehen.

.. note:: Bevor Sie mit diesem Projekt beginnen, empfehlen wir Ihnen, :ref:`bk_start_py` abzuschließen. Das Folgende wird Ihnen ein klares Verständnis von Blynk vermitteln.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein komplettes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

Sie können sie auch einzeln über die untenstehenden Links kaufen.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - KOMPONENTENBESCHREIBUNG
        - KAUF-LINK

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_humiture_sensor`
        - |link_humiture_buy|


**1. Verkabelung**

.. image:: img/wiring_blynk_temp.png

**2. Widget und Datenstrom erstellen**

1. Klicken Sie auf das Menü-Symbol in der oberen rechten Ecke und wählen Sie "Dashboard bearbeiten".

    .. image:: img/sp220913_180231.png

2. Fügen Sie ein Anzeige-Widget und ein Diagramm-Widget zum Dashboard hinzu.

    .. image:: img/sp220914_175437.png

3. Erstellen Sie einen Datenstrom für das Anzeige-Widget (ich habe V5 verwendet). Es wird zur Anzeige der Temperatur verwendet. Setzen Sie **DATA TYPE** auf ``Double`` und **DECIMALS** auf ``#. #`` (zwei gültige Dezimalstellen).

    .. image:: img/sp220914_182300.png

4. Fügen Sie den gerade erstellten V5-Datenstrom zum Diagramm-Widget hinzu.

    .. image:: img/sp220914_183039.png

#. Wenn Sie fertig sind, klicken Sie oben rechts auf "Speichern und anwenden".

    .. image:: img/sp220913_182300.png


**3. Code ausführen**

1. Den Code bearbeiten

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_temp.py

2. Suchen Sie die untenstehende Zeile und fügen Sie Ihren ``BLYNK_AUTH_TOKEN`` ein.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Führen Sie den Code aus.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_temp.py

4. Gehen Sie zu Blynk. Jetzt können Sie die Temperatur und das Temperaturänderungs-Liniendiagramm im Dashboard anzeigen.

    .. image:: img/sp220915_101137.png


#. Wenn Sie Blynk auf mobilen Geräten verwenden möchten, lesen Sie bitte :ref:`blynk_mobile`.
