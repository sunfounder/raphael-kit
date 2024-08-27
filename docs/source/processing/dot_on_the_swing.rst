.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _dot_on_the_swing:

Punto sull'Altalena
========================

In questo progetto, sono collegati 3 pulsanti: uno per cambiare la dimensione del punto, uno per cambiare la posizione e l'ultimo per cambiare il colore. Se premi tutti e 3 i pulsanti contemporaneamente, otterrai un punto che oscilla e ha un colore variabile.

.. image:: img/dancing_dot.png

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
    *   - :ref:`cpn_button`
        - |link_button_buy|

**Cablatura**

.. image:: img/circuit_dancing_dot.png

**Sketch**

.. code-block:: arduino

    import processing.io.*;

    // Definisci un'istanza dell'oggetto Dot
    Dot myDot;

    // Definisci i pin che leggeranno le pressioni dei pulsanti
    int[] pins = { 18, 23, 24 };

    void setup() {
        size(400, 400);
        // Modifica la modalità colore dello sketch a HSB
        colorMode(HSB, 360, 100, 100);
        noStroke();

        for (int i = 0; i < pins.length; i++) {
            GPIO.pinMode(pins[i], GPIO.INPUT_PULLUP);
        }

        // Crea un Dot al centro dello schermo 
        myDot = new Dot(width / 2, height / 2, 100, 255);
    }

    void draw() {
        background(0); 

        // Modifica gli attributi del Dot in base a quali pulsanti sono premuti
        if (GPIO.digitalRead(pins[0]) == GPIO.LOW) {myDot.setSize();} 
        if (GPIO.digitalRead(pins[1]) == GPIO.LOW) {myDot.setPosition();} 
        if (GPIO.digitalRead(pins[2]) == GPIO.LOW) {myDot.setColor();} 

        // Aggiorna lo stato del Dot
        myDot.update();
        // E disegnalo sullo schermo
        myDot.show();
    }

    class Dot { 

        float initX;
        float initY;
        float currentX;
        float currentY;
        int positionRange = 60;

        float initSize;
        float currentSize;
        int sizeRange = 50;

        int initColor;
        int currentColor;
        int ColorRange = 80;

        float timer = 0.0;
        float speed = 0.06;

        Dot(float x, float y, float s, int c) {
            initX = x;
            initY = y;
            currentX = x;
            currentY = y;

            initSize = s;
            currentSize = s;

            initColor = c;
            currentColor = c;
        }

        void setSize() {
            currentSize = initSize + sizeRange * sin( timer );
        }

        void setPosition() {
            currentY = initY + positionRange * cos( timer *2);
        }

        void setColor() {
            currentColor = int(initColor + ColorRange * sin( timer ));
        }

        void update() {
            timer += speed;
        }

        void show() {
            fill(currentColor, 100, 100); 
            ellipse(currentX, currentY, currentSize, currentSize);
        }
    }

**Come funziona?**

Invece di disegnare direttamente il punto, creiamo qui una classe ``Dot``.
Poi, dichiariamo l'oggetto (in questo caso ``myDot``).

Questo è un modo semplice per disegnare punti con proprietà identiche multiple.
Ad esempio, se aggiungiamo tre funzioni al punto in questo progetto - cambiare dimensione, cambiare posizione e cambiare colore - allora ogni punto che dichiariamo avrà la stessa funzione.
Possiamo usare lo stesso pulsante per far fare loro la stessa cosa, o possiamo usare pulsanti diversi per controllare ogni punto separatamente.

Usare le **classi** rende il tuo sketch elegante, potente e flessibile.

`Class (computer programming) - Wikipedia <https://en.wikipedia.org/wiki/Class_(computer_programming)>`_

Successivamente, diamo un'occhiata più da vicino alla classe ``Dot``.

.. code-block:: arduino

    Dot(float x, float y, float s, int c)

Nella dichiarazione, è necessario passare quattro parametri, che sono il valore delle coordinate X e Y della posizione, la dimensione e il colore (qui è impostato in modalità colore `HSB <https://it.wikipedia.org/wiki/HSB>`_ ).

Ogni parametro sarà assegnato a 2 serie di valori (valore iniziale e valore corrente).

.. code-block:: arduino

    float initX;
    float initY;
    float currentX;
    float currentY;
    int positionRange = 60;

    float initSize;
    float currentSize;
    int sizeRange = 50;

    int initColor;
    int currentColor;
    int ColorRange = 80;

Oltre al valore iniziale e al valore corrente, c'è anche una serie di valori di intervallo. Non è difficile capire che il valore iniziale viene utilizzato per determinare lo stato iniziale del punto (determinato dai parametri in ingresso), mentre il valore corrente cambierà all'interno dell'intervallo per far muovere il punto.

Pertanto, ad eccezione del valore della coordinata X, i valori correnti degli altri tre parametri sono calcolati come segue:

.. code-block:: arduino

    void setSize() {
        currentSize = initSize + sizeRange * sin( timer );
    }

    void setPosition() {
        currentY = initY + positionRange * cos( timer *2);
    }

    void setColor() {
        currentColor = int(initColor + ColorRange * sin( timer ));
    }

Se hai familiarità con le funzioni trigonometriche, non sarà difficile comprendere `sine and cosine <https://en.wikipedia.org/wiki/Sine>`_,  che forniscono una variazione periodica liscia (da -1 a 1) del valore corrente del punto.

Abbiamo anche bisogno di aggiungere un seme, ``timer``, per la variazione periodica. Aggiunge il valore fisso nel metodo ``update()`` e viene chiamato in ``draw()``.

.. code-block:: arduino

    void update() {
        timer += speed;
    }

Infine, il punto viene visualizzato in base al valore corrente utilizzando il metodo ``show()``, che viene anche chiamato in ``draw()``.

.. code-block:: arduino

    void show() {
        fill(currentColor, 100, 100); 
        ellipse(currentX, currentY, currentSize, currentSize);
    }

**E adesso?**

Una volta padroneggiato l'uso delle classi, sarai già in grado di disegnare più punti con le stesse proprietà, quindi perché non provare a fare qualcosa di più interessante.
Ad esempio, perché non disegnare un sistema binario stabile, o creare un gioco simile a 'DUET'?
