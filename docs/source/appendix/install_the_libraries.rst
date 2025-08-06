.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

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
.. _create_virtual:

仮想環境の作成
~~~~~~~~~~~~~~~~~~~~~~~

Raspberry Piや類似のデバイスを使用する場合、 ``pip`` を仮想環境でパッケージをインストールすることをお勧めします。これにより、依存関係の分離、システムのセキュリティの向上、システムのクリーンさの維持、プロジェクトの移行と共有の容易化が行われ、依存関係の管理が簡素化されます。これらの利点により、仮想環境はPython開発において非常に重要で便利なツールとなっています。

以下に、仮想環境を作成する手順を示します。

**1. 仮想環境の作成**

まず、システムにPythonがインストールされていることを確認する必要があります。Pythonバージョン3.3以降では、仮想環境を作成するための ``venv`` モジュールが付属しており、別途インストールする必要はありません。Python 2またはPython 3.3以前のバージョンを使用している場合は、 ``virtualenv`` をインストールする必要があります。

* Python 3の場合：

Python 3.3以降のバージョンでは、 ``venv`` モジュールを直接使用できます：

.. raw:: html

    <run></run>

.. code-block:: shell

    python3 -m venv myenv

これにより、現在のディレクトリに名前が ``myenv`` の仮想環境が作成されます。

* Python 2の場合：

まだPython 2を使用している場合は、まず ``virtualenv`` をインストールする必要があります：

.. raw:: html

    <run></run>

.. code-block:: shell

    pip install virtualenv

次に、仮想環境を作成します：

.. raw:: html

    <run></run>

.. code-block:: shell

    virtualenv myenv

これにより、現在のディレクトリに名前が ``myenv`` の仮想環境が作成されます。

**2. 仮想環境の有効化**

仮想環境を作成した後、使用するためにそれを有効化する必要があります。

.. note::

    Raspberry Piを再起動するたびや、新しいターミナルを開くたびに、仮想環境を有効化するために次のコマンドを再度実行する必要があります。

.. raw:: html

    <run></run>

.. code-block:: shell

    source myenv/bin/activate

仮想環境が有効化されると、コマンドラインのプロンプトの前に環境名が表示され、仮想環境内で作業していることが示されます。

**3. 仮想環境の終了**

作業を完了し、仮想環境から退出したい場合は、単純に次のコマンドを実行します：

.. raw:: html

    <run></run>

.. code-block:: shell

    deactivate

これにより、システムのグローバルPython環境に戻ります。

**4. 仮想環境の削除**

特定の仮想環境をもはや必要としない場合は、単純にその仮想環境を含むディレクトリを削除できます：

.. raw:: html

    <run></run>

.. code-block:: shell

    rm -rf myenv


Luma.LED_Matrix
~~~~~~~~~~~~~~~~~~~~~~~

これは、Raspberry Piや他のLinuxベースのシングルボードコンピュータで、MAX7219ドライバ（SPI経由）、WS2812（NeoPixels、Pimoroni Unicorn pHat/HatおよびUnicorn Hat HDを含む）、およびAPA102（DotStar）を使用してLEDマトリックスディスプレイとインターフェースを作成するためのPython 3ライブラリです。

#. 現在のユーザー（"pi"を自分のユーザー名に置き換えてください）がSPIおよびGPIOインターフェースにアクセスする権限を持つようにするため、ユーザーを ``spi`` および ``gpio`` グループに追加します。

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell

        sudo usermod -a -G spi,gpio pi

   このコマンドを実行した後、システムを再起動するか、ログアウトして再ログインすることをお勧めします。

#. 必要な依存関係をインストールします。 ``apt`` を使用してビルドツールと関連の開発ライブラリをインストールしてください。これらのライブラリは、特定のPythonパッケージをコンパイルおよびインストールするために必要です。

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
    
        sudo apt update
        sudo apt install -y build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff-dev

#. 仮想環境を作成します。ここで、 ``~/my_env`` は仮想環境のパスであり、カスタマイズすることができます。

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       python3 -m venv ~/my_env

#. 仮想環境を作成した後、使用するために有効化します。

   .. note::
   
       Raspberry Piを再起動するか新しいターミナルを開くたびに、仮想環境を再度有効化する必要があります。

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       source ~/my_env/bin/activate
   
   仮想環境が有効になっていると、コマンドプロンプトの前に環境名が表示され、仮想環境内で作業していることが確認できます。

#. 仮想環境内で、 ``pip`` と ``setuptools`` をアップグレードして、最新バージョンのパッケージをインストールできるようにします。
   
   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell

        pip install --upgrade pip setuptools

#. 次に、 ``luma.led_matrix`` をインストールします。
   
   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell
   
        pip install luma.led_matrix

#. インストール後、以下のコマンドを実行して ``luma.led_matrix`` が正しくインストールされていることを確認できます。成功すると、 ``luma.led_matrix`` のバージョン番号が表示されます。
   
   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell

        python3 -c "import luma.led_matrix; print(luma.led_matrix.__version__)"

#. 作業が完了し、仮想環境を終了したい場合は、次のコマンドを実行してください。
   
   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       deactivate

* 参考: `Luma.LED_Matrix <https://luma-led-matrix.readthedocs.io/en/latest/install.html>`_

.. _mfrc522_lib:

MFRC522
~~~~~~~~~~~~~~~~~~~~~~~~~~~

``spidev`` ライブラリはSPIとのインタラクションを助け、このチュートリアルではRaspberry PiがRFID RC522と対話するために必要です。

以下のコマンドでRaspberry PiにMFRC522ライブラリをインストールします。

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install mfrc522

MFRC522ライブラリには ``MFRC522.py`` と ``SimpleMFRC522.py`` という2つのファイルが含まれています。

そのうち ``MFRC522.py`` はRFID RC522インターフェースの実装で、このライブラリはPiのSPIインターフェースを通じてRFIDと通信するすべての重い作業を処理します。

``SimpleMFRC522.py`` は ``MFRC522.py`` ファイルを大幅に簡略化し、いくつかの関数しか扱わなくてもよいようにしています。
