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

.. _bk_start:

Blynk の開始
=========================

このプロジェクトでは Blynk の使い方を学びます。

Blynk 上のウィジェットを操作すると、Raspberry Pi がその値を出力します。

以下の手順に従ってください。順序を飛ばさずに進めることが重要です。


1. Blynk の設定
--------------------------

1. `BLYNK <https://blynk.io/>`_ へアクセスし、**START FREE** をクリックします。

    .. image:: img/sp220607_142551.png

#. メールアドレスを入力してアカウントを登録します。

    .. image:: img/sp220607_142807.png

#. メールに届いたリンクを開き、アカウント登録を完了します。

    .. image:: img/sp220607_142936.png

#. 登録後、**Blynk Tour** が表示されます。Blynk の基本情報を知るために読むことをおすすめします。

    .. image:: img/sp220607_143244.png

#. 次にテンプレートとデバイスを作成する必要がありますが、ここでは **Cancel** をクリックします。

    .. image:: img/sp220607_143608.png

#. ナビゲーションバーから **Developer Zone** を選択します。

    .. image:: img/develop_zone.png

#. **Create New Template** をクリックします。

    .. image:: img/new_template.png

#. **NAME** を自由に入力し、**HARDWARE** は **Raspberry Pi** を選択し、**Done** をクリックします。

    .. image:: img/sp220913_170402.png

#. Info ページに移動したら、右上の **save** をクリックします。

    .. image:: img/sp220913_171202.png

#. ナビゲーションバーから **Devices** ページへ移動します。

    .. image:: img/devices.jpg

#. **Create New Device** をクリックします。

    .. image:: img/new_devices.png

#. **From template** を選択します。

    .. image:: img/create_new_device.png

#. **TEMPLATE** は先ほど設定したものを選択し、**DEVICE NAME** は自由に設定して **Create** をクリックします。

    .. image:: img/sp220913_173507.png

#. 次のようなページが表示されれば、初期設定は完了です。

    .. image:: img/my_device.png


2. ダッシュボード編集
--------------------------------

1. **edit dashboard** をクリックします。

    .. image:: img/edit_dashboard.png

#. 任意の制御ウィジェットをダッシュボードにドラッグします。例として Switch と Slider を追加しました。

    .. image:: img/sp220913_180725.png

#. ウィジェットの設定アイコンをタップします。

    .. image:: img/sp220913_180806.png

#. Datastream を作成し、**Virtual Pin** を選択します。

    .. image:: img/sp220913_180906.png

#. Datastream の設定を完了します。Switch 用の場合、**DATA TYPE** を ``Integer``、**MIN** を ``0``、**MAX** を ``1`` に設定して作成し、保存します。

    .. image:: img/sp220913_181113.png

#. 同様に Slider ウィジェット用の Datastream を作成し、**DATA TYPE**、**MIN**、**MAX** を必要に応じて設定します。

    .. image:: img/sp220913_182042.png

#. 完了したら、右上の **Save And Apply** をクリックします。

    .. image:: img/sp220913_182300.png


3. Blynk ライブラリのインストール
----------------------------------------------------------

以下のコマンドでインストールします。

.. raw:: html

   <run></run>

.. code-block::

    cd ~
    git clone https://github.com/vshymanskyy/blynk-library-python.git
    cd blynk-library-python
    sudo python3 setup.py


4. サンプルコードのダウンロード
-------------------------------

以下のコマンドを実行してサンプルコードを取得します。

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~
    git clone https://github.com/sunfounder/blynk-raspberrypi-python.git


5. コードの実行
-----------------

1. Blynk の Device Info ページに移動し、**FIRMWARE CONFIGURATION** にある **BLYNK_AUTH_TOKEN** をコピーします。

    .. image:: img/sp220913_182456.png

2. コードを編集します。

.. raw:: html

    <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_start.py

3. 以下の行を見つけ、 ``BLYNK_AUTH_TOKEN`` を貼り付けます。

.. code-block:: 

    BLYNK_AUTH = 'YourAuthToken'

4. コードを実行します。

.. raw:: html

    <run></run>

.. code-block:: 

    sudo python3 blynk_start.py

5. Blynk のダッシュボードにアクセスし、ウィジェットを操作します。

    .. image:: img/sp220913_183529.png

6. ターミナルにあなたの操作が表示されるはずです。

.. code-block:: 

    ..
       ___  __          __
      / _ )/ /_ _____  / /__
     / _  / / // / _ \/  '_/
    /____/_/\_, /_//_/_/\_\
            /___/ for Python v1.0.0 (linux)

    Connecting to blynk.cloud:443...
    Blynk ready. Ping: 142 ms
    V0 value: ['1']
    V0 value: ['0']
    V1 value: ['3']
    V1 value: ['8']
    V0 value: ['1']
