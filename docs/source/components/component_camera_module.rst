.. _camera_module:

カメラモジュール
====================================

**説明**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

こちらはOV5647センサーを搭載した5MPのRaspberry Pi用カメラモジュールです。付属のリボンケーブルをRaspberry PiのCSI（Camera Serial Interface）ポートに接続するだけで、すぐに使用可能です。

このモジュールは小型で、寸法は25mm x 23mm x 9mm、重さは3gです。そのため、モバイル機器やサイズ・重量が重要な用途に最適です。カメラはネイティブで5メガピクセルの解像度を持ち、固定フォーカスレンズが搭載されています。静止画は2592 x 1944ピクセルで、また1080p30、720p60、640x480p90ビデオもサポートしています。

.. note::

   このモジュールは、写真とビデオのキャプチャのみが可能で、音声は録音できません。

**仕様**

* **静止画解像度**: 2592×1944 
* **サポートするビデオ解像度**: 1080p/30 fps, 720p/60fps, 640 x480p 60/90ビデオ録画
* **開口部 (F)**: 1.8 
* **視野角**: 65度 
* **寸法**: 24mmx23.5mmx8mm 
* **重量**: 3g 
* **インターフェース**: CSIコネクタ
* **対応OS**: Raspberry Pi OS（最新版推奨）



カメラモジュールの組み立て
----------------------------------------



カメラモジュールまたはRaspberry Piには平らなプラスチックコネクタがあります。黒い固定スイッチを慎重に引き出し、FFCケーブルを指示された方向でプラスチックコネクタに差し込み、固定スイッチを元の位置に戻します。

FFCケーブルが正しく取り付けられている場合、それはまっすぐで、優しく引っ張っても外れません。そうでない場合は、再度取り付けてください。

.. image:: img/connect_ffc.png
.. image:: img/1.10_camera.png
   :width: 700

.. warning::

   電源が入った状態でカメラを取り付けないでください。カメラが壊れる可能性があります。



.. _enable_camera:

カメラインターフェースの有効化
------------------------------------------------

以下のコマンドを実行して、Raspberry Piのカメラインターフェースを有効にします。すでに有効にしている場合はこのステップをスキップしてください。

.. raw:: html

   <run></run>

.. code-block:: 

   sudo raspi-config

**3 インターフェーシングオプション**

.. image:: img/image282.png
   :align: center

**P1 カメラ**

.. image:: img/camera_config1.png
   :align: center

**<Yes>、次に<Ok> -> <Finishz>**

.. image:: img/camera_config2.png
   :align: center

設定が完了したら、Raspberry Piを再起動することをお勧めします。

.. raw:: html

   <run></run>

.. code-block:: 

   sudo reboot

**例**

* :ref:`3.1.1_py` （Pythonプロジェクト）
* :ref:`3.1.2_py` （Pythonプロジェクト）
* :ref:`4.1.1_py` （Pythonプロジェクト）
* :ref:`4.1.4_py` （Pythonプロジェクト）
* :ref:`4.1.5_py` （Pythonプロジェクト）
* :ref:`1.10_scratch` （Scratchプロジェクト）
* :ref:`1.18_scratch` （Scratchプロジェクト）

