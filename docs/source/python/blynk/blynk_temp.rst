温度記録器
====================

このプロジェクトでは、Blynkを使って現在の温度とその変化をライングラフで確認できます。

.. note:: このプロジェクトに取り掛かる前に、 :ref:`bk_start` を完了することをお勧めします。これにより、Blynkについての基本的な理解が得られます。

**必要なコンポーネント**

このプロジェクトで必要な部品は以下の通りです。

一式をまとめて購入すると便利です。下記にリンクを掲載しています：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称
        - このキットのアイテム
        - リンク
    *   - Raphaelキット
        - 337
        - |link_Raphael_kit|

部品を個別に購入する場合は、以下のリンクからどうぞ。

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - 部品説明
        - 購入リンク
    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_humiture_sensor`
        - |link_humiture_buy|


**1. 配線**

.. image:: img/wiring_blynk_temp.png


**2. ウィジェットとデータストリームの作成**

1. 右上のメニューアイコンをクリックし、ダッシュボードの編集を選択します。

    .. image:: img/sp220913_180231.png

2. ダッシュボードにゲージウィジェットとチャートウィジェットを追加します。

    .. image:: img/sp220914_175437.png

3. ゲージウィジェット用のデータストリーム（V5を使用）を作成します。温度表示に使用します。 **DATA TYPE** は ``Double`` 、 **DECIMALS** は ``#. #`` （有効数字2桁）に設定します。

    .. image:: img/sp220914_182300.png

4. チャートウィジェットに先ほど作成したV5データストリームを追加します。

    .. image:: img/sp220914_183039.png

#. 設定が完了したら、右上にある「保存して適用」をクリックします。

    .. image:: img/sp220913_182300.png


**3. コードの実行**

1. コードを編集します。

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_temp.py

2. 下記の行を見つけて、 ``BLYNK_AUTH_TOKEN`` を貼り付けます。

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. コードを実行します。

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_temp.py

4. Blynkのダッシュボードで、温度やその変化のライングラフを確認できます。

    .. image:: img/sp220915_101137.png

#. モバイルデバイスでBlynkを利用する場合は、 :ref:`blynk_mobile` を参照してください。

