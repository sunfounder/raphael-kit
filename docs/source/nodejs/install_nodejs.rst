.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Che cos'è Node.js?
=====================

Node.js è stato rilasciato a maggio 2009 e sviluppato da Ryan Dahl. È un ambiente di runtime JavaScript basato sul motore Chrome V8. Utilizza un modello I/O non bloccante e basato su eventi per permettere a JavaScript di funzionare come piattaforma di sviluppo lato server.

In parole semplici, Node.js è JavaScript che gira sul server. Se sei già familiare con JavaScript, allora imparerai facilmente Node.js.

Node.js usa solitamente il comando ``npm install xxx`` per installare pacchetti di terze parti, il che richiede di installare lo strumento npm, simile allo strumento pip in python.

Installare o aggiornare nodejs e npm
---------------------------------------

Esegui i seguenti comandi per installare e aggiornare nodejs e npm.

.. raw:: html

    <run></run>

.. code-block::

    sudo apt-get update
    sudo apt-get install nodejs
    sudo apt-get install npm 
    sudo npm install npm -g

Poi verifica la versione corrente di Node con il seguente comando.

.. raw:: html

    <run></run>

.. code-block::

    node -v

Usa il seguente comando per verificare la versione corrente di npm.

.. raw:: html

    <run></run>

.. code-block::

    npm -v
