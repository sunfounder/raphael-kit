.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi!

.. _cpn_buzzer:

Cicalino
===========

.. image:: img/buzzer.png
    :width: 600

Come tipo di cicalino elettronico con una struttura integrata, i cicalini alimentati da corrente continua (DC) sono ampiamente utilizzati in computer, stampanti, fotocopiatrici, allarmi, giocattoli elettronici, dispositivi elettronici automobilistici, telefoni, timer e altri prodotti o dispositivi elettronici con funzione vocale.

I cicalini possono essere suddivisi in attivi e passivi (vedi immagine seguente). Ruota il cicalino in modo che i suoi pin siano rivolti verso l'alto: il cicalino con una scheda verde è un cicalino passivo, mentre quello avvolto da un nastro nero è attivo.

La differenza tra un cicalino attivo e uno passivo:

Un cicalino attivo ha una sorgente oscillante integrata, quindi emette suoni quando viene alimentato. Tuttavia, un cicalino passivo non dispone di tale sorgente, pertanto non emetterà suoni se si utilizzano segnali DC; invece, è necessario utilizzare onde quadre con una frequenza compresa tra 2K e 5K per farlo funzionare. Il cicalino attivo è generalmente più costoso di quello passivo a causa dei numerosi circuiti oscillanti integrati.

Di seguito è riportato il simbolo elettrico di un cicalino. Ha due pin, con poli positivo e negativo. La superficie con un + rappresenta l'anodo, mentre l'altro è il catodo.

.. image:: img/buzzer_symbol.png
    :width: 150

Puoi controllare i pin del cicalino: il più lungo è l'anodo e il più corto è il catodo. Non confondere le polarità durante il collegamento, altrimenti il cicalino non emetterà suoni.

`Buzzer - Wikipedia <https://en.wikipedia.org/wiki/Buzzer>`_

**Esempio**

* :ref:`1.2.1_c` (C Project)
* :ref:`1.2.2_c` (C Project)
* :ref:`1.2.1_py` (Python Project)
* :ref:`1.2.2_py` (Python Project)
* :ref:`1.13_scratch` (Scratch Project)
* :ref:`1.14_scratch` (Scratch Project)

