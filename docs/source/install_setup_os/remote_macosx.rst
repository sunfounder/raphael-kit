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

Mac OS X 利用者向け
==========================

Mac OS X 利用者にとって、SSH (Secure Shell) は Raspberry Pi にリモートで安全かつ便利にアクセスして操作する方法を提供します。  
これは特に、Raspberry Pi をリモートで作業する場合やモニターを接続していない場合に便利です。  
Mac のターミナルアプリケーションを使用することで、安全な接続を確立できます。  
接続手順は、Raspberry Pi のユーザー名とホスト名を組み合わせた SSH コマンドを使用します。初回接続時には Raspberry Pi の認証を確認するセキュリティプロンプトが表示されます。

#. SSH 接続を開始するには、 ``ssh <ユーザー名>@<ホスト名>.local`` または ``ssh <ユーザー名>@<IP アドレス>`` と入力します。例:

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac_vnc14.png

#. 初回ログイン時にはセキュリティメッセージが表示されます。**yes** と入力して続行します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Raspberry Pi のパスワードを入力します。入力したパスワードは画面に表示されませんが、これは標準的なセキュリティ機能です。

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 
