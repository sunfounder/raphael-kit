SPI設定
-----------------------

**ステップ1**: お使いのRaspberry PiのSPIポートを有効にしてください（すでに有効化している場合はこのステップをスキップ。不明な場合は、続けてください）。

.. raw:: html

   <run></run>
  
.. code-block:: 

    sudo raspi-config

**3 インターフェースオプション**

.. image:: img/image282.png
    :align: center

**P4 SPI**

.. image:: img/image285.png
    :align: center

**<YES>を選択し、<OK>と<Finish>をクリックしてください。**

.. image:: img/image286.png
    :align: center

**ステップ2**: SPIモジュールがロードされていることを確認します。

.. raw:: html

   <run></run>
  
.. code-block:: 

    ls /dev/sp*

次のようなコードが表示されます（番号は異なる場合があります）。

.. code-block:: 

    /dev/spidev0.0  /dev/spidev0.1

**ステップ3**: PythonモジュールSPI-Pyをインストールします。

.. raw:: html

   <run></run>
  
.. code-block:: 

    git clone https://github.com/lthiery/SPI-Py.git
    cd SPI-Py
    sudo python3 setup.py install

.. note::
    このステップはPythonユーザーのためのものです。C言語を使用している場合は、このステップをスキップしてください。

