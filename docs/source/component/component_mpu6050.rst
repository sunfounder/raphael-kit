.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_mpu6050:

Modulo MPU6050
=====================

.. image:: img/mpu6050_pic.png
    :width: 200
    :align: center

L'MPU-6050 è un dispositivo di tracciamento del movimento a 6 assi 
(combina un giroscopio a 3 assi e un accelerometro a 3 assi).

I suoi tre sistemi di coordinate sono definiti come segue:

Posiziona l'MPU6050 piatto sul tavolo, assicurandoti che la faccia 
con l'etichetta sia rivolta verso l'alto e che un punto su questa 
superficie sia nell'angolo in alto a sinistra. La direzione verticale 
verso l'alto è l'asse Z del chip. La direzione da sinistra a destra è 
considerata l'asse X. Di conseguenza, la direzione da dietro a davanti 
è definita come asse Y.

.. image:: img/mpu223.png


**Accelerometro a 3 assi**

L'accelerometro si basa sul principio dell'effetto piezoelettrico, la capacità 
di alcuni materiali di generare una carica elettrica in risposta a uno stress 
meccanico applicato.

Immagina una scatola cuboidale con una piccola sfera all'interno, come nell'immagine 
sopra. Le pareti di questa scatola sono fatte di cristalli piezoelettrici. Ogni volta 
che inclini la scatola, la sfera viene costretta a muoversi nella direzione dell'inclinazione, 
a causa della gravità. La parete con cui la sfera collide crea piccole correnti piezoelettriche. 
Ci sono in totale tre coppie di pareti opposte in un cuboide. Ogni coppia corrisponde a un asse 
nello spazio tridimensionale: X, Y e Z. A seconda della corrente prodotta dalle pareti piezoelettriche, 
possiamo determinare la direzione dell'inclinazione e la sua entità.

.. image:: img/mpu224.png


Possiamo utilizzare l'MPU6050 per rilevare la sua accelerazione su ciascun asse di 
coordinate (nello stato statico da scrivania, l'accelerazione sull'asse Z è pari a 1 
unità di gravità, mentre sugli assi X e Y è pari a 0). Se è inclinato o in condizioni 
di assenza di peso/sovrappeso, la lettura corrispondente cambierà.

Ci sono quattro tipi di intervalli di misura che possono essere selezionati programmando:
 +/-2g, +/-4g, +/-8g e +/-16g (2g per impostazione predefinita), corrispondenti a ciascuna 
 precisione. I valori vanno da -32768 a 32767.

La lettura dell'accelerometro viene convertita in un valore di accelerazione mappando la 
lettura dall'intervallo di lettura all'intervallo di misura.

Accelerazione = (Dati grezzi dell'asse dell'accelerometro / 65536 \* Intervallo di accelerazione 
a piena scala) g

Prendendo come esempio l'asse X, quando i dati grezzi dell'asse X dell'accelerometro sono 
16384 e l'intervallo è selezionato come +/-2g:

**Accelerazione lungo l'asse X = (16384 / 65536 \* 4) g**  **=1g**

**Giroscopio a 3 assi**

I giroscopi si basano sul principio dell'accelerazione di Coriolis. Immagina una struttura 
simile a una forcella, che è in costante movimento avanti e indietro. È tenuta in posizione 
utilizzando cristalli piezoelettrici. Ogni volta che tenti di inclinare questa struttura, i 
cristalli subiscono una forza nella direzione dell'inclinazione. Questo è causato dall'inerzia 
della forcella in movimento. I cristalli quindi producono una corrente in accordo con l'effetto 
piezoelettrico, e questa corrente viene amplificata.

.. image:: img/mpu225.png

Anche il giroscopio ha quattro tipi di intervalli di misura: +/- 250, +/- 500, +/- 1000,
 +/- 2000. Il metodo di calcolo e l'Accelerazione sono fondamentalmente coerenti.

La formula per convertire la lettura in velocità angolare è la seguente:

Velocità angolare = (Dati grezzi dell'asse del giroscopio / 65536 \* Intervallo del 
giroscopio a piena scala) °/s

Prendendo come esempio l'asse X, i dati grezzi dell'asse X dell'accelerometro sono 16384 
e l'intervallo è + / - 250°/ s:

**Velocità angolare lungo l'asse X = (16384 / 65536 \* 500)°/s** **=125°/s**

**Esempi**

* :ref:`2.2.9_c` (C Project)
* :ref:`2.2.9_py` (Python Project)