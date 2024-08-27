.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.12_scratch_pi5:

1.12 Lampada d'Acqua
=========================

Oggi utilizzeremo un LED Bar Graph, un Raspberry Pi e Scratch per creare una Lampada d'Acqua.

Il LED Bar Graph si accenderà in sequenza seguendo la direzione delle frecce sul palco.

.. image:: img/1.12_header.png

Componenti Necessari
------------------------

In questo progetto, avremo bisogno dei seguenti componenti. 

.. image:: img/1.12_list.png

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
    *   - :ref:`cpn_bar_graph`
        - \-

Costruire il Circuito
--------------------------

.. image:: img/1.12_image66.png

Carica il Codice e Vedi Cosa Succede
----------------------------------------

Carica il file di codice (``1.12_water_lamp.sb3``) sul tuo computer e aprilo su Scratch 3.

Cliccando su **Arrow1**, i LED sul LED Bar si accendono in sequenza da sinistra a destra (uno alla volta) e poi si spengono. Cliccando su **Arrow2**, i LED si accendono nell'ordine opposto.

Suggerimenti sugli Sprite
-----------------------------

Elimina lo sprite predefinito e scegli lo sprite **Arrow1**.

.. image:: img/1.12_graph1.png

Qui avremo bisogno di 2 sprite **Arrow1**, che possono essere duplicati con il pulsante duplicato.

.. image:: img/1.12_scratch_duplicate.png

Clicca sullo sprite **Arrow 2** e cambia la direzione della freccia selezionando il costume 2.

.. image:: img/1.12_graph2.png


Ora creiamo una variabile.

.. image:: img/1.12_graph3.png


Nominala come **num**.

.. image:: img/1.12_graph4.png


Segui lo stesso metodo per creare una lista chiamata **led**.

.. image:: img/1.12_graph6.png


Dopo aver aggiunto gli elementi, dovresti vedere la variabile **num** e la lista **led** nell'area di lavoro.

Clicca su **+** per aggiungere 10 elementi alla lista e inserisci i numeri dei pin in ordine (17,18,27,22,23,24,25,2,3,8).

.. image:: img/1.12_graph7.png

Suggerimenti sul Codice
------------------------------

.. image:: img/1.12_graph10.png
  :width: 300

Questo è un blocco evento che viene attivato quando lo sprite corrente viene cliccato.

.. image:: img/1.12_graph8.png
  :width: 300

Il valore iniziale della variabile **num** determina quale LED si accenderà per primo.

.. image:: img/1.12_graph9.png

Imposta il pin corrispondente a **num** nella lista led su low per accendere il LED, quindi imposta il pin corrispondente a **num-1** su high per spegnere il LED precedente.
