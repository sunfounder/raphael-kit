.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _remote_desktop:

Remote-Desktop-Zugriff auf den Raspberry Pi
==================================================

Für alle, die eine grafische Benutzeroberfläche (GUI) der Befehlszeile vorziehen, unterstützt der Raspberry Pi Remote-Desktop-Funktionalität. Diese Anleitung zeigt dir, wie du VNC (Virtual Network Computing) für den Fernzugriff einrichtest und verwendest.

Wir empfehlen, dafür den `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ zu verwenden.

**VNC-Dienst auf dem Raspberry Pi aktivieren**

Der VNC-Dienst ist im Raspberry Pi OS vorinstalliert, aber standardmäßig deaktiviert. Befolge diese Schritte, um ihn zu aktivieren:

#. Gib den folgenden Befehl im Raspberry-Pi-Terminal ein:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Navigiere mit der Pfeiltaste nach unten zu **Interfacing Options** und drücke **Enter**.

    .. image:: img/config_interface.png
        :align: center

#. Wähle **VNC** aus den Optionen.

    .. image:: img/vnc.png
        :align: center

#. Verwende die Pfeiltasten, um **<Yes>** -> **<OK>** -> **<Finish>** auszuwählen und die Aktivierung des VNC-Dienstes abzuschließen.

    .. image:: img/vnc_yes.png
        :align: center

**Anmeldung über VNC Viewer**

#. Lade den `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ auf deinen PC herunter und installiere ihn.

#. Starte nach der Installation den VNC Viewer. Gib den Hostnamen oder die IP-Adresse deines Raspberry Pi ein und drücke **Enter**.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Wenn du dazu aufgefordert wirst, gib den Benutzernamen und das Passwort deines Raspberry Pi ein und klicke auf **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Nun hast du Zugriff auf die Desktop-Oberfläche deines Raspberry Pi.

    .. image:: img/bullseye_desktop.png
        :align: center

