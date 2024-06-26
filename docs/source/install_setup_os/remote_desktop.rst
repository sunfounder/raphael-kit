.. _remote_desktop:

Accès à Distance au Bureau pour Raspberry Pi
==================================================

Pour ceux qui préfèrent une interface graphique (GUI) à l'accès en ligne de commande, le Raspberry Pi prend en charge la fonctionnalité de bureau à distance. Ce guide vous expliquera comment configurer et utiliser VNC (Virtual Network Computing) pour un accès à distance.

Nous vous recommandons d'utiliser `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ à cet effet.

**Activation du Service VNC sur Raspberry Pi**

Le service VNC est pré-installé dans le système d'exploitation Raspberry Pi OS mais est désactivé par défaut. Suivez ces étapes pour l'activer :

#. Entrez la commande suivante dans le terminal Raspberry Pi :

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Naviguez jusqu'à **Options d'interface** à l'aide de la touche fléchée vers le bas, puis appuyez sur **Entrée**.

    .. image:: img/config_interface.png
        :align: center

#. Sélectionnez **VNC** dans les options.

    .. image:: img/vnc.png
        :align: center

#. Utilisez les touches fléchées pour choisir **<Yes>** -> **<OK>** -> **<Finish>** et finalisez l'activation du service VNC.

    .. image:: img/vnc_yes.png
        :align: center

**Connexion via VNC Viewer**

#. Téléchargez et installez `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ sur votre ordinateur personnel.

#. Une fois installé, lancez VNC Viewer. Entrez le nom d'hôte ou l'adresse IP de votre Raspberry Pi et appuyez sur Entrée.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Lorsque vous y êtes invité, entrez le nom d'utilisateur et le mot de passe de votre Raspberry Pi, puis cliquez sur **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Vous aurez maintenant accès à l'interface de bureau de votre Raspberry Pi.

    .. image:: img/bullseye_desktop.png
        :align: center

