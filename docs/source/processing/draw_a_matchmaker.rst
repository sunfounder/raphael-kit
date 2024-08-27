.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara & Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _draw_a_matchmaker:

Disegna un Cupido
=========================

Stai utilizzando l'Processing Development Environment (o PDE). Non c'è molto altro: l'area principale è l'Editor di Testo e c'è una fila di pulsanti in alto; questo è il pannello degli strumenti. 
Sotto l'editor trovi l'Area Messaggi, e più in basso ancora la Console. 
L'Area Messaggi è utilizzata per messaggi di una sola riga, mentre la Console fornisce dettagli più tecnici.

Facciamo pratica con l'utilizzo di Processing e disegniamo un cupido.

**Sketch**

Copia lo sketch qui sotto in Processing ed eseguilo. Apparirà una nuova finestra di visualizzazione e un cupido festoso sarà disegnato.

.. code-block:: arduino

    size(200,200);
    background(92, 168, 0); 
    rectMode(CENTER);
    rect(100,120,20,60);
    ellipse(100,80,45,45);
    line(90,150,80,170);
    line(110,150,120,170);
    line(90,110,70,100);
    line(110,110,130,100);

.. image:: img/draw_one1.png

.. note:: 

    Se lo esegui e l'area dei messaggi diventa rossa segnalando degli errori, significa che c'è qualcosa che non va nello sketch. Assicurati di copiare esattamente lo sketch di esempio: i numeri devono essere racchiusi tra parentesi, con virgole tra ciascun numero, e le righe devono terminare con un punto e virgola.


**Come funziona?**

Il punto chiave è capire che la finestra di visualizzazione può essere trattata come un quadrato di carta.

Ogni pixel della finestra di visualizzazione è una coordinata (x,y) che determina la posizione di un punto nello spazio. L'origine (0,0) delle coordinate si trova nell'angolo in alto a sinistra, la direzione positiva dell'asse X è orizzontalmente verso destra, e la direzione positiva dell'asse Y è verticalmente verso il basso.

Quello che dobbiamo fare è specificare quale forma e colore deve apparire a queste coordinate pixel.

Ad esempio, disegniamo un rettangolo di larghezza 20 e altezza 60 con coordinate (100,120) come punto centrale.

.. code-block:: arduino

    rectMode(CENTER);
    rect(100,120,20,60);

.. image:: img/draw_one_coodinate.png

Una volta compresa la relazione tra la finestra di visualizzazione e gli assi, questo sketch non sarà difficile per noi, dobbiamo solo capire alcune semplici istruzioni per il disegno di grafici.

    * ``size(width, height)``: Definisce le dimensioni della finestra di visualizzazione in larghezza e altezza, in unità di pixel.
    * ``background(red, green, blue)``: Imposta il colore di sfondo della finestra di visualizzazione.
    * ``rectMode(mode)``: Modifica il punto di origine dal quale i rettangoli vengono disegnati, cambiando il modo in cui vengono interpretati i parametri forniti a ``rect()``.
    * ``rect(x, y, width, height)``: Disegna un rettangolo sullo schermo.
    * ``ellipse(x, y, width, height)``: Disegna un'ellisse (ovale) sullo schermo.
    * ``line(x1, y1, x2, y2)``: Disegna una linea (un percorso diretto tra due punti) sullo schermo.

Per maggiori dettagli consulta la `Processing Reference <https://processing.org/reference/>`_.
