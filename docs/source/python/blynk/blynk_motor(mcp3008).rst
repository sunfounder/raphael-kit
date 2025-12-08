.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティ (Facebook) へようこそ！  
    Raspberry Pi、Arduino、ESP32 を仲間と共にさらに深く学びましょう。

    **参加する理由**

    - **専門的サポート**: 販売後の問題や技術的な課題をコミュニティとチームで解決
    - **学びと共有**: 技術やチュートリアルを交換し、スキルを向上
    - **限定プレビュー**: 新製品発表や先行情報に早期アクセス
    - **特別割引**: 新製品を特別価格で購入可能
    - **イベント・プレゼント企画**: プレゼントや季節キャンペーンに参加

    👉 一緒に探求し、創造しましょう。今すぐ [|link_sf_facebook|] をクリックして参加！

.. _blynk_motor2_py_mcp3008:

スマートファン (MCP3008)
===========================

このプロジェクトでは、Blynk を使用して温度を確認し、リモートでファンをオンにすることができます。

.. note:: このプロジェクトを始める前に、:ref:`bk_start` を完了することをお勧めします。  
   以下の内容で Blynk について明確に理解できるようになります。

**必要な部品**

このプロジェクトで必要な部品は以下の通りです。

部品を一式そろえたキットを購入すると便利です。リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名称
        - キット内数量
        - リンク
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

個別に購入する場合は以下のリンクを参照してください。

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - 部品名
        - 購入リンク

    *   - :ref:`cpn_gpio_extension_board`
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
    *   - :ref:`cpn_mcp3008`
        - \-
    *   - :ref:`cpn_thermistor`
        - |link_thermistor_buy|
    *   - :ref:`cpn_motor`
        - |link_motor_buy|

**1. 配線**

.. image:: img/3.1.4_smart_fan_iot.png

**2. ウィジェットとデータストリームの作成**

1. 右上のメニューアイコンをクリックし、ダッシュボードの編集を選択します。

    .. image:: img/sp220913_180231.png

2. ダッシュボードに Switch ウィジェットと Label ウィジェットを追加します。

    .. image:: img/sp220914_175437.png

3. Switch ウィジェット用にデータストリームを作成します (例では V3 を使用)。これはモーターのオン/オフ制御に使用します。

    .. image:: img/sp220914_155911.png

4. Label ウィジェット用にデータストリームを作成します (例では V0 を使用)。これは温度表示に使用します。  
   **DATA TYPE** を String に設定します。

    .. image:: img/sp220914_175616.png

5. 完了したら、右上の **Save And Apply** をクリックします。

    .. image:: img/sp220913_182300.png

**3. コードの実行**

1. コードを編集します。

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_motor(mcp3008).py

2. 以下の行を見つけ、 ``BLYNK_AUTH_TOKEN`` を貼り付けます。

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. コードを実行します。

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_motor(mcp3008).py

4. Blynk にアクセスし、ダッシュボード上で Label ウィジェットを通じて温度を確認し、Switch ウィジェットを使ってファンをオン/オフできます。

5. モバイルデバイスで Blynk を使用したい場合は、:ref:`blynk_mobile` を参照してください。
