.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato alle nuove anteprime dei prodotti.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.3_scratch_pi5:

1.3 Tumbler
==================

In questo progetto, realizzeremo un giocattolo tumbler controllato da un interruttore a inclinazione.

.. image:: img/1.3_header.png

Componenti Necessari
------------------------------

In questo progetto, abbiamo bisogno dei seguenti componenti.

.. image:: img/1.3_component.png

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

Costruire il Circuito
-------------------------

.. image:: img/1.3_fritzing.png


Carica il Codice e Vedi Cosa Succede
-------------------------------------------

Carica il file di codice (``1.3_tumbler.sb3``) in Scratch 3.

Quando l'interruttore a inclinazione è posizionato verticalmente, il tumbler resta in piedi. Se lo inclini, il tumbler cadrà. Rimettilo in posizione verticale e il tumbler si rialzerà di nuovo.


Suggerimenti sugli Sprite
----------------------------
Seleziona Sprite1 e clicca su **Costumi** nell'angolo in alto a sinistra; carica **tumbler1.png** e **tumbler2.png** dal percorso ``~/raphael-kit/scratch/picture`` tramite il pulsante **Carica Costume**; elimina i 2 costumi predefiniti e rinomina lo sprite come **tumbler**.

.. image:: img/1.3_add_tumbler.png

Suggerimenti sul Codice
------------------------------

.. image:: img/1.3_title2.png
  :width: 400

Quando viene cliccata la bandiera verde, lo stato iniziale di gpio17 è impostato su basso.

.. image:: img/1.3_title4.png
  :width: 400

Quando pin17 è basso (l'interruttore a inclinazione è in posizione verticale), cambiamo il costume dello sprite tumbler in tumbler1 (stato verticale).

.. image:: img/1.3_title3.png
  :width: 400

Quando pin17 è alto (interruttore inclinato), cambiamo il costume dello sprite tumbler in tumbler2 (stato inclinato).
