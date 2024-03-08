.. _cpn_74hc595:

74HC595
===========

.. image:: img/74HC595.png

Der 74HC595 besteht aus einem 8-Bit-Schieberegister und einem Speicherregister mit dreistufigen parallelen Ausgängen. Er wandelt serielle Eingaben in parallele Ausgaben um, sodass Sie IO-Ports eines MCU sparen können.
Wenn MR (Pin10) auf hohem Pegel und OE (Pin13) auf niedrigem Pegel ist, werden Daten bei der steigenden Flanke von SHcp eingegeben und gelangen über die steigende Flanke von SHcp in das Speicherregister. Wenn die beiden Uhren miteinander verbunden sind, ist das Schieberegister immer einen Impuls früher als das Speicherregister. Im Speicherregister gibt es einen seriellen Schiebeeingangspin (Ds), einen seriellen Ausgangspin (Q) und einen asynchronen Reset-Button (niedriger Pegel). Das Speicherregister gibt einen Bus mit einem parallelen 8-Bit und in drei Zuständen aus. Wenn OE aktiviert (niedriger Pegel) ist, werden die Daten im Speicherregister auf den Bus ausgegeben.

* `74HC595 Datenblatt <https://www.ti.com/lit/ds/symlink/cd74hc595.pdf?ts=1617341564801>`_

.. image:: img/74hc595_pin.png
    :width: 600

Pins des 74HC595 und ihre Funktionen:

* **Q0-Q7**: 8-Bit parallele Datenausgangspins, geeignet zur direkten Steuerung von 8 LEDs oder 8 Pins eines 7-Segment-Displays.
* **Q7’**: Serieller Ausgangspin, verbunden mit DS eines anderen 74HC595, um mehrere 74HC595s in Serie zu verbinden.
* **MR**: Reset-Pin, aktiv auf niedrigem Pegel.
* **SHcp**: Zeitsequenzeingabe des Schieberegisters. Bei der steigenden Flanke verschieben sich die Daten im Schieberegister um jeweils ein Bit, d.h. Daten in Q1 verschieben sich nach Q2 usw. Bei der fallenden Flanke bleiben die Daten im Schieberegister unverändert.
* **STcp**: Zeitsequenzeingabe des Speicherregisters. Bei der steigenden Flanke werden die Daten im Schieberegister in das Speicherregister verschoben.
* **CE**: Ausgabefähiger Pin, aktiv auf niedrigem Pegel.
* **DS**: Serieller Dateneingangspin.
* **VCC**: Positive Versorgungsspannung.
* **GND**: Masse.

**Beispiel**

* :ref:`1.1.4_c` (C-Projekt)
* :ref:`1.1.5_c` (C-Projekt)
* :ref:`3.1.1_c` (C-Projekt)
* :ref:`3.1.6_c` (C-Projekt)
* :ref:`3.1.12_c` (C-Projekt)
* :ref:`1.1.4_py` (Python-Projekt)
* :ref:`1.1.5_py` (Python-Projekt)
* :ref:`4.1.7_py` (Python-Projekt)
* :ref:`4.1.12_py` (Python-Projekt)
* :ref:`4.1.18_py` (Python-Projekt)
