.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _check_pigpio:

pigpioの確認
===================

pigpioは、Raspberry PiのGPIOチャンネルを制御するために使用されるモジュールです。このパッケージには、Raspberry Pi上のGPIOを制御するためのいくつかの方法が提供されています。例やドキュメンテーションについては、 https://www.npmjs.com/package/pigpio をご参照ください。

以下のコマンドを入力して、pigpioライブラリをインストールします。

.. raw:: html

    <run></run>

.. code-block::

    npm install pigpio

ライブラリが正常にインストールされたかどうかを確認するため、ディレクトリを変更し、nodejsに入力します:

.. raw:: html

    <run></run>

.. code-block::

    cd ~/raphael-kit/nodejs
    nodejs

.. image:: img/pigpio1.png

次に、require('pigpio')を入力します:

.. raw:: html

    <run></run>

.. code-block::

    require('pigpio')

.. image:: img/pigpio2.png   

上記の画面が表示されれば、ライブラリのインストールは成功しています。

node CLIを終了する場合は、Ctrl+Cを2回押してください。

.. image:: img/pigpio3.png
