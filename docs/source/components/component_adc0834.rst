.. _adc0834:

ADC0834
==============

Der ADC0834 ist ein 8-Bit-Analog-Digital-Umsetzer auf Basis einer sukzessiven Approximation, der mit einem konfigurierbaren Mehrkanal-Multiplexer und einer seriellen Ein-/Ausgabe ausgestattet ist. Die serielle Ein-/Ausgabe ist so konfiguriert, dass sie mit Standard-Schieberegistern oder Mikroprozessoren kommunizieren kann.

.. image:: img/image309.png


**Ablauf einer Umwandlung**

Eine Umwandlung wird gestartet, indem CS auf niedrig gesetzt wird, was alle Logikschaltungen aktiviert. CS muss während des gesamten Umwandlungsprozesses niedrig gehalten werden. Anschließend wird ein Takt-Eingang vom Prozessor empfangen. Bei jedem Übergang von niedrig nach hoch des Takt-Eingangs wird die Daten auf DI in das Multiplexer-Adressen-Schieberegister getaktet. Das erste logische Hoch am Eingang ist das Startbit. Einem Startbit folgt ein 3- bis 4-Bit-Zuweisungswort. Bei jedem weiteren Übergang von niedrig nach hoch des Takt-Eingangs werden das Startbit und das Zuweisungswort durch das Schieberegister verschoben. Wenn das Startbit in die Startposition des Multiplexerregisters verschoben wird, wird der Eingangskanal ausgewählt und die Umwandlung beginnt. Der SAR-Statusausgang (SARS) wird hochgeschaltet, um anzuzeigen, dass eine Umwandlung im Gange ist, und DI zum Multiplexer-Schieberegister wird während der Umwandlung deaktiviert.

Es wird automatisch ein Intervall von einem Taktzyklus eingefügt, um dem ausgewählten Multiplexkanal Zeit zum Setteln zu geben. Der Datenausgang DO verlässt den Hochimpedanz-Zustand und liefert für diese eine Taktperiode des Multiplexer-Setzlungszeit ein führendes Niedrig. Der SAR-Komparator vergleicht aufeinanderfolgende Ausgänge von der Widerstandsleiter mit dem eingehenden analogen Signal. Der Ausgang des Komparators gibt an, ob der analoge Eingang größer oder kleiner als der Ausgang der Widerstandsleiter ist. Während der Umwandlung wird die Umwandlungsdaten gleichzeitig vom DO-Ausgangspin ausgegeben, wobei das am stärksten signifikante Bit (MSB) zuerst kommt.

Nach acht Taktperioden ist die Umwandlung abgeschlossen und der SARS-Ausgang wird niedrig. Schließlich gibt er die Daten des am wenigsten signifikanten Bits nach dem MSB-Datenstrom aus.

.. image:: img/image175.png


**ADC0834 MUX ADRESSENSTEUERUNGSLOGIK-TABELLE**

.. image:: img/image176.png

* `ADC0831 Serien-Datenblatt <https://www.ti.com/lit/ds/symlink/adc0831-n.pdf>`_

**Beispiel**

* :ref:`2.1.7_c` (C-Projekt)
* :ref:`2.2.1_c` (C-Projekt)
* :ref:`2.2.2_c` (C-Projekt)
* :ref:`3.1.4_c` (C-Projekt)
* :ref:`3.1.5_c` (C-Projekt)
* :ref:`3.1.7_c` (C-Projekt)
* :ref:`2.1.7_py` (Python-Projekt)
* :ref:`2.2.1_py` (Python-Projekt)
* :ref:`2.2.2_py` (Python-Projekt)
* :ref:`4.1.10_py` (Python-Projekt)
* :ref:`4.1.11_py` (Python-Projekt)
* :ref:`4.1.13_py` (Python-Projekt)
