.. _draw_a_matchmaker:

Einen Streichholzmann zeichnen
====================================

Sie befinden sich jetzt in der Processing Development Environment (oder PDE).
Es gibt nicht viel dazu; der große Bereich ist der Texteditor und oben gibt es eine Reihe von Schaltflächen; das ist die Werkzeugleiste.
Unterhalb des Editors befindet sich der Nachrichtenbereich und darunter die Konsole.
Der Nachrichtenbereich wird für Einzeilennachrichten verwendet und die Konsole für detailliertere technische Informationen.

Lassen Sie uns mit der Verwendung von Processing vertraut werden und einen Streichholzmann zeichnen.

**Skizze**

Kopieren Sie die untenstehende Skizze in Processing und führen Sie sie aus. Ein neues Anzeigefenster wird geöffnet und ein fröhlicher Streichholzmann wird gezeichnet.

.. code-block:: arduino

    size(200,200);
    background(92, 168, 0); 
    rectMode(CENTER);
    rect(100,120,20,60);
    ellipse(100,80,45,45);
    line(90,150,80,170);
    line(110,150,120,170);
    line(90,110,70,100);
    line(110,110,130,100);

.. image:: img/draw_one1.png

.. note:: 

    Wenn Sie es ausführen und der Nachrichtenbereich rot wird und einige Fehler anzeigt, dann stimmt etwas mit der Skizze nicht. Stellen Sie sicher, dass Sie die Beispiel-Skizze genau kopieren: Zahlen sollten in Klammern stehen, mit Kommas zwischen jeder Zahl, und Zeilen sollten mit Semikolons enden.

**Wie funktioniert das?**

Der Schlüssel hier ist zu erkennen, dass das Anzeigefenster wie ein Quadrat aus Papier behandelt werden kann.

Jeder Pixel des Anzeigefensters ist ein Koordinatenpunkt (x,y), der die Position eines Punktes im Raum bestimmt. Der Ursprung (0,0) der Koordinaten befindet sich in der oberen linken Ecke, die positive Richtung der X-Achse geht horizontal nach rechts und die positive Richtung der Y-Achse geht vertikal nach unten.

Unsere Aufgabe ist es zu bestimmen, welche Form und Farbe an diesen Pixel-Koordinaten erscheinen sollen.

Zum Beispiel ein Rechteck von 20 Breite und 60 Höhe zeichnen, mit den Koordinaten (100,120) als Mittelpunkt.

.. code-block:: arduino

    rectMode(CENTER);
    rect(100,120,20,60);

.. image:: img/draw_one_coodinate.png

Sobald wir die Beziehung zwischen dem Anzeigefenster und den Achsen verstehen, ist diese Skizze für uns nicht schwierig. Wir müssen nur einige einfache Grafikanweisungen verstehen.

    * ``size(width, height)``: Definiert die Abmessungen des Anzeigefensters in Pixeln.
    * ``background(red, green, blue)``: Legt die Hintergrundfarbe des Anzeigefensters fest.
    * ``rectMode(mode)``: Modifiziert die Position, von der aus Rechtecke gezeichnet werden, indem die Art und Weise geändert wird, wie die an ``rect()`` übergebenen Parameter interpretiert werden.
    * ``rect(x, y, width, height)``: Zeichnet ein Rechteck auf den Bildschirm.
    * ``ellipse(x, y, width, height)``: Zeichnet eine Ellipse (Oval) auf den Bildschirm.
    * ``line(x1, y1, x2, y2)``: Zeichnet eine Linie (einen direkten Pfad zwischen zwei Punkten) auf den Bildschirm.

Für mehr Informationen verweisen Sie bitte auf `Processing Referenz <https://processing.org/reference/>`_.
