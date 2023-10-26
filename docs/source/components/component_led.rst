.. _led:

LED
==========

.. image:: img/LED.png
    :width: 400

Die Halbleiterlichtemittierende Diode ist eine Art Bauteil, welches elektrische Energie über PN-Übergänge in Lichtenergie umwandeln kann. Je nach Wellenlänge kann sie in Laserdiode, Infrarot-Lichtemittierende Diode und sichtbare Lichtemittierende Diode unterteilt werden, die allgemein als Lichtemittierende Diode (LED) bekannt ist.

Dioden haben eine unidirektionale Leitfähigkeit, daher fließt der Strom wie im Schaltbildsymbol durch den Pfeil angezeigt. An die Anode muss eine positive Spannung und an die Kathode eine negative Spannung angelegt werden, damit die LED leuchtet.

.. image:: img/led_symbol.png


Eine LED hat zwei Pins. Der längere ist die Anode und der kürzere die Kathode. Achten Sie darauf, sie nicht verkehrt herum anzuschließen. In der LED gibt es eine feste Vorwärtsspannung, sie kann daher nicht direkt mit der Schaltung verbunden werden, da die Versorgungsspannung diesen Abfall übersteigen und die LED dadurch verbrennen kann. Die Vorwärtsspannung der roten, gelben und grünen LED beträgt 1,8 V und die der weißen 2,6 V. Die meisten LEDs können einem maximalen Strom von 20 mA standhalten, daher muss ein strombegrenzender Widerstand in Reihe geschaltet werden.

Die Formel für den Widerstandswert lautet:

    R = (Vsupply – VD)/I

**R** steht für den Widerstandswert des strombegrenzenden Widerstandes, **Vsupply** für die Versorgungsspannung, **VD** für den Spannungsabfall und **I** für den Arbeitsstrom der LED.

Hier ist eine detaillierte Einführung zur LED: `LED - Wikipedia <https://en.wikipedia.org/wiki/Light-emitting_diode>`_.

**Beispiel**

* :ref:`1.1.1_c` (C-Projekt)
* :ref:`3.1.6_c` (C-Projekt)
* :ref:`1.1.1_py` (Python-Projekt)
* :ref:`4.1.12_py` (Python-Projekt)
* :ref:`1.1_scratch` (Scratch-Projekt)
