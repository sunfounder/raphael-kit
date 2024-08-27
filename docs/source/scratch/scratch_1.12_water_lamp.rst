.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime.
    - **Sconti Speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _1.12_scratch:

1.12 Lampada d'Acqua
==============================

Oggi useremo il Grafico a Barre LED, Raspberry Pi e Scratch per creare una Lampada d'Acqua.

Le barre LED si accenderanno in sequenza seguendo la direzione delle frecce sul palco.

.. image:: img/1.12_header.png

Componenti Necessari
----------------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.12_list.png

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
    *   - :ref:`cpn_bar_graph`
        - \-

Costruisci il Circuito
-----------------------------

.. image:: img/1.12_image66.png

Carica il Codice e Guarda Cosa Succede
-----------------------------------------

Carica il file di codice (``1.12_water_lamp.sb3``) dal tuo computer su Scratch 3.

Cliccando su **Arrow1**, i LED sul grafico a barre si accenderanno in sequenza da sinistra a destra (uno alla volta) e poi si spegneranno. Clicca su **Arrow2** e i LED si accenderanno nell'ordine opposto.

Suggerimenti sugli Sprite
---------------------------------

Elimina lo sprite predefinito e scegli lo sprite **Arrow1**.

.. image:: img/1.12_graph1.png

Avremo bisogno di 2 sprite **Arrow1**, che possono essere duplicati con il pulsante duplica.

.. image:: img/1.12_scratch_duplicate.png

Clicca sullo sprite **Arrow2** e cambia la direzione della freccia selezionando il costume 2.

.. image:: img/1.12_graph2.png

Ora creiamo una variabile.

.. image:: img/1.12_graph3.png

Nominala **num**.

.. image:: img/1.12_graph4.png

Segui lo stesso metodo per creare una lista chiamata **led**.

.. image:: img/1.12_graph6.png

Dopo averla aggiunta, dovresti vedere la variabile **num** e la lista **led** nell'area del palco.

Clicca su **+** per aggiungere 10 elementi alla lista e inserisci i numeri dei pin in ordine (17,18,27,22,23,24,25,2,3,8).

.. image:: img/1.12_graph7.png

Suggerimenti sui Codici
------------------------------

.. image:: img/1.12_graph10.png
  :width: 300

Questo è un blocco di eventi che si attiva quando lo sprite corrente viene cliccato.

.. image:: img/1.12_graph8.png
  :width: 300

Il valore iniziale della variabile **num** determina quale LED si accende per primo.

.. image:: img/1.12_graph9.png

Imposta il pin corrispondente a **num** nella lista led su basso per accendere il LED, e poi imposta il pin corrispondente a **num-1** su alto per spegnere il LED precedente.

