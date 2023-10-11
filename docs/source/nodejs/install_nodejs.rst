.. _install_nodejs:

Nodejsとは？
---------------------------

Node.jsは2009年5月にリリースされ、Ryan Dahlによって開発されました。これはChrome V8エンジンに基づくJavaScriptランタイム環境です。イベント駆動型、ノンブロッキングI/Oモデルを使用して、JavaScriptをサーバーサイド開発プラットフォーム上で実行することができます。

簡単に言うと、Node.jsはサーバー上で動作するJavaScriptです。Javascriptに慣れていれば、Node.jsを簡単に学ぶことができます。

Nodejsは通常、 ``npm install xxx`` というコマンドを使用してサードパーティのパッケージをインストールします。これにはnpmツールのインストールが必要で、これはpythonのpipツールに似ています。

nodejsとnpmのインストールまたは更新
------------------------------------------

nodejsとnpmをインストールおよび更新するには、以下のコマンドを実行します。

.. raw:: html

    <run></run>

.. code-block::

    sudo apt-get update
    sudo apt-get install nodejs
    sudo apt-get install npm 
    sudo npm install npm -g

次に、以下のコマンドで現在のNodeのバージョンを確認します。

.. raw:: html

    <run></run>

.. code-block::

    node -v

以下のコマンドで現在のnpmのバージョンを確認します。

.. raw:: html

    <run></run>

.. code-block::

    npm -v
