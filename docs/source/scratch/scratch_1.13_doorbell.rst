.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue abilità.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _1.13_scratch:

1.13 Campanello
====================

Oggi costruiremo un campanello: clicca sullo sprite Button 3 sul palco, il buzzer suonerà; clicca di nuovo e il buzzer smetterà di suonare.

.. image:: img/1.13_header.png

Componenti Necessari
------------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.13_list.png

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
    *   - :ref:`cpn_buzzer`
        - \-
    *   - :ref:`cpn_transistor`
        - |link_transistor_buy|

Costruisci il Circuito
----------------------------

.. image:: img/1.13_image106.png

Carica il Codice e Guarda Cosa Succede
---------------------------------------------

Carica il file di codice (``1.13_doorbell.sb3``) su Scratch 3.

Clicca sulla bandiera verde sul palco. Quando clicchiamo sullo sprite Button 3, questo diventerà blu e il buzzer suonerà; cliccando di nuovo, lo sprite **Button3** tornerà grigio e il buzzer smetterà di suonare.


Suggerimenti sugli Sprite
-----------------------------

Elimina lo sprite predefinito, quindi scegli lo sprite **Button 3**.

.. image:: img/1.13_scratch_button3.png

Imposta poi la dimensione su 200.

.. image:: img/1.13_scratch_button3_size.png

Suggerimenti sui Codici
----------------------------

.. image:: img/1.13_buzzer4.png
  :width: 400

Questo blocco ti permette di cambiare il costume dello sprite.

.. image:: img/1.13_buzzer5.png
  :width: 400

Imposta gpio17 su basso per far suonare il buzzer; impostalo su alto e il buzzer non suonerà.


Qui utilizziamo l'interruttore **status**, e useremo un diagramma di flusso per aiutarti a comprendere tutto il codice.

Quando viene cliccata la bandiera verde, lo **status** verrà inizialmente impostato su 0 e il programma attenderà che lo sprite venga cliccato; se lo sprite **button3** viene cliccato, il costume verrà cambiato in **button-b** (blu) e lo **status** sarà impostato su 1. Quando il programma principale riceve lo **status** pari a 1, farà suonare il buzzer a intervalli di 0,1s. Se **button3** viene cliccato di nuovo, il costume sarà cambiato in **button-a** (grigio) e lo **status** sarà nuovamente impostato su 0.

.. image:: img/1.13_scratch_code.png

