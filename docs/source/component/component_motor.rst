.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_motor:

Motore DC
===================

.. image:: img/image114.jpeg
    :align: center

Questo è un motore DC da 3V. Quando applichi un livello alto e un livello basso ai due terminali, il motore inizierà a ruotare.

* **Dimensioni**: 25*20*15MM
* **Tensione di funzionamento**: 1-6V
* **Corrente a vuoto** (3V): 70mA
* **Velocità a vuoto** (3V): 13000RPM
* **Corrente di stallo** (3V): 800mA
* **Diametro dell'albero**: 2mm

Il motore a corrente continua (DC) è un attuatore continuo che converte l'energia elettrica in energia meccanica. I motori DC fanno funzionare pompe rotative, ventilatori, compressori, giranti e altri dispositivi producendo una rotazione angolare continua.

Un motore DC è costituito da due parti: la parte fissa del motore chiamata **statore** e la parte interna del motore chiamata **rotore** (o **armatura** di un motore DC) che ruota per produrre movimento.
La chiave per generare il movimento è posizionare l'armatura all'interno del campo magnetico del magnete permanente (il cui campo si estende dal polo nord al polo sud). L'interazione tra il campo magnetico e le particelle cariche in movimento (il filo che trasporta corrente genera il campo magnetico) produce la coppia che fa ruotare l'armatura.

.. image:: img/motor_sche.png
    :align: center

La corrente fluisce dal terminale positivo della batteria attraverso il circuito, passando attraverso le spazzole di rame fino al commutatore e poi all'armatura.
Ma a causa delle due interruzioni nel commutatore, questo flusso si inverte a metà di ogni rotazione completa.
Questa inversione continua converte essenzialmente l'alimentazione DC della batteria in AC, permettendo all'armatura di sperimentare la coppia nella direzione giusta al momento giusto per mantenere la rotazione.

**Esempi**

* :ref:`1.3.1_c` (C Project)
* :ref:`3.1.4_c` (C Project)
* :ref:`1.3.1_py` (Python Project)
* :ref:`4.1.10_py` (Python Project)
* :ref:`1.17_scratch` (Scratch Project)