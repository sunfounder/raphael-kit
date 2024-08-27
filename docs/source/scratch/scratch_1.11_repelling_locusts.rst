.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anticipazioni.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _1.11_scratch:

1.11 Scacciare le cavallette
===============================

Oggi useremo un modulo di evitamento ostacoli a infrarossi, Raspberry Pi e Scratch 
per creare un gioco di respingimento delle cavallette.

Metti la mano davanti al modulo di evitamento ostacoli e vedrai le cavallette scappare via.

.. image:: img/1.11_header.png

Componenti Necessari
---------------------------------

In questo progetto, avremo bisogno dei seguenti componenti. 

.. image:: img/1.11_component.png

È sicuramente comodo acquistare un kit completo, ecco il link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - ELEMENTI NEL KIT
        - LINK
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

Puoi anche acquistarli separatamente dai link qui sotto.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUZIONE AI COMPONENTI
        - LINK PER L'ACQUISTO

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_avoid_module`
        - |link_obstacle_avoidance_buy|

Costruisci il Circuito
--------------------------

.. image:: img/1.11_fritzing.png
    :width: 700
    :align: center

Carica il Codice e Guarda Cosa Succede
-------------------------------------------

Carica il file di codice (``1.11_repelling_locusts.sb3``) su Scratch 3.

Metti la mano davanti al modulo di evitamento ostacoli e vedrai le cavallette scappare via.


Suggerimenti sugli Sprite
----------------------------

Seleziona Sprite1 e clicca su **Costumi** in alto a sinistra; carica **locust1.png**, **locust2.png** e **locust3.png** dal percorso ``~/raphael-kit/scratch/picture`` tramite il pulsante **Carica Costume**; elimina i 2 costumi predefiniti e rinomina lo sprite in **locust**.

.. image:: img/1.11_ir1.png

Suggerimenti sui Codici
---------------------------

.. image:: img/1.11_ir2.png
  :width: 400

Quando il modulo di evitamento ostacoli IR non rileva ostacoli (nessuna mano davanti alla sonda), il gpio è alto.

.. image:: img/1.11_ir3.png
  :width: 400

Quando gpio17 è alto (nessun ostacolo davanti al modulo di evitamento ostacoli IR), cambia il costume dello sprite locust a locust1 (le cavallette si radunano nel grano). Al contrario, quando gpio17 è basso (metti la mano davanti al modulo di evitamento ostacoli IR), cambia il costume dello sprite locust a locust2 (cavallette respinte), poi cambia il costume dello sprite locust a locust3 (cavallette completamente scacciate) dopo 0,5 secondi.
