.. _i2c_config:

I2C設定
-----------------------

**ステップ1**: Raspberry PiのI2Cポートを有効にします（既に有効にしている場合はこのステップをスキップしてください。不明な場合は続けてください）。

.. raw:: html

   <run></run>
  
.. code-block:: 

    sudo raspi-config

**3 インターフェイスオプション**

.. image:: img/image282.png
    :align: center

**P5 I2C**

.. image:: img/image283.png
    :align: center

**<Yes>, では <Ok> -> <Finish>**

.. image:: img/image284.png
    :align: center

**ステップ2**: i2cモジュールがロードされているか確認します。

.. raw:: html

   <run></run>
 
.. code-block:: 

    lsmod | grep i2c

次のようなコードが表示されれば成功です（数字は異なる場合があります）。表示されない場合は、 ``sudo reboot`` でRaspberry Piを再起動してください。

.. code-block:: 

    i2c_dev                     6276    0
    i2c_bcm2708                 4121    0

**ステップ3**: i2c-toolsをインストールします。

.. raw:: html

   <run></run>
 
.. code-block:: 

    sudo apt-get install i2c-tools

**ステップ4**: I2Cデバイスのアドレスを確認します。

.. raw:: html

   <run></run>
  
.. code-block:: 

    i2cdetect -y 1      # Raspberry Pi 2以降のバージョン用

.. raw:: html

   <run></run>
 
.. code-block:: 

    i2cdetect -y 0      # Raspberry Pi 1用


.. code-block:: 

    pi@raspberrypi ~ $ i2cdetect -y 1
        0  1  2  3   4  5  6  7  8  9   a  b  c  d  e  f
    00:           -- -- -- -- -- -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    40: -- -- -- -- -- -- -- -- 48 -- -- -- -- -- -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- -- --

I2Cデバイスが接続されている場合、そのデバイスのアドレスが表示されます。

**ステップ5**:

**C言語ユーザー向け**: libi2c-devをインストールします。

.. raw:: html

   <run></run>
 
.. code-block:: 

    sudo apt-get install libi2c-dev 

**Pythonユーザー向け**: I2Cのsmbusをインストールします。

.. raw:: html

   <run></run>
 
.. code-block:: 

    sudo pip3 install smbus2

