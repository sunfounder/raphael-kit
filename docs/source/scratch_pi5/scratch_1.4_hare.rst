.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi problemi post-vendita e affronta sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _1.4_scratch_pi5:

1.4 Lepre
==============

Oggi utilizzeremo un pulsante, Raspberry Pi e Scratch per creare una lepre con varie trasformazioni!

Quando premiamo il primo pulsante, la lepre nell'area di scena cambierà il colore del corpo; quando premiamo il secondo pulsante, la lepre cambierà dimensione; quando premiamo il terzo pulsante, la lepre farà un passo avanti.

.. image:: img/1.4_header.png

Componenti Necessari
------------------------------

In questo progetto, abbiamo bisogno dei seguenti componenti.

.. image:: img/1.4_list.png

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
    *   - :ref:`cpn_button`
        - |link_button_buy|

Costruire il Circuito
------------------------

.. image:: img/1.4_scratch_button.png

Carica il Codice e Vedi Cosa Succede
-------------------------------------------

Carica il file di codice (``1.4_hare.sb3``) in Scratch 3.

Ora puoi provare a premere ciascuno dei 3 pulsanti per vedere come cambierà la lepre sulla scena.


Suggerimenti sugli Sprite
-----------------------------

Clicca sul pulsante **Scegli uno Sprite** nell'angolo in basso a destra dell'area sprite, inserisci **Lepre** nella casella di ricerca, quindi clicca per aggiungerla.

.. image:: img/1.4_button1.png

Elimina Sprite1.

.. image:: img/1.4_button2.png


Suggerimenti sul Codice
----------------------------

.. image:: img/1.4_button3.png
  :width: 400

Questo è un blocco evento che si attiva quando il livello di GPIO17 è alto, il che significa che il pulsante è stato premuto in quel momento.

.. image:: img/1.4_button4.png
  :width: 400

Questo è un blocco per cambiare il colore della **Lepre**, l'intervallo del valore è 0 ~ 199, oltre 199 tornerà a 0.

.. image:: img/1.4_button5.png
  :width: 250

Questo è un blocco utilizzato per cambiare la dimensione dello sprite, più alto è il valore, più grande sarà lo sprite.

.. note::
  Lo sprite non può crescere all'infinito e la sua dimensione massima è correlata alla dimensione dell'immagine originale.

.. image:: img/1.4_button6.png
  :width: 200

Questo è un blocco che cambia i costumi dello sprite e, quando il costume della **Lepre** continua a cambiare, esegue una serie di azioni coerenti. Ad esempio, in questo progetto, fai fare un passo avanti alla **Lepre**.
