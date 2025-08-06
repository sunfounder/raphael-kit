.. note::

    こんにちは、SunFounder Raspberry Pi & Arduino & ESP32 愛好者コミュニティ (Facebook) へようこそ！  
    Raspberry Pi、Arduino、ESP32 を仲間と一緒にさらに深く学びましょう。

    **参加する理由**

    - **専門的なサポート**: 販売後の問題や技術的な課題をコミュニティとチームで解決。
    - **学びと共有**: 技術やチュートリアルを交換し、スキルを向上。
    - **限定プレビュー**: 新製品発表や先行情報に早期アクセス。
    - **特別割引**: 新製品を特別価格で購入可能。
    - **イベント・プレゼント企画**: プレゼントや季節キャンペーンに参加。

    👉 一緒に探求し、創造しましょう。今すぐ [|link_sf_facebook|] をクリックして参加！

.. _remote_desktop:

Raspberry Pi のリモートデスクトップアクセス
==================================================

コマンドラインよりもグラフィカルユーザインターフェース (GUI) を好む場合、Raspberry Pi はリモートデスクトップ機能をサポートしています。  
このガイドでは、リモートアクセスに VNC (Virtual Network Computing) を利用する方法を説明します。

この目的のために、`VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ の使用を推奨します。

**Raspberry Pi での VNC サービス有効化**

Raspberry Pi OS には VNC サービスが標準でインストールされていますが、デフォルトでは無効になっています。  
以下の手順で有効にしてください。

#. Raspberry Pi のターミナルで次のコマンドを入力します。

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 矢印キーを使って **Interfacing Options** に移動し、**Enter** を押します。

    .. image:: img/config_interface.png
        :align: center

#. オプションの中から **VNC** を選択します。

    .. image:: img/vnc.png
        :align: center

#. 矢印キーで **<Yes>** -> **<OK>** -> **<Finish>** を選び、VNC サービスの有効化を完了します。

    .. image:: img/vnc_yes.png
        :align: center

**VNC Viewer でのログイン**

#. パーソナルコンピュータに `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ をダウンロードしてインストールします。

#. インストール完了後、VNC Viewer を起動します。Raspberry Pi のホスト名または IP アドレスを入力し、Enter キーを押します。

    .. image:: img/vnc_viewer1.png
        :align: center

#. プロンプトが表示されたら、Raspberry Pi のユーザー名とパスワードを入力し、**OK** をクリックします。

    .. image:: img/vnc_viewer2.png
        :align: center

#. これで Raspberry Pi のデスクトップ画面にアクセスできるようになります。

    .. image:: img/bullseye_desktop.png
        :align: center
