.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _blinking_dot:

Punto Lampeggiante
=======================

In questo progetto, disegneremo un punto su Processing, che lampeggia in sincronia con il LED. Per favore, costruisci il circuito come mostrato nello schema ed esegui lo sketch.

.. image:: img/blinking_dot.png
.. image:: img/clickable_dot_on.png

**Componenti Necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti.

È sicuramente conveniente acquistare un kit completo, ecco il link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - ELEMENTI IN QUESTO KIT
        - LINK
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

Puoi anche acquistarli separatamente dai link qui sotto.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUZIONE AI COMPONENTI
        - LINK DI ACQUISTO

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_led`
        - |link_led_buy|

**Cablatura**

.. image:: img/image49.png

**Sketch**

.. code-block:: Arduino

    import processing.io.*;
    int ledPin = 17; 
    boolean state = true; 

    void setup() {
        size(100, 100);
        frameRate(2); //imposta la frequenza dei fotogrammi
        GPIO.pinMode(ledPin, GPIO.OUTPUT); //imposta ledPin su modalità output 
    }

    void draw() {
        state = !state;
        if (state==true) {
            GPIO.digitalWrite(ledPin, GPIO.LOW); //led acceso 
            fill(255, 0, 0); //imposta il colore del led acceso
        } else {
            GPIO.digitalWrite(ledPin, GPIO.HIGH); //led spento
            fill(155); //imposta il colore del led spento
        } 
        ellipse(width/2, height/2, width*0.75, height*0.75);
    }

**Come funziona?**

All'inizio dello sketch, è necessario includere la libreria GPIO di Processing con ``import processing.io.*;``, indispensabile per gli esperimenti con i circuiti.

La **frequenza dei fotogrammi** è la frequenza con cui appaiono i fotogrammi sulla scheda, espressa in hertz (Hz). In altre parole, è anche la frequenza con cui viene chiamata la funzione ``draw()``. In ``setup()``, impostando la **frequenza dei fotogrammi** a 2, la funzione ``draw()`` verrà chiamata ogni 0,5s.

Ogni chiamata alla funzione ``draw()`` inverte il valore di ``state`` e lo valuta. Se il valore è ``true``, il LED si accende e il pennello viene riempito di rosso; altrimenti, il LED si spegne e il pennello viene riempito di grigio.

Dopo aver completato la valutazione, viene utilizzata la funzione ``ellipse()`` per disegnare un cerchio. È importante notare che ``width`` e ``height`` sono variabili di sistema utilizzate per memorizzare la larghezza e l'altezza della finestra di visualizzazione.

Ci sono altri due punti da considerare. Quando si utilizzano i GPIO, è necessario usare la funzione ``GPIO.pinMode()`` per impostare lo stato INPUT/OUTPUT del pin, e successivamente utilizzare la funzione ``GPIO.digitalWrite()`` per assegnare un valore (HIGH/LOW) al pin.

.. note::

    Cerca di evitare di usare ``delay()`` in ``draw()`` perché potrebbe influenzare l'aggiornamento della finestra di visualizzazione.
