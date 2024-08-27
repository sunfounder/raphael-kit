.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.11_scratch_pi5:

1.11 Scacciare le Cavallette
============================


Oggi useremo un modulo di evitamento ostacoli IR, un Raspberry Pi e Scratch per creare un gioco in cui si scacciano le cavallette.

Posiziona la mano davanti al modulo di evitamento ostacoli e vedrai le cavallette allontanarsi.

.. image:: img/1.11_header.png

Componenti Necessari
-------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.11_component.png

È sicuramente comodo acquistare un kit completo, ecco il link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome
        - COMPONENTI IN QUESTO KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

Puoi anche acquistarli separatamente dai link sottostanti.

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

Costruire il Circuito
------------------------

.. image:: img/1.11_fritzing.png
    :width: 700
    :align: center

Carica il Codice e Vedi Cosa Succede
----------------------------------------

Carica il file di codice (``1.11_repelling_locusts.sb3``) su Scratch 3.

Posiziona la mano davanti al modulo di evitamento ostacoli e vedrai le cavallette allontanarsi.


Suggerimenti sugli Sprite
----------------------------

Seleziona Sprite1 e clicca su **Costumi** nell'angolo in alto a sinistra; carica **locust1.png**, **locust1.png** e **locust3.png** dal percorso ``~/raphael-kit/scratch/picture`` tramite il pulsante **Carica Costume**; elimina i 2 costumi predefiniti e rinomina lo sprite in **locust**.

.. image:: img/1.11_ir1.png

Suggerimenti sul Codice
--------------------------

.. image:: img/1.11_ir2.png
  :width: 400

Quando il modulo di evitamento ostacoli IR non rileva ostacoli (nessuna mano davanti alla sonda), gpio è alto.

.. image:: img/1.11_ir3.png
  :width: 400

Quando gpio17 è alto (nessun ostacolo davanti al modulo IR), cambia il costume dello sprite locusta in locust1 (le cavallette si radunano nel grano). Al contrario, quando gpio17 è basso (metti la mano davanti al modulo di evitamento ostacoli IR), cambia il costume dello sprite locusta in locust2 (scaccia le cavallette), poi dopo 0,5 secondi cambia il costume in locust3 (le cavallette sono completamente scacciate).

