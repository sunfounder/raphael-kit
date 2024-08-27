.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e Giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _blynk_motor_py:

Ventola Intelligente
========================

In questo progetto, puoi visualizzare la temperatura da Blynk e accendere la ventola da remoto.

.. note:: Prima di iniziare questo progetto, ti consigliamo di completare :ref:`bk_start_py`. Di seguito troverai una spiegazione chiara di Blynk.

**Componenti necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti. 

È sicuramente comodo acquistare un intero kit, ecco il link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - ELEMENTI IN QUESTO KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

Puoi anche acquistarli separatamente dai link seguenti.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUZIONE AI COMPONENTI
        - LINK DI ACQUISTO

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

**1. Collegamenti**

.. image:: img/wiring_blynk_motor.png


**2. Crea Widget e Datastream**

1. Clicca sull'icona del menu in alto a destra e seleziona modifica dashboard.

    .. image:: img/sp220913_180231.png

2. Aggiungi un widget Interruttore e un widget Etichetta alla Dashboard.

    .. image:: img/sp220914_175437.png

3. Crea un Datastream (io ho usato V3) per il widget Interruttore. Sarà utilizzato per accendere il motore.

    .. image:: img/sp220914_155911.png

4. Crea un Datastream per il widget Etichetta (io ho usato V0). Sarà utilizzato per visualizzare la temperatura. Imposta **DATA TYPE** su String.

    .. image:: img/sp220914_175616.png

#. Al termine, clicca su Salva e Applica in alto a destra.

    .. image:: img/sp220913_182300.png


**3. Esegui il Codice**

1. Modifica il codice

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_motor.py

2. Trova la seguente linea e incolla il tuo ``BLYNK_AUTH_TOKEN``.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Esegui il codice.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_motor.py

4. Vai su Blynk, nella Dashboard puoi controllare la temperatura tramite il widget Etichetta; puoi accendere/spegnere la ventola tramite il widget Interruttore.

#. Se desideri utilizzare Blynk sui dispositivi mobili, fai riferimento a :ref:`blynk_mobile`.
