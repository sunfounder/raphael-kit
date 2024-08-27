.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino e ESP32 con altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci dei nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e Giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _show_number:

Mostra Numero
=============================================

In questo progetto, usiamo Processing per pilotare un display a 7 segmenti e mostrare cifre da 0 a 9 e lettere da A a F.

**Componenti necessari**

In questo progetto, abbiamo bisogno dei seguenti componenti.

È sicuramente comodo acquistare un intero kit, ecco il link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nome	
        - ELEMENTI IN QUESTO KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

Puoi anche acquistarli separatamente dai link seguenti.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUZIONE AI COMPONENTI
        - LINK DI ACQUISTO

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_7_segment`
        - |link_7segment_buy|
    *   - :ref:`cpn_74hc595`
        - |link_74hc595_buy|

**Schema di collegamento**

.. image:: img/image125.png

**Sketch**

.. code-block:: arduino

	import processing.io.*;

	int SDI=17;   //ingresso dati seriali
	int RCLK=18;  //ingresso clock di memoria (STCP)
	int SRCLK =27;   //ingresso clock del registro a scorrimento (SHCP)


	int[] SegCode= {0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71};

	void hc595_shift(int dat){
	  int i;

	  for(i=0;i<8;i++){
		int n=(0x80 & (dat << i)); 
		if ( n==0){
		  GPIO.digitalWrite(SDI, 0);
		} else {
		  GPIO.digitalWrite(SDI, 1);
		}
		GPIO.digitalWrite(SRCLK, 1);
		delay(1);
		GPIO.digitalWrite(SRCLK, 0);
	  }

		GPIO.digitalWrite(RCLK, 1);
		delay(1);
		GPIO.digitalWrite(RCLK, 0);
	}

	void setup() {
		size(400, 200);
		frameRate(10);
		
		GPIO.pinMode(SDI, GPIO.OUTPUT); 
		GPIO.pinMode(RCLK, GPIO.OUTPUT); 
		GPIO.pinMode(SRCLK, GPIO.OUTPUT); 
	  
		GPIO.digitalWrite(SDI, 0);
		GPIO.digitalWrite(RCLK, 0);
		GPIO.digitalWrite(SRCLK, 0);
		
		fill(0,25,88);
		textAlign(CENTER,CENTER);
		textSize(height*0.8);
	}

	void draw() {

		background(255);
		int number = (frameCount%100)/10;
		text(number, width/2, height/2);
		hc595_shift(SegCode[number]);
	}

**Come funziona?**

Importa ``processing.io.*`` e utilizza la libreria di funzioni GPIO per controllare i pin del display digitale.

Definisci l'array ``SegCode = {0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71}``, che rappresenta un array di codici segmenti da 0 a F in esadecimale (Catodo comune).

La funzione ``setup()`` imposta i tre pin SDI, RCLK e SRCLK come output e inizializza i dati a 0.

La funzione ``hc595_shift(int dat)`` viene utilizzata per trasferire i ``SegCode`` al 74HC595.
 
.. code:: 

	void hc595_shift(int dat){
	  int i;

	  for(i=0;i<8;i++){
		int n=(0x80 & (dat << i));
		if ( n==0){
		  GPIO.digitalWrite(SDI, 0);
		} else {
		  GPIO.digitalWrite(SDI, 1);
		}
		GPIO.digitalWrite(SRCLK, 1);
		delay(1);
		GPIO.digitalWrite(SRCLK, 0);
	  }

		GPIO.digitalWrite(RCLK, 1);
		delay(1);
		GPIO.digitalWrite(RCLK, 0);
	}
 
``n=(0x80 & (dat << i))`` significa spostare i dati a sinistra di ``i`` bit e poi eseguire l'operazione ``&`` con 0x80.

La regola dell'operazione ``&`` è che quando entrambi i lati di ``&`` sono 1, il risultato è 1, altrimenti è 0.

Ad esempio, supponiamo dat=0x3f,i=2(0011 1111 << 2 si sposta a 1111 1100), quindi 1111 1100 & 1000 0000 (0x80)) = 1000 0000.

Infine, assegna i dati al pin SDI (DS) bit per bit.

 
``digitalWrite(SRCLK, 1)`` quando SRCLK genera un impulso di salita da 0 a 1, i dati vengono trasferiti dal registro DS al registro a scorrimento;
 
``digitalWrite(RCLK, 1)`` quando RCLK genera un impulso di salita da 0 a 1, i dati vengono trasferiti dal registro a scorrimento al registro di memoria.

.. code::

	fill(0,25,88);
	textAlign(CENTER,CENTER);
	textSize(height*0.8);

La funzione ``fill()`` usata in ``setup()`` riempie il colore del testo, ``textAlign(CENTER,CENTER)`` è utilizzata per centrare il testo, ``textSize(height*0.8)`` cambia l'altezza del testo al 80% dell'altezza originale.
Queste funzioni permettono di personalizzare lo stile del testo visualizzato in Processing.

.. code::

	void draw() {

		background(255);
		int number = (frameCount%100)/10;
		text(number, width/2, height/2);
		hc595_shift(SegCode[number]);
	}

Il ``frameCount`` è un contatore, correlato a ``frameRate``.
Di default, ``frameRate`` è 60, il che significa che ``frameCount`` si accumulerà 60 volte al secondo.

In questo modo, possiamo far visualizzare a Processing e al display a 7 segmenti cifre da 0 a 9 e lettere da A a F contemporaneamente.
