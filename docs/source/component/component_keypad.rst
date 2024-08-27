.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_keypad:

Tastierino
============================

Un tastierino è una matrice rettangolare di 12 o 16 pulsanti OFF-(ON).
I loro contatti sono accessibili tramite un connettore adatto per il collegamento con un cavo piatto o per l'inserimento in una scheda a circuiti stampati.
In alcuni tastierini, ciascun pulsante è collegato a un contatto separato nel connettore, mentre tutti i pulsanti condividono una massa comune.

.. image:: img/keypad314.png

Più frequentemente, i pulsanti sono codificati in matrice, il che significa che ognuno di essi collega una coppia unica di conduttori in una matrice.
Questa configurazione è ideale per il polling da parte di un microcontrollore, che può essere programmato per inviare un impulso di uscita a ciascuno dei quattro fili orizzontali a turno.
Durante ogni impulso, controlla in sequenza i restanti quattro fili verticali per determinare quale, se presente, sta trasmettendo un segnale.
Si dovrebbero aggiungere resistenze di pull-up o pull-down ai fili di ingresso per evitare che gli ingressi del microcontrollore si comportino in modo imprevedibile quando non è presente alcun segnale.

**Esempi**

* :ref:`2.1.8_c` (C Project)
* :ref:`3.1.8_c` (C Project)
* :ref:`3.1.11_c` (C Project)
* :ref:`2.1.8_py` (Python Project)
* :ref:`4.1.14_py` (Python Project)
* :ref:`4.1.17_py` (Python Project)