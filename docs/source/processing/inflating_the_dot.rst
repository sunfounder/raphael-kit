.. _inflating_the_dot:

ドットの拡大
===========================

次に、ボタンでドットのサイズを制御できる回路を作成しましょう。
ボタンを押すと、ドットはすぐに大きくなり、ボタンを離すと、ドットは徐々に小さくなります。これにより、ドットは膨らんでいる風船のように見えます。

.. image:: img/dot_size.png

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
    *   - :ref:`cpn_button`
        - |link_button_buy|

**配線図**

.. image:: img/button_pressed.png

**スケッチ**

.. code-block:: arduino

    import processing.io.*;
    int buttonPin = 18; 

    float diameter;

    void setup() {
        size(200, 200);
        frameRate(64); //set frame rate
        GPIO.pinMode(buttonPin, GPIO.INPUT_PULLUP); 
        diameter = width*0.5;
    }

    void draw() {
        if (GPIO.digitalRead(buttonPin)==GPIO.LOW) {
            if(diameter<width*0.8) {diameter=diameter+5;}
        } else {
            if(diameter>=width*0.2) {diameter--;}
        } 
        background(192, 16, 18);
        ellipse(width/2, height/2,diameter, diameter);
    }

**どのように動作するのか？**

このプロジェクトは、GPIOの出力機能を使用した前の2つのプロジェクトとは異なり、入力機能を使用しています。

``GPIO.pinMode()`` 関数は、 ``buttonPin`` をプルアップ入力モードに設定するために使用され、これにより、デフォルトの状態でピンが自動的にハイになります。

次に ``GPIO.digitalRead()`` 関数を使用して ``buttonPin`` の値を読み取ります。値がLOWの場合、ボタンが押されていることを意味し、その時点でドットの直径を5増加させます。ボタンが放されたら、ドットの直径は1減少します。


