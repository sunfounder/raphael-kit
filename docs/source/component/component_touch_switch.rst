.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_touch_switch:

Modulo Interruttore a Sfioramento
======================================

.. image:: img/touch168.png
    :width: 300
    :align: center

Il modulo interruttore a sfioramento funziona rilevando un cambiamento di capacità dovuto all'influenza di un oggetto esterno. La piastra a sfioramento è coperta da materiale isolante e l'utente non entra in contatto con il circuito elettrico.

Un interruttore capacitivo ha diversi strati: la piastra superiore isolante seguita dalla piastra a sfioramento, un altro strato isolante e poi la piastra di massa.

.. image:: img/touch169.jpeg

In pratica, un sensore capacitivo può essere realizzato su un PCB a doppia faccia considerando un lato come il sensore a sfioramento e il lato opposto come la piastra di massa del condensatore. Quando si applica tensione tra queste piastre, le due piastre si caricano. In stato di equilibrio, le piastre hanno la stessa tensione della sorgente di alimentazione.

Il circuito del rilevatore di sfioramento contiene un oscillatore la cui frequenza dipende dalla capacità del touchpad. Quando un dito si avvicina al touchpad, la capacità aggiuntiva provoca un cambiamento nella frequenza di questo oscillatore interno. Il circuito rilevatore traccia la frequenza dell'oscillatore a intervalli regolari e, quando lo spostamento supera la soglia di cambiamento, il circuito attiva un evento di pressione del tasto.


**Esempi**


* :ref:`2.1.3_c` (C Project)
* :ref:`2.1.3_py` (Python Project)
* :ref:`1.9_scratch` (Scratch Project)