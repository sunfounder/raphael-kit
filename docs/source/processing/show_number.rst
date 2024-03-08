.. _show_number:

Zahlenanzeige
=============================================

In diesem Projekt verwenden wir Processing, um eine 7-Segment-Anzeige zu steuern, die eine Zahl von 0 bis 9 und einen Buchstaben von A bis F anzeigt.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein komplettes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

Sie können sie auch einzeln über die untenstehenden Links kaufen.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - KOMPONENTENBESCHREIBUNG
        - KAUF-LINK

    *   - :ref:`cpn_gpio_board`
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

**Verdrahtung**

.. image:: img/image125.png

**Skizze**

.. code-block:: arduino

	import processing.io.*;

	int SDI=17;   //serial data input
	int RCLK=18;  //memory clock input(STCP)
	int SRCLK =27;   //shift register clock input(SHCP)


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

**Wie funktioniert das?**

Importieren Sie ``processing.io.*`` und verwenden Sie die GPIO-Funktionsbibliothek, um die Pins der Digitalröhre zu steuern.

Definieren Sie das Array ``SegCode = {0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71}``, 
welches ein Segment-Code-Array von 0 bis F im Hexadezimalformat (Gemeinsame Kathode) darstellt.

Die ``setup()`` Funktion legt die drei Pins SDI, RCLK und SRCLK als Ausgang fest und die Anfangsdaten als 0.

Die Funktion ``hc595_shift(int dat)`` wird verwendet, um das ``SegCode`` auf 74HC595 zu verschieben.

.. code:: 

	void hc595_shift(int dat){
	  int i;

	  for(i=0;i<8;i++){
		int n=(0x80 & (dat << i));
		if (n==0){
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

``n=(0x80 & (dat << i))`` bedeutet, dass dat um ``i`` Bits nach links verschoben und dann mit 0x80 verknüpft wird.

Die Regel für die ``&``-Operation ist, dass wenn beide Seiten von ``&`` 1 sind, das Ergebnis 1 ist, ansonsten ist das Ergebnis 0.

Zum Beispiel, nehmen wir an dat=0x3f,i=2 (0011 1111 << 2 wird verschoben zu 1111 1100), dann ergibt 1111 1100 & 1000 0000 (0x80) = 1000 0000.

Zuletzt werden die dat-Daten bitweise SDI(DS) zugewiesen.

``digitalWrite(SRCLK, 1)``: Wenn SRCLK einen ansteigenden Puls von 0 auf 1 erzeugt, werden die Daten vom DS-Register ins Schieberegister übertragen;

``digitalWrite(RCLK, 1)``: Wenn RCLK einen ansteigenden Puls von 0 auf 1 erzeugt, werden die Daten vom Schieberegister ins Speicherregister übertragen.

.. code::

	fill(0,25,88);
	textAlign(CENTER,CENTER);
	textSize(height*0.8);

Die in ``setup()`` verwendete Funktion ``fill()`` füllt die Textfarbe, ``textAlign(CENTER,CENTER)`` zentriert den Text, und ``textSize(height*0.8)`` ändert die Textgröße auf das 0,8-fache der Originalgröße. Mit diesen Funktionen kann der auf Processing angezeigte Textstil angepasst werden.

.. code::

	void draw() {

		background(255);
		int number = (frameCount%100)/10;
		text(number, width/2, height/2);
		hc595_shift(SegCode[number]);
	}

``frameCount`` ist ein Samen, der mit ``frameRate`` zusammenhängt.
Standardmäßig beträgt ``frameRate`` 60, was bedeutet, dass ``frameCount`` 60 Mal pro Sekunde akkumuliert wird.

So können Processing und die 7-Segment-Anzeige gleichzeitig die Zahlen von 0 bis 9 und A bis F anzeigen.