``RPi.GPIO`` の確認
=================================

Pythonユーザーであれば、 ``RPi.GPIO`` というAPIを使ってGPIOをプログラムできます。

``RPi.GPIO`` は、Raspberry PiのGPIOチャンネルを制御するためのモジュールです。このパッケージには、Raspberry Pi上のGPIOを制御するためのクラスが含まれています。

RPi.GPIOがインストールされているかどうかをテストするには、Pythonで以下のように入力します。

.. raw:: html

   <run></run>

.. code-block::

    python

.. image:: ../img/image27.png

Python CLIで ``import RPi.GPIO`` と入力します。エラーが出なければ、RPi.GPIOがインストールされているということです。

.. raw:: html

   <run></run>

.. code-block::

    import RPi.GPIO

.. image:: ../img/image28.png

Python CLIを終了するには、以下のように入力します：

.. raw:: html

   <run></run>

.. code-block::

    exit()

.. image:: ../img/image29.png
