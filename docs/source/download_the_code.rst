.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

コードのダウンロード
=================

このキットで使用されているすべてのサンプルプログラムは、公式 GitHub リポジトリに保存されています。  
以下のコマンドを使用して、プロジェクト一式を Raspberry Pi にダウンロードしてください。

リポジトリをクローンする
--------------------

#. Raspberry Pi にログインし、次を実行します：

   .. raw:: html
   
       <run></run>
   
   .. code-block:: bash
   
      cd ~/
      git clone https://github.com/sunfounder/raphael-kit.git --depth 1

#. プロジェクトディレクトリに移動します：

   .. raw:: html
   
       <run></run>
   
   .. code-block:: bash
   
      cd ~/raphael-kit/

#. ファイル一覧を表示します：

   .. raw:: html
   
       <run></run>
   
   .. code-block:: bash
   
      ls

#. 次のような構成が表示されます：

   .. code-block:: text
   
      raphael-kit/
      ├── c/
      ├── iot/
      ├── music/
      ├── nodejs/
      ├── python-pi5/
      ├── python/
      ├── scratch/
      └── README.md


プロジェクト構成の概要
--------------------------

各フォルダの簡単な説明は以下のとおりです：

* **c/**  

  Raspberry Pi 上で C 言語によるプログラミングを好むユーザー向けの、C 言語サンプルおよびライブラリです。

* **iot/**  

  Blynk プラットフォームとの連携、センサーのデモ、通信モジュールなど、IoT 関連のサンプルが含まれています。

* **music/** 

  後続のプロジェクトで使用される ``doorbell.wav`` や ``my_music.mp3`` などの音声リソースが含まれています。

* **nodejs/**

  Raspberry Pi 上で JavaScript ベースの開発を行うユーザー向けの Node.js サンプルです。

* **python/**  

  ``RPi.GPIO`` ライブラリを使用して書かれた Python のサンプルプログラムで、ほとんどの Raspberry Pi ボードに対応しています。

* **python-pi5/**  

  **Raspberry Pi 5** 向けに最適化された、``GPIO Zero`` ライブラリを使用した Python サンプルです。

* **scratch/** 

  グラフィカルプログラミングを学ぶ初心者向けに設計された Scratch のサンプルです。

* **README.md**  

  リポジトリに関する基本情報および一般的な使用方法が記載されています。

これで、お好みのプログラミング言語やプロジェクトタイプに対応するフォルダに入り、サンプルを実行できるようになりました。
