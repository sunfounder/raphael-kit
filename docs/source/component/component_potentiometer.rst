.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_potentiometer:

Potenziometro
==================

.. image:: img/potentiometer.png
    :align: center
    :width: 150

Il potenziometro è un componente resistivo con 3 terminali e il suo valore di resistenza può essere regolato in base a una variazione regolare.

I potenziometri sono disponibili in diverse forme, dimensioni e valori, ma hanno tutti i seguenti elementi in comune:

* Hanno tre terminali (o punti di connessione).
* Hanno una manopola, vite o cursore che può essere spostato per variare la resistenza tra il terminale centrale e uno dei terminali esterni.
* La resistenza tra il terminale centrale e uno dei terminali esterni varia da 0 Ω alla resistenza massima del potenziometro quando la manopola, vite o cursore viene spostata.

Ecco il simbolo del circuito del potenziometro.

.. image:: img/potentiometer_symbol.png
    :align: center
    :width: 400

Le funzioni del potenziometro nel circuito sono le seguenti:

#. Servire come divisore di tensione

    Il potenziometro è un resistore regolabile continuamente. Quando si regola l'albero o la manopola scorrevole del potenziometro, il contatto mobile scivolerà sul resistore. A questo punto, può essere emessa una tensione in base alla tensione applicata sul potenziometro e all'angolo in cui il braccio mobile si è ruotato o alla distanza percorsa.

#. Servire come reostato

    Quando il potenziometro viene utilizzato come reostato, collegare il pin centrale e uno degli altri 2 pin nel circuito. In questo modo si può ottenere un valore di resistenza variabile in modo fluido e continuo lungo il percorso del contatto mobile.

#. Servire come controllore di corrente

    Quando il potenziometro funge da controllore di corrente, il terminale del contatto scorrevole deve essere collegato come uno dei terminali di uscita.

Se desideri saperne di più sul potenziometro, fai riferimento a: `Potenziometro - Wikipedia <https://en.wikipedia.org/wiki/Potentiometer>`_

**Esempi**

* :ref:`2.1.7_c` (C Project)
* :ref:`2.1.7_py` (Python Project)


