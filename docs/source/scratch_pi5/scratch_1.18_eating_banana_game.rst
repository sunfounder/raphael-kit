.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.18_scratch_pi5:

1.18 Gioco della Banana
===========================

Descrizione
--------------

Scratch ha un modulo di espansione per il Video Sensing, che può attivare la fotocamera in Scratch e rilevare il movimento degli oggetti sullo schermo della fotocamera.

Oggi utilizzeremo la fotocamera per creare un gioco in cui bisogna far mangiare più banane possibile alla scimmia entro il tempo stabilito.

Gioca in un ambiente con sfondo bianco, clicca sulla bandiera verde per iniziare. Muovi oggetti colorati davanti alla fotocamera per controllare lo sprite della scimmia.

.. image:: img/1.18_header.png

Componenti Necessari
---------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.18_photo1.png

È sicuramente comodo acquistare un kit completo, ecco il link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - COMPONENTI IN QUESTO KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

Puoi anche acquistarli separatamente dai link sottostanti.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUZIONE AI COMPONENTI
        - LINK PER L'ACQUISTO

    *   - :ref:`cpn_camera_module`
        - |link_camera_buy|


Costruisci il Circuito
------------------------

.. image:: img/1.10_camera.png

.. note::

    Devi fare riferimento a :ref:`cpn_camera_module` per collegare il modulo fotocamera e abilitare l'interfaccia della fotocamera Raspberry Pi.

Carica il Codice e Guarda Cosa Succede
-----------------------------------------

Carica il file di codice (``1.18_eating_banana_game.sb3``) su Scratch 3.

Suggerimenti sul Codice
---------------------------

Sistema la scimmia e le banane

Per prima cosa, elimina lo sprite originale, poi aggiungi lo sprite Scimmia e lo sprite Banane, e modifica la loro dimensione a 50.

Fai apparire le banane in modo casuale.

.. image:: img/1.18_code1.png

Le banane scompaiono dopo essere state incontrate dalla scimmia, il che significa che sono state mangiate e ricompaiono in modo casuale.

.. image:: img/1.18_code2.png

Fai apparire la scimmia al centro del palco e inizializza i dati della fotocamera (trasparenza impostata a 20).

.. image:: img/1.18_code3.png

Se la fotocamera rileva un oggetto in movimento, fai muovere la scimmia verso di esso.

.. image:: img/1.18_code4.png

Ora clicca sulla bandiera verde nella parte superiore dell'area del palco per iniziare il gioco.

Fai mangiare banane alla scimmia, è molto affamata! Prova a giocare su uno sfondo bianco per evitare interferenze da altri oggetti.



Sfida
---------

Credo che sarai abbastanza ingegnoso da programmare e realizzare presto questo gioco. Ora, aggiungeremo qualche sfida per arricchire il contenuto del gioco.

· Quando la scimmia mangia una banana, aggiungiamo 1 punto al punteggio. Entro 30 secondi, chi ottiene il punteggio più alto?

· Quando la scimmia mangia una banana, emettiamo un effetto sonoro appropriato.
