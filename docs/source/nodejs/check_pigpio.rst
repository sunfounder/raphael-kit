Prüfung von pigpio
===================

pigpio ist ein Modul zur Steuerung der GPIO-Kanäle des Raspberry Pi. Dieses Paket bietet einige Methoden zur Steuerung von GPIO am Raspberry Pi. Für Beispiele und Dokumentation besuchen Sie bitte: https://www.npmjs.com/package/pigpio.

Geben Sie den folgenden Befehl ein, um die pigpio-Bibliothek zu installieren.

.. raw:: html

    <run></run>

.. code-block::

    npm install pigpio

Um zu überprüfen, ob die Bibliothek erfolgreich installiert wurde, wechseln Sie das Verzeichnis und starten Sie nodejs:

.. raw:: html

    <run></run>

.. code-block::

    cd ~/raphael-kit/nodejs
    nodejs

.. image:: img/pigpio1.png

Geben Sie dann require('pigpio') ein:

.. raw:: html

    <run></run>

.. code-block::

    require('pigpio')

.. image:: img/pigpio2.png   

Wenn der oben gezeigte Bildschirm erscheint, war die Installation der Bibliothek erfolgreich.

Wenn Sie die node CLI verlassen möchten, drücken Sie bitte zweimal Ctrl+C.

.. image:: img/pigpio3.png
