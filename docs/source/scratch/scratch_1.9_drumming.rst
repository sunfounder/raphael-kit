.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anticipazioni.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _1.9_scratch:

1.9 Suonare il Tamburo
============================

In questo progetto, suoniamo il tamburo con un modulo di interruttore touch.

.. image:: img/1.9_header.png

Componenti Necessari
--------------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.9_component.png

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
    *   - :ref:`cpn_touch_switch`
        - |link_touch_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-

Costruisci il Circuito
-------------------------

.. image:: img/1.9_fritzing.png


Carica il Codice e Guarda Cosa Succede
-----------------------------------------

Carica il file di codice (``1.9_drumming.sb3``) su Scratch 3.

Quando tocchi il modulo dell'interruttore touch, sentirai il suono dei tamburi provenire dall'altoparlante.


Suggerimenti sugli Sprite
----------------------------

Elimina lo sprite predefinito, poi trova lo sprite **Drum-snare** e aggiungilo, e cambia la sua dimensione a 200.

.. image:: img/1.9_touch1.png

Scratch ha un'estensione **Musica** per suonare strumenti e tamburi, ora aggiungila tramite il pulsante **Aggiungi Estensione**.

.. image:: img/1.9_touch2.png

Suggerimenti sui Codici
--------------------------

.. image:: img/1.9_touch3.png
  :width: 400

Quando pin17 è basso (non toccato sul modulo touch), cambia il costume dello sprite **Drum-snare** a **drum-snare-a**.

.. image:: img/1.9_touch4.png
  :width: 600

Quando tocchi il modulo dell'interruttore touch, gpio17 è basso. A questo punto, il costume dello sprite **Drum-snare** viene cambiato in **drum-snare-b** e il suono del tamburo viene riprodotto tramite l'altoparlante.
