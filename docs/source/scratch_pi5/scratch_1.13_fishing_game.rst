.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.16_scratch_pi5:

1.16 Gioco di Pesca
========================

Oggi realizzeremo un gioco di pesca.

Osserva l'acqua nell'area dello stage e, se trovi un pesce all'amo, ricorda di inclinare l'interruttore per catturarlo.

.. image:: img/1.16_header.png

Componenti Necessari
------------------------------

In questo progetto, avremo bisogno dei seguenti componenti. 

.. image:: img/1.16_component.png

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

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_tilt_switch`
        - \-

Costruisci il Circuito
-----------------------

.. image:: img/1.16_fritzing.png

Carica il Codice e Guarda Cosa Succede
-------------------------------------------

Carica il file di codice (``1.16_fishing_game.sb3``) su Scratch 3.

Vedrai un bambino che pesca; dopo un po' di tempo, quando la superficie dell'acqua si muove, puoi scuotere l'interruttore inclinabile per catturare il pesce.
Ricorda, se non continui a scuotere l'interruttore, il pesce scapperà.

Suggerimenti sugli Sprite
-----------------------------

Seleziona lo sprite Sprite1, clicca su **Costumi** nell'angolo in alto a sinistra; carica 6 immagini (**fish1** a **fish6**) dal percorso ``~/raphael-kit/scratch/picture`` tramite il pulsante **Carica Costume**; elimina i 2 costumi predefiniti e rinomina lo sprite in **fish**.

.. image:: img/1.16_upload_fish.png


Suggerimenti sul Codice
--------------------------

.. image:: img/1.16_fish2.png
  :width: 400

Imposta il costume iniziale dello sprite **fish** su **fish1** e assegna il valore di **fish_status** a 0 (quando **fish_status=0**, significa che il pesce non è all'amo; quando **fish_status=1**, significa che il pesce è all'amo).

.. image:: img/1.16_fish3.png
  :width: 400

Quando **fish_status=0**, ovvero il pesce non è ancora all'amo, inizia il gioco di pesca. Aspetta un tempo casuale tra 0 e 10 secondi, poi assegna a **fish_status** il valore 1, che significa che il pesce è all'amo, e trasmetti un messaggio "Il pesce sta abboccando".

.. note::

  Lo scopo del blocco di trasmissione è inviare un messaggio ad altri blocchi di codice o ad altri sprite. Il messaggio può essere una richiesta o un comando.

.. image:: img/1.16_fish4.png
  :width: 400

Quando il messaggio "Il pesce sta abboccando" viene ricevuto, fai cambiare lo sprite del pesce tra i costumi **fish2** e **fish3** in modo che possiamo vedere il pesce abboccare.

.. image:: img/1.16_fish5.png
  :width: 400

Dopo aver cambiato il costume, se il gioco non è finito, significa che il pesce si è staccato dall'amo e se n'è andato, quindi cambieremo il costume dello sprite **fish** in **fish6** (stato del pesce scappato).

.. image:: img/1.16_fish6.png
  :width: 400

Quando gpio17 è alto (l'interruttore inclinabile è inclinato), significa che la canna da pesca è stata tirata su. A questo punto viene valutato il valore di fish_status. Se è 1, significa che la canna da pesca è stata tirata su quando il pesce era all'amo e il costume viene cambiato in **fish4** (pesce catturato). Al contrario, se la canna da pesca è stata tirata su quando il pesce non era all'amo, il costume viene cambiato in **fish5** (non è stato catturato nulla).

