.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi!

.. _cpn_adc0834:

ADC0834
==============

L'ADC0834 è un convertitore analogico-digitale a 8 bit di approssimazione 
successiva, dotato di un multiplexer multicanale configurabile in ingresso 
e di input/output seriale. L'input/output seriale è configurato per interfacciarsi 
con registri a scorrimento standard o microprocessori.

.. image:: img/image309.png


**Sequenza di Operazione**

Una conversione viene avviata abbassando il segnale CS, che abilita tutti i 
circuiti logici. CS deve essere mantenuto basso per l'intero processo di 
conversione. Un segnale di clock viene quindi ricevuto dal processore. Ad 
ogni transizione da basso ad alto del segnale di clock, i dati su DI vengono 
caricati nel registro di indirizzi del multiplexer. Il primo impulso alto in 
ingresso rappresenta il bit di avvio. Una parola di assegnazione da 3 a 4 bit 
segue il bit di avvio. Ad ogni successiva transizione da basso ad alto del 
segnale di clock, il bit di avvio e la parola di assegnazione vengono spostati 
attraverso il registro a scorrimento. Quando il bit di avvio raggiunge la 
posizione di partenza del registro del multiplexer, il canale di ingresso viene 
selezionato e inizia la conversione. L'uscita dello stato del SAR (SARS) si alza 
per indicare che è in corso una conversione, e DI al registro a scorrimento del 
multiplexer viene disabilitato per tutta la durata della conversione.

Viene automaticamente inserito un intervallo di un periodo di clock per consentire 
al canale selezionato del multiplexer di stabilizzarsi. L'uscita dati DO esce dallo 
stato ad alta impedenza e fornisce un livello basso per questo periodo di clock di 
tempo di stabilizzazione del multiplexer. Il comparatore SAR confronta le uscite 
successive della scala resistiva con il segnale analogico in ingresso. L'uscita del 
comparatore indica se l'ingresso analogico è maggiore o minore dell'uscita della scala 
resistiva. Man mano che la conversione procede, i dati della conversione vengono 
contemporaneamente inviati dal pin di uscita DO, con il bit più significativo (MSB) per primo.

Dopo otto periodi di clock, la conversione è completata e l'uscita SARS si abbassa. 
Infine, i dati vengono forniti con il bit meno significativo per primo, successivamente 
allo stream di dati con MSB per primo.

.. image:: img/image175.png


**Tabella di Controllo degli Indirizzi MUX per ADC0834**

.. image:: img/image176.png

* `ADC0831 series Datasheet <https://www.ti.com/lit/ds/symlink/adc0831-n.pdf>`_

**Esempio**

* :ref:`2.1.7_c` (C Project)
* :ref:`2.2.1_c` (C Project)
* :ref:`2.2.2_c` (C Project)
* :ref:`3.1.4_c` (C Project)
* :ref:`3.1.5_c` (C Project)
* :ref:`3.1.7_c` (C Project)
* :ref:`2.1.7_py` (Python Project)
* :ref:`2.2.1_py` (Pyhton Project)
* :ref:`2.2.2_py` (Pyhton Project)
* :ref:`4.1.10_py` (Pyhton Project)
* :ref:`4.1.11_py` (Pyhton Project)
* :ref:`4.1.13_py` (Pyhton Project)