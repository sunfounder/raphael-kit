.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara & Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e anteprime.
    - **Sconti Esclusivi**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni e giveaway durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi!

Video 21: Utilizzo del Sensore Ultrasonico HC-SR04 per l'Ecolocalizzazione
=======================================================================================

Questo tutorial copre il processo di creazione di un sensore di distanza ultrasonico con un Raspberry Pi utilizzando il sensore HC-SR04. 
Il video spiega i principi dell'ecolocalizzazione, introduce i componenti necessari, mostra la configurazione del cablaggio 
e guida passo dopo passo attraverso il processo di programmazione. 
Sottolinea l'importanza della precisione nei tempi di esecuzione del codice per misurazioni accurate delle distanze e promuove buone pratiche ingegneristiche.

1. **Introduzione all'Ecolocalizzazione**: Utilizzo del suono per rilevare la posizione degli oggetti, ispirato da pipistrelli e balene.
2. **Panoramica dei Componenti**: Introduzione al sensore ultrasonico HC-SR04 e alla sua connessione con il Raspberry Pi.
3. **Configurazione del Cablaggio**: Collegamento del sensore HC-SR04 ai pin GPIO del Raspberry Pi per alimentazione, massa, trigger ed eco.
4. **Processo di Programmazione**: Guida al codice Python per generare impulsi ultrasonici, attivare il sensore e misurare il tempo di ritorno dell'eco.
5. **Considerazioni sui Tempi**: Importanza della precisione nei tempi per una misurazione accurata della distanza.
6. **Buone Pratiche Ingegneristiche**: Sottolinea la pianificazione e la comprensione del codice prima dell'implementazione.
7. **Attesa del Pin Echo**: Utilizzo di un ciclo while per attendere che il pin echo vada alto.
8. **Registrazione del Tempo di Inizio**: Cattura del tempo di sistema quando il pin echo va alto per segnare l'inizio della misurazione.
9. **Misurazione del Tempo di Viaggio del Ping**: Calcolo del tempo di viaggio del ping determinando la differenza di tempo tra quando il pin echo va alto e basso.
10. **Conversione delle Unità**: Moltiplicazione del tempo di viaggio del ping per un milione per una migliore leggibilità.
11. **Introduzione di un Ritardo**: Introduzione di un ritardo dopo ogni misurazione per prevenire eco multiple.
12. **Calcolo della Distanza**: Utilizzo della velocità del suono e del tempo di viaggio del ping per calcolare la distanza dall'obiettivo.

**Video**

.. raw:: html

    <iframe width="700" height="500" src="https://www.youtube.com/embed/SoAGLXoQ5XI?si=OPMqLtQ53hKNHs4j" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
