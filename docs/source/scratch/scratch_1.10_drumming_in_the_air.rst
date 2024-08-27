.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anticipazioni.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _1.10_scratch:

1.10 Suonare il Tamburo nell'Aria
==================================

Oggi impareremo a utilizzare la fotocamera del Raspberry Pi, Scratch ha un modulo di espansione per Video Sensing che accende la fotocamera in Scratch e rileva il movimento degli oggetti sulla scena.

.. image:: img/1.10_header.png

Componenti Necessari
------------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.10_list.png

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
    *   - :ref:`cpn_audio_speaker`
        - \-
    *   - :ref:`cpn_camera_module`
        - |link_camera_buy|

Costruisci il Circuito
-------------------------

.. image:: img/1.10_fritzing_speaker.png

.. image:: img/1.10_camera.png

.. note::
  
  Devi fare riferimento a :ref:`cpn_camera_module` per collegare il modulo fotocamera e abilitare l'interfaccia fotocamera del Raspberry Pi.


Carica il Codice e Guarda Cosa Succede
-------------------------------------------

Carica il file di codice (``1.10_drumming_in_the_air.sb3``) su Scratch 3.

Clicca sulla bandierina verde per avviare il gioco, posiziona la tua mano davanti al modulo fotocamera e Scratch 3 farà suonare strumenti musicali quando la tua mano toccherà uno strumento nell'area della scena.

.. note::

  Per una migliore esperienza di gioco, prova a giocare su uno sfondo bianco per evitare interferenze dalla fotocamera causate da altri oggetti.

Suggerimenti sugli Sprite
-----------------------------------

Elimina prima gli sprite predefiniti, poi trova lo sprite **Drum-cymbal** e lo sprite **Drum-snare** e aggiungili.

.. image:: img/1.10_camera1.png

Clicca sull'icona **Aggiungi Estensione** in basso a sinistra di Scratch e aggiungi le estensioni **Musica** e **Video Sensing**.

.. image:: img/1.10_scratch.png

.. image:: img/1.10_scratch2.png

Suggerimenti sui Codici
-------------------------------

.. image:: img/1.10_camera3.png

Quando viene cliccata la bandierina verde, il sistema continua a rilevare se la nostra mano si muove sopra lo sprite **Drum-cymbal** per più di 60. Se è così, si presume che la nostra mano abbia toccato lo sprite e viene riprodotto il suono dello strumento Open Hi-Hat.

.. note::

  L'entità del movimento si riferisce al cambiamento delle coordinate nell'area della scena, calcolato rispetto alla variazione delle coordinate dell'oggetto di rilevamento sulla scena.

.. image:: img/1.10_camera4.png

Allo stesso modo, se viene rilevato che il movimento della nostra mano sullo sprite **Drum-snare** è superiore a 60, si considera che la nostra mano abbia toccato lo sprite e viene riprodotto il suono dello strumento tamburo rullante.

