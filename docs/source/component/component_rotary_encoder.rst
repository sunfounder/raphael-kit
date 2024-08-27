.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_rotary_encoder:

Modulo Encoder Rotativo
=============================

.. image:: img/rotary_encoder_pic.png
    :width: 300
    :align: center

Un encoder rotativo è un sensore di posizione che converte la rotazione di una manopola in un segnale di uscita, indicando la direzione in cui la manopola viene ruotata.

Gli encoder rotativi sono versioni digitali dei potenziometri, offrendo una maggiore versatilità. Possono ruotare continuamente, mentre i potenziometri hanno una rotazione limitata. I potenziometri indicano la posizione esatta della manopola, mentre gli encoder rotativi mostrano le variazioni di posizione.

Esistono principalmente due tipi di encoder rotativi: assoluti e incrementali (relativi). In questo kit viene utilizzato un encoder incrementale.

Gli encoder incrementali producono onde quadre bifase, con una differenza di fase di 90 gradi comunemente indicata come canali A e B.

Come illustrato di seguito, quando il canale A passa da un livello alto a un livello basso, se il canale B è a un livello alto, significa che l'encoder rotativo sta ruotando in senso orario (CW); se in quel momento il canale B è a un livello basso, significa che la rotazione è in senso antiorario (CCW). Pertanto, leggendo il valore del canale B quando il canale A è a un livello basso, possiamo determinare la direzione in cui l'encoder rotativo ruota.



.. image:: img/image206.png
    :width: 600
    :align: center
	
**Esempi**


* :ref:`2.1.6_c` (C Project)
* :ref:`2.1.6_py` (Python Project)
