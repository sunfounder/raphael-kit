.. _set_up_your_raspberry_pi:

Richten Sie Ihren Raspberry Pi ein
=====================================

Wenn Sie einen Bildschirm haben
------------------------------------

Wenn Sie einen Bildschirm besitzen, wird es für Sie einfacher sein, den Raspberry Pi zu bedienen.

**Benötigte Komponenten**

* Ein beliebiger Raspberry Pi   
* 1 * Stromadapter
* 1 * Micro-SD-Karte
* 1 * Bildschirm-Stromadapter
* 1 * HDMI-Kabel
* 1 * Bildschirm
* 1 * Maus
* 1 * Tastatur

#. Stecken Sie die mit dem Raspberry Pi OS vorbereitete SD-Karte in den Micro-SD-Kartenslot auf der Unterseite Ihres Raspberry Pi.

#. Schließen Sie Maus und Tastatur an.

#. Verbinden Sie den Bildschirm über den HDMI-Port mit dem Raspberry Pi und stellen Sie sicher, dass Ihr Bildschirm in eine Steckdose eingesteckt und eingeschaltet ist.

   .. note::
   
      Bei Verwendung eines Raspberry Pi 4 sollten Sie den Bildschirm mit dem HDMI0-Port (am nächsten zum Stromanschluss) verbinden.

#. Verwenden Sie den Stromadapter, um den Raspberry Pi mit Strom zu versorgen. Nach einigen Sekunden wird der Raspberry Pi OS-Desktop angezeigt.

   .. image:: img/login1.png
       :align: center
   
   .. raw:: html
   
       <br/>

#. Sie können einen Webbrowser auf Ihrem Raspberry Pi-System starten und diese Anleitung aufrufen. So können Sie Anweisungen bequem kopieren und im Terminal ausführen.

   .. image:: img/login2.png
       :align: center
   
.. raw:: html
   
   <br/>

.. _no_screen:

Wenn Sie keinen Bildschirm haben
----------------------------------

Wenn Sie keinen Monitor besitzen, können Sie sich remote in Ihren Raspberry Pi einloggen.

**Benötigte Komponenten**

* Ein beliebiger Raspberry Pi   
* 1 * Stromadapter
* 1 * Micro-SD-Karte

Sie können den SSH-Befehl verwenden, um die Bash-Shell des Raspberry Pi zu öffnen. Bash ist die standardmäßige Standard-Shell für Linux. Die Shell selbst ist ein Befehl (Anweisung), wenn der Benutzer Unix/Linux verwendet. Das meiste, was Sie tun müssen, kann über die Shell erledigt werden.

Wenn Sie mit dem Befehlsfenster für den Zugriff auf Ihren Raspberry Pi nicht zufrieden sind, können Sie auch die Fernzugriffsfunktion verwenden, um Dateien auf Ihrem Raspberry Pi über eine grafische Benutzeroberfläche (GUI) einfach zu verwalten.

Unten finden Sie detaillierte Tutorials für jedes System.



.. toctree::

    remote_macosx
    remote_windows
    remote_linux

