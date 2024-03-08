.. _1.7_scratch:

1.7 貯金箱
=========================

このプロジェクトでは、スピードセンサーモジュール、Raspberry Pi、およびScratchを使用して貯金箱を作成します。

スピードセンサーモジュールの中央に紙を置くと、ステージ上の貯金箱にコインが落ちるのが見えます。

.. image:: img/1.7_header.png

必要な部品
------------------------------

このプロジェクトには、以下の部品が必要です。

.. image:: img/1.7_component.png

キット全体を購入するのは確かに便利です。こちらがリンクです：

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
    *   - :ref:`cpn_speed_sensor`
        - \-

回路を組む
---------------------

.. image:: img/1.7_fritzing.png

コードをロードして動作を確認する
---------------------------------------

コードファイル(``1.7_piggy_bank.sb3``)をScratch 3にロードします。

スピードセンサーの中央の2つの端子のうち、1つは光を送信するためのもの、もう1つは光を受信するためのものです。中央に紙を置いて光の伝送を遮断すると、スピードセンサーは高レベルを出力します。この時点でScratchは高レベルを受け取り、スプライトのコスチュームを切り替え、ステージ上の貯金箱にコインが落ちるのを見ることができます。

スプライトに関するヒント
---------------------------------

Sprite1を選択し、左上の **Costumes** をクリックします。 **Upload Costume** ボタンを使用して ``~/raphael-kit/scratch/picture`` のパスから **piggybank1.png**、 **piggybank2.png**、および **piggybank3.png** をアップロードします。デフォルトの2つのコスチュームを削除し、スプライトの名前を **piggybank** に変更します。

.. image:: img/1.7_photoInterrupter1.png

コードに関するヒント
-------------------------------

.. image:: img/1.7_code2.png

pin17が低いとき(コインが入れられていない場合)、スプライトのコスチュームを **piggybank1** に切り替えます。

.. image:: img/1.7_code3.png

pin17が高いとき(コインが入れられた場合)、スプライトのコスチュームを **piggybank2** に切り替え、0.5秒後に **piggybank3** に切り替えます。これにより、ステージ上の貯金箱にコインが落ちるのが見えます。

