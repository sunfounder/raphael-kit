.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.5_scratch_pi5:

1.5 Sveglia il gufo
=======================

Oggi giocheremo a svegliare il gufo.

Quando qualcuno si avvicina al modulo sensore PIR, il gufo si sveglierà dal sonno.

.. image:: img/1.5_header.png

Componenti Necessari
--------------------------------

In questo progetto, abbiamo bisogno dei seguenti componenti.

.. image:: img/1.5_component.png

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
    *   - :ref:`cpn_pir`
        - \-

Costruire il Circuito
-------------------------

.. image:: img/1.5_fritzing.png

Ci sono due potenziometri sul modulo PIR: uno per regolare la sensibilità e l'altro per regolare la distanza di rilevamento. Per far funzionare meglio il modulo PIR, è necessario girarli entrambi in senso antiorario fino alla fine.

.. image:: ../img/PIR_TTE.png
    :width: 400
    :align: center

Carica il Codice e Vedi Cosa Succede
---------------------------------------

Carica il file di codice (``1.5_wake_up_the_owl.sb3``) in Scratch 3.

Quando ti avvicini al modulo sensore PIR, vedrai il gufo nell'area della scena aprire le ali e svegliarsi, e quando ti allontani, il gufo tornerà a dormire.


Suggerimenti sugli Sprite
-----------------------------

Seleziona Sprite1 e clicca su **Costumi** nell'angolo in alto a sinistra; carica **owl1.png** e **owl2.png** dal percorso ``~/raphael-kit/scratch/picture`` tramite il pulsante **Carica Costume**; elimina i 2 costumi predefiniti e rinomina lo sprite in **gufo**.

.. image:: img/1.5_pir1.png

Suggerimenti sul Codice
---------------------------

.. image:: img/1.3_title2.png

Quando viene cliccata la bandiera verde, lo stato iniziale di gpio17 è impostato su basso.

.. image:: img/1.5_owl1.png
  :width: 400

Quando pin17 è basso (nessuno si sta avvicinando), cambia il costume dello sprite gufo in owl1 (stato di sonno).

.. image:: img/1.5_owl2.png
  :width: 400

Quando pin17 è alto (qualcuno si sta avvicinando), cambia il costume dello sprite gufo in owl2 (stato di veglia).
