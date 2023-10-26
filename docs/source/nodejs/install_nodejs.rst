Was ist Nodejs?
---------------------------

Node.js wurde im Mai 2009 von Ryan Dahl veröffentlicht. Es handelt sich um eine JavaScript-Laufzeitumgebung, die auf der Chrome V8 Engine basiert. Sie verwendet ein ereignisgesteuertes, nicht-blockierendes I/O-Modell, um JavaScript auf der serverseitigen Entwicklungsplattform auszuführen.

Einfach ausgedrückt, ist Node.js JavaScript, das auf dem Server läuft. Wenn Sie mit Javascript vertraut sind, werden Sie Node.js leicht erlernen.

Nodejs verwendet normalerweise den Befehl ``npm install xxx``, um Drittanbieter-Pakete zu installieren. Dafür müssen wir das npm-Tool installieren, ähnlich dem pip-Tool in Python.

Nodejs und npm installieren oder aktualisieren
-------------------------------------------------

Führen Sie die folgenden Befehle aus, um nodejs und npm zu installieren und zu aktualisieren.

.. raw:: html

    <run></run>

.. code-block::

    sudo apt-get update
    sudo apt-get install nodejs
    sudo apt-get install npm 
    sudo npm install npm -g

Überprüfen Sie anschließend die aktuelle Node-Version mit dem folgenden Befehl.

.. raw:: html

    <run></run>

.. code-block::

    node -v

Mit dem folgenden Befehl überprüfen Sie die aktuelle npm-Version.

.. raw:: html

    <run></run>

.. code-block::

    npm -v
