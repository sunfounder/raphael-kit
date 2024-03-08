.. _cpn_7_segment:

7-Segment-Anzeige
======================

.. image:: img/7-seg.jpg

Eine 7-Segment-Anzeige ist eine Komponente in Form einer 8, die 7 LEDs enthält. Jede LED wird als Segment bezeichnet – wenn sie aktiviert wird, bildet ein Segment einen Teil einer anzuzeigenden Zahl.

Es gibt zwei Arten von Pin-Verbindungen: Gemeinsame Kathode (CC) und Gemeinsame Anode (CA). Wie der Name schon sagt, hat eine CC-Anzeige alle Kathoden der 7 LEDs verbunden, während eine CA-Anzeige alle Anoden der 7 Segmente verbunden hat.

In diesem Set verwenden wir die 7-Segment-Anzeige mit gemeinsamer Kathode. Hier ist das elektronische Symbol dazu.

.. image:: img/segment_cathode.png
    :width: 800

Jede der LEDs in der Anzeige erhält ein positionsabhängiges Segment, dessen Verbindungspins aus dem rechteckigen Kunststoffgehäuse herausgeführt werden. Diese LED-Pins sind von "a" bis "g" beschriftet und repräsentieren jede einzelne LED. Die anderen LED-Pins sind miteinander verbunden und bilden einen gemeinsamen Pin. Durch das Vorwärtsbiasen der entsprechenden Pins der LED-Segmente in einer bestimmten Reihenfolge leuchten einige Segmente auf und andere bleiben dunkel, wodurch der entsprechende Charakter auf der Anzeige dargestellt wird.

**Anzeigecodes** 

Um Ihnen zu helfen zu verstehen, wie 7-Segment-Anzeigen (Gemeinsame Kathode) Zahlen anzeigen, haben wir die folgende Tabelle erstellt. Die Zahlen sind die Nummern 0-F, die auf der 7-Segment-Anzeige dargestellt werden; (DP) GFEDCBA bezieht sich auf das entsprechende LED-Set, das auf 0 oder 1 gesetzt ist. Zum Beispiel bedeutet 00111111, dass DP und G auf 0 gesetzt sind, während alle anderen auf 1 gesetzt sind. Daher wird die Zahl 0 auf der 7-Segment-Anzeige angezeigt, während HEX-Code der hexadezimalen Nummer entspricht.

.. image:: img/segment_code.png

**Beispiel**

* :ref:`1.1.4_c` (C-Projekt)
* :ref:`1.1.4_py` (Python-Projekt)

