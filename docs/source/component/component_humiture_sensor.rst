.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_humiture_sensor:

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
