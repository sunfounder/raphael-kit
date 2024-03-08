.. _1.2_Scratch:

1.2 カラフルなボール
=====================

ステージエリアの異なる色のボールをクリックすると、RGB LEDが異なる色で点灯します。

.. image:: img/1.2_header.png

必要な部品
------------------------------

このプロジェクトには、以下の部品が必要です。

.. image:: img/1.2_list.png

キット全体を購入するのが便利です。リンクは以下のとおりです：

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

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`RGB LED`
        - |link_rgb_led_buy|

回路を組む
---------------------

.. image:: img/1.2_image61.png

コードをロードして結果を確認する
-----------------------------------------

コードファイル(``1.2_colorful_balls.sb3``)をScratch 3にロードした後、対応するボールをクリックすると、RGB LEDがそれぞれ黄色、青、赤、緑、または紫で点灯します。

スプライトに関するヒント
------------------------

デフォルトのスプライトを削除し、 **Ball** スプライトを選択します。

.. image:: img/1.2_ball.png

それを5回複製します。

.. image:: img/1.2_duplicate_ball.png

これらの5つの **Ball** スプライトに異なる衣装を選び、それらを対応する位置に移動します。

.. image:: img/1.2_rgb1.png

コードに関するヒント
---------------------
コードを理解する前に、 `RGBカラーモデル <https://en.wikipedia.org/wiki/RGB_color_model>`_ を理解する必要があります。

RGBカラーモデルは、赤、緑、青の光をさまざまな方法で加えることで、幅広い色を再現する加算色モデルです。

加算色混合：赤と緑を加えると黄色になり、緑と青を加えるとシアンになり、青と赤を加えるとマゼンダになり、3つの原色をすべて加えると白になります。

.. image:: img/1.2_rgb_addition.png
  :width: 400

RGB LEDは1つのパッケージ内の3つのLED（赤LED、緑LED、青LED）の組み合わせであり、これら3つの色を組み合わせることでほぼ任意の色を生成することができます。
4本のピンがあり、1本はGNDで、残りの3本のピンはそれぞれ3つのLEDを制御します。

そのため、RGB LEDを黄色に点灯させるコードは次のとおりです。

.. image:: img/1.2_rgb3.png

ボールスプライト（黄色のボール）をクリックすると、gpio17を高く設定し（赤LEDがオン）、gpio18を高く設定し（緑LEDがオン）、gpio27を低く設定する（青LEDがオフ）ので、RGB LEDが黄色に点灯します。

対応する色でRGB LEDを点灯させるために、同じ方法で他のスプライトにコードを書くことができます。

