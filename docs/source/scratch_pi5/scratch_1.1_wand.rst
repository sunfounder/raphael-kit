.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.1_scratch_pi5:

1.1 Bacchetta Magica
======================

Oggi utilizzeremo LED, Raspberry Pi e Scratch per creare un gioco divertente. Quando agitiamo la bacchetta magica, il LED lampeggerà.

.. image:: img/1.1_header.png

Componenti Necessari
---------------------------------

In questo progetto, avremo bisogno dei seguenti componenti.

.. image:: img/1.1_list.png

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
    *   - :ref:`cpn_led`
        - |link_led_buy|

Costruire il Circuito
--------------------------

.. image:: img/1.1_image49.png

Aggiungi Estensione GPIO
---------------------------

Clicca sul pulsante **Aggiungi Estensione** nell'angolo in basso a sinistra, quindi aggiungi **Raspberry Pi GPIO**, un'estensione che usiamo per tutti i nostri progetti Scratch.

.. image:: img/1.1_scratchled1.png
    :align: center

.. image:: img/1.1_scratchled2.png
    :align: center

.. image:: img/1.1_scratchled3.png
    :align: center

Carica il Codice e Vedi Cosa Succede
-----------------------------------------

Carica il file di codice dal tuo computer (``~/raphael-kit/scratch/code``) su Scratch 3.

.. image:: img/1.1_scratch_step1.png

.. image:: img/1.1_scratch_step2.png

Dopo aver cliccato sulla bacchetta magica nell'area di scena, vedrai che il LED lampeggerà per due secondi.

.. image:: img/1.1_step3.png


Suggerimenti sugli Sprite
------------------------------

Clicca su **Carica Sprite**.

.. image:: img/1.1_upload_sprite.png

Carica **Wand.png** dal percorso ``~/raphael-kit/scratch/picture`` su Scratch 3.

.. image:: img/1.1_upload.png

Infine, elimina **Sprite1**.

.. image:: img/1.1_delete.png

Suggerimenti sul Codice
---------------------------

.. image:: img/1.1_LED1.png
  :width: 300

Questo è un blocco di eventi il cui trigger è cliccare sulla bandiera verde nell'area di scena. All'inizio di tutti i codici è richiesto un evento di trigger, e puoi selezionare altri eventi di trigger nella categoria **Eventi** della **palette dei blocchi**.

.. image:: img/1.1_events.png
  :width: 300

Ad esempio, possiamo ora cambiare l'evento di trigger in un clic sullo sprite.

.. image:: img/1.1_LED2.png
  :width: 300

Questo è un blocco con un numero impostato di cicli. Quando inseriamo il numero 10, gli eventi nel blocco verranno eseguiti 10 volte.

.. image:: img/1.1_LED4.png
  :width: 300

Questo blocco viene utilizzato per mettere in pausa il programma per un certo periodo di tempo in secondi.

.. image:: img/1.1_LED3.png
  :width: 500

Poiché in Scratch viene utilizzato il metodo di denominazione BCM, questo codice imposta GPIO17 (BCM17) a 0V (livello basso). Poiché il catodo del LED è collegato a GPIO17, il LED si accenderà. Al contrario, se imposti GPIO(BCM17) su alto, il LED si spegnerà.
