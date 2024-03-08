.. _cpn_4_digit:

4-stellige 7-Segment-Anzeige
==================================

Die 4-stellige 7-Segment-Anzeige besteht aus vier zusammenarbeitenden 7-Segment-Anzeigen.

.. image:: img/4-digit-sche.png

Jede Anzeige der 4-stelligen 7-Segment-Anzeige arbeitet unabhängig. Sie nutzt das Prinzip der menschlichen visuellen Persistenz, um die Zeichen jedes 7-Segments schnell nacheinander in einer Schleife anzuzeigen und so durchgehende Zeichenfolgen zu bilden.

Als Beispiel, wenn "1234" auf der Anzeige dargestellt wird, wird "1" auf dem ersten 7-Segment angezeigt, und "234" wird nicht dargestellt. Nach einer kurzen Zeit zeigt das zweite 7-Segment "2", während das 1., 3. und 4. 7-Segment nichts anzeigt, und so weiter. Die vier Anzeigen zeigen der Reihe nach. Dieser Vorgang ist sehr kurz (typischerweise 5ms), und aufgrund des optischen Nachleuchteffekts und des Prinzips der visuellen Restwahrnehmung sehen wir vier Zeichen gleichzeitig.

.. image:: img/image78.png

**Anzeigecodes**

Um Ihnen zu helfen zu verstehen, wie 7-Segment-Anzeigen (Gemeinsame Anode) Zahlen anzeigen, haben wir die folgende Tabelle erstellt. Die Zahlen sind die Nummern 0-F, die auf der 7-Segment-Anzeige dargestellt werden; (DP) GFEDCBA bezieht sich auf das entsprechende LED-Set, das auf 0 oder 1 gesetzt ist. Zum Beispiel bedeutet 11000000, dass DP und G auf 1 gesetzt sind, während alle anderen auf 0 gesetzt sind. Daher wird die Zahl 0 auf der 7-Segment-Anzeige angezeigt, während HEX-Code der hexadezimalen Nummer entspricht.

.. image:: img/common_anode.png

**Beispiel**

* :ref:`1.1.5_c` (C-Projekt)
* :ref:`3.1.1_c` (C-Projekt)
* :ref:`3.1.6_c` (C-Projekt)
* :ref:`3.1.12_c` (C-Projekt)
* :ref:`1.1.5_py` (Python-Projekt)
* :ref:`4.1.3_py` (Python-Projekt)
* :ref:`4.1.7_py` (Python-Projekt)
* :ref:`4.1.12_py` (Python-Projekt)
* :ref:`4.1.18_py` (Python-Projekt)
