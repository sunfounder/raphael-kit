.. _spi_configuration:

SPI 設定
-----------------------

#. Raspberry Pi で SPI インターフェースを有効にします。すでに有効になっている場合は、このステップを省略できます。よく分からない場合は、以下の手順に従ってください。

   * Raspberry Pi 設定ツールを開きます:

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         sudo raspi-config

   * **3 インターフェース オプション**

     .. image:: img/image282.png
        :align: center

   * **I3 SPI**

     .. image:: img/i3spi.png
        :align: center
     
   * **<YES> を選択し、<OK> と <Finish> をクリックします。**

     .. image:: img/image286.png
        :align: center 

#. SPI モジュールが有効になっているか確認します。

   * 次のコマンドを実行します:

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         ls /dev/sp*

   * 次のような出力が表示されるはずです:


     .. code-block:: 
     
         /dev/spidev0.0  /dev/spidev0.1

   これらのデバイスが表示された場合、SPI インターフェースは有効で使用可能です。

#. ``spidev`` Python ライブラリをインストールします。

   * ``pip`` を使用してインストールするには次のコマンドを実行します:

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         sudo pip3 install spidev
     
   このライブラリは /dev/spidevX.Y を使用して SPI デバイスと通信するための Python インターフェースを提供します。
