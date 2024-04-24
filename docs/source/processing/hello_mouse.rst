.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _hello_mouse:

マウスで描く
==================

このプロジェクトでは、マウスが点に向かって線を引き続けます。マウスを動かすと、ユニークな星の線を描くことができます。マウスをクリックすると、描画がリスタートされます。

.. image:: img/hello_mouse1.png

**スケッチ**

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

    void mousePressed() {
        pointX=mouseX;
        pointY=mouseY;
        background(192, 16, 18);
    }

**どのように動作するのか？**

前のプロジェクトはアニメーションやインタラクションなしで一つの画像を描画していました。

インタラクティブなスケッチを作成する場合、フレームを構築するために ``setup()`` と ``draw()`` 関数（これらは自動的に呼び出される組み込み関数）を追加する必要があります。

* ``setup()``: スケッチの開始時に一度だけ実行されます。
* ``draw()``: 繰り返し実行され、アニメーションを描画するためのスケッチを通常追加します。

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

上記のスケッチは、インタラクティブなスケッチとしてすでにスムーズに動作しています。

次に、マウスのクリックイベントを追加できます。このイベントは ``mousePressed()`` 関数で実装でき、ターゲットポイントを更新し、画面をクリアするステートメントを追加します。

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

    void mousePressed() {
        pointX=mouseX;
        pointY=mouseY;
        background(192, 16, 18);
    }

詳しくは `Processing Reference <https://processing.org/reference/>`_ を参照してください。


