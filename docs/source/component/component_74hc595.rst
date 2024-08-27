.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi!

.. _cpn_74hc595:

74HC595
===========

.. image:: img/74HC595.png

Il 74HC595 è composto da un registro a scorrimento a 8 bit e un registro di memoria con uscite parallele a tre stati. Converte l'ingresso seriale in uscita parallela in modo da poter risparmiare le porte IO di un microcontrollore.
Quando MR (pin 10) è a livello alto e OE (pin 13) è a livello basso, i dati vengono inseriti sul fronte di salita di SHcp e vanno al registro di memoria attraverso il fronte di salita di SHcp. Se i due clock sono collegati insieme, il registro a scorrimento è sempre un impulso avanti rispetto al registro di memoria. Nel registro di memoria è presente un pin di ingresso a scorrimento seriale (Ds), un pin di uscita seriale (Q) e un pulsante di reset asincrono (livello basso). Il registro di memoria fornisce un Bus parallelo a 8 bit in tre stati. Quando OE è attivo (livello basso), i dati nel registro di memoria vengono inviati al bus.

* `Scheda tecnica del 74HC595 <https://www.ti.com/lit/ds/symlink/cd74hc595.pdf?ts=1617341564801>`_

.. image:: img/74hc595_pin.png
    :width: 600

Pin del 74HC595 e le loro funzioni:

* **Q0-Q7**: Pin di uscita dati paralleli a 8 bit, in grado di controllare direttamente 8 LED o 8 pin di un display a 7 segmenti.
* **Q7’**: Pin di uscita seriale, collegato a DS di un altro 74HC595 per connettere più 74HC595 in serie.
* **MR**: Pin di reset, attivo a livello basso.
* **SHcp**: Ingresso della sequenza temporale del registro a scorrimento. Sul fronte di salita, i dati nel registro a scorrimento si spostano successivamente di un bit, cioè i dati in Q1 si spostano su Q2, e così via. Sul fronte di discesa, i dati nel registro a scorrimento rimangono invariati.
* **STcp**: Ingresso della sequenza temporale del registro di memoria. Sul fronte di salita, i dati nel registro a scorrimento si spostano nel registro di memoria.
* **CE**: Pin di abilitazione dell'uscita, attivo a livello basso.
* **DS**: Pin di ingresso dati seriali.
* **VCC**: Tensione di alimentazione positiva.
* **GND**: Massa.

**Esempio**

* :ref:`1.1.4_c` (Progetto in C)
* :ref:`1.1.5_c` (Progetto in C)
* :ref:`3.1.1_c` (Progetto in C)
* :ref:`3.1.6_c` (Progetto in C)
* :ref:`3.1.12_c` (Progetto in C)
* :ref:`1.1.4_py` (Progetto in Python)
* :ref:`1.1.5_py` (Progetto in Python)
* :ref:`4.1.7_py` (Progetto in Python)
* :ref:`4.1.12_py` (Progetto in Python)
* :ref:`4.1.18_py` (Progetto in Python)
