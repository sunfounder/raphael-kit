.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue abilità.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _1.18_scratch:

1.18 Gioco della Banana
==========================

Descrizione
--------------

Scratch ha un modulo di espansione Video Sensing, che può attivare la fotocamera in Scratch e rilevare il movimento degli oggetti sullo schermo della fotocamera.

Oggi useremo la fotocamera per creare un gioco di mangiare le banane. Nel tempo stabilito, aiuta la scimmia a mangiare più banane possibile.

Per giocare contro uno sfondo bianco, clicca sulla bandiera verde per iniziare. Muovi oggetti colorati davanti alla fotocamera per controllare la sprite Scimmia.

.. image:: img/1.18_header.png

Componenti Necessari
-----------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.18_photo1.png

È sicuramente conveniente acquistare un kit completo, ecco il link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome
        - ELEMENTI NEL KIT
        - LINK
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

Puoi anche acquistarli separatamente dai link qui sotto.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUZIONE AI COMPONENTI
        - LINK PER L'ACQUISTO

    *   - :ref:`cpn_camera_module`
        - |link_camera_buy|

Costruisci il Circuito
--------------------------

.. image:: img/1.10_camera.png

.. note::

    Devi fare riferimento a :ref:`cpn_camera_module` per collegare il modulo fotocamera e abilitare l'interfaccia fotocamera del Raspberry Pi.

Carica il Codice e Guarda Cosa Succede
------------------------------------------

Carica il file di codice (``1.18_eating_banana_game.sb3``) su Scratch 3.

Suggerimenti sui Codici
--------------------------

Sistema la scimmia e le banane

Per prima cosa, eliminiamo la sprite originale, quindi aggiungiamo la sprite Scimmia e la sprite Banane, e ridimensioniamole al 50%.

Fai apparire le banane in posizioni casuali.

.. image:: img/1.18_code1.png

Le banane scompaiono quando incontrano la scimmia, il che significa che sono state mangiate e ricompaiono in una posizione casuale.

.. image:: img/1.18_code2.png

Fai apparire la scimmia al centro del palco e inizializza i dati della fotocamera (la trasparenza è impostata su 20).

.. image:: img/1.18_code3.png

Se la fotocamera rileva un oggetto in movimento, fai muovere la scimmia verso l'oggetto.

.. image:: img/1.18_code4.png

Ora, clicca sulla bandiera verde in alto nell'area del palco per avviare il gioco.

Fai mangiare le banane alla scimmia, è molto affamata! Prova a giocare su uno sfondo bianco per evitare interferenze da parte di altri oggetti.



Sfida
------

Sono sicuro che sarai abbastanza intelligente da programmare e implementare presto questo gioco. Ora, aggiungeremo alcune sfide per arricchire il contenuto del nostro gioco.

· Quando la scimmia mangia una banana, aggiungiamo 1 punto al punteggio. In 30 secondi, vedi chi ottiene il punteggio più alto!

· Quando la scimmia mangia una banana, emette un effetto sonoro adatto.
