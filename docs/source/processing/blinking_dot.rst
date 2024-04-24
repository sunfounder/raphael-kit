.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _blinking_dot:

点の点滅
===========================

このプロジェクトでは、LEDと同期して点滅する点をProcessingで描画します。図に示されているように回路を組み立て、スケッチを実行してください。

.. image:: img/blinking_dot.png
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

.. code-block:: Arduino

    import processing.io.*;
    int ledPin = 17; 
    boolean state = true; 

    void setup() {
        size(100, 100);
        frameRate(2); //set frame rate
        GPIO.pinMode(ledPin, GPIO.OUTPUT); //set the ledPin to output mode 
    }

    void draw() {
        state = !state;
        if (state==true) {
            GPIO.digitalWrite(ledPin, GPIO.LOW); //led on 
            fill(255, 0, 0); //set the fill color of led on
        } else {
            GPIO.digitalWrite(ledPin, GPIO.HIGH); //led off
            fill(155); //set the fill color of led off
        } 
        ellipse(width/2, height/2, width*0.75, height*0.75);
    }

**どのように動作するのか？**

スケッチの最初に、回路実験に欠かせないProcessingのGPIO機能ライブラリを ``import processing.io.*;`` で組み込む必要があります。

**フレームレート** は、ボード上に表示されるビットマップの頻度で、ヘルツ(Hz)で表されます。言い換えれば、 ``draw()`` 関数が呼ばれる頻度でもあります。 ``setup()`` で **フレームレート** を2に設定すると、 ``draw()`` が0.5秒ごとに呼び出されます。

``draw()`` 関数の呼び出しごとに ``state`` の逆を取り、それを決定します。値が ``true`` の場合、LEDは点灯し、筆は赤で塗りつぶされます。そうでなければ、LEDは消灯し、筆は灰色で塗りつぶされます。

判定を完了した後、 ``ellipse()`` 関数を使用して円を描画します。 ``width`` と ``height`` は、表示ウィンドウの幅と高さを格納するために使用されるシステム変数であることに注意してください。

注意すべき他の2点は、GPIOを使用する場合、 ``GPIO.pinMode()`` 関数を使用してピンの入力/出力状態を設定し、 ``GPIO.digitalWrite()`` 関数を使用してピンに値（HIGH/LOW）を割り当てる必要があることです。

.. note::

    ``draw()`` 内で ``delay()`` を使用することは避けてください。これは表示ウィンドウのリフレッシュに影響します。
