.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _dot_on_the_swing:

ブランコ上のドット
==============================

このプロジェクトでは、3つのボタンが接続されています。1つはドットのサイズを変更するため、もう1つは位置を変更するため、最後の1つは色を変更するためです。3つのボタンを同時に押すと、ブランコを揺らしているような可変色のドットが得られます。

.. image:: img/dancing_dot.png

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

.. image:: img/circuit_dancing_dot.png

**スケッチ**

.. code-block:: arduino

    import processing.io.*;

    // Define an instance of the Dot object
    Dot myDot;

    // Define the pins that will be reading button presses
    int[] pins = { 18, 23, 24 };

    void setup() {
        size(400, 400);
        // Change the color mode of the sketch to HSB
        colorMode(HSB, 360, 100, 100);
        noStroke();

        for (int i = 0; i < pins.length; i++) {
            GPIO.pinMode(pins[i], GPIO.INPUT_PULLUP);
        }

        // Create a Dot in the middle of the screen 
        myDot = new Dot(width / 2, height / 2, 100, 255);
    }

    void draw() {
        background(0); 

        // Modify attributes of the Dot depending on which buttons are pressed
        if (GPIO.digitalRead(pins[0]) == GPIO.LOW) {myDot.setSize();} 
        if (GPIO.digitalRead(pins[1]) == GPIO.LOW) {myDot.setPosition();} 
        if (GPIO.digitalRead(pins[2]) == GPIO.LOW) {myDot.setColor();} 

        // Update the Dot state
        myDot.update();
        // And draw it to the screen
        myDot.show();
    }

    class Dot { 

        float initX;
        float initY;
        float currentX;
        float currentY;
        int positionRange = 60;

        float initSize;
        float currentSize;
        int sizeRange = 50;

        int initColor;
        int currentColor;
        int ColorRange = 80;

        float timer = 0.0;
        float speed = 0.06;

        Dot(float x, float y, float s, int c) {
            initX = x;
            initY = y;
            currentX = x;
            currentY = y;

            initSize = s;
            currentSize = s;

            initColor = c;
            currentColor = c;
        }

        void setSize() {
            currentSize = initSize + sizeRange * sin( timer );
        }

        void setPosition() {
            currentY = initY + positionRange * cos( timer *2);
        }

        void setColor() {
            currentColor = int(initColor + ColorRange * sin( timer ));
        }

        void update() {
            timer += speed;
        }

        void show() {
            fill(currentColor, 100, 100); 
            ellipse(currentX, currentY, currentSize, currentSize);
        }
    }

**どのように動作するのか？**

ここでは直接ドットを描画するのではなく、 ``Dot`` クラスを作成します。
そして、オブジェクト（この場合は ``myDot`` ）を宣言します。

これは、多くの同一のプロパティを持つドットを描画するための簡単な方法です。
たとえば、このプロジェクトでドットに3つの機能を追加する場合 - サイズの変更、位置の変更、および色の変更 - すべてのドットには同じ機能があります。
同じボタンを使用して、彼らに同じことをさせることができます。また、各ドットを個別に制御するために異なるボタンを使用することもできます。

**クラス** を使用すると、スケッチが美しく、パワフルで、柔軟になります。

`クラス (コンピュータプログラミング) - Wikipedia <https://en.wikipedia.org/wiki/Class_(computer_programming)>`_

次に、 ``Dot`` クラスを詳しく見てみましょう。

.. code-block:: arduino

    Dot(float x, float y, float s, int c)

宣言には、位置のXおよびY座標値、サイズ、色（ここでは `HSBカラーモード <https://en.wikipedia.org/wiki/HSL_and_HSV>`_ に設定されています）の4つのパラメータを渡す必要があります。

各パラメータは2組の値（初期値と現在の値）に割り当てられます。

.. code-block:: arduino

    float initX;
    float initY;
    float currentX;
    float currentY;
    int positionRange = 60;

    float initSize;
    float currentSize;
    int sizeRange = 50;

    int initColor;
    int currentColor;
    int ColorRange = 80;

初期値と現在の値の他にも、範囲値のセットがあります。初期値は、ドットの初期状態を決定するために使用され（入力パラメータで決定される）、現在の値は、ドットを動かすための範囲内で変更されることが容易に理解できるでしょう。

したがって、X座標値を除いて、他の3つのパラメータの現在の値は以下のように計算されます：

.. code-block:: arduino

    void setSize() {
        currentSize = initSize + sizeRange * sin( timer );
    }

    void setPosition() {
        currentY = initY + positionRange * cos( timer *2);
    }

    void setColor() {
        currentColor = int(initColor + ColorRange * sin( timer ));
    }

三角関数に慣れていれば、 `サインとコサイン <https://en.wikipedia.org/wiki/Sine>`_ を理解するのは難しくないでしょう。これにより、ドットの現在の値の滑らかな周期的な変化（-1から1まで）が得られます。

また、周期的な変動のための種、 ``timer`` を追加する必要があります。 ``update()`` の方法で固定値が追加され、 ``draw()`` で呼び出されます。

.. code-block:: arduino

    void update() {
        timer += speed;
    }

最後に、 ``show()`` メソッドを使用して、現在の値に基づいてドットを表示します。これも ``draw()`` で呼び出されます。

.. code-block:: arduino

    void show() {
        fill(currentColor, 100, 100); 
        ellipse(currentX, currentY, currentSize, currentSize);
    }

**さらに?**

クラスの使用をマスターすると、同じプロパティを持つ複数のドットを描画することができます。ですから、もっとクールなことを試してみてはどうでしょうか。
例えば、安定した連星系を描画するか、'DUET'ゲームを作るのはどうでしょうか？



