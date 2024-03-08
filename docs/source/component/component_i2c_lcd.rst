.. _cpn_i2c_lcd1602:

I2C LCD1602
==============

.. image:: img/i2c_lcd1602.png
    :width: 800

* **GND**: Masse
* **VCC**: Spannungsversorgung, 5V.
* **SDA**: Serielle Datenleitung. Mit VCC über einen Pullup-Widerstand verbinden.
* **SCL**: Serielle Taktleitung. Mit VCC über einen Pullup-Widerstand verbinden.

Wie wir alle wissen, bereichern LCDs und andere Anzeigen zwar die Mensch-Maschine-Interaktion, sie haben jedoch eine gemeinsame Schwäche. Wenn sie an einen Controller angeschlossen werden, werden mehrere IOs des Controllers belegt, der nicht viele externe Ports hat. Dies schränkt auch andere Funktionen des Controllers ein.

Daher wurde LCD1602 mit einem I2C-Modul entwickelt, um dieses Problem zu lösen. Das I2C-Modul verfügt über einen integrierten PCF8574 I2C-Chip, der I2C-Serien-Daten in parallele Daten für das LCD-Display umwandelt.

* `PCF8574 Datenblatt <https://www.ti.com/lit/ds/symlink/pcf8574.pdf?ts=1627006546204&ref_url=https%253A%252F%252Fwww.google.com%252F>`_

**I2C-Adresse**

Die Standardadresse ist in der Regel 0x27, in einigen Fällen kann sie jedoch 0x3F sein.

Wenn man die Standardadresse von 0x27 als Beispiel nimmt, kann die Geräteadresse durch Kurzschließen der A0/A1/A2-Pads geändert werden; im Standardzustand sind A0/A1/A2 1, und wenn das Pad kurzgeschlossen wird, sind A0/A1/A2 0.

.. image:: img/i2c_address.jpg
    :width: 600

**Hintergrundbeleuchtung/Kontrast**

Die Hintergrundbeleuchtung kann durch einen Jumper aktiviert werden; zum Deaktivieren den Jumper entfernen. Das blaue Potentiometer auf der Rückseite dient zur Einstellung des Kontrasts (Verhältnis der Helligkeit zwischen dem hellsten Weiß und dem dunkelsten Schwarz).

.. image:: img/back_lcd1602.jpg

* **Jumper**: Mit diesem Jumper kann die Hintergrundbeleuchtung aktiviert werden. Entfernen Sie diesen Jumper, um die Hintergrundbeleuchtung zu deaktivieren.
* **Potentiometer**: Dient zur Einstellung des Kontrasts (Klarheit des angezeigten Texts), im Uhrzeigersinn erhöhen und gegen den Uhrzeigersinn verringern.

**Beispiel**

* :ref:`1.1.7_c` (C-Projekt)
* :ref:`3.1.3_c` (C-Projekt)
* :ref:`3.1.7_c` (C-Projekt)
* :ref:`3.1.8_c` (C-Projekt)
* :ref:`3.1.11_c` (C-Projekt)
* :ref:`1.1.7_py` (Python-Projekt)
* :ref:`4.1.9_py` (Python-Projekt)
* :ref:`4.1.13_py` (Python-Projekt)
* :ref:`4.1.14_py` (Python-Projekt)
* :ref:`4.1.17_py` (Python-Projekt)

