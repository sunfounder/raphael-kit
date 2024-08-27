.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.2_scratch_pi5:

1.2 Palline Colorate
========================

Cliccando sulle palline colorate nell'area di scena, il LED RGB si accenderà con colori diversi.

.. image:: img/1.2_header.png

Componenti Necessari
-------------------------------

In questo progetto, abbiamo bisogno dei seguenti componenti.

.. image:: img/1.2_list.png

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
    *   - :ref:`cpn_rgb_led`
        - |link_rgb_led_buy|

Costruire il Circuito
-------------------------

.. image:: img/1.2_image61.png

Carica il Codice e Vedi Cosa Succede
-----------------------------------------

Dopo aver caricato il file di codice (``1.2_colorful_balls.sb3``) in Scratch 3, il LED RGB si accenderà di giallo, blu, rosso, verde o viola rispettivamente quando clicchi sulla pallina corrispondente.

Suggerimenti sugli Sprite
-----------------------------

Elimina lo sprite predefinito, poi seleziona lo sprite **Ball**.

.. image:: img/1.2_ball.png

E duplicalo 5 volte.

.. image:: img/1.2_duplicate_ball.png

Scegli costumi diversi per questi 5 sprite **Ball** e spostali nelle posizioni corrispondenti.

.. image:: img/1.2_rgb1.png

Suggerimenti sul Codice
------------------------------
Prima di comprendere il codice, dobbiamo capire il `RGB color model <https://en.wikipedia.org/wiki/RGB_color_model>`_.

Il modello di colore RGB è un modello di colore additivo in cui la luce rossa, verde e blu viene combinata in vari modi per riprodurre un'ampia gamma di colori.

Miscelazione dei colori additiva: aggiungendo rosso al verde si ottiene il giallo; aggiungendo verde al blu si ottiene il ciano; aggiungendo blu al rosso si ottiene il magenta; aggiungendo tutti e tre i colori primari si ottiene il bianco.

.. image:: img/1.2_rgb_addition.png
  :width: 400

Un LED RGB è una combinazione di 3 LED (LED rosso, LED verde, LED blu) in un unico pacchetto; puoi produrre quasi qualsiasi colore combinando questi tre colori.
Ha 4 pin, uno dei quali è GND, mentre gli altri 3 controllano i 3 LED rispettivamente.

Quindi il codice per accendere il LED RGB di colore giallo è il seguente.

.. image:: img/1.2_rgb3.png

Quando si clicca sullo sprite Ball (pallina gialla), impostiamo gpio17 su alto (LED rosso acceso), gpio18 su alto (LED verde acceso) e gpio27 su basso (LED blu spento), così il LED RGB si accenderà di giallo.

Puoi scrivere codici simili per altri sprite per far accendere i LED RGB nei colori corrispondenti.

