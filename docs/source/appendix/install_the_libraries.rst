ライブラリのインストール
==========================

C言語ユーザー向け
-------------------

BCM2835
~~~~~~~~~~~~~~~
このライブラリはRaspberry Pi（RPi）用のC言語ライブラリです。Broadcom BCM 2835チップにアクセスするためのGPIOやその他のIO機能を提供します。これにより、RPiボードの26ピンIDEプラグ上のGPIOピンを制御し、さまざまな外部デバイスとインターフェースすることができます。

デジタル入力の読み取りやデジタル出力の設定、SPIとI2Cの使用、システムタイマーへのアクセス等の関数が提供されています。割り込みはサポートされていませんが、ポーリングによるピンイベント検出がサポートされています。

すべてのRPIバージョンおよびDebian Buster 10を含むすべてのDebianバージョンで動作します。

ターミナルを開き、 ``~`` パスに ``bcm2835`` ライブラリをダウンロードしてください。

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~
    wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.69.tar.gz

ダウンロードしたパッケージを解凍します。

.. raw:: html

   <run></run>

.. code-block:: 

    tar zxvf bcm2835-1.69.tar.gz

以下のコマンドでBCM2835ライブラリをインストールします。

.. raw:: html

   <run></run>

.. code-block:: 

    cd bcm2835-1.69
    ./configure
    make
    sudo make check
    sudo make install

* 参考: `bcm2835 <http://www.airspayce.com/mikem/bcm2835/>`_  


Pythonユーザー向け
----------------------

Luma.LED_Matrix
~~~~~~~~~~~~~~~~~~~~~~~

このライブラリはPython 3用で、MAX7219ドライバー（SPIを使用）、WS2812（NeoPixels、Pimoroni Unicorn pHat/HatとUnicorn Hat HD）、およびAPA102（DotStar）を使用してLEDマトリックスディスプレイとインターフェースします。

まず、必要な依存ライブラリを以下のコマンドでインストールします。

.. raw:: html

   <run></run>

.. code-block:: 

    sudo usermod -a -G spi,gpio pi
    sudo apt install build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5

.. note:: warning

    Raspbianでaptと共にバンドルされているデフォルトのpipとsetuptoolsは非常に古く、コンポーネントが正しくインストールされない場合があります。最初にそれらをアップグレードしてください。

    .. raw:: html

       <run></run>

    .. code-block:: 

        sudo -H pip install --upgrade --ignore-installed pip setuptools

次に、PyPIからluma.led_matrixライブラリの最新版をインストールします。

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 -m pip install --upgrade luma.led_matrix

* 参考: `Luma.LED_Matrix <https://luma-led-matrix.readthedocs.io/en/latest/install.html>`_

SpidevとMFRC522
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``spidev`` ライブラリはSPIとのインタラクションを助け、このチュートリアルではRaspberry PiがRFID RC522と対話するために必要です。

以下のコマンドでRaspberry Piに ``spidev`` を ``pip`` 経由でインストールします。

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install spidev

続いて、MFRC522ライブラリをインストールします。

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install mfrc522

MFRC522ライブラリには ``MFRC522.py`` と ``SimpleMFRC522.py`` という2つのファイルが含まれています。

そのうち ``MFRC522.py`` はRFID RC522インターフェースの実装で、このライブラリはPiのSPIインターフェースを通じてRFIDと通信するすべての重い作業を処理します。

``SimpleMFRC522.py`` は ``MFRC522.py`` ファイルを大幅に簡略化し、いくつかの関数しか扱わなくてもよいようにしています。
