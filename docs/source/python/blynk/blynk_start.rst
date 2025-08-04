.. note::

    Ciao, benvenuto nella Community Facebook di appassionati di SunFounder Raspberry Pi & Arduino & ESP32! Approfondisci Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _bk_start_py:

Iniziare con Blynk
=========================

Imparerai come utilizzare Blynk in questo progetto.

Quando attivi i widget su Blynk, il tuo Raspberry Pi stamperà i loro valori.

Segui i passaggi seguenti e tieni presente che devi eseguirli in ordine senza saltare alcun capitolo.

1. Configurazione di Blynk
--------------------------

1. Vai su `BLYNK <https://blynk.io/>`_ e clicca su **START FREE**. 

    .. image:: img/sp220607_142551.png

#. Inserisci il tuo indirizzo email per registrare un account.

    .. image:: img/sp220607_142807.png

#. Vai alla tua email per completare la registrazione dell'account.

    .. image:: img/sp220607_142936.png

#. Successivamente apparirà il **Blynk Tour** e potrai leggerlo per conoscere le informazioni di base su Blynk.

    .. image:: img/sp220607_143244.png

#. Poi dobbiamo creare un template e un dispositivo, clicca su **Cancel**.

    .. image:: img/sp220607_143608.png

#. Vai alla Developer Zone dalla barra di navigazione.

    .. image:: img/develop_zone.png

#. Crea un nuovo Template.

    .. image:: img/new_template.png

#. Compila **NAME** liberamente; **HARDWARE** deve essere **Raspberry Pi**. Poi **Done**.

    .. image:: img/sp220913_170402.png

#. Verrai reindirizzato alla pagina Info, clicca semplicemente su *save* in alto a destra.

    .. image:: img/sp220913_171202.png

#. Vai alla pagina **Devices** dalla barra di navigazione.

    .. image:: img/devices.jpg

#. Crea un nuovo dispositivo.

    .. image:: img/new_devices.png

#. Da template.

    .. image:: img/create_new_device.png

#. Seleziona **TEMPLATE** come quello appena creato, **DEVICE NAME** può essere personalizzato. Poi clicca su Create.

    .. image:: img/sp220913_173507.png

#. Ora dovresti vedere una pagina come questa, il che significa che la configurazione iniziale di Blynk è completa.

    .. image:: img/my_device.png


2. Modifica della Dashboard
---------------------------

1. Clicca su *edit dashboard*.

    .. image:: img/edit_dashboard.png

#. Trascina sulla Dashboard qualsiasi widget di CONTROLLO desideri. Io ho trascinato un interruttore (*Switch*) e un cursore (*Slider*).

    .. image:: img/sp220913_180725.png

#. Tocca l'icona delle impostazioni sul widget.

    .. image:: img/sp220913_180806.png

#. Crea un Datastream, seleziona *Virtual Pin*.

    .. image:: img/sp220913_180906.png

#. Completa la configurazione del datastream. Qui il datastream è creato per lo Switch, quindi **DATA TYPE** seleziona ``Integer``, **MIN** e **MAX** impostati su ``0`` e ``1``. Crea e poi salva.

    .. image:: img/sp220913_181113.png

#. Usa gli stessi passaggi per creare un Datastream per il widget Slider, e ancora, modifica **DATA TYPE**, **MIN** e **MAX** secondo le tue necessità.

    .. image:: img/sp220913_182042.png

#. Quando hai finito, clicca su *Save And Apply* in alto a destra.

    .. image:: img/sp220913_182300.png


3. Installazione della libreria Blynk
-------------------------------------

Esegui il seguente comando per installarla.

.. raw:: html

   <run></run>

.. code-block::

    cd ~
    git clone https://github.com/vshymanskyy/blynk-library-python.git
    cd blynk-library-python
    sudo python3 setup.py

4. Scaricare l'esempio
----------------------

Abbiamo fornito alcuni esempi, esegui il seguente comando per scaricarli.

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~
    git clone https://github.com/sunfounder/blynk-raspberrypi-python.git

5. Esecuzione del codice
------------------------

1. Vai alla pagina Device Info di Blynk, vedrai alcune informazioni sotto **FIRMWARE CONFIGURATION**, devi copiare il **BLYNK_AUTH_TOKEN**.

    .. image:: img/sp220913_182456.png

2. Modifica il codice.

.. raw:: html

    <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_start.py

3. Trova la seguente riga e incolla il tuo ``BLYNK_AUTH_TOKEN``.

.. code-block:: 

    BLYNK_AUTH = 'YourAuthToken'

4. Esegui il codice.

.. raw:: html

    <run></run>

.. code-block:: 

    sudo python3 blynk_start.py

5. Vai su Blynk e utilizza i widget sulla Dashboard.

    .. image:: img/sp220913_183529.png

6. Ora potrai vedere le tue azioni sul terminale.

.. code-block:: 

    ..
       ___  __          __
      / _ )/ /_ _____  / /__
     / _  / / // / _ \/  '_/
    /____/_/\_, /_//_/_/\_\
            /___/ for Python v1.0.0 (linux)

    Connecting to blynk.cloud:443...
    Blynk ready. Ping: 142 ms
    V0 value: ['1']
    V0 value: ['0']
    V1 value: ['3']
    V1 value: ['8']
    V0 value: ['1']
