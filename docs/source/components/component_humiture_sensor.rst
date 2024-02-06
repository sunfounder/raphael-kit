
.. _human_sensor_module:


湿温センサモジュール
==========================

.. image:: img/dht11_pic.png
    :width: 400
    :align: center

このデジタル温度・湿度センサDHT11は、温度と湿度のキャリブレートされたデジタル信号出力を含む複合センサです。専用のデジタルモジュール集積技術と温湿度センシング技術が採用されており、製品の高い信頼性と長期間にわたる優れた安定性が確保されています。

使用可能なピンは3つのみ: VCC, GND, DATAです。
通信プロセスは、DATAラインからDHT11に開始信号を送り、DHT11がこれを受信して応答信号を返すことから始まります。次に、ホストは応答信号を受け取り、40ビットの温湿データ（8ビットの湿度整数 + 8ビットの湿度小数 + 8ビットの温度整数 + 8ビットの温度小数 + 8ビットのチェックサム）を受信します。

.. image:: img/Dht11.png

* `DHT11データシート <https://components101.com/sites/default/files/component_datasheet/DHT11-Temperature-Sensor.pdf>`_

**例**

* :ref:`2.2.3_c` (Cプロジェクト)
* :ref:`2.2.3_py` (Pythonプロジェクト)