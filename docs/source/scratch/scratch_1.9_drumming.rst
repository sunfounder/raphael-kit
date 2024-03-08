.. _1.9_scratch:

1.9 ドラム演奏
================

このプロジェクトでは、タッチスイッチモジュールでドラムを演奏します。

.. image:: img/1.9_header.png

必要な部品
------------------------------

このプロジェクトには、以下の部品が必要です。

.. image:: img/1.9_component.png

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
    *   - :ref:`cpn_touch_switch`
        - |link_touch_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-

回路を組む
---------------------

.. image:: img/1.9_fritzing.png

コードをロードして動作を確認する
---------------------------------------

コードファイル(``1.9_drumming.sb3``)をScratch 3にロードします。

タッチスイッチモジュールにタップすると、スピーカーからドラムの音が聞こえます。

スプライトに関するヒント
---------------------------------

デフォルトのスプライトを削除し、 **Drum-snare** スプライトを見つけて追加し、そのサイズを200に変更します。

.. image:: img/1.9_touch1.png

Scratchには楽器やドラムを再生する **Music** 拡張機能があります。今、 **Add Extension** ボタンを使って追加します。

.. image:: img/1.9_touch2.png

コードに関するヒント
-------------------------------

.. image:: img/1.9_touch3.png
  :width: 400

pin17が低いとき(タッチスイッチモジュールにタップされていない場合)、 **Drum-snare** スプライトのコスチュームを **drum-snare-a** に切り替えます。

.. image:: img/1.9_touch4.png
  :width: 600

タッチスイッチモジュールにタップすると、gpio17は低いです。この時点で、 **Drum-snare** スプライトのコスチュームを **drum-snare-b** に切り替え、スピーカーでドラムの音を再生します。
