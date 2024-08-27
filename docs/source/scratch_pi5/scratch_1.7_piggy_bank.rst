.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.7_scratch_pi5:

1.7 Salvadanaio
=========================

In questo progetto utilizzeremo un modulo sensore di velocità, Raspberry Pi e Scratch per realizzare un salvadanaio.

Posiziona un pezzo di carta al centro del modulo sensore di velocità e vedrai una moneta cadere nel salvadanaio sul palco.


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
        - OGGETTI IN QUESTO KIT
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
    *   - :ref:`cpn_speed_sensor`
        - \-

Costruire il Circuito
------------------------

.. image:: img/1.7_fritzing.png

Carica il Codice e Vedi Cosa Succede
-----------------------------------------

Carica il file di codice (``1.7_piggy_bank.sb3``) su Scratch 3.

I 2 terminali al centro del sensore di velocità, uno invia la luce, l'altro la riceve; se posizioni un pezzo di carta al centro per isolare la trasmissione della luce, il sensore di velocità emetterà un segnale di alto livello. A questo punto, Scratch riceve il segnale di alto livello, quindi cambia i costumi dello sprite e vedrai una moneta cadere nel salvadanaio sul palco.

Suggerimenti sugli Sprite
------------------------------

Seleziona Sprite1 e clicca su **Costumi** nell'angolo in alto a sinistra; carica **piggybank1.png**, **piggybank2.png** e **piggybank3.png** dal percorso ``~/raphael-kit/scratch/picture`` tramite il pulsante **Carica Costume**; elimina i 2 costumi predefiniti e rinomina lo sprite in **piggybank**.

.. image:: img/1.7_photoInterrupter1.png

Suggerimenti sul Codice
-----------------------------

.. image:: img/1.7_code2.png

Quando pin17 è basso (non ci sono monete nel salvadanaio), cambia il costume dello sprite in **piggybank1**.

.. image:: img/1.7_code3.png

Quando pin17 è alto (è stata inserita una moneta), cambia il costume dello sprite in **piggybank2**, e dopo 0,5s passa a **piggybank3**, così vedremo una moneta cadere nel salvadanaio sul palco.

