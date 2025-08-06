.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

Linux/Unix 利用者向け
==========================

#. Linux/Unix システムで **ターミナル** を探して開きます。

#. Raspberry Pi が同じネットワークに接続されていることを確認します。以下を入力して確認します: ``ping <hostname>.local``。例:

    .. code-block::

        ping raspberrypi.local

    ネットワークに接続されていれば、Raspberry Pi の IP アドレスが表示されます。

    * もしターミナルに ``Ping request could not find host pi.local. Please check the name and try again.`` のようなメッセージが表示された場合は、入力したホスト名を再確認してください。
    * IP アドレスが取得できない場合は、Raspberry Pi 側のネットワークまたは WiFi 設定を確認してください。

#. SSH 接続を開始するには ``ssh <ユーザー名>@<ホスト名>.local`` または ``ssh <ユーザー名>@<IPアドレス>`` を入力します。例:

    .. code-block::

        ssh pi@raspberrypi.local

#. 初回ログイン時にはセキュリティメッセージが表示されます。``yes`` と入力して続行します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 以前設定したパスワードを入力します。セキュリティ上の理由から、入力中はパスワードが表示されません。

    .. note::
        ターミナルにパスワードが表示されないのは正常な動作です。正しいパスワードを入力してください。

#. ログインに成功すると、Raspberry Pi に接続された状態となり、次のステップに進む準備が整います。
