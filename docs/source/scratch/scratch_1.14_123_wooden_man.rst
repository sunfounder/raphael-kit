.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue abilità.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _1.14_scratch:

1.14 Gioco del Manichino
==============================

Oggi giocheremo al gioco del manichino 123.

Clicca sulla bandiera verde per iniziare il gioco, tieni premuto il tasto freccia destra sulla tastiera per far camminare lo sprite verso destra. Se la luce verde è accesa, lo sprite può muoversi; ma quando il LED rosso è acceso, devi fermare lo sprite; altrimenti il buzzer continuerà a suonare.

.. image:: img/1.14_header.png

Componenti Necessari
----------------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.14_component.png

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
        - |link_passive_buzzer_buy|
    *   - :ref:`cpn_led`
        - |link_led_buy|
    *   - :ref:`cpn_transistor`
        - |link_transistor_buy|


Costruisci il Circuito
---------------------------

.. image:: img/1.14_fritzing.png


Carica il Codice e Guarda Cosa Succede
------------------------------------------

Carica il file di codice (``1.14_123_wooden_man.sb3``) su Scratch 3.

Quando il LED verde è acceso, puoi usare il tasto freccia destra per controllare **Avery** che cammina verso destra; quando il LED rosso è acceso, se continui a far muovere **Avery**, un allarme suonerà.

Suggerimenti sugli Sprite
------------------------------
Elimina lo sprite predefinito, quindi scegli lo sprite **Avery che Cammina**.

.. image:: img/1.14_wooden1.png
  :width: 400

Suggerimenti sui Codici
-------------------------------

.. image:: img/1.14_wooden2.png
  :width: 400

Inizializza tutti i pin su alto.

.. image:: img/1.14_wooden3.png
  :width: 400

Quando il gioco inizia, assegna la variabile **status** a 1, indicando che lo sprite Avery può muoversi, quindi imposta gpio18 su basso, che accenderà il LED verde per 5 secondi.

.. image:: img/1.14_wooden4.png
  :width: 400

Imposta gpio18 su alto, poi imposta gpio27 su basso, il che significa spegnere il LED verde e accendere il LED giallo per 0,5 secondi.

.. image:: img/1.14_wooden5.png
  :width: 400

Assegna la variabile **status** a 0, il che significa che lo sprite Avery non può muoversi; poi imposta gpio27 su basso e gpio17 su alto, che spegnerà il LED giallo e accenderà il LED rosso per 3 secondi. Infine, imposta gpio17 su alto per spegnere il LED rosso.

.. image:: img/1.14_wooden6.png
  :width: 400

Quando premi il tasto freccia destra sulla tastiera, dobbiamo cambiare il costume dello sprite **Avery che Cammina** al prossimo costume in modo da vedere Avery camminare verso destra. Poi dobbiamo determinare il valore della variabile **status**. Se è 0, significa che lo sprite Avery non si muove in questo momento e il buzzer suonerà per avvertirti che non puoi premere di nuovo il tasto freccia destra.
