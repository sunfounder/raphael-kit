.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi!

.. _cpn_dot_matrix:

Modulo Matrice LED
==============================

.. image:: img/max7219_module.jpg
    :width: 400
    :align: center

Questo è un modulo matrice a punti 8x8 a catodo comune pilotato dal MAX7219, il modulo funziona a una tensione operativa di 5V, la dimensione è di 50mmx32mmx15mm, il lato sinistro è la porta di ingresso, il lato destro è la porta di uscita, supporta la cascata di più moduli.

* **VCC**: Tensione di alimentazione positiva. Collegare a +5V.
* **GND**: Terra (entrambi i pin GND devono essere collegati).
* **DIN**: Ingresso di dati seriali. I dati vengono caricati nel registro a scorrimento interno a 16 bit sul fronte di salita del segnale CLK.
* **CS**: Ingresso di selezione del chip. I dati seriali vengono caricati nel registro a scorrimento mentre CS è basso. Gli ultimi 16 bit di dati seriali vengono memorizzati sul fronte di salita di CS.
* **CLK**: Ingresso del clock seriale. Frequenza massima di 10MHz. Sul fronte di salita del segnale CLK, i dati vengono trasferiti nel registro a scorrimento interno. Sul fronte di discesa del segnale CLK, i dati vengono trasferiti in uscita da DOUT. Sul MAX7221, l'ingresso CLK è attivo solo quando CS è basso.

**MAX7219**

Il MAX7219 è un driver di visualizzazione a catodo comune compatto con input/output seriale che interfaccia microprocessori (µPs) a display LED numerici a 7 segmenti fino a 8 cifre, display a barra o 64 LED individuali. Include a bordo un decodificatore BCD codice-B, circuiti di scansione multiplex, driver di segmenti e cifre, e una RAM statica 8x8 che memorizza ogni cifra.

È richiesto solo un resistore esterno per impostare la corrente del segmento per tutti i LED. Il MAX7221 è compatibile con SPI™, QSPI™ e MICROWIRE™ e ha driver di segmenti con limitazione della velocità di variazione per ridurre le interferenze elettromagnetiche (EMI).

Un'interfaccia seriale a 4 fili si connette a tutti i µPs comuni. Le singole cifre possono essere indirizzate e aggiornate senza riscrivere l'intero display. Il MAX7219/MAX7221 consente inoltre all'utente di selezionare la decodifica in codice B o senza decodifica per ciascuna cifra.

.. image:: img/max7219_sche.png

* `MAX7219 Datasheet <https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf>`_

**Esempio**

* :ref:`1.1.6_c` (C Project)
* :ref:`3.1.12_c` (C Project)
* :ref:`1.1.6_py` (Python Project)
* :ref:`4.1.19_py` (Python Project)
