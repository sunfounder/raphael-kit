.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anticipazioni.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _1.2_scratch:

1.2 Palline Colorate
=========================


Cliccando sulle diverse palline colorate nell'area di scena, il LED RGB si illuminerà in diversi colori.

.. image:: img/1.2_header.png

Componenti Necessari
------------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.2_list.png

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
    *   - :ref:`cpn_rgb_led`
        - |link_rgb_led_buy|

Costruisci il Circuito
-------------------------

.. image:: img/1.2_image61.png


Carica il Codice e Guarda Cosa Succede
--------------------------------------------

Dopo aver caricato il file di codice (``1.2_colorful_balls.sb3``) su Scratch 3, il LED RGB si illuminerà di giallo, blu, rosso, verde o viola rispettivamente quando cliccherai sulla pallina corrispondente.

Suggerimenti sugli Sprite
----------------------------

Elimina lo sprite predefinito, poi scegli lo sprite **Pallina**.

.. image:: img/1.2_ball.png

E duplicalo 5 volte.

.. image:: img/1.2_duplicate_ball.png

Scegli costumi diversi per questi 5 sprite **Pallina** e spostali nelle posizioni corrispondenti.

.. image:: img/1.2_rgb1.png

Suggerimenti sui Codici
----------------------------

Prima di comprendere il codice, dobbiamo capire il `modello di colore RGB <https://it.wikipedia.org/wiki/Modello_di_colore_RGB>`_.

Il modello di colore RGB è un modello di colore additivo in cui la luce rossa, verde e blu viene combinata in vari modi per riprodurre un'ampia gamma di colori.

Miscela di colori additiva: aggiungendo il rosso al verde si ottiene il giallo; aggiungendo il verde al blu si ottiene il ciano; aggiungendo il blu al rosso si ottiene il magenta; aggiungendo insieme tutti e tre i colori primari si ottiene il bianco.

.. image:: img/1.2_rgb_addition.png
  :width: 400

Un LED RGB è una combinazione di 3 LED (LED rosso, LED verde, LED blu) in un unico pacchetto, puoi produrre quasi tutti i colori combinando questi tre colori.
Ha 4 pin, uno dei quali è GND, e gli altri 3 pin controllano rispettivamente i 3 LED.

Quindi il codice per far illuminare il LED RGB di giallo è il seguente.

.. image:: img/1.2_rgb3.png


Quando lo sprite Pallina (pallina gialla) viene cliccato, impostiamo gpio17 su alto (LED rosso acceso), gpio18 su alto (LED verde acceso) e gpio27 su basso (LED blu spento) in modo che il LED RGB si illumini di giallo.

Puoi scrivere codici per gli altri sprite nello stesso modo per far illuminare i LED RGB nei colori corrispondenti.

