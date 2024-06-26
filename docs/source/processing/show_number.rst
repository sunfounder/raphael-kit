 
.. _show_number:

Afficher un chiffre
=======================

Dans ce projet, nous utilisons Processing pour piloter un afficheur 7 segments afin d'afficher un chiffre de 0 à 9 et les lettres de A à F.

**Composants nécessaires**

Pour ce projet, nous avons besoin des composants suivants.

Il est très pratique d'acheter un kit complet, voici le lien :

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nom
        - COMPOSANTS DANS CE KIT
        - LIEN
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

Vous pouvez également les acheter séparément via les liens ci-dessous.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUCTION DES COMPOSANTS
        - LIEN D'ACHAT

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

**Câblage**

.. image:: img/image125.png

**Esquisse**

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

**Comment ça fonctionne ?**

Importez ``processing.io.*`` et utilisez la bibliothèque de fonctions GPIO pour contrôler les broches du tube numérique.

Définissez le tableau ``SegCode = {0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71}`` 
qui représente un tableau de codes de segments de 0 à F en Hexadécimal (cathode commune).

La fonction ``setup()`` définit les trois broches SDI, RCLK et SRCLK comme sorties, et les données initiales comme étant 0.

La fonction ``hc595_shift(int dat)`` est utilisée pour transférer le ``SegCode`` vers le 74HC595.
 
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
 
``n=(0x80 & (dat << i))`` signifie décaler dat vers la gauche de ``i`` bits puis faire l'opération ``&`` avec 0x80.

La règle de l'opération ``&`` est que lorsque les deux côtés de ``&`` sont 1, le résultat est 1, sinon le résultat est 0.

Par exemple, supposons dat=0x3f,i=2(0011 1111 << 2 décalé à 1111 1100), alors 1111 1100 & 1000 0000 (0x80) = 1000 0000.

Enfin, assignez les données dat à SDI(DS) par bits.
 
``digitalWrite(SRCLK, 1)`` lorsque SRCLK génère une impulsion montante de 0 à 1, les données seront transférées du registre DS au registre de décalage ;
 
``digitalWrite(RCLK, 1)`` lorsque RCLK génère une impulsion montante de 0 à 1, les données seront transférées du registre de décalage au registre de stockage.

.. code::

	fill(0,25,88);
	textAlign(CENTER,CENTER);
	textSize(height*0.8);

La fonction ``fill()`` utilisée dans ``setup()`` peut remplir la couleur du texte, ``textAlign(CENTER,CENTER)`` est utilisée pour centrer le texte, ``textSize(height*0.8)`` change la hauteur du texte à 0,8 fois l'original.
Ces fonctions peuvent personnaliser le style du texte affiché sur le processing

.. code::

	void draw() {

		background(255);
		int number = (frameCount%100)/10;
		text(number, width/2, height/2);
		hc595_shift(SegCode[number]);
	}

Le ``frameCount`` est une graine, qui est liée à ``frameRate``.
Par défaut, ``frameRate`` est 60, ce qui signifie que ``frameCount`` s'accumulera 60 fois par seconde.

Nous pouvons alors laisser Processing et l'affichage 7 segments afficher le chiffre de 0 à 9 et de A à F simultanément.
