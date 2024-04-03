.. _1.14_scratch:

1.14 123木人形
===========================

今日は、123木人形というゲームをプレイします。

緑の旗をクリックしてゲームを開始し、キーボードの右矢印キーを押してスプライトを右に進めます。緑のLEDが点灯している場合、スプライトは移動できます。しかし、赤いLEDが点灯している場合、スプライトの移動を停止しなければなりません。そうしないとブザーが鳴り続けます。

.. image:: img/1.14_header.png

必要な部品
------------------------------

このプロジェクトには、以下の部品が必要です。

.. image:: img/1.14_component.png

キット全体を購入するのは確かに便利です。以下がリンクです：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットのアイテム
        - リンク
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

以下のリンクから部品を個別に購入することもできます。

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
    *   - :ref:`cpn_buzzer`
        - |link_passive_buzzer_buy|
    *   - :ref:`cpn_led`
        - |link_led_buy|
    *   - :ref:`cpn_transistor`
        - |link_transistor_buy|

回路を組む
---------------------

.. image:: img/1.14_fritzing.png

コードをロードして結果を確認する
---------------------------------------

Scratch 3に( ``1.14_123_wooden_man.sb3`` )のコードファイルをロードします。

緑色の LED が点灯している場合は、右矢印キーを使用して **Avery** が右に歩くように制御できます。赤色の LED が点灯しているときに **Avery** を右に動かし続けると、アラームが鳴ります。

スプライトに関するヒント
---------------------------------

デフォルトのスプライトを削除し、 **Avery Walking** スプライトを選択します。

.. image:: img/1.14_wooden1.png
  :width: 400

コードに関するヒント
-------------------------------

.. image:: img/1.14_wooden2.png
  :width: 400

すべてのピンを高に初期化します。

.. image:: img/1.14_wooden3.png
  :width: 400

ゲームが開始されると、status変数に1を割り当て、Avery Walkingスプライトが動くことを示し、次にgpio18を低に設定して緑のLEDを5秒間点灯させます。

.. image:: img/1.14_wooden4.png
  :width: 400

gpio18を高に設定し、次にgpio27を低に設定します。これは、緑のLEDをオフにし、黄色のLEDを0.5秒間点灯させることを意味します。

.. image:: img/1.14_wooden5.png
  :width: 400

status変数に0を割り当てることで、Avery Walkingスプライトはこの瞬間に動かないことを示します。次に、gpio27を低くし、gpio17を高く設定して、黄色のLEDをオフにし、赤いLEDを3秒間点灯させます。最後に、gpio17を高く設定して赤いLEDをオフにします。

.. image:: img/1.14_wooden6.png
  :width: 400

キーボードの右矢印キーを押すと、 **Avery Walking** スプライトを次のコスチュームに切り替えて、Averyが右に歩いているのを見ることができます。次に、 **status** 変数の値を判断する必要があります。0の場合、Avery Walkingスプライトはこの瞬間に動かないことを示し、ブザーが鳴って警告します。

