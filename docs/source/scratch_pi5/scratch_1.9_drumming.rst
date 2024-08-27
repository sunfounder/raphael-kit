.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.9_scratch_pi5:

1.9 Batteria
=================

In questo progetto, suoniamo la batteria con un modulo touch switch.

.. image:: img/1.9_header.png

Componenti Necessari
----------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.9_component.png

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
    *   - :ref:`cpn_touch_switch`
        - |link_touch_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-

Costruire il Circuito
-------------------------

.. image:: img/1.9_fritzing.png


Carica il Codice e Vedi Cosa Succede
---------------------------------------

Carica il file di codice (``1.9_drumming.sb3``) su Scratch 3.

Quando tocchi il modulo touch switch, sentirai il suono dei tamburi provenire dall'altoparlante.


Suggerimenti sugli Sprite
-----------------------------

Elimina lo sprite predefinito, poi trova lo sprite **Drum-snare**, aggiungilo e cambia la dimensione a 200.

.. image:: img/1.9_touch1.png

Scratch ha un'estensione **Musica** per suonare strumenti e tamburi, ora aggiungila tramite il pulsante **Aggiungi Estensione**.

.. image:: img/1.9_touch2.png

Suggerimenti sul Codice
----------------------------

.. image:: img/1.9_touch3.png
  :width: 400

Quando pin17 è basso (non premuto sul modulo touch switch), cambia il costume dello sprite **Drum-snare** in **drum-snare-a**.

.. image:: img/1.9_touch4.png
  :width: 600

Quando tocchi il modulo touch switch, gpio17 è basso. A questo punto, il costume dello sprite **Drum-snare** viene cambiato in **drum-snare-b** e il suono del tamburo viene riprodotto dall'altoparlante.

