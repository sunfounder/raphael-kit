.. _blynk_light_py:

Intelligentes Licht
===================

In diesem Projekt nutzen wir Blynks Slider, um die Helligkeit der LED zu steuern und sie mit einem Schalter ein- und auszuschalten.

.. note:: Bevor Sie mit diesem Projekt beginnen, empfehlen wir Ihnen, :ref:`bk_start_py` abzuschließen. Dies wird Ihnen ein klares Verständnis für Blynk vermitteln.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen. Hier ist der Link:

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

    *   - :ref:`gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`breadboard`
        - |link_breadboard_buy|
    *   - :ref:`wires`
        - |link_wires_buy|
    *   - :ref:`resistor`
        - |link_resistor_buy|
    *   - :ref:`led`
        - |link_led_buy|

**1. Verdrahtung**

.. image:: img/wiring_led1.png

**2. Widget und Datenstrom erstellen**

1. Klicken Sie auf das Menü-Symbol in der oberen rechten Ecke und wählen Sie "Dashboard bearbeiten".

    .. image:: img/sp220913_180231.png

2. Fügen Sie dem Dashboard ein Schalter-Widget und ein Schieberegler-Widget hinzu.

    .. image:: img/sp220914_160427.png

3. Erstellen Sie einen Datenstrom für das Schalter-Widget (ich habe V3 verwendet). Damit steuern Sie das Ein- und Ausschalten der LED.

    .. image:: img/sp220914_155911.png

4. Erstellen Sie einen Datenstrom für das Schieberegler-Widget (ich habe V2 verwendet). Sein Wertebereich liegt zwischen 0 und 100. Damit steuern Sie die Helligkeit der LED.

    .. image:: img/sp220914_160234.png

#. Wenn Sie fertig sind, klicken Sie oben rechts auf "Speichern und Anwenden".

    .. image:: img/sp220913_182300.png


**3. Code ausführen**

1. Den Code bearbeiten

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_light.py

2. Suchen Sie die untenstehende Zeile und fügen Sie Ihren ``BLYNK_AUTH_TOKEN`` ein.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Führen Sie den Code aus.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_light.py

4. Gehen Sie zu Blynk und bedienen Sie das Widget im Dashboard. Wenn Sie jetzt das Schalter-Widget klicken, wird die LED ein-/ausgeschaltet. Das Bewegen des Schieberegler-Widgets ändert die Helligkeit der LED.

#. Wenn Sie Blynk auf mobilen Geräten nutzen möchten, ziehen Sie bitte :ref:`blynk_mobile` zurate.
