.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

Per Raspberry Pi 5
==============================================

Il rilascio del Raspberry Pi 5 ci ha portato un modello più potente, ma ha 
introdotto anche alcune modifiche, 
in particolare per quanto riguarda il GPIO. Sebbene mantenga l'interfaccia 
standard a 40 pin, la funzionalità è cambiata a causa della connessione con 
il nuovo chip southbridge RP1 integrato. Questo chip personalizzato RP1 gestisce 
ora le periferiche sul Pi 5, causando varie problematiche di compatibilità. 
Attualmente, solo la libreria GPIO Zero, mantenuta ufficialmente dall'organizzazione 
Raspberry Pi, è completamente compatibile. Abbiamo sviluppato una serie di corsi 
specificamente focalizzati su questa libreria.

.. toctree::
    :maxdepth: 1
    
    python_pi5/play_with_python_pi5
    c_pi5/play_with_c
