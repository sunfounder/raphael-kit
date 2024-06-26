Pour les utilisateurs de Windows
====================================

Pour les utilisateurs de Windows 10 ou supérieur, la connexion à distance à un Raspberry Pi peut être réalisée via les étapes suivantes :

#. Recherchez ``powershell`` dans la barre de recherche Windows. Faites un clic droit sur ``Windows PowerShell`` et sélectionnez ``Exécuter en tant qu'administrateur``.

    .. image:: img/powershell_ssh.png
        :align: center

#. Déterminez l'adresse IP de votre Raspberry Pi en tapant ``ping -4 <hostname>.local`` dans PowerShell.

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    L'adresse IP du Raspberry Pi sera affichée une fois connecté au réseau.

    * Si le terminal affiche ``Ping request could not find host pi.local. Please check the name and try again.``, vérifiez que le nom d'hôte saisi est correct.
    * Si l'adresse IP reste introuvable, vérifiez les paramètres réseau ou WiFi sur le Raspberry Pi.

#. Une fois l'adresse IP confirmée, connectez-vous à votre Raspberry Pi en utilisant ``ssh <username>@<hostname>.local`` ou ``ssh <username>@<IP address>``.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Si une erreur apparaît indiquant ``The term 'ssh' is not recognized as the name of a cmdlet...``, votre système peut ne pas avoir les outils SSH préinstallés. Dans ce cas, vous devez installer manuellement OpenSSH en suivant :ref:`openssh_powershell`, ou utiliser un outil tiers comme décrit dans :ref:`login_windows`.

#. Un message de sécurité apparaîtra lors de votre première connexion. Tapez ``yes`` pour continuer.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Entrez le mot de passe que vous avez précédemment défini. Notez que les caractères du mot de passe ne s'afficheront pas à l'écran, ce qui est une fonctionnalité de sécurité standard.

    .. note::
        L'absence de caractères visibles lors de la saisie du mot de passe est normale. Assurez-vous de saisir le mot de passe correct.

#. Une fois connecté, votre Raspberry Pi est prêt pour les opérations à distance.

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center
