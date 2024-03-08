.. _1.3_scratch:

1.3 タンブラー
==================

このプロジェクトでは、傾きスイッチで制御されるタンブラートイを作成します。

.. image:: img/1.3_header.png

必要な部品
------------------------------

このプロジェクトには、以下の部品が必要です。

.. image:: img/1.3_component.png

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
    *   - :ref:`cpn_tilt_switch` 
        - \-

回路を組む
---------------------

.. image:: img/1.3_fritzing.png

コードをロードして動作を確認する
-----------------------------------------

コードファイル(``1.3_tumbler.sb3``)をScratch 3にロードします。

傾きスイッチが直立しているとき、タンブラーは立っています。傾けると、タンブラーも倒れます。再び直立させると、タンブラーは再び立ち上がります。

スプライトに関するヒント
---------------------------------
Sprite1 を選択し、左上隅にある **Costumes** をクリックします。 **Upload Costume** ボタンを使用して、 ``~/raphael-kit/scratch/picture`` パスから **tumbler1.png** と **tumbler2.png** をアップロードします。 デフォルトの 2 つのコスチュームを削除し、スプライトの名前を **tumbler** に変更します。

.. image:: img/1.3_add_tumbler.png

コードに関するヒント
-------------------------------

.. image:: img/1.3_title2.png
  :width: 400

緑の旗がクリックされると、gpio17の初期状態が低く設定されます。

.. image:: img/1.3_title4.png
  :width: 400

pin17が低い場合（傾きスイッチが直立している場合）、タンブラースプライトの衣装をtumbler1（直立状態）に切り替えます。

.. image:: img/1.3_title3.png
  :width: 400

pin17が高い場合（傾きスイッチが傾いている場合）、タンブラースプライトの衣装をtumbler2（傾いた状態）に切り替えます。
