.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.15_scratch_pi5:

1.15 Gonfiare il Palloncino
===============================

In questo progetto, giocheremo con un palloncino.

Spostando lo slider a sinistra si inizia a gonfiare il palloncino, che crescerà sempre di più. Se il palloncino diventa troppo grande, scoppierà; se è troppo piccolo, non salirà in aria. Devi giudicare il momento giusto per spostare lo slider a destra e fermare il gonfiaggio.

.. image:: img/1.15_header.png

Componenti Necessari
------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.15_component.png

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
    *   - :ref:`cpn_slide_switch`
        - |link_slide_switch_buy|
    *   - :ref:`cpn_capacitor`
        - |link_capacitor_buy|

Costruisci il Circuito
-------------------------

.. image:: img/1.15_scratch_fritzing.png

Carica il Codice e Guarda Cosa Succede
--------------------------------------------

Carica il file di codice (``1.15_inflating_the_balloon.sb3``) in Scratch 3.

Spostando lo slider a sinistra, il palloncino inizierà a gonfiarsi sempre di più. Se diventa troppo grande, scoppierà; se è troppo piccolo, non salirà in aria. Devi decidere quando spostare lo slider a destra per fermare il gonfiaggio.


Suggerimenti sugli Sprite
------------------------------

Elimina lo sprite Sprite1 precedente, poi aggiungi lo sprite **Balloon1**.

.. image:: img/1.15_slide1.png

Questo progetto utilizza un effetto sonoro di esplosione del palloncino, vediamo come aggiungerlo.

Clicca sull'opzione **Suono** in alto, quindi clicca su **Carica Suono** per caricare il file ``boom.wav`` dal percorso ``~/raphael-kit/scratch/sound`` su Scratch 3.

.. image:: img/1.15_slide2.png

Suggerimenti sul Codice
---------------------------

.. image:: img/1.15_slide3.png
  :width: 500

Questo è un blocco evento, e la condizione di attivazione è che gpio17 sia alto, cioè che lo switch sia spostato a sinistra.

.. image:: img/1.15_slide4.png
  :width: 400

Imposta la soglia della dimensione dello sprite Balloon1 a 120.

.. image:: img/1.15_slide7.png
  :width: 400

Sposta le coordinate dello sprite Balloon1 a (0,0), che è il centro dell'area dello stage.

.. image:: img/1.15_slide8.png
  :width: 300

Imposta la dimensione dello sprite Balloon1 a 50 e mostralo nell'area dello stage.

.. image:: img/1.15_slide5.png


Imposta un ciclo per gonfiare il palloncino. Questo ciclo si interrompe quando lo slider viene spostato a destra.

All'interno di questo ciclo, la dimensione del palloncino aumenta di 1 ogni 0.1s, e se supera ``maxSize``, il palloncino scoppierà, in quel momento verrà riprodotto il suono di esplosione e il codice si interromperà.

.. image:: img/1.15_slide6.png
  :width: 600

Dopo che l'ultimo ciclo si interrompe (lo slider viene spostato a destra), determina 
la posizione dello sprite Balloon1 in base alla sua dimensione. Se la dimensione dello 
sprite Balloon1 è maggiore di 90, salirà (sposta le coordinate a (0, 90)), altrimenti 
atterrerà (sposta le coordinate a (0, -149)).

