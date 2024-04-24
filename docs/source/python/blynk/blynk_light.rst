.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

スマートライト
===============

このプロジェクトでは、Blynkのスライダーを使用してLEDの明るさを制御し、スイッチでオン/オフします。

.. note:: このプロジェクトを開始する前に、 :ref:`bk_start` を完了することをお勧めします。それによって、Blynkに関する理解が深まります。


**必要なコンポーネント**

このプロジェクトで必要なコンポーネントは以下の通りです。

一式を購入することが便利です、リンクはこちら：

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - 名前	
        - このキットのアイテム
        - リンク
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

以下のリンクから個々に購入することもできます。

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - コンポーネント紹介
        - 購入リンク
    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_led`
        - |link_led_buy|

**1. 配線**

.. image:: img/wiring_led1.png

**2. ウィジェットとデータストリームの作成**

1. 右上のメニューアイコンをクリックして、ダッシュボードの編集を選択します。

    .. image:: img/sp220913_180231.png

2. ダッシュボードにスイッチウィジェットとスライダーウィジェットを追加します。

    .. image:: img/sp220914_160427.png

3. スイッチウィジェット用のデータストリームを作成します（V3を使用しました）。これはLEDのオン/オフ制御に使用されます。

    .. image:: img/sp220914_155911.png

4. スライダーウィジェット用のデータストリームを作成します（V2を使用しました）、値の範囲は0から100です、これはLEDの明るさを制御するために使用されます。

    .. image:: img/sp220914_160234.png

#. 完了したら、右上の「保存して適用」をクリックします。

    .. image:: img/sp220913_182300.png

**3. コードの実行**

1. コードを編集します

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_light.py

2. 下記の行を探して、 ``BLYNK_AUTH_TOKEN`` を貼り付けます。

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. コードを実行します。

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_light.py

4. Blynkに移動して、ダッシュボードのウィジェットを操作します。スイッチウィジェットをクリックするとLEDがオン/オフになり、スライダーウィジェットを操作するとLEDの明るさが変わります。

#. もしBlynkをモバイルデバイスで使用したい場合は、 :ref:`blynk_mobile` を参照してください。