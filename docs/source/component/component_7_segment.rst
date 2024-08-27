.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi!

.. _cpn_7_segment:

Display a 7 segmenti
==========================

.. image:: img/7-seg.jpg

Un display a 7 segmenti è un componente a forma di 8 che contiene 7 LED. Ogni LED è 
chiamato segmento - quando viene alimentato, un segmento forma parte di un numero da 
visualizzare.

Esistono due tipi di connessione dei pin: Catodo Comune (CC) e Anodo Comune (CA). Come 
suggerisce il nome, un display CC ha tutti i catodi dei 7 LED collegati, mentre un display 
CA ha tutti gli anodi dei 7 segmenti collegati.

In questo kit utilizziamo il display a 7 segmenti a Catodo Comune, ecco il simbolo elettronico.

.. image:: img/segment_cathode.png
    :width: 800

Ognuno dei LED nel display è assegnato a un segmento posizionale con uno dei suoi pin di 
connessione esteso fuori dal pacchetto plastico rettangolare. Questi pin dei LED sono 
etichettati da "a" a "g", rappresentando ciascun LED individuale. Gli altri pin dei LED 
sono collegati insieme formando un pin comune. Quindi, polarizzando direttamente i pin 
appropriati dei segmenti LED in un ordine particolare, alcuni segmenti si illumineranno 
mentre altri rimarranno spenti, mostrando così il carattere corrispondente sul display.

**Codici di visualizzazione**

Per aiutarti a capire come i display a 7 segmenti (Catodo Comune) mostrano i numeri, 
abbiamo disegnato la seguente tabella. I numeri rappresentano i valori da 0 a F visualizzati 
sul display a 7 segmenti; (DP) GFEDCBA si riferisce al set di LED corrispondenti impostato 
su 0 o 1. Ad esempio, 00111111 significa che DP e G sono impostati su 0, mentre gli altri 
sono impostati su 1. Pertanto, il numero 0 viene visualizzato sul display a 7 segmenti, 
mentre il Codice HEX corrisponde al numero esadecimale.

.. image:: img/segment_code.png

**Esempio**

* :ref:`1.1.4_c` (C Project)
* :ref:`1.1.4_py` (Python Project)
