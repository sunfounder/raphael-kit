Pour les utilisateurs de Linux/Unix
============================================

#. Localisez et ouvrez le **Terminal** sur votre système Linux/Unix.

#. Assurez-vous que votre Raspberry Pi est connecté au même réseau. Vérifiez ceci en tapant `ping <hostname>.local`. Par exemple :

    .. code-block::

        ping raspberrypi.local

    Vous devriez voir l'adresse IP du Raspberry Pi s'il est connecté au réseau.

    * Si le terminal affiche un message du type ``Ping request could not find host pi.local. Please check the name and try again.``, vérifiez le nom d'hôte que vous avez entré.
    * Si vous ne parvenez pas à récupérer l'adresse IP, inspectez les paramètres de votre réseau ou WiFi sur le Raspberry Pi.

#. Initiez une connexion SSH en tapant ``ssh <username>@<hostname>.local`` ou ``ssh <username>@<IP address>``. Par exemple :

    .. code-block::

        ssh pi@raspberrypi.local

#. Lors de votre première connexion, vous recevrez un message de sécurité. Tapez ``yes`` pour continuer.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Entrez le mot de passe que vous avez défini précédemment. Notez que pour des raisons de sécurité, le mot de passe ne sera pas visible pendant que vous tapez.

    .. note::
        Il est normal que les caractères du mot de passe ne s'affichent pas dans le terminal. Assurez-vous simplement de taper le mot de passe correct.

#. Une fois que vous vous êtes connecté avec succès, votre Raspberry Pi est maintenant connecté et vous êtes prêt à passer à l'étape suivante.

