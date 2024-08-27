.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e Giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _blynk_reed_py:

Sensore Porta/Finestra
=========================

Quando sei fuori casa, ti sei probabilmente chiesto: "Le porte e le finestre di casa mia sono chiuse?"

Per risolvere questo problema, in questo progetto costruiremo un sensore per porte e finestre utilizzando un interruttore Reed e magneti.

Installa questo sensore e magnete su entrambi i lati della porta o della finestra. Potrai verificare se le tue porte e finestre sono chiuse o meno tramite l'app Blynk sul tuo telefono.

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
    *   - :ref:`cpn_reed_switch`
        - |link_reed_switch_buy|


**1. Collegamenti**

.. image:: img/wiring_blynk_reed.png

**2. Crea Datastream**

1. Clicca sull'icona del menu in alto a destra e seleziona modifica dashboard.

    .. image:: img/sp220913_180231.png

2. Vai alla pagina dei Datastream e crea un nuovo Datastream.

    .. image:: img/sp220914_165911.png

3. Crea un Virtual Pin V4.

    .. image:: img/sp220914_170113.png

#. Al termine, clicca su Salva e Applica in alto a destra.

    .. image:: img/sp220913_182300.png

**3. Esegui il Codice**

1. Modifica il codice

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_reed.py

2. Trova la seguente linea e incolla il tuo ``BLYNK_AUTH_TOKEN``.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Esegui il codice.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_reed.py

**4. Apri l'APP Blynk**

.. note::

    Poiché i datastream possono essere creati solo su Blynk tramite web, sarà necessario fare riferimento a diversi progetti per creare i datastream sul web, quindi seguire il tutorial di seguito per creare i widget in Blynk sul tuo dispositivo mobile.

#. Apri Google Play o l'APP Store sul tuo dispositivo mobile e cerca "Blynk IoT" (non Blynk(legacy)) per scaricarlo.
#. Dopo aver aperto l'APP, accedi con lo stesso account usato nel client web.
#. Vai su **Dashboard** (se non ne hai uno, creane uno) e vedrai che i **Dashboard** per dispositivi mobili e web sono indipendenti l'uno dall'altro.

    .. image:: img/APP_1.jpg

#. Clicca sull'icona **Modifica**.
#. Clicca sull'area vuota. 
#. Scegli il widget **LED**.

    .. image:: img/APP_2.jpg      

#. Ora vedrai il widget **LED** nell'area vuota, anche se sembra una griglia vuota, cliccaci sopra.
#. Appariranno le impostazioni del widget **LED**, seleziona il datastream **V4** che hai appena impostato nella pagina web. Ricorda che ogni widget corrisponde a un diverso datastream in ogni progetto.
#. Torna alla pagina **Dashboard**. Ora, se il widget **LED** è colorato, la tua porta o finestra è aperta; se il widget **LED** non è colorato, la porta o finestra è chiusa.

    .. image:: img/APP_3.jpg
