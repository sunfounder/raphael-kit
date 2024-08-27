.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.13_scratch_pi5:

1.13 Campanello
==================

Oggi realizzeremo un campanello: clicca sullo sprite Button 3 sullo stage e il buzzer suonerà; clicca di nuovo e il buzzer smetterà di suonare.

.. image:: img/1.13_header.png

Componenti Necessari
-----------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.13_list.png

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
    *   - :ref:`cpn_buzzer`
        - \-
    *   - :ref:`cpn_transistor`
        - |link_transistor_buy|

Costruire il Circuito
------------------------

.. image:: img/1.13_image106.png

Carica il Codice e Vedi Cosa Succede
---------------------------------------

Carica il file di codice (``1.13_doorbell.sb3``) su Scratch 3.

Clicca sulla bandiera verde sullo stage. Quando clicchiamo sullo sprite Button 3, questo diventerà blu e il buzzer suonerà; cliccando di nuovo, lo sprite **Button3** tornerà grigio e il buzzer smetterà di suonare.


Suggerimenti sugli Sprite
-------------------------

Elimina lo sprite predefinito e scegli lo sprite **Button 3**.

.. image:: img/1.13_scratch_button3.png

Imposta quindi la dimensione su 200.

.. image:: img/1.13_scratch_button3_size.png

Suggerimenti sul Codice
---------------------------

.. image:: img/1.13_buzzer4.png
  :width: 400

Questo blocco consente di cambiare il costume dello sprite.

.. image:: img/1.13_buzzer5.png
  :width: 400

Imposta gpio17 su low per far suonare il buzzer; impostalo su high e il buzzer non suonerà più.

Lo switch **status** viene utilizzato qui e useremo un diagramma di flusso per aiutarti a capire l'intero codice.

Quando si clicca sulla bandiera verde, lo **status** viene inizialmente impostato su 0, aspettando che lo sprite venga cliccato; se lo sprite **Button3** viene cliccato, cambierà il costume in **button-b** (blu) e lo **status** verrà impostato su 1. Quando il programma principale riceve lo **status** come 1, farà suonare il buzzer a intervalli di 0,1s. 
Se **Button3** viene cliccato di nuovo, cambierà costume in **button-a** (grigio) e lo **status** tornerà a 0.

.. image:: img/1.13_scratch_code.png
