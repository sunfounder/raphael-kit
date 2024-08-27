.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anticipazioni.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _1.7_scratch:

1.7 Salvadanaio
=========================

In questo progetto utilizzeremo un modulo sensore di velocità, un Raspberry Pi e Scratch per creare un salvadanaio.

Metti un foglio di carta nel mezzo del modulo sensore di velocità e vedrai una moneta cadere nel salvadanaio sulla scena.

.. image:: img/1.7_header.png

Componenti Necessari
------------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.7_component.png

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
    *   - :ref:`cpn_speed_sensor`
        - \-

Costruisci il Circuito
----------------------------

.. image:: img/1.7_fritzing.png

Carica il Codice e Guarda Cosa Succede
-----------------------------------------

Carica il file di codice (``1.7_piggy_bank.sb3``) su Scratch 3.

I due terminali nel mezzo del sensore di velocità, uno invia luce e l'altro la riceve; se metti un foglio di carta in mezzo per isolare la trasmissione della luce, il sensore di velocità emetterà un livello alto. A questo punto, Scratch riceve il livello alto, cambia i costumi dello sprite e vedrai una moneta cadere nel salvadanaio sulla scena.

Suggerimenti sugli Sprite
--------------------------------

Seleziona Sprite1 e clicca su **Costumi** nell'angolo in alto a sinistra; carica **piggybank1.png**, **piggybank2.png** e **piggybank3.png** dal percorso ``~/raphael-kit/scratch/picture`` tramite il pulsante **Carica Costume**; elimina i 2 costumi predefiniti e rinomina lo sprite in **piggybank**.

.. image:: img/1.7_photoInterrupter1.png

Suggerimenti sui Codici
----------------------------

.. image:: img/1.7_code2.png

Quando pin17 è basso (non sono state inserite monete), cambia il costume dello sprite in **piggybank1**.

.. image:: img/1.7_code3.png

Quando pin17 è alto (è stata inserita una moneta), cambia il costume dello sprite in **piggybank2**, e dopo 0,5 secondi passa a **piggybank3**, così vedremo una moneta cadere nel salvadanaio sulla scena.
