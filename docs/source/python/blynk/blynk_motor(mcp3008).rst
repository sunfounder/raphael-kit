.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook!  
    Tauche tiefer ein in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse nach dem Kauf auftretende Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugriff auf neue Produktankündigungen und exklusive Einblicke.
    - **Sonderrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nimm an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu forschen und zu erschaffen? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _blynk_motor2_py_mcp3008:

Smart Ventilator (MCP3008)
===========================

In diesem Projekt kannst du die Temperatur über Blynk sehen und den Ventilator aus der Ferne einschalten.

.. note::  
    Bevor du dieses Projekt startest, empfehlen wir dir, :ref:`bk_start_py` abzuschließen. Dies gibt dir ein klares Verständnis von Blynk.

**Benötigte Komponenten**

In diesem Projekt benötigen wir die folgenden Komponenten. 

Es ist definitiv bequem, ein komplettes Kit zu kaufen, hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ELEMENTE IN DIESEM KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

Du kannst sie auch einzeln über die folgenden Links kaufen.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - KOMPONENTENBESCHREIBUNG
        - KAUFLINK

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

**1. Verdrahtung**

.. image:: img/3.1.4_smart_fan_iot.png


**2. Widget und Datenstream erstellen**

1. Klicke auf das Menüsymbol oben rechts und wähle „Dashboard bearbeiten“.

    .. image:: img/sp220913_180231.png

2. Füge ein Schalter-Widget und ein Label-Widget zum Dashboard hinzu.

    .. image:: img/sp220914_175437.png

3. Erstelle einen Datenstream (hier wurde V3 verwendet) für das Schalter-Widget. Es wird verwendet, um den Motor einzuschalten.

    .. image:: img/sp220914_155911.png

4. Erstelle einen Datenstream für das Label-Widget (hier wurde V0 verwendet). Es wird verwendet, um die Temperatur anzuzeigen. Setze **DATENTYP** auf „String“.

    .. image:: img/sp220914_175616.png

#. Wenn du fertig bist, klicke oben rechts auf „Speichern und Anwenden“.

    .. image:: img/sp220913_182300.png


**3. Code ausführen**

1. Bearbeite den Code

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_motor(mcp3008).py

2. Finde die folgende Zeile und füge dein ``BLYNK_AUTH_TOKEN`` ein.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Führe den Code aus.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_motor(mcp3008).py

4. Gehe zu Blynk. Auf dem Dashboard kannst du über das Label-Widget die Temperatur überprüfen und über das Schalter-Widget den Ventilator ein- oder ausschalten.

#. Wenn du Blynk auf mobilen Geräten verwenden möchtest, lies bitte :ref:`blynk_mobile`.
