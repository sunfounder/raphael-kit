.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_led:

LED
==========

.. image:: img/LED.png
    :width: 400

Il diodo emettitore di luce a semiconduttore è un tipo di componente che può convertire l'energia elettrica in energia luminosa tramite giunzioni PN. In base alla lunghezza d'onda, può essere categorizzato in diodo laser, diodo a emissione di infrarossi e diodo a emissione di luce visibile, comunemente noto come diodo a emissione di luce (LED). 
                    
Il diodo ha una conduttività unidirezionale, quindi la corrente fluirà come indicato dalla freccia nel simbolo del circuito. È possibile fornire energia positiva solo all'anodo e negativa al catodo. In questo modo, l'LED si accenderà.

.. image:: img/led_symbol.png


Un LED ha due pin. Quello più lungo è l'anodo, quello più corto è il catodo. Assicurati di non collegarli in modo inverso. C'è una caduta di tensione diretta fissa nell'LED, quindi non può essere collegato direttamente al circuito perché la tensione di alimentazione potrebbe superare questa caduta e causare la bruciatura dell'LED. La tensione diretta degli LED rossi, gialli e verdi è di 1,8 V, mentre quella degli LED bianchi è di 2,6 V. La maggior parte degli LED può sopportare una corrente massima di 20 mA, quindi è necessario collegare una resistenza limitatrice di corrente in serie.

La formula per calcolare il valore della resistenza è la seguente:

    R = (Vsupply – VD)/I

**R** rappresenta il valore della resistenza limitatrice di corrente, **Vsupply** la tensione di alimentazione, **VD** la caduta di tensione e **I** la corrente di lavoro dell'LED.

Qui trovi una presentazione dettagliata sull'LED: `LED - Wikipedia <https://en.wikipedia.org/wiki/Light-emitting_diode>`_.

**Esempi**

* :ref:`1.1.1_c` (C Project)
* :ref:`3.1.6_c` (C Project)
* :ref:`1.1.1_py` (Python Project)
* :ref:`4.1.12_py` (Python Project)
* :ref:`1.1_scratch` (Scratch Project)
