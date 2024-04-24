.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _bk_start:

Blynkを始めよう
=========================

このプロジェクトでは、Blynkの使用方法を学びます。

Blynkのウィジェットをトリガーすると、Raspberry Piはその値を出力します。

以下の手順に従ってください。すべての章を順番に進め、スキップしないでください。



1. Blynkの設定
--------------------------



1. `BLYNK <https://blynk.io/>`_  にアクセスし、 **START FREE** をクリックします。

    .. image:: img/sp220607_142551.png

#. メールアドレスを入力してアカウントを登録します。

    .. image:: img/sp220607_142807.png

#. 登録したメールアドレスにアクセスして、アカウント登録を完了します。

    .. image:: img/sp220607_142936.png

#. その後、 **Blynk Tour** が表示されるので、Blynkについての基本情報を学びます。

    .. image:: img/sp220607_143244.png

#. 次に、テンプレートとデバイスを作成する必要があります。 **Cancel** をクリックします。

    .. image:: img/sp220607_143608.png

#. ナビゲーションバーからTemplateに移動します。

    .. image:: img/sp220913_170029.png

#. 新しいテンプレートを作成します。

    .. image:: img/sp220913_170206.png


#. **NAME** を入力し、 **HARDWARE** は **Raspberry Pi** に設定します。そして、 **Done** をクリックします。

    .. image:: img/sp220913_170402.png


#. Infoページにリダイレクトされるので、右上の保存ボタンをクリックします。

    .. image:: img/sp220913_171202.png

#. ナビゲーションバーから **Search** ページに移動します。

    .. image:: img/sp220913_172727.png

#. 新しいデバイスを作成します。

    .. image:: img/sp220913_173259.png

#. テンプレートから選択します。

    .. image:: img/sp220913_173350.png

#. 先ほど設定した **TEMPLATE** を選択し、 **DEVICE NAME** はカスタマイズ可能です。Createをクリックします。

    .. image:: img/sp220913_173507.png


#. このようなページが表示されれば、Blynkの初期設定が完了です。

    .. image:: img/sp220913_173950.png


2. ダッシュボードの編集
--------------------------------


1. 右上のメニューアイコンをクリックして、ダッシュボードの編集を選択します。

    .. image:: img/sp220913_180231.png

#. ダッシュボードに追加したいCONTROLウィジェットをドラッグします。私はSwitchとSliderを追加しました。

    .. image:: img/sp220913_180725.png

#. ウィジェットの設定アイコンをタップします。

    .. image:: img/sp220913_180806.png

#. データストリームを作成し、Virtual Pinを選択します。

    .. image:: img/sp220913_180906.png

#. データストリームの設定を完了します。ここではSwitch用に作成されたデータストリームで、 **DATA TYPE** は ``Interger`` に、 **MIN** と **MAX** は ``0`` と ``1`` に設定します。作成したら保存します。

    .. image:: img/sp220913_181113.png

#. Sliderウィジェット用のデータストリームも同様の手順で作成し、 **DATA TYPE** 、 **MIN** 、 **MAX** を必要に応じて修正します。

    .. image:: img/sp220913_182042.png

#. 完了したら、右上のSave And Applyをクリックします。

    .. image:: img/sp220913_182300.png


3. Blynkライブラリのインストール
----------------------------------

以下のコマンドを実行してインストールします。

.. raw:: html

   <run></run>

.. code-block::

    cd ~
    git clone https://github.com/vshymanskyy/blynk-library-python.git
    cd blynk-library-python
    sudo python3 setup.py

4. サンプルのダウンロード
-----------------------------

いくつかのサンプルを提供していますので、以下のコマンドを実行してダウンロードしてください。

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~
    git clone https://github.com/sunfounder/blynk-raspberrypi-python.git


5. コードの実行
-----------------



1. BlynkのDevice Infoページに移動し、 **FIRMWARE CONFIGURATION** の下に表示される情報から、 **BLYNK_AUTH_TOKEN** をコピーします。

    .. image:: img/sp220913_182456.png

2. コードを編集します。

.. raw:: html

    <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_start.py

3. 下記の行を探して、 ``BLYNK_AUTH_TOKEN`` を貼り付けます。

.. code-block:: 

    BLYNK_AUTH = 'YourAuthToken'

4. コードを実行します。

.. raw:: html

    <run></run>

.. code-block:: 

    sudo python3 blynk_start.py

5. Blynkに移動して、ダッシュボードのウィジェットを操作します。

    .. image:: img/sp220913_183529.png

6. これで、ターミナルで操作内容が表示されるようになります。

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

