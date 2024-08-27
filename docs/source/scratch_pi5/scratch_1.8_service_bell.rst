.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.8_scratch_pi5:

1.8 Campanello di Servizio
================================

Oggi useremo un Micro Interruttore, altoparlanti, modulo amplificatore audio, Raspberry Pi e Scratch per creare un campanello di servizio.

Premi il Micro Interruttore per far suonare il campanello di servizio.

.. image:: img/1.8_header.png

Componenti Necessari
--------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.8_component.png

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
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_micro_switch`
        - \-
    *   - :ref:`cpn_capacitor`
        - |link_capacitor_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-

Costruire il Circuito
--------------------------

.. image:: img/1.8_fritzing.png


Carica il Codice e Vedi Cosa Succede
------------------------------------------

Carica il file di codice (``1.8_service_bell.sb3``) su Scratch 3.

Premi il micro interruttore e il campanello suonerà una volta.

.. note::

  Se il tuo Raspberry Pi è collegato a uno schermo con altoparlanti, potrebbe non riprodurre suoni tramite l'altoparlante esterno. Consulta :ref:`change_audio_output` per trovare la soluzione.

  Inoltre, se vuoi regolare il livello del volume, consulta :ref:`adjust_volume`.

Suggerimenti sugli Sprite
-----------------------------------

Seleziona Sprite1 e clicca su **Costumi** nell'angolo in alto a sinistra; carica **bell1.png** e **bell2.png** dal percorso ``~/raphael-kit/scratch/picture`` tramite il pulsante **Carica Costume**; elimina i 2 costumi predefiniti e rinomina lo sprite in **bell**.

.. image:: img/1.8_travel1.png

Nell'opzione **Suoni**, carica il file ``bell.wav`` dal percorso ``~/raphael-kit/scratch/sound`` su Scratch 3.

.. image:: img/1.8_travel2.png

Suggerimenti sul Codice
-----------------------------

.. image:: img/1.8_travel3.png
  :width: 400

Quando pin17 è alto (il Micro Interruttore non è premuto), cambia il costume dello sprite **bell** in **bell1** (stato rilasciato).

.. image:: img/1.8_travel4.png
  :width: 400

Premi il micro interruttore, gpio17 sarà a livello basso. In questo momento, cambia il costume dello sprite **bell** in **bell2** (stato premuto), e riproduci un effetto sonoro tramite l'altoparlante.

