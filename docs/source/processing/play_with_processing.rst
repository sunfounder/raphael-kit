.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e Giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _play_with_processing:

Gioca con Processing 
=======================================

Che cos'è Processing？
---------------------------

Processing è un semplice ambiente di programmazione creato per facilitare lo sviluppo di applicazioni orientate visivamente, con un'enfasi sull'animazione e la fornitura di feedback istantaneo attraverso l'interazione. 
Gli sviluppatori volevano un modo per “schizzare” idee in codice. 
Con l'espansione delle sue capacità nell'ultimo decennio, Processing è stato utilizzato non solo per il ruolo di schizzo, ma anche per lavori di produzione avanzati. 
Originariamente costruito come un'estensione specifica del dominio di Java per artisti e designer, Processing è evoluto in uno strumento completo di design e prototipazione utilizzato per installazioni su larga scala, motion graphics e visualizzazioni di dati complesse.

Processing è basato su Java, ma poiché gli elementi di programmazione in Processing sono abbastanza semplici, puoi imparare a usarlo anche se non conosci Java. Se hai familiarità con Java, è meglio dimenticare che Processing ha a che fare con Java per un po', finché non capisci come funziona l'API.


Questo testo è tratto dal tutorial, `Processing Overview <https://processing.org/tutorials/overview/>`_.


Installa Processing
------------------------------

.. note:: 

    Prima di poter utilizzare Processing, è necessario accedere al desktop di Raspberry Pi in remoto (:ref:`remote_desktop`) o collegare un display per il Raspberry Pi.

.. Esegui il seguente comando nel Terminale per installare Processing.

.. .. raw:: html

..    <run></run>

.. .. code-block:: 

..     curl https://processing.org/download/install-arm.sh | sudo sh

.. Una volta completata l'installazione, digita ``processing`` per aprirlo.


.. .. image:: img/processing1.png


.. Per un tutorial dettagliato, fai riferimento a `Pi Processing <https://pi.processing.org/>`_.

#. Prima visita https://processing.org/download e seleziona la versione ``Linux（Raspberry Pi 32-bit）`` o ``Linux（Raspberry Pi 64-bit）``. Utilizzando questo metodo, potrai sempre scaricare l'ultima versione.

    Oppure puoi usare il seguente comando per scaricare Processing dal Terminale.

    .. code-block:: 

        wget https://github.com/benfry/processing4/releases/download/processing-1293-4.3/processing-4.3-linux-arm32.tgz

    .. code-block:: 

        wget https://github.com/benfry/processing4/releases/download/processing-1293-4.3/processing-4.3-linux-arm64.tgz


#. Verrà scaricato un file ``.tar.gz``, che la maggior parte degli utenti Linux dovrebbe conoscere. Estrai il file che hai appena scaricato dalla sua posizione.

    .. code-block:: 

        tar xvfz processing-xxxx.tgz

    Sostituisci xxxx con il resto del nome del file, che è il numero di versione. Questo creerà una cartella chiamata processing-xxxx o qualcosa di simile.

#. Quindi vai a quella directory:

    .. code-block:: 

        cd processing-xxxx

#. E avvialo:

.. code-block:: 

    ./processing

#. Con un po' di fortuna, ora dovrebbe essere visibile la finestra principale di Processing.

    .. image:: img/processing2.png


Installa Hardware I/O
-------------------------

Per poter utilizzare i GPIO del Raspberry Pi, devi aggiungere manualmente una `Hardware I/O library <https://processing.org/reference/libraries/io/index.html>`_.

Clicca su ``Sketch`` -> ``Import Library`` -> ``Add Library...`` 

.. image:: img/import-00.png

Trova Hardware I/O, selezionalo e poi clicca su Install. Una volta terminato, apparirà un'icona con un segno di spunta.

.. image:: img/import-02.png


Progetti
---------------

.. toctree::
    draw_a_matchmaker
    hello_mouse
    blinking_dot
    clickable_dot
    clickable_color_blocks
    inflating_the_dot
    dot_on_the_swing
    metronome
    show_number
    drag_number
