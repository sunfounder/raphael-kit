.. _show_number:

数字の表示
=============================================

このプロジェクトでは、processingを使用して7セグメントディスプレイを駆動し、0から9、AからFまでの数字を表示します。

**必要な部品**

このプロジェクトには、以下の部品が必要です。

キット全体を購入することは確かに便利です。以下がリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットのアイテム
        - リンク
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

以下のリンクから個別に購入することもできます。

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - コンポーネントの紹介
        - 購入リンク

    *   - :ref:`GPIO拡張ボード`
        - |link_gpio_board_buy|
    *   - :ref:`ブレッドボード`
        - |link_breadboard_buy|
    *   - :ref:`ジャンパーワイヤー`
        - |link_wires_buy|
    *   - :ref:`抵抗器`
        - |link_resistor_buy|
    *   - :ref:`7セグメントディスプレイ`
        - |link_7segment_buy|
    *   - :ref:`74HC595`
        - |link_74hc595_buy|

**配線図**

.. image:: img/image125.png

**スケッチ**

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

**どのように動作するのか？**

``processing.io.*`` をインポートし、GPIO関数ライブラリを使用してデジタルチューブのピンを制御します。

``SegCode = {0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71}`` の配列を定義して、16進数の0からFまでのセグメントコード配列（コモンカソード）を表現します。

``setup()`` 関数は、三つのピンSDI、RCLK、およびSRCLKを出力として設定し、初期データを0とします。

``hc595_shift(int dat)`` 関数は、 ``SegCode`` を74HC595にシフトするために使用されます。

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

``n=(0x80 & (dat << i))`` は、datを ``i`` ビット左にシフトしてから0x80と ``&`` 操作をすることを意味します。

``&`` 操作のルールは、 ``&`` の両方が1の場合、結果は1であり、それ以外の場合、結果は0です。

例として、dat=0x3f、i=2(0011 1111 << 2は1111 1100にシフト)と仮定します。その後、1111 1100 & 1000 0000(0x80) = 1000 0000となります。

最後に、datデータをビットごとにSDI(DS)に割り当てます。

``digitalWrite(SRCLK, 1)`` SRCLKが0から1への立ち上がりエッジパルスを生成すると、データはDSレジスタからシフトレジスタに転送されます。

``digitalWrite(RCLK, 1)`` RCLKが0から1への立ち上がりエッジパルスを生成すると、データはシフトレジスタからストレージレジスタに転送されます。

.. code::

	fill(0,25,88);
	textAlign(CENTER,CENTER);
	textSize(height*0.8);

``setup()`` で使用される ``fill()`` 関数はテキストの色を塗りつぶすことができ、 ``textAlign(CENTER,CENTER)`` はテキストを中央にするために使用され、 ``textSize(height*0.8)`` はテキストの高さを元の0.8倍に変更します。
これらの関数は、processingに表示されるテキストスタイルをカスタマイズできます。

.. code::

	void draw() {

		background(255);
		int number = (frameCount%100)/10;
		text(number, width/2, height/2);
		hc595_shift(SegCode[number]);
	}

``frameCount`` はシードであり、 ``frameRate`` に関連します。
デフォルトでは ``frameRate`` は60であり、これは ``frameCount`` が1秒に60回蓄積されることを意味します。

その後、processingと7セグメント表示を使用して、0から9、AからFまでの数字を同時に表示することができます。
