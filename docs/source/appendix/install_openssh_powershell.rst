.. _openssh_powershell:


Powershell で OpenSSH を導入する
-----------------------------------

``ssh <ユーザー名>@<ホスト名>.local``（または ``ssh <ユーザー名>@<IP アドレス>``）を使って Raspberry Pi に接続するとき、次のようなエラーメッセージが表示される場合があります。

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


これは、お使いのコンピュータのシステムが古く、`OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ が事前に導入されていないことを意味します。以下の手順に従って手動で導入してください。

#. Windows デスクトップの検索ボックスに ``powershell`` と入力し、``Windows PowerShell`` を右クリックし、表示されたメニューから ``管理者として実行`` を選びます。

    .. image:: img/powershell_ssh.png
        :align: center

#. 次のコマンドを使って ``OpenSSH.Client`` を導入します。

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. 導入後、次のような出力が返されます。

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 次のコマンドで導入を確認します。

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. ``OpenSSH.Client`` が正しく導入されたことを示すメッセージが表示されます。

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning::
        上記の表示が出ない場合は、Windows システムが依然として古いため、:ref:`login_windows` などの第三者 SSH ツールを導入することをお勧めします。

#. PowerShell を再起動し、再び管理者として実行します。これで ``ssh`` コマンドを使って Raspberry Pi に接続できるようになります。このとき、以前設定したパスワードの入力を求められます。

    .. image:: img/powershell_login.png
