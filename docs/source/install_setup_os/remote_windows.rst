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

Windows 利用者向け
=======================

Windows 10 以上を利用している場合、次の手順で Raspberry Pi へのリモートログインが可能です。

#. Windows の検索ボックスで ``powershell`` を検索します。``Windows PowerShell`` を右クリックし、``管理者として実行`` を選択します。

    .. image:: img/powershell_ssh.png
        :align: center

#. PowerShell で ``ping -4 <ホスト名>.local`` と入力し、Raspberry Pi の IP アドレスを確認します。

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    Raspberry Pi がネットワークに接続されていれば、その IP アドレスが表示されます。

    * ターミナルに ``Ping request could not find host pi.local. Please check the name and try again.`` と表示された場合は、入力したホスト名が正しいか確認してください。
    * IP アドレスが取得できない場合は、Raspberry Pi 側のネットワークまたは WiFi 設定を確認してください。

#. IP アドレスを確認したら、``ssh <ユーザー名>@<ホスト名>.local`` または ``ssh <ユーザー名>@<IP アドレス>`` を使って Raspberry Pi にログインします。

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        ``The term 'ssh' is not recognized as the name of a cmdlet...`` というエラーが表示された場合は、システムに SSH ツールがインストールされていない可能性があります。  
        この場合は、:ref:`openssh_powershell` に従って OpenSSH を手動でインストールするか、:ref:`login_windows` に記載されているサードパーティーツールを使用してください。

#. 初回ログイン時にはセキュリティメッセージが表示されます。``yes`` と入力して続行します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 以前設定したパスワードを入力します。パスワード入力中は画面に文字が表示されませんが、これは標準的なセキュリティ仕様です。

    .. note::
        パスワード入力時に文字が表示されないのは正常な動作です。正しいパスワードを入力してください。

#. 接続に成功すると、Raspberry Pi がリモート操作可能になります。

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center
