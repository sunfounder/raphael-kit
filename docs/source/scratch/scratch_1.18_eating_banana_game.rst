.. _1.18_scratch:

1.18 Bananen Essen Spiel
~~~~~~~~~~~~~~~~~~~~~~~~

Beschreibung
---------------

Scratch verfügt über ein Video-Sensing-Erweiterungsmodul, mit dem die Kamera in Scratch aktiviert und die Bewegung von Objekten auf dem Kamerabildschirm erkannt werden kann.

Heute werden wir die Kamera verwenden, um ein Bananen-Ess-Spiel zu erstellen. Innerhalb der festgelegten Zeit soll dem Affen geholfen werden, mehr Bananen zu essen.

Um das Spiel vor einem weißen Hintergrund zu spielen, klicken Sie auf die grüne Flagge, um zu starten. Bewegen Sie farbige Objekte vor der Kamera, um den Affen-Sprite zu steuern.

.. image:: img/1.18_header.png

Benötigte Komponenten
------------------------------

Für dieses Projekt benötigen wir folgende Komponenten.

.. image:: img/1.18_photo1.png

Es ist definitiv praktisch, ein ganzes Set zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

Sie können diese auch einzeln über die untenstehenden Links kaufen.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - KOMPONENTEN-VORSTELLUNG
        - KAUF-LINK

    *   - :ref:`camera_module`
        - |link_camera_buy|


Schaltung aufbauen
---------------------

.. image:: img/1.10_camera.png

.. note::

    Sie müssen sich auf :ref:`camera_module` beziehen, um das Kameramodul anzuschließen und die Raspberry Pi Kamera-Schnittstelle zu aktivieren.

Laden Sie den Code und sehen Sie, was passiert
---------------------------------------------------

Laden Sie die Code-Datei (``1.18_eating_banana_game.sb3``) in Scratch 3.

Tipps zu Codes
----------------

Ordnen Sie Affen und Bananen an.

Zuerst löschen wir den ursprünglichen Sprite, dann fügen wir den Affen-Sprite und den Bananen-Sprite hinzu und ändern ihre Größen auf 50.

Lassen Sie die Bananen zufällig erscheinen.

.. image:: img/1.18_code1.png

Die Banane verschwindet, nachdem sie dem Affen begegnet ist, was bedeutet, dass sie vom Affen gegessen wurde und zufällig wieder erscheint.

.. image:: img/1.18_code2.png

Lassen Sie den Affen in der Mitte der Bühne erscheinen und initialisieren Sie die Kameradaten (Transparenz ist auf 20 eingestellt).

.. image:: img/1.18_code3.png

Wenn die Kamera ein bewegendes Objekt erkennt, soll sich der Affe auf das Objekt zubewegen.

.. image:: img/1.18_code4.png

Jetzt klicken Sie auf die grüne Flagge oben im Bühnenbereich, um das Spiel zu starten.

Lassen Sie den Affen Bananen essen, er ist sehr hungrig! Versuchen Sie, dieses Spiel vor einem weißen Hintergrund zu spielen, um Störungen durch andere Objekte zu vermeiden.

Herausforderung
---------------------

Ich bin überzeugt, dass Sie bald schlau genug sein werden, dieses Spiel zu programmieren und umzusetzen. Als Nächstes werden wir einige Herausforderungen hinzufügen, um unseren Spielinhalt zu bereichern.

· Wenn der Affe eine Banane isst, fügen wir 1 zum Punktestand hinzu. Innerhalb von 30s, sehen Sie, wer den höchsten Punktestand hat!

· Wenn der Affe eine Banane isst, gibt er einen passenden Soundeffekt ab.
