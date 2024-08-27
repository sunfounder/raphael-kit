.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e Giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _bk_start_py:

Inizia con Blynk
=========================

Imparerai a utilizzare Blynk in questo progetto.

Nel caso tu attivi widget su Blynk, il tuo Raspberry Pi stamperà i loro valori.

Segui i passaggi sottostanti e assicurati di farli nell'ordine corretto senza saltare alcun capitolo.



1. Configurare Blynk
---------------------

1. Vai a `BLYNK <https://blynk.io/>`_ e clicca su **START FREE**.

    .. image:: img/sp220607_142551.png

#. Inserisci il tuo indirizzo email per registrare un account.

    .. image:: img/sp220607_142807.png

#. Vai al tuo indirizzo email per completare la registrazione dell'account.

    .. image:: img/sp220607_142936.png

#. Successivamente, apparirà **Blynk Tour** e potrai leggerlo per apprendere le informazioni di base su Blynk.

    .. image:: img/sp220607_143244.png

#. Successivamente dobbiamo creare un template e un dispositivo, clicca su **Cancel**.

    .. image:: img/sp220607_143608.png

#. Vai su Template dalla barra di navigazione.

    .. image:: img/sp220913_170029.png

#. Crea un nuovo template

    .. image:: img/sp220913_170206.png

#. Compila il campo **NOME**, inserendo quello che preferisci; **HARDWARE** deve essere **Raspberry Pi**. Poi clicca su **Done**.

    .. image:: img/sp220913_170402.png

#. Sarai reindirizzato alla pagina delle informazioni, clicca su salva in alto a destra.

    .. image:: img/sp220913_171202.png

#. Vai alla pagina **Search** dalla barra di navigazione.

    .. image:: img/sp220913_172727.png

#. Crea un nuovo dispositivo.

    .. image:: img/sp220913_173259.png

#. Dal template.

    .. image:: img/sp220913_173350.png

#. Seleziona il **TEMPLATE** che hai appena impostato, **DEVICE NAME** può essere personalizzato. Poi clicca su Crea.

    .. image:: img/sp220913_173507.png

#. Ora dovresti vedere una pagina come questa, il che significa che la tua configurazione iniziale di Blynk è completa.

    .. image:: img/sp220913_173950.png


2. Modifica Dashboard
---------------------------

1. Clicca sull'icona del menu in alto a destra e seleziona modifica dashboard.

    .. image:: img/sp220913_180231.png

#. Poi trascina qualsiasi widget di controllo desiderato sul Dashboard. Ho trascinato un Interruttore e uno Slider.

    .. image:: img/sp220913_180725.png

#. Tocca l'icona delle impostazioni sul widget.

    .. image:: img/sp220913_180806.png

#. Crea Datastream, seleziona Virtual Pin.

    .. image:: img/sp220913_180906.png

#. Completa la configurazione del datastream. Questo è il datastream creato per l'interruttore, quindi **DATA TYPE** seleziona ``Interger``, **MIN** e **MAX** imposta a ``0`` e ``1``. Crea e poi Salva.

    .. image:: img/sp220913_181113.png

#. Usa gli stessi passaggi per creare un datastream per il widget slider, e ancora, modifica **DATA TYPE**, **MIN** e **MAX** in base alle tue necessità.

    .. image:: img/sp220913_182042.png

#. Al termine, clicca su Salva e Applica in alto a destra.

    .. image:: img/sp220913_182300.png


3. Installa la libreria Blynk
---------------------------------

Esegui il seguente comando per installarla.

.. raw:: html

   <run></run>

.. code-block::

    cd ~
    git clone https://github.com/vshymanskyy/blynk-library-python.git
    cd blynk-library-python
    sudo python3 setup.py

4. Scarica l'esempio
-------------------------

Abbiamo fornito alcuni esempi, esegui il seguente comando per scaricarli.

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~
    git clone https://github.com/sunfounder/blynk-raspberrypi-python.git


5. Esegui il codice
----------------------


1. Vai alla pagina delle informazioni del dispositivo su Blynk, vedrai alcune informazioni sotto **FIRMWARE CONFIGURATION**, devi copiare **BLYNK_AUTH_TOKEN**.

    .. image:: img/sp220913_182456.png

2. Modifica il codice.

.. raw:: html

    <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_start.py

3. Trova la seguente linea e incolla il tuo ``BLYNK_AUTH_TOKEN``.

.. code-block:: 

    BLYNK_AUTH = 'YourAuthToken'

4. Esegui il codice.

.. raw:: html

    <run></run>

.. code-block:: 

    sudo python3 blynk_start.py

5. Vai su Blynk e utilizza il widget sul Dashboard.

    .. image:: img/sp220913_183529.png

6. Ora sarai in grado di vedere le tue azioni nel terminale.

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







