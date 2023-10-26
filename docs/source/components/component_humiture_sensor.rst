.. _humiture_sensor:

Feuchtigkeits- und Temperatursensor Modul
============================================

.. image:: img/dht11_pic.png
    :width: 400
    :align: center

Der digitale Temperatur- und Feuchtigkeitssensor DHT11 ist ein Kombinationssensor, der einen kalibrierten digitalen Signaloutput für Temperatur und Feuchtigkeit liefert. 
Die Technologien spezialisierter digitaler Modulsammlungen sowie die Technologie zur Temperatur- und Feuchtigkeitserfassung gewährleisten eine hohe Zuverlässigkeit und hervorragende Langzeitstabilität des Produkts.

Es stehen nur drei Pins zur Verfügung: VCC, GND und DATA. 
Der Kommunikationsprozess beginnt damit, dass die DATA-Leitung Startsignale an DHT11 sendet. Der DHT11 empfängt diese Signale und gibt ein Antwortsignal zurück. 
Dann empfängt der Host das Antwortsignal und beginnt mit dem Empfang von 40-bit Feuchtigkeits- und Temperaturdaten (8-bit Feuchtigkeits-Ganzzahl + 8-bit Feuchtigkeits-Dezimalzahl + 8-bit Temperatur-Ganzzahl + 8-bit Temperatur-Dezimalzahl + 8-bit Prüfsumme).

.. image:: img/Dht11.png

* `DHT11 Datenblatt <https://components101.com/sites/default/files/component_datasheet/DHT11-Temperature-Sensor.pdf>`_

**Beispiel**

* :ref:`2.2.3_c` (C-Projekt)
* :ref:`2.2.3_py` (Python-Projekt)
