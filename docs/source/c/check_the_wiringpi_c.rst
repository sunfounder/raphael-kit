.. _install_wiringpi:

WiringPiのインストールと確認
=======================================

``wiringPi`` は、Raspberry Piに適用されるC言語のGPIOライブラリです。これはGNU Lv3に準拠しています。wiringPiの関数はArduinoのwiringシステムの関数に似ています。これにより、Arduinoに慣れているユーザーがwiringPiをより簡単に使用できます。

``wiringPi`` には、Raspberry Piのさまざまなインターフェイスを制御できる多くのGPIOコマンドが含まれています。

以下のコマンドを実行して、 ``wiringPi`` ライブラリをインストールしてください。

.. raw:: html

   <run></run>

.. code-block::

    sudo apt-get update
    git clone https://github.com/WiringPi/WiringPi
    cd WiringPi 
    ./build

wiringPiライブラリが正常にインストールされたかどうかは、次の指示に従って確認できます。

.. raw:: html

   <run></run>

.. code-block::

    gpio -v

.. image:: ../img/image30.png

次のコマンドでGPIOを確認します:

.. raw:: html

   <run></run>

.. code-block::

    gpio readall

.. image:: ../img/image31.png

wiringPiの詳細については、 `WiringPi <https://github.com/WiringPi/WiringPi>`_ を参照してください。

