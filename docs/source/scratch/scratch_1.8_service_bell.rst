.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anticipazioni.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _1.8_scratch:

1.8 Campanello di Servizio
==================================

Oggi utilizzeremo un Micro Switch, altoparlanti, un modulo amplificatore audio, un Raspberry Pi e Scratch per creare un campanello di servizio.

Tocca il Micro Switch per far suonare il campanello di servizio.

.. image:: img/1.8_header.png

Componenti Necessari
---------------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.8_component.png

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
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_micro_switch`
        - \-
    *   - :ref:`cpn_capacitor`
        - |link_capacitor_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-

Costruisci il Circuito
-------------------------

.. image:: img/1.8_fritzing.png


Carica il Codice e Guarda Cosa Succede
--------------------------------------------

Carica il file di codice (``1.8_service_bell.sb3``) su Scratch 3.

Premi il micro switch e il campanello di servizio suonerà una volta.


.. note::
  
  Se il tuo Raspberry Pi è collegato a uno schermo con altoparlanti, potrebbe non emettere suoni da questo altoparlante esterno. Per la soluzione, fai riferimento a :ref:`change_audio_output`.

  Inoltre, se desideri regolare il livello del volume, consulta :ref:`adjust_volume`.

Suggerimenti sugli Sprite
------------------------------

Seleziona Sprite1 e clicca su **Costumi** nell'angolo in alto a sinistra; carica **bell1.png** e **bell2.png** dal percorso ``~/raphael-kit/scratch/picture`` tramite il pulsante **Carica Costume**; elimina i 2 costumi predefiniti e rinomina lo sprite in **campanello**.

.. image:: img/1.8_travel1.png

Nell'opzione **Suoni**, carica il file ``bell.wav`` dal percorso ``~/raphael-kit/scratch/sound`` su Scratch 3.

.. image:: img/1.8_travel2.png

Suggerimenti sui Codici
-----------------------------------

.. image:: img/1.8_travel3.png
  :width: 400

Quando pin17 è alto (il Micro switch non è premuto), cambia il costume dello sprite **campanello** in **bell1** (stato rilasciato).

.. image:: img/1.8_travel4.png
  :width: 400

Premi il micro switch, gpio17 va a livello basso. A questo punto, cambia il costume dello sprite **campanello** in **bell2** (stato premuto) e riproduci un effetto sonoro tramite l'altoparlante.
