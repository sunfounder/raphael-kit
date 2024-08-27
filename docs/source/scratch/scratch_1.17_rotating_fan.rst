.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue abilità.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _1.17_scratch:

1.17 Ventilatore Rotante
========================

In questo progetto realizzeremo una sprite a forma di stella e un ventilatore rotante.

.. image:: img/1.17_header.png

Componenti Necessari
---------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.17_list.png

È sicuramente conveniente acquistare un kit completo, ecco il link:

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
    *   - :ref:`cpn_power_module`
        - \-
    *   - :ref:`cpn_l293d`
        - \-
    *   - :ref:`cpn_motor`
        - |link_motor_buy|

Costruisci il Circuito
-------------------------

.. image:: img/1.17_image117.png

Carica il Codice e Guarda Cosa Succede
-----------------------------------------

Carica il file di codice (``1.17_rotating_fan.sb3``) su Scratch 3.

Dopo aver cliccato sulla bandiera verde nel palco, clicca sulla sprite stella; la sprite e il motore inizieranno a ruotare in senso orario. Puoi cambiare la direzione di rotazione cliccando sulle due sprite **freccia**. Quando clicchi di nuovo sulla sprite **stella**, sia la sprite che il motore smetteranno di ruotare.

Suggerimenti sugli Sprite
-----------------------------

Elimina lo sprite predefinito, poi seleziona la sprite **Stella** e la sprite **Freccia1**, e duplica la Freccia1 una volta.

.. image:: img/1.17_motor1.png

Nell'opzione **Costumi**, cambia la sprite Freccia2 con un costume in una direzione diversa.

.. image:: img/1.17_motor2.png

Regola la dimensione e la posizione dello sprite in modo appropriato.

.. image:: img/1.17_motor3.png


Suggerimenti sui Codici
------------------------

**Diagramma di Flusso**

.. image:: img/1.17_scratch.png

In questo codice, vedrai 2 blocchi rosa, gira a sinistra e gira a destra, che sono i nostri blocchi personalizzati (funzioni).

.. image:: img/1.17_new_block.png

**Come Creare un Blocco?**

Impariamo a creare un blocco (funzione). Il blocco (funzione) può essere utilizzato per semplificare il programma, soprattutto se esegui la stessa operazione più volte. Mettere queste operazioni in un nuovo blocco dichiarato può essere molto conveniente.

Per prima cosa trova **I Miei Blocchi** nella palette dei blocchi, quindi seleziona **Crea un Blocco**.

.. image:: img/1.17_motor4.png

Inserisci il nome del nuovo blocco.

.. image:: img/1.17_motor5.png

Dopo aver scritto la funzione del nuovo blocco nell'area di codifica, salvala e troverai il blocco nella palette dei blocchi.

.. image:: img/1.17_motor6.png

**gira a sinistra**

Questo è il codice all'interno del blocco gira a sinistra per far ruotare il motore in senso antiorario.

.. image:: img/1.17_motor12.png
  :width: 400

**gira a destra**

Questo è il codice all'interno del blocco gira a destra per far ruotare il motore in senso orario.

.. image:: img/1.17_motor11.png
  :width: 400

