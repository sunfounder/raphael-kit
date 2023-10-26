.. _l293d:

L293D 
=================

L293D ist ein integrierter 4-Kanal-Motor-Treiberchip mit hoher Spannung und hohem Strom. 
Er wurde entwickelt, um sich mit Standard-DTL und TTL-Logikpegeln zu verbinden und induktive Lasten zu steuern (wie Relaisspulen, Gleichstrommotoren, Schrittmotoren) sowie Leistungsschalttransistoren usw. 
Gleichstrommotoren sind Geräte, die Gleichstrom-Elektrizität in mechanische Energie umwandeln. Wegen ihrer überlegenen Drehzahlregelungsleistung sind sie im elektrischen Antrieb weit verbreitet.

Sehen Sie sich unten die Abbildung der Pins an. L293D hat zwei Pins (Vcc1 und Vcc2) für die Stromversorgung. 
Vcc2 dient zur Stromversorgung des Motors, während Vcc1 den Chip versorgt. Da hier ein kleiner Gleichstrommotor verwendet wird, verbinden Sie beide Pins mit +5V.

.. image:: img/l293d111.png

Das Folgende zeigt den internen Aufbau des L293D.
Der Pin EN ist ein Aktivierungspin und funktioniert nur bei hohem Pegel; A steht für Eingang und Y für Ausgang. 
Das Verhältnis zwischen ihnen ist unten rechts zu sehen. 
Wenn der Pin EN auf hohem Pegel ist und A ebenfalls hoch ist, gibt Y einen hohen Pegel aus; ist A niedrig, gibt Y einen niedrigen Pegel aus. Wenn der Pin EN auf niedrigem Pegel ist, arbeitet der L293D nicht.

.. image:: img/l293d334.png

* `L293D Datenblatt <https://www.ti.com/lit/ds/symlink/l293d.pdf?ts=1627004062301&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FL293D>`_

**Beispiel**

* :ref:`1.3.1_c` (C-Projekt)
* :ref:`3.1.4_c` (C-Projekt)
* :ref:`1.3.1_py` (Python-Projekt)
* :ref:`4.1.10_py` (Python-Projekt)
* :ref:`1.17_scratch` (Scratch-Projekt)
