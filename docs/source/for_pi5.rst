.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好家コミュニティへようこそ！他の愛好家たちと一緒に、Raspberry Pi、Arduino、ESP32の世界をより深く探求しましょう。

    **参加する理由**

    - **専門サポート**: コミュニティとチームの助けを借りて、アフターサービスや技術的な課題を解決します。
    - **学びと共有**: スキルを向上させるために、ヒントやチュートリアルを交換します。
    - **限定プレビュー**: 新製品の発表やプレビューに早期にアクセスできます。
    - **特別割引**: 最新の製品に対して、限定割引を享受できます。
    - **フェスティバルプロモーションとプレゼント**: プレゼントやホリデープロモーションに参加できます。

    👉 私たちと一緒に探索と創造を始めましょうか？[|link_sf_facebook|] をクリックして、今日参加してください！

すべてのモデルに対応（推奨）
============================

Raspberry Pi 5の発売により、より強力なモデルが登場しましたが、特にGPIOに関していくつかの変更も導入されました。標準の40ピンインターフェースを維持しているものの、新たに統合されたRP1サウスブリッジチップとの接続により機能が変わりました。このカスタムRP1チップは現在、Pi 5の周辺機器を処理しており、さまざまな互換性の問題を引き起こしています。現在、Raspberry Pi組織が公式に管理しているGPIO Zeroライブラリのみが完全に互換性があります。このライブラリに特化した一連のコースを開発しました。

.. toctree::
    :maxdepth: 1
    
    python_pi5/play_with_python_pi5
    c_pi5/play_with_c
    scratch_pi5/play_with_scratch

他のプログラミング言語との互換性の問題については、以下の詳細情報をご覧ください：

**C言語**

.. note::

    * wiringPiライブラリはバージョン3.0からRaspberry Pi 5と互換性があります。しかし、最新バージョンではPWM機能がまだ開発中です。
    * 現在、最新バージョンのwiringPiを使用して、Raspberry Pi 5との互換性のためにコースを更新しています。更新をお待ちください。

C言語の実装はwiringPiライブラリに依存しています。しかし、wiringPiコミュニティライブラリは現在アーカイブされ、更新が行われていないため、Raspberry Pi 5プロジェクトには不適切です。詳細については、https://github.com/WiringPi/WiringPi を参照してください。

.. image:: img/pi5_c_language.png

**Processing**

Raspberry Pi 5でProcessing 4を使用する際、GPIOプログラミングに課題が生じます。「Invalid argument」や「GPIO pin 17 seems to be unavailable on your platform」といったエラーがGPIO関連コードの実行中に発生します（添付画像に示されている通り）。詳細については、https://github.com/benfry/processing4/issues/807 をご覧ください。

.. image:: img/pi5_processing.png

**Node.js**

Node.jsはpigpioライブラリを使用していますが、現在のところRaspberry Pi 5をサポートしていません。詳細については、https://github.com/joan2937/pigpio/issues/589 をご覧ください。

.. image:: img/pi5_nodejs.png
    :width: 700

**Scratch**

.. note::
 
    * Scratch 3のバージョン3.30.8は現在Raspberry Pi 5と互換性があります。
    * 私たちのコースもRaspberry Pi 5との互換性を持つように更新中です。これらの更新をお待ちください。

64ビットシステムでは、Raspberry Pi GPIOライブラリのインポートに問題が発生し、応答しなくなります。詳細については、https://github.com/raspberrypi/bookworm-feedback/issues/91 を参照してください。
