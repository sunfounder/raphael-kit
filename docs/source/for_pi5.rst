.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

Per Pi 5
============================

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
    scratch_pi5/play_with_scratch

Per problemi di compatibilità con altri linguaggi di programmazione, vedere le informazioni dettagliate di seguito:

**Processing**

Quando si utilizza Processing 4 su Raspberry Pi 5, la programmazione GPIO incontra delle sfide. Errori come "Argomento non valido" e "Il pin GPIO 17 sembra non essere disponibile sulla tua piattaforma" si verificano durante l'esecuzione di codice relativo al GPIO (come illustrato nell'immagine allegata). Per ulteriori dettagli, visita: https://github.com/benfry/processing4/issues/807

.. image:: img/pi5_processing.png

**Node.js**

Node.js utilizza la libreria pigpio, che attualmente non supporta il Raspberry Pi 5. Per maggiori informazioni, visita: https://github.com/joan2937/pigpio/issues/589

.. image:: img/pi5_nodejs.png
    :width: 700


Su un sistema a 64 bit, l'importazione della libreria GPIO del Raspberry Pi presenta problemi, portando a un mancato funzionamento. Per maggiori dettagli, visita: https://github.com/raspberrypi/bookworm-feedback/issues/91.
