.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _blynk_motor_py:

Intelligenter Ventilator
========================

In diesem Projekt können Sie die Temperatur über Blynk ablesen und den Ventilator aus der Ferne einschalten.

.. note:: Bevor Sie mit diesem Projekt beginnen, empfehlen wir Ihnen, :ref:`bk_start_py` abzuschließen. Dies wird Ihnen ein klares Verständnis für Blynk vermitteln.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist sicherlich praktisch, gleich ein ganzes Kit zu kaufen. Hier finden Sie den Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

Sie können die Teile auch einzeln über die untenstehenden Links kaufen.

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

**1. Verdrahtung**

.. image:: img/wiring_blynk_motor.png

**2. Widget und Datenstrom erstellen**

1. Klicken Sie auf das Menü-Symbol in der oberen rechten Ecke und wählen Sie "Dashboard bearbeiten".

    .. image:: img/sp220913_180231.png

2. Fügen Sie ein Schalter-Widget und ein Beschriftungs-Widget zum Dashboard hinzu.

    .. image:: img/sp220914_175437.png

3. Erstellen Sie einen Datenstrom (ich habe V3 verwendet) für das Schalter-Widget. Dieser wird zum Einschalten des Motors verwendet.

    .. image:: img/sp220914_155911.png

4. Erstellen Sie einen Datenstrom für das Beschriftungs-Widget (ich habe V0 verwendet). Dieser wird zur Anzeige der Temperatur verwendet. Stellen Sie **DATA TYPE** auf Zeichenkette (String) ein.

    .. image:: img/sp220914_175616.png

#. Wenn Sie fertig sind, klicken Sie oben rechts auf "Speichern und Anwenden".

    .. image:: img/sp220913_182300.png

**3. Code ausführen**

1. Code bearbeiten

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_motor.py

2. Suchen Sie die untenstehende Zeile und fügen Sie Ihren ``BLYNK_AUTH_TOKEN`` ein.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Führen Sie den Code aus.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_motor.py

4. Öffnen Sie Blynk und auf dem Dashboard können Sie die Temperatur über das Beschriftungs-Widget überprüfen; Sie können den Ventilator über das Schalter-Widget ein- und ausschalten.

#. Falls Sie Blynk auf mobilen Geräten nutzen möchten, verweisen Sie bitte auf :ref:`blynk_mobile`.
