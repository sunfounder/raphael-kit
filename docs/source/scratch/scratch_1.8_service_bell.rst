.. _1.8_scratch:

1.8 サービスベル
===================

今日は、マイクロスイッチ、スピーカー、オーディオアンプモジュール、Raspberry Pi、およびScratchを使用してサービスベルを作成します。

マイクロスイッチをタップして、サービスベルの音を鳴らします。

.. image:: img/1.8_header.png

必要な部品
------------------------------

このプロジェクトには、以下の部品が必要です。

.. image:: img/1.8_component.png

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

    *   - :ref:`GPIO拡張ボード`
        - |link_gpio_board_buy|
    *   - :ref:`ブレッドボード`
        - |link_breadboard_buy|
    *   - :ref:`ジャンパーワイヤー`
        - |link_wires_buy|
    *   - :ref:`抵抗器`
        - |link_resistor_buy|
    *   - :ref:`マイクロスイッチ`
        - \-
    *   - :ref:`コンデンサ`
        - |link_capacitor_buy|
    *   - :ref:`オーディオモジュールとスピーカー`
        - \-

回路を組む
---------------------

.. image:: img/1.8_fritzing.png

コードをロードして動作を確認する
-----------------------------------------

コードファイル(``1.8_service_bell.sb3``)をScratch 3にロードします。

マイクロスイッチを押すと、サービスベルが1回鳴ります。

.. note::

  Raspberry Piがスピーカー付きの画面に接続されている場合、この外部スピーカーから音が出ない場合があります。解決策については、 :ref:`オーディオ出力の変更` を参照してください。

  また、ボリュームレベルを調整したい場合は、 :ref:`音量調整` を参照してください。

スプライトに関するヒント
---------------------------------

Sprite1を選択し、左上の **Costumes** をクリックします。 **Upload Costume** ボタンを使用して ``~/raphael-kit/scratch/picture`` のパスから **bell1.png** と **bell2.png** をアップロードします。デフォルトの2つのコスチュームを削除し、スプライトの名前を **bell** に変更します。

.. image:: img/1.8_travel1.png

**Sounds** オプションで、 ``~/raphael-kit/scratch/sound`` のパスから ``bell.wav`` をScratch 3にアップロードします。

.. image:: img/1.8_travel2.png

コードに関するヒント
-------------------------------

.. image:: img/1.8_travel3.png
  :width: 400

pin17が高いとき(マイクロスイッチが押されていない場合)、 **bell** スプライトのコスチュームを **bell1** に切り替えます。

.. image:: img/1.8_travel4.png
  :width: 400

マイクロスイッチを押すと、gpio17は低レベルになります。この時、 **bell** スプライトのコスチュームを **bell2** に切り替え、スピーカーを通じてサウンドエフェクトを再生します。

