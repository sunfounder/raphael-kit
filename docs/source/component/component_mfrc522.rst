.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_mfrc522:

Modulo MFRC522
=====================

**RFID**

La Radio Frequency Identification (RFID) si riferisce a tecnologie che
utilizzano la comunicazione wireless tra un oggetto (o tag) e un
dispositivo interrogante (o lettore) per tracciare e identificare
automaticamente tali oggetti. Il raggio di trasmissione del tag è limitato a diversi metri
dal lettore. Non è necessariamente richiesta una linea visibile diretta tra lettore e tag.

La maggior parte dei tag contiene almeno un circuito integrato (IC) e un'antenna.
Il microchip memorizza le informazioni ed è responsabile della gestione della
comunicazione a radiofrequenza (RF) con il lettore. I tag passivi non
hanno una fonte di energia indipendente e dipendono da un segnale elettromagnetico esterno,
fornito dal lettore, per alimentare le loro operazioni. I tag attivi contengono una fonte di energia indipendente, come una
batteria. Pertanto, possono avere capacità di elaborazione e trasmissione migliorate e un raggio d'azione più esteso.

.. image:: img/image230.png


**MFRC522**

MFRC522 è un tipo di chip integrato per la lettura e scrittura di carte. È comunemente
utilizzato nella radio a 13,56 MHz. Lanciato dalla NXP Company, è un chip a contatto non
basso consumo, basso costo e di piccole dimensioni, una scelta ideale per strumenti intelligenti e dispositivi portatili.

Il MFRC522 utilizza un concetto avanzato di modulazione e demodulazione che è
pienamente presente in tutti i tipi di metodi e protocolli di comunicazione 
senza contatto passivi a 13,56 MHz. Inoltre, supporta l'algoritmo di crittografia 
rapida CRYPTO1 per verificare i prodotti MIFARE. MFRC522 supporta anche la serie 
MIFARE di comunicazione senza contatto ad alta velocità, con una velocità di 
trasmissione dati bidirezionale fino a 424kbit/s. Come nuovo membro della serie 
di lettori altamente integrati a 13,56 MHz, il MFRC522 è molto simile ai già 
esistenti MFRC500 e MFRC530, ma presenta anche notevoli differenze. Comunica 
con la macchina host in modo seriale,
richiedendo meno cablaggio. È possibile scegliere tra la modalità SPI, I2C e UART seriale
(simile a RS232), il che aiuta a ridurre il numero di connessioni, risparmiare spazio 
sulla scheda PCB (dimensioni ridotte) e ridurre i costi.

**Esempi**

* :ref:`2.2.10_c` (C Project)
* :ref:`2.2.10_py` (Python Project)
* :ref:`4.1.19_py` (Python Project)