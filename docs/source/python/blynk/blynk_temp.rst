.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e concorsi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _blynk_temp_py:

Registratore di Temperatura
===============================

In questo progetto, potrai vedere la temperatura attuale e il grafico delle variazioni di temperatura direttamente su Blynk.

.. note:: Prima di iniziare questo progetto, ti consigliamo di completare :ref:`bk_start_py`. Questo ti darà una comprensione chiara di Blynk.

**Componenti Necessari**

Per questo progetto, ci servono i seguenti componenti. 

È decisamente conveniente acquistare un intero kit, ecco il link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - ELEMENTI IN QUESTO KIT
        - LINK
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

Puoi anche acquistarli separatamente dai link sottostanti.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUZIONE AI COMPONENTI
        - LINK PER L'ACQUISTO

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


**1. Cablaggio**

.. image:: img/wiring_blynk_temp.png


**2. Creazione Widget e Datastream**

1. Clicca sull'icona del menu in alto a destra e seleziona modifica dashboard.

    .. image:: img/sp220913_180231.png

2. Aggiungi un widget Gauge e un widget Chart alla dashboard.

    .. image:: img/sp220914_175437.png

3. Crea un Datastream per il widget Gauge (ho utilizzato V5). Verrà utilizzato per visualizzare la temperatura. Imposta **DATA TYPE** su ``Double``, **DECIMALS** su ``#. #`` (due cifre decimali).

    .. image:: img/sp220914_182300.png

4. Aggiungi il Datastream V5 appena creato al widget Chart.

    .. image:: img/sp220914_183039.png

#. Al termine, clicca su Salva e Applica in alto a destra.

    .. image:: img/sp220913_182300.png


**3. Esegui il Codice**

1. Modifica il codice

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_temp.py

2. Trova la seguente riga e incolla il tuo ``BLYNK_AUTH_TOKEN``.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Esegui il codice.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_temp.py

4. Vai su Blynk. Ora puoi visualizzare la temperatura e il grafico delle variazioni di temperatura sul Dashboard.

    .. image:: img/sp220915_101137.png


#. Se desideri utilizzare Blynk su dispositivi mobili, fai riferimento a :ref:`blynk_mobile`.
