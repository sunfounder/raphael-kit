.. _play_with_processing:

Processingを体験しよう(Pi 4)
=============================

Processingとは？
---------------------------

Processingは、アニメーションに焦点を当てた視覚的なアプリケーションの開発を容易にするために作成されたシンプルなプログラミング環境です。ユーザーがインタラクションを通じて即座のフィードバックを受け取ることを強調しています。
開発者はコードでアイディアを“スケッチ”する手段を求めていました。
過去10年間でその機能が拡張されてきた結果、Processingはスケッチの役割に加えて、本格的な生産レベルの作業にも使用されるようになりました。
元々はアーティストやデザイナーを対象としたJavaのドメイン固有の拡張として構築されたProcessingは、大規模なインストール作業、モーショングラフィックス、複雑なデータ可視化に使用される完全なデザインとプロトタイピングツールに進化しました。

ProcessingはJavaに基づいていますが、Processingのプログラム要素は比較的シンプルであるため、Javaを知らなくても使用することができます。Javaに慣れている場合は、APIの動作方法を理解するまで、ProcessingがJavaと何か関係があると考えるのはやめたほうがよいでしょう。

このテキストは、 `Processingの概要 <https://processing.org/tutorials/overview/>`_ からのものです。

Processingのインストール
------------------------------

.. note:: 

    Processingを使用する前に、Raspberry Piのデスクトップにリモートでアクセスする必要があります(:ref:`remote_desktop`)、またはRaspberry Pi用のディスプレイを接続する必要があります。

.. ターミナルで以下のコマンドを実行して、Processingをインストールしてください。

.. .. raw:: html

..    <run></run>

.. .. code-block:: 

..     curl https://processing.org/download/install-arm.sh | sudo sh

.. インストールが完了したら、``processing``と入力して開始してください。

.. .. image:: img/processing1.png

.. 詳しいチュートリアルは、`Pi Processing <https://pi.processing.org/>`_を参照してください。

#. まず https://processing.org/download にアクセスして、 ``Linux（Raspberry Pi 32-bit）`` または ``Linux（Raspberry Pi 64-bit）`` バージョンを選択してください。この方法を使用すると、常に最新バージョンをダウンロードできます。

    また、ターミナルから以下のコマンドを使用してProcessingをダウンロードすることもできます。

    .. code-block:: 

        wget https://github.com/benfry/processing4/releases/download/processing-1293-4.3/processing-4.3-linux-arm32.tgz

    .. code-block:: 

        wget https://github.com/benfry/processing4/releases/download/processing-1293-4.3/processing-4.3-linux-arm64.tgz


#. ``.tar.gz`` ファイルがダウンロードされます。ほとんどのLinuxユーザーはこのファイル形式を知っているでしょう。ダウンロードした場所からファイルを展開してください。

    .. code-block:: 

        tar xvfz processing-xxxx.tgz

    xxxxをファイル名の残り部分、つまりバージョン番号に置き換えてください。これにより、processing-xxxxという名前のフォルダが作成されるか、それに類似した名前のフォルダが作成されます。 

#. そのディレクトリに移動してください:

    .. code-block:: 

        cd processing-xxxx

#. そして、それを実行してください:

.. code-block:: 

    ./processing

#. うまくいけば、メインのProcessingウィンドウが表示されるはずです。

    .. image:: img/processing2.png

ハードウェアI/Oのインストール
--------------------------------

Raspberry PiのGPIOを使用するためには、手動で `ハードウェアI/Oライブラリ <https://processing.org/reference/libraries/io/index.html>`_ を追加する必要があります。

``Sketch`` -> ``Import Library`` -> ``Add Library...`` をクリックしてください。

.. image:: img/import-00.png

Hardware I/Oを探して選択し、インストールをクリックしてください。完了すると、チェックマークのアイコンが表示されます。

.. image:: img/import-02.png

プロジェクト
---------------

.. toctree::
    draw_a_matchmaker
    hello_mouse
    blinking_dot
    clickable_dot
    clickable_color_blocks
    inflating_the_dot
    dot_on_the_swing
    metronome
    show_number
    drag_number
