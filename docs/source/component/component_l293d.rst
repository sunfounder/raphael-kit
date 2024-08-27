.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_l293d:

L293D 
=================

L293D è un driver motore a 4 canali integrato in un chip con alta tensione e alta corrente. 
È progettato per connettersi ai livelli logici standard DTL, TTL e per pilotare carichi induttivi (come bobine di relè, motori DC, stepper motor) e transistor di commutazione di potenza, ecc. 
I motori DC sono dispositivi che trasformano l'energia elettrica continua in energia meccanica. Sono ampiamente utilizzati nella trazione elettrica per la loro eccellente capacità di regolazione della velocità.

Di seguito è riportato il diagramma dei pin. L293D ha due pin (Vcc1 e Vcc2) per l'alimentazione. 
Vcc2 è utilizzato per fornire alimentazione al motore, mentre Vcc1 fornisce alimentazione al chip. Poiché qui viene utilizzato un motore DC di piccole dimensioni, collega entrambi i pin a +5V.

.. image:: img/l293d111.png

Di seguito è riportata la struttura interna di L293D. 
Il pin EN è un pin di abilitazione e funziona solo con livello alto; A rappresenta l'ingresso e Y l'uscita. 
Puoi vedere la relazione tra loro nell'angolo in basso a destra. 
Quando il pin EN è ad alto livello, se A è alto, Y emette livello alto; se A è basso, Y emette livello basso. Quando il pin EN è a livello basso, L293D non funziona.

.. image:: img/l293d334.png

* `L293D Datasheet <https://www.ti.com/lit/ds/symlink/l293d.pdf?ts=1627004062301&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FL293D>`_

**Esempi**

* :ref:`1.3.1_c` (C Project)
* :ref:`3.1.4_c` (C Project)
* :ref:`1.3.1_py` (Python Project)
* :ref:`4.1.10_py` (Python Project)
* :ref:`1.17_scratch` (Scratch Project)