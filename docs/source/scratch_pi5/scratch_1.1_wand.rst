.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _1.1_scratch_pi5:

1.1 魔法の杖
=================

今日はLED、Raspberry Pi、そしてScratchを使用して楽しいゲームを作成します。魔法の杖を振ると、LEDが点滅します。

.. image:: img/1.1_header.png

必要な部品
------------------------------

このプロジェクトには、以下の部品が必要です。

.. image:: img/1.1_list.png

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
    *   - :ref:`cpn_led`
        - |link_led_buy|

回路を組む
-----------------------

.. image:: img/1.1_image49.png

GPIO拡張を追加
---------------------

左下の **拡張機能を追加** ボタンをクリックし、すべてのScratchプロジェクトで使用する **Raspberry Pi GPIO** 拡張機能を追加します。

.. image:: img/1.1_scratchled1.png
    :align: center

.. image:: img/1.1_scratchled2.png
    :align: center

.. image:: img/1.1_scratchled3.png
    :align: center

コードをロードして何が起こるかを確認する
-----------------------------------------

コンピュータから( ``~/raphael-kit/scratch/code`` )のコードファイルをScratch 3にロードします。

.. image:: img/1.1_scratch_step1.png

.. image:: img/1.1_scratch_step2.png

ステージエリアで魔法の杖をクリックすると、LEDが2秒間点滅することが確認できます。

.. image:: img/1.1_step3.png

スプライトに関するヒント
--------------------------

**Upload Sprite** をクリックします。

.. image:: img/1.1_upload_sprite.png

``~/raphael-kit/scratch/picture`` パスから **Wand.png** をScratch 3にアップロードします。

.. image:: img/1.1_upload.png

最後に、 **Sprite1** を削除します。

.. image:: img/1.1_delete.png

コードに関するヒント
---------------------

.. image:: img/1.1_LED1.png
  :width: 300

これは、ステージ上の緑の旗をクリックしたときのトリガー条件を持つイベントブロックです。すべてのコードの最初にはトリガーイベントが必要であり、 **block palette** の **Events** カテゴリで他のトリガーイベントを選択することができます。

.. image:: img/1.1_events.png
  :width: 300

たとえば、トリガーイベントをスプライトのクリックに変更することができます。

.. image:: img/1.1_LED2.png
  :width: 300

これは、一定回数のサイクルを持つブロックです。10という数字を入力すると、ブロック内のイベントが10回実行されます。

.. image:: img/1.1_LED4.png
  :width: 300

このブロックは、一定期間の間、プログラムを一時停止するために使用されます。

.. image:: img/1.1_LED3.png
  :width: 500

ScratchでBCM命名方法が使用されているので、このコードはGPIO17(BCM17)を0V(低レベル)に設定しています。LEDのカソードがGPIO17に接続されているため、LEDは点灯します。逆に、GPIO(BCM17)を高に設定すると、LEDはオフになります。
