スマートファン
====================

このプロジェクトでは、Blynkを通じて温度を確認し、遠隔操作で扇風機を起動することができます。

.. note:: このプロジェクトに取り組む前に、 :ref:`bk_start` を完了させることをお勧めします。これにより、Blynkに関する基本的な理解が得られます。

**必要なコンポーネント**

このプロジェクトに必要な部品は以下の通りです。

一式をまとめて購入することもできます。以下にリンクを貼っています：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前
        - このキットのアイテム
        - リンク
    *   - Raphaelキット
        - 337
        - |link_Raphael_kit|

個別に購入する場合、以下のリンクからどうぞ。

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
    *   - :ref:`cpn_power_module`
        - \-
    *   - :ref:`cpn_l293d`
        - \-
    *   - :ref:`cpn_adc0834`
        - \-
    *   - :ref:`cpn_thermistor`
        - |link_thermistor_buy|
    *   - :ref:`cpn_motor`
        - |link_motor_buy|


**1. 配線**

.. image:: img/wiring_blynk_motor.png


**2. ウィジェットとデータストリームの作成**

1. 画面右上のメニューアイコンをクリックし、ダッシュボードの編集を選びます。

    .. image:: img/sp220913_180231.png

2. ダッシュボードにスイッチウィジェットとラベルウィジェットを追加します。

    .. image:: img/sp220914_175437.png

3. スイッチウィジェット用にデータストリーム（ここではV3を使用）を作成します。このデータストリームはモーターの起動に使います。

    .. image:: img/sp220914_155911.png

4. ラベルウィジェット用にデータストリーム（こちらはV0を使用）を作成します。温度表示に使います。 **DATA TYPE** はStringに設定します。

    .. image:: img/sp220914_175616.png

#. 設定が完了したら、画面右上の「保存して適用」をクリックします。

    .. image:: img/sp220913_182300.png


**3. コードの実行**

1. コードを編集します。

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_motor.py

2. 下記の行を探して、 ``BLYNK_AUTH_TOKEN`` を貼り付けます。

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. コードを実行します。

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_motor.py

4. Blynkのダッシュボードで、ラベルウィジェットで温度を確認したり、スイッチウィジェットで扇風機の起動/停止ができます。

#. モバイルデバイスでBlynkを利用する場合は、 :ref:`blynk_mobile` を参照してください。

