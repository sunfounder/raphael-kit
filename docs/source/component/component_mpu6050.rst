.. _cpn_mpu6050:

MPU6050 Modul
===================

.. image:: img/mpu6050_pic.png
    :width: 200
    :align: center

Das MPU-6050 ist ein 6-Achsen-Bewegungssensor (kombiniert 3-Achsen-Gyroskop, 3-Achsen-Beschleunigungsmesser).

Seine drei Koordinatensysteme sind wie folgt definiert:

Legen Sie das MPU6050 flach auf den Tisch, so dass die Seite mit dem Etikett nach oben zeigt und ein Punkt auf dieser Oberfläche in der oberen linken Ecke liegt. Dann ist die aufrechte Richtung nach oben die z-Achse des Chips. Die Richtung von links nach rechts gilt als X-Achse. Entsprechend wird die Richtung von hinten nach vorne als Y-Achse definiert.

.. image:: img/mpu223.png

**3-Achsen-Beschleunigungsmesser**

Der Beschleunigungsmesser funktioniert nach dem Prinzip des piezoelektrischen Effekts, der Fähigkeit bestimmter Materialien, eine elektrische Ladung als Reaktion auf mechanischen Stress zu erzeugen.

Stellen Sie sich eine quaderförmige Box mit einem kleinen Ball darin vor, wie auf dem Bild oben. Die Wände dieser Box bestehen aus piezoelektrischen Kristallen. Wenn Sie die Box kippen, wird der Ball durch die Schwerkraft gezwungen, sich in Richtung der Neigung zu bewegen. Die Wand, gegen die der Ball stößt, erzeugt winzige piezoelektrische Ströme. Es gibt insgesamt drei Paare von gegenüberliegenden Wänden in einem Quader. Jedes Paar entspricht einer Achse im 3D-Raum: X, Y und Z Achsen. Je nach dem von den piezoelektrischen Wänden erzeugten Strom können wir die Richtung der Neigung und ihre Größe bestimmen.

.. image:: img/mpu224.png

Mit dem MPU6050 können wir seine Beschleunigung auf jeder Koordinatenachse erfassen (im stationären Desktop-Zustand beträgt die Z-Achsen-Beschleunigung 1 Gravitationseinheit, und die X- und Y-Achsen sind 0). Wenn es geneigt ist oder sich in einem zustandslosen/überlasteten Zustand befindet, wird der entsprechende Wert geändert.

Es gibt vier programmierbar wählbare Messbereiche: +/-2g, +/-4g, +/-8g und +/-16g (standardmäßig 2g), die jeder Präzision entsprechen. Werte reichen von -32768 bis 32767.

Die Messung des Beschleunigungsmessers wird durch Zuordnung der Messung vom Messbereich zum Messbereich in einen Beschleunigungswert umgewandelt.

Beschleunigung = (Rohdaten der Beschleunigungsmesserachse / 65536 * voller Beschleunigungsbereich) g

Nehmen Sie die X-Achse als Beispiel: Wenn die Rohdaten der Beschleunigungsmesser-X-Achse 16384 betragen und der Bereich auf +/-2g eingestellt ist:

**Beschleunigung entlang der X-Achse = (16384 / 65536 * 4) g = 1g**

**3-Achsen-Gyroskop**

Gyroskope funktionieren nach dem Prinzip der Coriolis-Beschleunigung. Stellen Sie sich vor, es gibt eine gabelartige Struktur, die sich ständig hin und her bewegt. Es wird mit piezoelektrischen Kristallen an Ort und Stelle gehalten. Wenn Sie versuchen, diese Anordnung zu kippen, erfahren die Kristalle eine Kraft in Richtung der Neigung. Dies geschieht aufgrund der Trägheit der sich bewegenden Gabel. Die Kristalle erzeugen so einen Strom im Einklang mit dem piezoelektrischen Effekt, und dieser Strom wird verstärkt.

.. image:: img/mpu225.png

Das Gyroskop hat auch vier Arten von Messbereichen: +/- 250, +/- 500, +/- 1000, +/- 2000. Die Berechnungsmethode und Beschleunigung sind im Grunde konsistent.

Die Formel zur Umwandlung der Messung in die Winkelgeschwindigkeit lautet:

Winkelgeschwindigkeit = (Rohdaten der Gyroskopachse / 65536 * voller Gyroskopbereich) °/s

Nehmen Sie als Beispiel die X-Achse, wenn die Rohdaten der Beschleunigungsmesser-X-Achse 16384 betragen und der Bereich +/- 250°/ s beträgt:

**Winkelgeschwindigkeit entlang der X-Achse = (16384 / 65536 * 500)°/s = 125°/s**

**Beispiel**

* :ref:`2.2.9_c` (C-Projekt)
* :ref:`2.2.9_py` (Python-Projekt)
