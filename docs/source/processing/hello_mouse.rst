.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara & Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _hello_mouse:

Ciao Mouse
====================

In questo progetto, il tuo mouse continuerà a tracciare linee verso un punto; muovi il mouse e disegnerai una linea unica di stelle. Premi il mouse per ricominciare il disegno.

.. image:: img/hello_mouse1.png

**Sketch**

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

    void mousePressed() {
        pointX=mouseX;
        pointY=mouseY;
        background(192, 16, 18);
    }

**Come funziona?**

Il progetto precedente disegnava un'unica immagine senza alcuna animazione o interazione.

Se vogliamo creare uno sketch interattivo, dobbiamo aggiungere le funzioni ``setup()`` e ``draw()`` (queste sono funzioni integrate che vengono chiamate automaticamente) per costruire la cornice.

* ``setup()``: Viene eseguito solo una volta all'avvio dello sketch.
* ``draw()``: Viene eseguito ripetutamente, e solitamente vi aggiungiamo lo sketch per disegnare l'animazione.

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

Questo sketch già funziona senza problemi come sketch interattivo.

Successivamente, puoi aggiungere un evento di clic del mouse. Questo evento può essere implementato con la funzione ``mousePressed()``, dove aggiungiamo istruzioni per aggiornare il punto di destinazione e pulire lo schermo.

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

    void mousePressed() {
        pointX=mouseX;
        pointY=mouseY;
        background(192, 16, 18);
    }

Per ulteriori informazioni consulta la `Processing Reference <https://processing.org/reference/>`_.
