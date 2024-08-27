.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

Altre lingue (per Pi 5)
==============================

Il lancio del Raspberry Pi 5 ci ha portato un modello più potente, ma ha anche introdotto alcuni cambiamenti, in particolare per quanto riguarda i GPIO.

Sebbene mantenga l'interfaccia standard a 40 pin, la funzionalità è cambiata a causa della connessione con il nuovo chip RP1 southbridge integrato. Questo chip RP1 personalizzato ora gestisce le periferiche sul Pi 5 e ha comportato varie preoccupazioni di compatibilità.

Linguaggio C
-------------
L'implementazione in linguaggio C si basa sulla libreria wiringPi. Tuttavia, la libreria della community di wiringPi è ora archiviata e non riceve più aggiornamenti, rendendola inadatta ai progetti per Raspberry Pi 5. Per ulteriori informazioni, fai riferimento a: https://github.com/WiringPi/WiringPi

.. image:: img/pi5_c_language.png

Processing
------------
Quando si utilizza Processing 4 su Raspberry Pi 5, la programmazione dei GPIO incontra delle difficoltà. Durante l'esecuzione del codice relativo ai GPIO, si verificano errori come "Argomento non valido" e "Il pin GPIO 17 sembra non essere disponibile sulla tua piattaforma" (come mostrato nell'immagine allegata). Per ulteriori dettagli, visita: https://github.com/benfry/processing4/issues/807

.. image:: img/pi5_processing.png

Node.js
---------
Node.js utilizza la libreria pigpio, che al momento non supporta Raspberry Pi 5. Per maggiori informazioni, visita: https://github.com/joan2937/pigpio/issues/589

.. image:: img/pi5_nodejs.png
    :width: 700

Scratch
--------
Su un sistema a 64 bit, l'importazione della libreria GPIO di Raspberry Pi presenta problemi, causando una mancata risposta. Per ulteriori informazioni, visita: https://github.com/raspberrypi/bookworm-feedback/issues/91

