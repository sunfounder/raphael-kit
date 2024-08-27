.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_reed_switch:

Modulo Interruttore Reed
===============================

.. image:: img/reed_switch.png
    :width: 300
    :align: center

* Utilizza un interruttore reed di tipo normalmente aperto.
* Uscita con comparatore, segnale pulito, buona forma d'onda, forte capacità di pilotaggio, superiore a 15mA.
* Tensione di funzionamento: 3.3V-5V
* Forma di uscita: uscita digitale (0 e 1).
* Con fori per bulloni fissi per un'installazione facile.
* Dimensioni del PCB: 3.2cm x 1.4cm.
* Utilizza comparatore LM393 a tensione ampia.

Il modulo interruttore reed è costituito da un interruttore reed, un potenziometro, un comparatore LM393, un LED, ecc. Il circuito interno è mostrato di seguito. Quando un magnete si avvicina al modulo, esso si attiva e il modulo emette un livello basso; in assenza di magnetismo, il modulo si disattiva e emette un livello alto. La distanza di induzione tra l'interruttore reed e il magnete dovrebbe essere inferiore a 1.5cm; oltre questa distanza, il modulo non sarà sensibile o non si attiverà. È possibile regolare la sensibilità tramite il potenziometro sul modulo.
    
.. image:: img/reedswitch_sche.jpg
    :width: 600
    :align: center

L'interruttore reed, noto anche come interruttore magnetico o reed switch, 
ha due lamelle metalliche interne, sigillate in un tubo di vetro riempito 
di gas inerte. Normalmente le due lamelle si sovrappongono ma sono separate 
da un gap e il circuito è interrotto. Quando un oggetto magnetico si avvicina, 
le due lamelle vengono attratte magneticamente, il circuito si chiude e si attiva. 
Pertanto, l'interruttore reed può essere utilizzato per realizzare un sensore magnetico.
        
.. image:: img/HowItWorksReed.jpg

**Esempi**

* :ref:`2.2.4_c` (C Project)
* :ref:`2.2.4_py` (Python Project)
* :ref:`4.1.6_py` (Python Project)
* :ref:`1.6_scratch` (Scratch Project)
