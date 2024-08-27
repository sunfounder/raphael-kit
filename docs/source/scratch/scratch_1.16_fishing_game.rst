.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue abilità.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _1.16_scratch:

1.16 Gioco di Pesca
==========================

Oggi realizzeremo un gioco di pesca.

Osserva l'acqua nell'area del palco e, se vedi un pesce all'amo, ricorda di inclinare l'interruttore per catturarlo.

.. image:: img/1.16_header.png

Componenti Necessari
--------------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.16_component.png

È sicuramente comodo acquistare un kit completo, ecco il link:

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
--------------------------

.. image:: img/1.16_fritzing.png

Carica il Codice e Guarda Cosa Succede
-----------------------------------------

Carica il file di codice (``1.16_fishing_game.sb3``) su Scratch 3.

Vedrai un bambino che pesca; dopo un po', quando l'acqua si muove, puoi scuotere l'interruttore a inclinazione per catturare il pesce.
Ricorda, se non continui a scuotere l'interruttore, il pesce scapperà.

Suggerimenti sugli Sprite
--------------------------------------

Seleziona lo Sprite1, clicca su **Costumi** nell'angolo in alto a sinistra; carica 6 immagini (**fish1** a **fish6**) dal percorso ``~/raphael-kit/scratch/picture`` tramite il pulsante **Carica Costume**; elimina i 2 costumi predefiniti e rinomina lo sprite in **fish**.

.. image:: img/1.16_upload_fish.png


Suggerimenti sui Codici
------------------------------

.. image:: img/1.16_fish2.png
  :width: 400

Imposta il costume iniziale dello sprite **fish** su **fish1** e assegna il valore di **fish_status** a 0 (quando **fish_status=0**, significa che il pesce non è ancora all'amo; quando **fish_status=1**, significa che il pesce è all'amo).

.. image:: img/1.16_fish3.png
  :width: 400

Quando **fish_status=0**, cioè il pesce non è ancora all'amo, inizia il gioco di pesca. Aspetta un tempo casuale da 0 a 10 secondi, poi assegna **fish_status** a 1, il che significa che il pesce è all'amo, e invia un messaggio "Il pesce sta abboccando".

.. note::

  Lo scopo del blocco di trasmissione è inviare un messaggio ad altri blocchi di codice o ad altri sprite. Il messaggio può essere una richiesta o un comando.

.. image:: img/1.16_fish4.png
  :width: 400

Quando il messaggio "Il pesce sta abboccando" viene ricevuto, fai sì che lo sprite pesce alterni i costumi **fish2** e **fish3** in modo che si veda il pesce abboccare.

.. image:: img/1.16_fish5.png
  :width: 400

Dopo aver cambiato il costume, se il gioco non è finito, significa che il pesce è scappato dall'amo, quindi cambiamo il costume dello sprite **fish** in **fish6** (pesce scappato).

.. image:: img/1.16_fish6.png
  :width: 400

Quando gpio17 è alto (l'interruttore a inclinazione è inclinato), significa che la canna da pesca è stata tirata su. In questo momento, viene valutato il valore di fish_status. Se è 1, significa che la canna da pesca è stata tirata su quando il pesce era all'amo e il costume viene cambiato in fish4 (pesce catturato). Al contrario, significa che la canna da pesca è stata tirata su quando il pesce non era all'amo e il costume viene cambiato in fish5 (nessuna cattura).
