.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.14_scratch_pi5:

1.14 Gioco 123 Statuetta di Legno
====================================

Oggi giocheremo al gioco "123 statuetta di legno".

Clicca sulla bandiera verde per iniziare il gioco, tieni premuta la freccia destra sulla tastiera per far muovere il personaggio verso destra. Se la luce verde è accesa, il personaggio può muoversi; ma quando si accende il LED rosso, devi fermare il personaggio; altrimenti, il cicalino continuerà a suonare.

.. image:: img/1.14_header.png

Componenti Necessari
-------------------------

In questo progetto, abbiamo bisogno dei seguenti componenti.

.. image:: img/1.14_component.png

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
        - |link_passive_buzzer_buy|
    *   - :ref:`cpn_led`
        - |link_led_buy|
    *   - :ref:`cpn_transistor`
        - |link_transistor_buy|

Costruisci il Circuito
--------------------------

.. image:: img/1.14_fritzing.png

Carica il Codice e Guarda Cosa Succede
-----------------------------------------

Carica il file di codice (``1.14_123_wooden_man.sb3``) in Scratch 3.

Quando il LED verde è acceso, puoi usare la freccia destra per controllare **Avery** e farlo camminare verso destra; quando il LED rosso è acceso, se continui a far muovere **Avery** verso destra, si attiverà un allarme.

Suggerimenti sugli Sprite
----------------------------
Elimina lo sprite predefinito, poi scegli lo sprite **Avery Walking**.

.. image:: img/1.14_wooden1.png
  :width: 400

Suggerimenti sul Codice
--------------------------

.. image:: img/1.14_wooden2.png
  :width: 400

Imposta tutti i pin su alto.

.. image:: img/1.14_wooden3.png
  :width: 400

Quando il gioco inizia, assegna la variabile di stato a 1, indicando che lo sprite Avery Walking è mobile, quindi imposta gpio18 su basso, accendendo il LED verde per 5 secondi.

.. image:: img/1.14_wooden4.png
  :width: 400

Imposta gpio18 su alto, poi imposta gpio27 su basso, il che significa spegnere il LED verde e accendere il LED giallo per 0,5 secondi.

.. image:: img/1.14_wooden5.png
  :width: 400

Assegna la variabile di stato a 0, il che significa che lo sprite Avery Walking non è più mobile; quindi imposta gpio27 su basso e gpio17 su alto, spegnendo il LED giallo e accendendo il LED rosso per 3 secondi. Infine, imposta gpio17 su alto per spegnere il LED rosso.

.. image:: img/1.14_wooden6.png
  :width: 400

Quando premi la freccia destra sulla tastiera, devi cambiare il costume dello sprite **Avery Walking** per vedere Avery che cammina verso destra. Poi devi verificare il valore della variabile **status**. Se è 0, significa che lo sprite Avery Walking non si sta muovendo in quel momento e il cicalino suonerà per avvertirti che non puoi premere nuovamente la freccia destra.
