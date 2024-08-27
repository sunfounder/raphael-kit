.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_ultrasonic_sensor:

Modulo Ultrasuoni
=============================

.. image:: img/ultrasonic_pic.png
    :width: 400
    :align: center

Il modulo di rilevamento a ultrasuoni offre una misurazione senza contatto da 2 cm a 400 cm, con un'accuratezza che può arrivare fino a 3 mm.
Può garantire che il segnale rimanga stabile entro 5 metri, indebolendosi gradualmente dopo i 5 metri fino a scomparire a 7 metri.

Il modulo comprende trasmettitori ultrasonici, ricevitore e circuito di controllo. I principi di base sono i seguenti:

#. Utilizzare un flip-flop IO per generare un segnale di livello alto di almeno 10us.

#. Il modulo invia automaticamente otto impulsi a 40kHz e rileva se vi è un segnale di ritorno.

#. Se il segnale ritorna, passando al livello alto, la durata del livello alto sull'uscita IO corrisponde al tempo trascorso dal momento dell'emissione dell'onda ultrasonica fino al suo ritorno. Qui, la distanza misurata = (tempo di livello alto \* velocità del suono (340 m / s)) / 2.

Il diagramma temporale è riportato di seguito.

.. image:: img/ultrasonic228.png

Basta fornire un breve impulso di 10us all'ingresso di trigger per avviare la misurazione; 
successivamente, il modulo invierà un burst di ultrasuoni di 8 cicli a 40 kHz e rileverà il 
suo eco. È possibile calcolare la distanza attraverso l'intervallo di tempo tra l'invio del 
segnale di trigger e la ricezione del segnale di eco.

Formula: us / 58 = centimetri o us / 148 = pollici; oppure: la distanza = tempo di livello 
alto \* velocità (340M/S) / 2; si consiglia di utilizzare un ciclo di misurazione superiore 
a 60ms per evitare collisioni tra il segnale di trigger e quello di eco.

**Esempi**

* :ref:`2.2.8_c` (C Project)
* :ref:`3.1.3_c` (C Project)
* :ref:`2.2.8_py` (Python Project)
* :ref:`4.1.9_py` (Python Project)
