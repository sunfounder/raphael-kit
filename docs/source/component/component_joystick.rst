.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_joystick:

Modulo Joystick
=======================

.. image:: img/joystick_pic.png
    :align: center
    :width: 600

Il concetto di base di un joystick è quello di tradurre il movimento di una leva in informazioni elettroniche che un computer può elaborare.

Per comunicare un'intera gamma di movimenti al computer, un joystick deve misurare la posizione della leva su due assi: l'asse X (da sinistra a destra) e l'asse Y (dall'alto verso il basso). Proprio come in geometria di base, le coordinate X-Y individuano esattamente la posizione della leva.

Per determinare la posizione della leva, il sistema di controllo del joystick monitora semplicemente la posizione di ciascun asse. Il design convenzionale del joystick analogico realizza questo controllo tramite due potenziometri, o resistori variabili.

Il joystick ha anche un ingresso digitale che si attiva quando il joystick viene premuto.

.. image:: img/joystick318.png
    :align: center
    :width: 600
	
**Esempi**

* :ref:`2.1.9_c` (C Project)
* :ref:`3.1.7_c` (C Project)
* :ref:`2.1.9_py` (Python Project)
* :ref:`4.1.13_py` (Python Project)