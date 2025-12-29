.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _1.8_scratch_pi5:

1.8 サービスベル
===================

今日は、マイクロスイッチ、スピーカー、オーディオアンプモジュール、Raspberry Pi、およびScratchを使用してサービスベルを作成します。

マイクロスイッチをタップして、サービスベルの音を鳴らします。

.. image:: img/1.8_header.png

必要な部品
------------------------------

このプロジェクトには、以下の部品が必要です。

.. image:: img/1.8_component.png

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
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_micro_switch`
        - \-
    *   - :ref:`cpn_capacitor`
        - |link_capacitor_buy|
    *   - :ref:`cpn_audio_speaker`
        - \-

回路を組む
---------------------

.. image:: img/1.8_fritzing.png

コードをロードして動作を確認する
-----------------------------------------

コードファイル( ``1.8_service_bell.sb3`` )をScratch 3にロードします。

マイクロスイッチを押すと、サービスベルが1回鳴ります。


スプライトに関するヒント
---------------------------------

Sprite1を選択し、左上の **Costumes** をクリックします。 **Upload Costume** ボタンを使用して ``~/raphael-kit/scratch/picture`` のパスから **bell1.png** と **bell2.png** をアップロードします。デフォルトの2つのコスチュームを削除し、スプライトの名前を **bell** に変更します。

.. image:: img/1.8_travel1.png

**Sounds** オプションで、 ``~/raphael-kit/scratch/sound`` のパスから ``bell.wav`` をScratch 3にアップロードします。

.. image:: img/1.8_travel2.png

コードに関するヒント
-------------------------------

.. image:: img/1.8_travel3.png
  :width: 400

pin17が高いとき(マイクロスイッチが押されていない場合)、 **bell** スプライトのコスチュームを **bell1** に切り替えます。

.. image:: img/1.8_travel4.png
  :width: 400

マイクロスイッチを押すと、gpio17は低レベルになります。この時、 **bell** スプライトのコスチュームを **bell2** に切り替え、スピーカーを通じてサウンドエフェクトを再生します。

