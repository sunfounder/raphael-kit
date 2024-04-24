.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_dot_matrix:

LED Matrix Modul
==============================

.. image:: img/max7219_module.jpg
    :width: 400
    :align: center

Dies ist ein gängiges Kathoden-8x8-Punkt-Matrix-Modul, das von MAX7219 angetrieben wird. Die Betriebsspannung des Moduls beträgt 5V, die Größe ist 50mmx32mmx15mm. Die linke Seite ist der Eingangsanschluss, die rechte Seite der Ausgangsanschluss. Es unterstützt die Kaskadierung mehrerer Module.

* **VCC**: Positive Versorgungsspannung. Verbinden mit +5V.
* **GND**: Masse (beide GND-Pins müssen verbunden werden)
* **DIN**: Serieller Dateneingang. Daten werden bei steigender Flanke von CLK in das interne 16-Bit-Schieberegister geladen.
* **CS**: Chip-Select Eingang. Serielle Daten werden geladen, während CS niedrig ist. Die letzten 16 Bits serieller Daten werden bei steigender Flanke von CS übernommen.
* **CLK**: Serieller Takteingang. Maximalrate 10MHz. Bei steigender Flanke von CLK werden Daten in das interne Schieberegister verschoben. Bei fallender Flanke von CLK werden Daten aus DOUT getaktet. Bei MAX7221 ist der CLK-Eingang nur aktiv, wenn CS niedrig ist.

**MAX7219**

Der MAX7219 ist ein kompakter, serieller Ein-/Ausgabe-Common-Kathoden-Anzeigetreiber, der Mikroprozessoren (µPs) mit bis zu 8-stelligen 7-Segment-LED-Anzeigen, Balkenanzeigen oder 64 einzelnen LEDs verbindet. Auf dem Chip enthalten sind ein BCD-Code-B Decoder, Multiplex-Scan-Schaltungen, Segment- und Zifferntreiber sowie ein 8x8 statischer RAM, der jede Ziffer speichert.

Es wird nur ein externer Widerstand benötigt, um den Segmentstrom für alle LEDs festzulegen. Der MAX7221 ist kompatibel mit SPI™, QSPI™ und MICROWIRE™ und verfügt über segmentierte Treiber mit begrenzter Flankensteilheit zur Reduzierung von EMI.

Eine praktische 4-Draht-Schnittstelle verbindet alle gängigen µPs. Einzelne Ziffern können adressiert und aktualisiert werden, ohne das gesamte Display neu zu schreiben. Der MAX7219/MAX7221 ermöglicht es dem Benutzer auch, die CodeB-Decodierung oder keine Decodierung für jede Ziffer auszuwählen.

.. image:: img/max7219_sche.png

* `MAX7219 Datenblatt <https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf>`_

**Beispiel**

* :ref:`1.1.6_c` (C-Projekt)
* :ref:`3.1.12_c` (C-Projekt)
* :ref:`1.1.6_py` (Python-Projekt)
* :ref:`4.1.19_py` (Python-Projekt)
