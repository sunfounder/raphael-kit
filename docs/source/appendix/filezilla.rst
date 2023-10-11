Filezilla Software
==========================

.. image:: img/filezilla_icon.png

ファイル転送プロトコル（FTP）は、コンピュータネットワーク上でサーバーからクライアントへコンピュータファイルを転送するための標準的な通信プロトコルです。

Filezillaはオープンソースソフトウェアで、FTPだけでなくFTP over TLS（FTPS）とSFTPにも対応しています。Raspberry Piへのローカルファイル（例えば画像やオーディオなど）のアップロード、あるいはRaspberry PiからのファイルのダウンロードにFilezillaを使用できます。

**ステップ1**： Filezillaをダウンロード。

`Filezillaの公式ウェブサイト <https://filezilla-project.org/>`_ からクライアントをダウンロードしてください。詳しい使い方は、 `Documentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_ を参照してください。

**ステップ2**： Raspberry Piに接続

簡単なインストールの後、`FTPサーバーに接続する <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_ 方法が3種類ありますが、ここでは **クイックコネクト** バーを使用します。 **ホスト名/IP** 、 **ユーザー名** 、 **パスワード** 、 **ポート（22）** を入力し、 **クイックコネクト** をクリックするか、 **Enter** キーを押してサーバーに接続します。

.. image:: img/filezilla_connect.png

.. note::

    クイックコネクトは、ログイン情報をテストするのに便利です。永続的なエントリーを作成したい場合は、成功したクイックコネクトの後に **File** -> **現在の接続をサイトマネージャーにコピー** を選択し、名前を入力して **OK** をクリックします。次回からは、 **File** -> **Site Manager** 内の保存されたサイトを選択して接続できます。

    .. image:: img/ftp_site.png

**ステップ3**： ファイルのアップロード/ダウンロード。

Raspberry Piにローカルファイルをドラッグ&ドロップでアップロードすることも、Raspberry Pi内のファイルをローカルにダウンロードすることもできます。

.. image:: img/upload_ftp.png