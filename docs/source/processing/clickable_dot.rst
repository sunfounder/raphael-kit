.. _clickable_dot:

クリック可能な点
==================

私たちは動きのあるグラフィックを描くこと、マウスイベントに反応すること、そしてLEDを制御することを試みました。それらの機能を組み合わせて、LEDを制御するためのクリック可能な点を描くのもいいでしょう！

.. image:: img/clickable_dot_on.png

**必要な部品**

このプロジェクトには、以下の部品が必要です。

キット全体を購入すると非常に便利です。以下がリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットのアイテム
        - リンク
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

以下のリンクから、それぞれ別々に購入することもできます。

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - コンポーネントの紹介
        - 購入リンク

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_led`
        - |link_led_buy|

**配線図**

.. image:: img/image49.png

**スケッチ**

.. code-block:: arduino

    import processing.io.*; 
    boolean state = false;
    int ledPin = 17;

    void setup() {
        GPIO.pinMode(ledPin, GPIO.OUTPUT);
        background(255);
    }

    void draw() {
        if (state == true) { 
            GPIO.digitalWrite(ledPin, GPIO.LOW);
            fill(255, 0, 0);
        }else { 
            GPIO.digitalWrite(ledPin, GPIO.HIGH);
            fill(155);
        }
        ellipse(width/2, height/2, width*0.75, height*0.75);
    }

    void mouseClicked() {
        //  toggles state:
        if (2*dist(mouseX,mouseY,width/2, height/2)<=width*0.75)
            {state = !state;}
    }

**どのように動作するのか？**

このプロジェクトは :ref:`blinking_dot` と多くの共通点がありますが、違いはトグル状態をマウスイベントに入れることです。
これにより、LEDは自動的に点滅せず、マウスクリックで点灯したり消灯したりします。

そして、 ``mouseClicked()`` イベントでは、クリック時のマウスの位置を判断するために ``dist()`` 関数が使用され、マウスとドットの中心との距離が半径より短い場合のみ、ドットがクリックされたとみなされます。
