.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi!

.. _cpn_4_digit:

Display a 7 Segmenti da 4 Cifre
====================================

Il display a 7 segmenti da 4 cifre è composto da quattro display a 7 segmenti che 
lavorano insieme.

.. image:: img/4-digit-sche.png

Il display a 7 segmenti da 4 cifre funziona in modo indipendente. Utilizza il principio 
della persistenza visiva umana per visualizzare rapidamente i caratteri di ciascun 
segmento in un ciclo, formando stringhe continue.

Ad esempio, quando sul display appare "1234", il primo segmento visualizza "1", mentre 
gli altri tre non mostrano nulla. Dopo un breve intervallo, il secondo segmento mostra "2",
e così via. Questo processo è molto veloce (tipicamente 5ms) e, grazie all'effetto 
dell'afterglow ottico e al principio del residuo visivo, siamo in grado di vedere tutti 
e quattro i caratteri contemporaneamente.

.. image:: img/image78.png

**Codici di visualizzazione**

Per aiutarti a comprendere come i display a 7 segmenti (Anodo comune) mostrano i numeri, 
abbiamo disegnato la seguente tabella. I numeri rappresentano i valori da 0 a F visualizzati 
sul display; (DP) GFEDCBA si riferisce al set di LED corrispondenti impostato su 0 o 1. Ad 
esempio, 11000000 indica che DP e G sono impostati su 1, mentre gli altri sono impostati 
su 0. Quindi, il numero 0 viene visualizzato sul display a 7 segmenti, mentre il Codice 
HEX corrisponde al numero esadecimale.

.. image:: img/common_anode.png

**Esempio**

* :ref:`1.1.5_c` (C Project)
* :ref:`3.1.1_c` (C Project)
* :ref:`3.1.6_c` (C Project)
* :ref:`3.1.12_c` (C Project)
* :ref:`1.1.5_py` (Python Project)
* :ref:`4.1.3_py` (Pyhton Project)
* :ref:`4.1.7_py` (Pyhton Project)
* :ref:`4.1.12_py` (Pyhton Project)
* :ref:`4.1.18_py` (Pyhton Project)

