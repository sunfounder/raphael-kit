.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue abilità.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _1.15_scratch:

1.15 Gonfiare il Palloncino
===============================

Qui giocheremo a un gioco di gonfiaggio del palloncino.

Spostando il cursore verso sinistra, il palloncino inizierà a gonfiarsi e diventerà sempre più grande. Se il palloncino diventa troppo grande, scoppierà; se è troppo piccolo, non si solleverà nell'aria. Dovrai decidere quando spostare l'interruttore a destra per fermare il gonfiaggio.

.. image:: img/1.15_header.png

Componenti Necessari
------------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.15_component.png

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
    *   - :ref:`cpn_slide_switch`
        - |link_slide_switch_buy|
    *   - :ref:`cpn_capacitor`
        - |link_capacitor_buy|

Costruisci il Circuito
---------------------------

.. image:: img/1.15_scratch_fritzing.png

Carica il Codice e Guarda Cosa Succede
-------------------------------------------

Carica il file di codice (``1.15_inflating_the_balloon.sb3``) su Scratch 3.

Spostando il cursore verso sinistra, il palloncino inizierà a gonfiarsi e diventerà sempre più grande. Se il palloncino diventa troppo grande, scoppierà; se è troppo piccolo, non si solleverà nell'aria. Dovrai decidere quando spostare l'interruttore a destra per fermare il gonfiaggio.


Suggerimenti sugli Sprite
--------------------------------

Elimina lo sprite precedente **Sprite1**, quindi aggiungi lo sprite **Balloon1**.

.. image:: img/1.15_slide1.png

In questo progetto viene utilizzato un effetto sonoro di esplosione del palloncino, vediamo come è stato aggiunto.

Clicca sull'opzione **Sound** in alto, quindi clicca su **Upload Sound** per caricare ``boom.wav`` dal percorso ``~/raphael-kit/scratch/sound`` su Scratch 3.

.. image:: img/1.15_slide2.png

Suggerimenti sui Codici
--------------------------------

.. image:: img/1.15_slide3.png
  :width: 500

Questo è un blocco evento, e la condizione di attivazione è che gpio17 sia alto, cioè che l'interruttore sia spostato a sinistra.

.. image:: img/1.15_slide4.png
  :width: 400

Imposta la soglia della dimensione dello sprite Ballon1 su 120.

.. image:: img/1.15_slide7.png
  :width: 400

Sposta le coordinate dello sprite Ballon1 a (0,0), che è il centro dell'area del palco.

.. image:: img/1.15_slide8.png
  :width: 300

Imposta la dimensione dello sprite Ballon1 su 50 e visualizzalo nell'area del palco.

.. image:: img/1.15_slide5.png


Imposta un ciclo per gonfiare il palloncino, questo ciclo si ferma quando l'interruttore a cursore viene spostato a destra.

All'interno di questo ciclo, la dimensione del palloncino aumenta di 1 ogni 0,1s, e se è più grande di ``maxSize``, il palloncino scoppierà, in quel momento si sentirà il suono dell'esplosione e il codice verrà interrotto.

.. image:: img/1.15_slide6.png
  :width: 600

Dopo l'uscita dall'ultimo ciclo (interruttore spostato a destra), determina la posizione dello sprite Ballon1 in base alla sua dimensione. Se la dimensione dello sprite Ballon1 è maggiore di 90, sollevalo (sposta le coordinate a (0, 90), altrimenti atterra (sposta le coordinate a (0, -149)).
