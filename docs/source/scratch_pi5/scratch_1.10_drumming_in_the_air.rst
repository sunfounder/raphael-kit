.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a giveaway e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.10_scratch_pi5:

1.10 Suonare il Tamburo in Aria
==================================

Oggi impareremo a utilizzare la fotocamera Raspberry Pi. Scratch dispone di un modulo di espansione per il Video Sensing, che attiva la fotocamera in Scratch e rileva il movimento degli oggetti nell'area dello stage.

.. image:: img/1.10_header.png

Componenti Necessari
------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.10_list.png

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
    *   - :ref:`cpn_audio_speaker`
        - \-
    *   - :ref:`cpn_camera_module`
        - |link_camera_buy|

Costruire il Circuito
-------------------------

.. image:: img/1.10_fritzing_speaker.png

.. image:: img/1.10_camera.png

.. note::
  
  Devi fare riferimento a :ref:`cpn_camera_module` per collegare il modulo fotocamera e attivare l'interfaccia della fotocamera del Raspberry Pi.


Carica il Codice e Vedi Cosa Succede
------------------------------------

Carica il file di codice (``1.10_drumming_in_the_air.sb3``) su Scratch 3.

Clicca sulla bandiera verde per avviare il gioco. Posiziona la tua mano davanti al modulo fotocamera e Scratch 3 riprodurrà suoni di strumenti quando la tua mano toccherà uno strumento nell'area dello stage.

.. note::

  Per una migliore esperienza di gioco, prova a giocare su uno sfondo bianco per evitare interferenze con la fotocamera da parte di altri oggetti.

Suggerimenti sugli Sprite
------------------------------

Elimina gli sprite predefiniti, quindi trova gli sprite **Drum-cymbal** e **Drum-snare** e aggiungili.

.. image:: img/1.10_camera1.png

Clicca sull'icona **Aggiungi Estensione** in basso a sinistra su Scratch e aggiungi le estensioni **Musica** e **Video Sensing**.

.. image:: img/1.10_scratch.png

.. image:: img/1.10_scratch2.png

Suggerimenti sul Codice
---------------------------

.. image:: img/1.10_camera3.png

Quando si clicca sulla bandiera verde, si cicla continuamente per rilevare se la nostra mano si muove sopra lo sprite **Drum-cymbal** con un movimento superiore a 60. Se sì, si presume che la nostra mano abbia toccato lo sprite e viene riprodotto il suono dello strumento Hi-Hat aperto.

.. note::

  L'entità del movimento si riferisce al cambiamento delle coordinate nell'area dello stage, calcolato rispetto alla quantità di variazione delle coordinate del target di rilevamento nell'area dello stage.

.. image:: img/1.10_camera4.png

Allo stesso modo, se il movimento della nostra mano sullo sprite **Drum-snare** viene rilevato come superiore a 60, si considera che la mano abbia toccato lo sprite e viene riprodotto il suono dello strumento rullante.
