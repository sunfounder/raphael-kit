.. _set_up_your_raspberry_pi:

Raspberry Pi einrichten
=======================

Wenn Sie einen Bildschirm haben
-------------------------------

Wenn Sie einen Bildschirm besitzen, wird es Ihnen leicht fallen, mit dem Raspberry Pi zu arbeiten.

**Benötigte Komponenten**

* Ein Raspberry Pi   
* 1 * Netzadapter
* 1 * Micro SD-Karte
* 1 * Bildschirmnetzadapter
* 1 * HDMI-Kabel
* 1 * Bildschirm
* 1 * Maus
* 1 * Tastatur

#. Stecken Sie die mit dem Raspberry Pi OS vorbereitete SD-Karte in den Micro SD-Kartensteckplatz auf der Unterseite Ihres Raspberry Pi.

#. Schließen Sie Maus und Tastatur an.

#. Verbinden Sie den Bildschirm über den HDMI-Anschluss mit dem Raspberry Pi und stellen Sie sicher, dass Ihr Bildschirm an eine Steckdose angeschlossen und eingeschaltet ist.

    .. note::

        Wenn Sie einen Raspberry Pi 4 verwenden, müssen Sie den Bildschirm an den HDMI0 anschließen (am nächsten zum Stromanschluss).

#. Verwenden Sie den Netzadapter, um den Raspberry Pi mit Strom zu versorgen. Nach einigen Sekunden wird der Raspberry Pi OS-Desktop angezeigt.

    .. image:: img/login1.png
        :align: center

.. _no_screen:

Wenn Sie keinen Bildschirm haben
-----------------------------------

Wenn Sie keinen Monitor besitzen, können Sie sich aus der Ferne in Ihren Raspberry Pi einloggen.

Sie können den SSH-Befehl verwenden, um die Bash-Shell des Raspberry Pi zu öffnen. Bash ist die standardmäßige Shell für Linux. Die Shell selbst ist ein Befehl (Anweisung), wenn der Benutzer Unix/Linux verwendet. Das Meiste, was Sie tun müssen, kann über die Shell erledigt werden.

Wenn Sie nicht nur über das Befehlsfenster auf Ihren Raspberry Pi zugreifen möchten, können Sie auch die Remote-Desktop-Funktion verwenden, um Dateien auf Ihrem Raspberry Pi über eine grafische Benutzeroberfläche zu verwalten.

Unten finden Sie detaillierte Anleitungen für jedes System.


.. toctree::

    remote_macosx
    remote_windows
    remote_linux

