.. _check_pigpio:

pigpioの確認
===================

pigpioは、Raspberry PiのGPIOチャンネルを制御するために使用されるモジュールです。このパッケージには、Raspberry Pi上のGPIOを制御するためのいくつかの方法が提供されています。例やドキュメンテーションについては、 https://www.npmjs.com/package/pigpio をご参照ください。

以下のコマンドを入力して、pigpioライブラリをインストールします。

.. raw:: html

    <run></run>

.. code-block::

    npm install pigpio

ライブラリが正常にインストールされたかどうかを確認するため、ディレクトリを変更し、nodejsに入力します:

.. raw:: html

    <run></run>

.. code-block::

    cd ~/raphael-kit/nodejs
    nodejs

.. image:: img/pigpio1.png

次に、require('pigpio')を入力します:

.. raw:: html

    <run></run>

.. code-block::

    require('pigpio')

.. image:: img/pigpio2.png   

上記の画面が表示されれば、ライブラリのインストールは成功しています。

node CLIを終了する場合は、Ctrl+Cを2回押してください。

.. image:: img/pigpio3.png
