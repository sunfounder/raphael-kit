.. _openssh_powershell:

OpenSSH über Powershell installieren
---------------------------------------

Wenn Sie ``ssh <username>@<hostname>.local`` (oder ``ssh <username>@<IP address>``) verwenden, um sich mit Ihrem Raspberry Pi zu verbinden, aber die folgende Fehlermeldung erscheint:

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

bedeutet dies, dass Ihr Computersystem zu alt ist und `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ nicht vorinstalliert ist. Sie müssen es manuell gemäß der folgenden Anleitung installieren.

#. Geben Sie ``powershell`` in das Suchfeld Ihres Windows-Desktops ein, klicken Sie mit der rechten Maustaste auf ``Windows PowerShell`` und wählen Sie im erscheinenden Menü ``Als Administrator ausführen``.

    .. image:: img/powershell_ssh.png
        :align: center

#. Verwenden Sie den folgenden Befehl, um ``OpenSSH.Client`` zu installieren.

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Nach der Installation wird die folgende Ausgabe zurückgegeben.

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Überprüfen Sie die Installation mit dem folgenden Befehl.

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Nun wird angezeigt, dass ``OpenSSH.Client`` erfolgreich installiert wurde.

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning::
        Wenn die obige Meldung nicht erscheint, bedeutet dies, dass Ihr Windows-System immer noch zu alt ist. Es wird empfohlen, ein SSH-Tool eines Drittanbieters zu installieren, wie in :ref:`login_windows` beschrieben.

#. Starten Sie nun PowerShell neu und führen Sie es erneut als Administrator aus. An diesem Punkt können Sie sich mit dem ``ssh``-Befehl bei Ihrem Raspberry Pi anmelden, wobei Sie nach dem zuvor eingerichteten Passwort gefragt werden.

    .. image:: img/powershell_login.png
