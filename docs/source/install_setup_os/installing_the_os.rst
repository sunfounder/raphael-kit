.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _install_os:

OS のインストール
=======================

**必要な部品**

* Raspberry Pi
* パーソナルコンピュータ
* Micro SD カード 

**インストール手順**

#. `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_ のダウンロードページにアクセスし、使用しているオペレーティングシステムに対応した Imager バージョンを選択します。ファイルをダウンロードして開き、インストールを開始します。

    .. image:: img/os_install_imager.png

#. OS によっては、インストール中にセキュリティ警告が表示される場合があります。例えば Windows では警告メッセージが表示されることがあります。その場合は **詳細情報** を選択し、**実行** をクリックします。画面の指示に従って Raspberry Pi Imager のインストールを完了させます。

    .. image:: img/os_info.png

#. SD カードをコンピュータまたはノートパソコンの SD カードスロットに挿入します。

#. Raspberry Pi Imager アプリケーションを起動します。アイコンをクリックするか、ターミナルで ``rpi-imager`` と入力します。

    .. image:: img/os_open_imager.png

#. **CHOOSE DEVICE** をクリックし、リストから使用する Raspberry Pi モデルを選択します。

    .. image:: img/os_choose_device.png

#. 次に **Choose OS** をクリックして、インストールするオペレーティングシステムを選択します。

    .. image:: img/os_choose_os.png

#. **Choose Storage** をクリックし、インストール先のストレージデバイスを選択します。

    .. note::

        正しいストレージデバイスを選択してください。複数のストレージデバイスが接続されている場合は、混乱を避けるため不要なデバイスを取り外してください。

    .. image:: img/os_choose_sd.png

#. **NEXT** をクリックし、**EDIT SETTINGS** をクリックして OS 設定をカスタマイズします。もし Raspberry Pi 用のモニターを使用する場合は、このステップをスキップして「Yes」をクリックし、インストールを開始できます。その他の設定は後でモニター上で行えます。

    .. image:: img/os_enter_setting.png

#. Raspberry Pi の **ホスト名** を設定します。

    .. note::

        ホスト名は Raspberry Pi のネットワーク識別子です。``<hostname>.local`` または ``<hostname>.lan`` を使って Pi にアクセスできます。

    .. image:: img/os_set_hostname.png

#. Raspberry Pi の管理者アカウント用 **ユーザー名** と **パスワード** を作成します。

    .. note::

        Raspberry Pi にはデフォルトパスワードがないため、独自のユーザー名とパスワードを設定することはセキュリティ上重要です。

    .. image:: img/os_set_username.png

#. ワイヤレス LAN を構成するため、ネットワークの **SSID** と **パスワード** を入力します。

    .. note::

        ``Wireless LAN country`` は、お住まいの地域に対応する `ISO/IEC alpha2 コード <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ （2文字コード）に設定してください。

    .. image:: img/os_set_wifi.png

#. **SERVICES** をクリックし、**SSH** を有効にしてパスワード認証による安全なリモートアクセスを許可します。設定を保存することを忘れないでください。

    .. image:: img/os_enable_ssh.png

#. 設定を確認し、**Yes** をクリックします。

    .. image:: img/os_click_yes.png

#. SD カードに既存のデータがある場合はバックアップを取り、データ損失を防いでください。バックアップが不要であれば **Yes** をクリックして進めます。

    .. image:: img/os_continue.png

#. OS のインストールプロセスが SD カードに開始されます。完了すると確認ダイアログが表示されます。

    .. image:: img/os_finish.png
        :align: center
