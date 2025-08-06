.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _cpn_gpio_board:

.. _cpn_gpio_extension_board:

GPIO拡張ボード
=====================

コマンドの学習を始める前に、まずはRaspberry Piのピンについて詳しく知る必要があります。これは後の学習で重要となります。

GPIO拡張ボードを使用することで、Raspberry Piのピンを簡単にブレッドボードに引き出すことができます。これにより、頻繁な挿入・抜去によるGPIOの損傷を防ぐことができます。こちらはRaspberry Pi Model B+、2 Model B、および3, 4 Model B用の40ピンGPIO拡張ボードとGPIOケーブルです。

.. image:: img/image32.png
    :align: center

**ピン番号**

Raspberry Piのピンには、wiringPi、BCM、Boardという3つの命名方法があります。

これらの命名方法のうち、40ピンGPIO拡張ボードはBCMという命名方法を採用しています。ただし、I2CポートやSPIポートなど特殊なピンには、それ自体に付いている名称が用いられます。

次の表は、GPIO拡張ボード上の各ピンのWiringPi、Board、および固有のNameによる命名方法を示しています。例えば、GPIO17の場合、Boardの命名方法では11、wiringPiの命名方法では0、固有の命名方法ではGPIO0となります。

.. note::

    1）C言語では、WiringPiという命名方法が使用されます。
    
    2）Python言語では、適用される命名方法は **Board** と **BCM** であり、 ``GPIO.setmode()`` 関数を用いて設定します。

    3）Scratch 3およびProcessingでは、適用される命名方法は **BCM** です。

.. image:: img/gpio_board.png
