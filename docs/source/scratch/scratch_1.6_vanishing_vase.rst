.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anticipazioni.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _1.6_scratch:

1.6 Vaso Scomparso
==========================

Adesso facciamo un piccolo trucco di magia, non facciamo nulla e poi il vaso scompare misteriosamente.

.. image:: img/1.6_header.png

Componenti Necessari
--------------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.6_component.png

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
    *   - :ref:`cpn_reed_switch`
        - |link_reed_switch_buy|

Costruisci il Circuito
-------------------------

.. image:: img/1.6_fritzing.png

Carica il Codice e Guarda Cosa Succede
-----------------------------------------

Carica il file di codice (``1.6_vanishing_vase.sb3``) su Scratch 3.

Quando utilizzi un magnete vicino al modulo reed switch, un vaso apparirà sulla scena; allontana il magnete e il vaso scomparirà.

Suggerimenti sugli Sprite
--------------------------------

Seleziona Sprite1 e clicca su **Costumi** nell'angolo in alto a sinistra; carica **desk1.png** e **desk2.png** dal percorso ``~/raphael-kit/scratch/picture`` tramite il pulsante **Carica Costume**; elimina i 2 costumi predefiniti e rinomina lo sprite in **scrivania**.

.. image:: img/1.6_vase.png

Suggerimenti sui Codici
------------------------------

.. image:: img/1.6_reed2.png
  :width: 400

Quando il magnete è vicino al modulo reed switch, gpio17 è basso e il costume dello sprite **scrivania** cambia in **desk1** (il vaso è ancora sulla scrivania).

.. image:: img/1.6_reed3.png
  :width: 400

Dopo aver allontanato il magnete, gpio17 è alto e in questo momento il costume dello sprite **scrivania** cambia in **desk2** (solo la scrivania).
