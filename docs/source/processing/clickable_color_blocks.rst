.. _clickable_color_blocks:

クリック可能なカラーブロック
=============================

すでにLEDの制御のためのクリック可能な点を描画して試してみましたが、さらに一歩進めて、RGBの色を調整するための3つの色付きの四角を描くことを試みましょう！

.. image:: img/colorful_square.png

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

    *   - :ref:`GPIO拡張ボード`
        - |link_gpio_board_buy|
    *   - :ref:`ブレッドボード`
        - |link_breadboard_buy|
    *   - :ref:`ジャンパーワイヤー`
        - |link_wires_buy|
    *   - :ref:`RGB LED`
        - |link_rgb_led_buy|

**配線図**

.. image:: img/image61.png

**スケッチ**

.. code-block:: arduino

    import processing.io.*; // use the GPIO library

    int[] pins = { 17, 18, 27 };

    void setup() {
        for (int i = 0; i < pins.length; i++) {
            GPIO.pinMode(pins[i], GPIO.OUTPUT);
        }
        size(300, 100);
        background(255);
    }

    void draw() {
        fill(255, 0, 0);
        rect(0, 0, width/3, height);

        fill(0,255,0);
        rect(width/3, 0, 2*width/3, height);

        fill(0,0,255);
        rect(2*width/3, 0, width, height);
    }

    void mouseClicked() {
        for (int i = 0; i < pins.length; i++) {
            GPIO.digitalWrite(pins[i],GPIO.LOW);
        }
        if (mouseX<width/3){
            GPIO.digitalWrite(pins[0],GPIO.HIGH);
        }else if (mouseX>width/3&&mouseX<2*width/3){
            GPIO.digitalWrite(pins[1],GPIO.HIGH);
        }else if (mouseX>2*width/3){
            GPIO.digitalWrite(pins[2],GPIO.HIGH);
        }        
    }


**どのように動作するのか？**

このプロジェクトは :ref:`clickable_dot` と多くの共通点がありますが、マウスのクリックイベントを判断する条件を微調整しています。

まず、 ``draw()`` で三つの色ブロックを描画し、次にmouseX（マウスのX軸座標）の値に基づいてクリックされたカラーブロックを取得し、最後にRGBを対応する色に点灯させます。

**さらに詳しくは？**

光の追加に基づいて、RGB LEDは7色を表示できます - 赤に緑を追加すると黄色になり、三つの原色をすべて合わせると白になります。
これを自分で試してみてください。
