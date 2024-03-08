.. _cpn_ultrasonic_sensor:

Ultraschallmodul
================================

.. image:: img/ultrasonic_pic.png
    :width: 400
    :align: center

Das Ultraschall-Entfernungsmessmodul bietet eine berührungslose Messfunktion von 2 cm bis 400 cm, und die Messgenauigkeit kann bis zu 3 mm betragen.
Es gewährleistet, dass das Signal innerhalb von 5 m stabil bleibt und das Signal nach 5 m allmählich abgeschwächt wird, bis es an der 7 m Position verschwindet.

Das Modul enthält Ultraschallsender, Empfänger und Steuerschaltung. Die Grundprinzipien sind wie folgt:

#. Ein IO-Flip-Flop verarbeitet ein mindestens 10 µs langes High-Level-Signal.

#. Das Modul sendet automatisch acht 40 kHz und prüft, ob ein Pulssignal zurückkehrt.

#. Wenn das Signal zurückkommt, im High-Level-Bereich, ist die High-Output-IO-Dauer die Zeit vom Senden der Ultraschallwelle bis zu ihrer Rückkehr. Hier ergibt sich die Testentfernung = (High-Zeit x Schallgeschwindigkeit (340 m/s) / 2.

Das Timing-Diagramm ist unten dargestellt.

.. image:: img/ultrasonic228.png

Es ist nur notwendig, einen kurzen 10µs-Impuls für den Trigger-Eingang zu liefern, um die Entfernungsmessung zu starten. Danach wird das Modul 
einen 8-Zyklus-Ultraschallimpuls mit 40 kHz senden und sein
Echo erhöhen. Die Entfernung kann durch das Zeitintervall zwischen
dem Senden des Trigger-Signals und dem Empfang des Echo-Signals berechnet werden.

Formel: µs / 58 = Zentimeter oder µs / 148 = Zoll; oder: die Entfernung = High-Level-Zeit * Geschwindigkeit (340M/S) / 2; es wird empfohlen, 
den Messzyklus über 60ms zu verwenden, um Signalüberlagerungen von
Trigger-Signal und dem Echo-Signal zu verhindern.

**Beispiel**

* :ref:`2.2.8_c` (C-Projekt)
* :ref:`3.1.3_c` (C-Projekt)
* :ref:`2.2.8_py` (Python-Projekt)
* :ref:`4.1.9_py` (Python-Projekt)
