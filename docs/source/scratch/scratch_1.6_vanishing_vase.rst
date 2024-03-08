.. _1.6_scratch:

1.6 花瓶の消失
========================

さて、ちょっとしたマジックトリックをやってみましょう。何もしないで、なぜか花瓶が消える。

.. image:: img/1.6_header.png

必要な部品
------------------------------

このプロジェクトには、以下の部品が必要です。

.. image:: img/1.6_component.png

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
    *   - :ref:`cpn_reed_switch`
        - |link_reed_switch_buy|

回路を組む
---------------------

.. image:: img/1.6_fritzing.png

コードをロードして動作を確認する
---------------------------------------

コードファイル(``1.6_vanishing_vase.sb3``)をScratch 3にロードします。

リードスイッチモジュールに磁石を近づけると、ステージに花瓶が表示されます。磁石を取り除くと、花瓶が消えます。

スプライトに関するヒント
---------------------------------

Sprite1を選択し、左上の **Costumes** をクリックします。 **Upload Costume** ボタンを使用して ``~/raphael-kit/scratch/picture`` のパスから **desk1.png** と **desk2.png** をアップロードします。デフォルトの2つのコスチュームを削除し、スプライトの名前を **desk** に変更します。

.. image:: img/1.6_vase.png

コードに関するヒント
-------------------------------

.. image:: img/1.6_reed2.png
  :width: 400

磁石がリードスイッチモジュールに近づくと、gpio17は低くなり、 **desk** スプライトのコスチュームは **desk1** （デスク上の花瓶）に切り替えられます。

.. image:: img/1.6_reed3.png
  :width: 400

磁石を取り除くと、gpio17は高くなります。この時、 **desk** スプライトのコスチュームは **desk2** （デスクのみ）に切り替えられます。
