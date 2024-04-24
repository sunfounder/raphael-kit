.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _hello_mouse:

Hallo Maus
==================

In diesem Projekt wird Ihre Maus ständig Linien zu einem Punkt schießen; bewegen Sie die Maus, und Sie werden eine einzigartige Linie aus Sternen zeichnen. Drücken Sie die Maus, um die Zeichnung neu zu starten.

.. image:: img/hello_mouse1.png

**Skizze**

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

    void mousePressed() {
        pointX=mouseX;
        pointY=mouseY;
        background(192, 16, 18);
    }

**Wie funktioniert das?**

Das vorherige Projekt hat ein einzelnes Bild gezeichnet, ohne Animation oder Interaktion.

Wenn wir eine interaktive Skizze erstellen wollen, müssen wir die ``setup()`` und ``draw()`` Funktionen hinzufügen (dies sind eingebaute Funktionen, die automatisch aufgerufen werden), um den Rahmen zu erstellen.

* ``setup()``: Wird nur einmal zu Beginn der Skizze ausgeführt.
* ``draw()``: Wird wiederholt ausgeführt, hier fügen wir normalerweise die Skizze zum Zeichnen der Animation hinzu.

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

Die obige Skizze funktioniert bereits reibungslos als interaktive Skizze.

Als nächstes können Sie ein Mausklick-Ereignis hinzufügen. Dieses Ereignis kann mit der ``mousePressed()`` Funktion implementiert werden, in der wir Anweisungen zum Aktualisieren des Zielpunkts und zum Löschen des Bildschirms hinzufügen.

.. code-block:: arduino

    int pointX = 172;
    int pointY = 88;

    void setup() {
        size(400, 400);
        stroke(255);
        background(192, 16, 18);
    }

    void draw() {
        line(pointX, pointY, mouseX, mouseY);
    }

    void mousePressed() {
        pointX=mouseX;
        pointY=mouseY;
        background(192, 16, 18);
    }

Für mehr Informationen verweisen Sie bitte auf `Processing Referenz <https://processing.org/reference/>`_.

