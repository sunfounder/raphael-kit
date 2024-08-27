.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_speed_sensor:

Modulo Sensore di Velocità
=============================

.. image:: img/speed_sensor1.png
    :width: 300
    :align: center

Il sensore di velocità è composto da due parti: un trasmettitore e un ricevitore. Il trasmettitore emette luce, che poi entra nel ricevitore.

Se il fascio di luce tra l'emettitore e il ricevitore viene interrotto da un ostacolo, il ricevitore non rileverà la luce incidente e il pin D0 emetterà un livello basso.

.. note::
    Il pin A0 su questo modulo è vuoto e non è collegato a nessun circuito.

.. image:: img/speed_sensor2.png

**Esempi**

* :ref:`2.2.6_c` (C Project)
* :ref:`2.2.6_py` (Python Project)
* :ref:`1.7_scratch` (Scratch Project)