.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.6_scratch_pi5:

1.6 Vaso Magico
========================

Ora facciamo un piccolo trucco di magia: senza fare nulla, il vaso sparirà improvvisamente.

.. image:: img/1.6_header.png

Componenti Necessari
------------------------------

In questo progetto, abbiamo bisogno dei seguenti componenti.

.. image:: img/1.6_component.png

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
    *   - :ref:`cpn_reed_switch`
        - |link_reed_switch_buy|

Costruire il Circuito
------------------------

.. image:: img/1.6_fritzing.png

Carica il Codice e Vedi Cosa Succede
----------------------------------------

Carica il file di codice (``1.6_vanishing_vase.sb3``) in Scratch 3.

Quando avvicini un magnete al modulo reed switch, sul palco apparirà un vaso; togli il magnete e il vaso scomparirà.

Suggerimenti sugli Sprite
--------------------------------

Seleziona Sprite1 e clicca su **Costumi** nell'angolo in alto a sinistra; carica **desk1.png** e **desk2.png** dal percorso ``~/raphael-kit/scratch/picture`` tramite il pulsante **Carica Costume**; elimina i 2 costumi predefiniti e rinomina lo sprite in **desk**.

.. image:: img/1.6_vase.png

Suggerimenti sul Codice
---------------------------

.. image:: img/1.6_reed2.png
  :width: 400

Quando il magnete è vicino al modulo reed switch, gpio17 è basso e il costume dello sprite **desk** viene cambiato in **desk1** (il vaso è ancora sulla scrivania).

.. image:: img/1.6_reed3.png
  :width: 400

Dopo aver tolto il magnete, gpio17 è alto; a questo punto, il costume dello sprite **desk** viene cambiato in **desk2** (solo la scrivania).

