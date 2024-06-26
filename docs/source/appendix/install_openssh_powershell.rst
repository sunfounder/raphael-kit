.. _openssh_powershell:

Installer OpenSSH via Powershell
====================================

Lorsque vous utilisez ``ssh <username>@<hostname>.local`` (ou ``ssh <username>@<IP address>``) pour vous connecter à votre Raspberry Pi, mais que le message d'erreur suivant apparaît.

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.


Cela signifie que votre système informatique est trop ancien et ne dispose pas de `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ préinstallé. Vous devez suivre le tutoriel ci-dessous pour l'installer manuellement.

#. Tapez ``powershell`` dans la barre de recherche de votre bureau Windows, faites un clic droit sur ``Windows PowerShell``, et sélectionnez ``Exécuter en tant qu'administrateur`` dans le menu qui apparaît.

    .. image:: img/powershell_ssh.png
        :align: center

#. Utilisez la commande suivante pour installer ``OpenSSH.Client``.

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Après l'installation, la sortie suivante sera affichée.

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Vérifiez l'installation en utilisant la commande suivante.

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Il vous indiquera maintenant que ``OpenSSH.Client`` a été installé avec succès.

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Si l'invite ci-dessus n'apparaît pas, cela signifie que votre système Windows est encore trop ancien et il est conseillé d'installer un outil SSH tiers, comme :ref:`login_windows`.

#. Redémarrez maintenant PowerShell et continuez à l'exécuter en tant qu'administrateur. À ce stade, vous pourrez vous connecter à votre Raspberry Pi en utilisant la commande ``ssh``, où il vous sera demandé d'entrer le mot de passe que vous avez configuré précédemment.

    .. image:: img/powershell_login.png
