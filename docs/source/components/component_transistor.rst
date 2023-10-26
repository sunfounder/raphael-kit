.. _transistor:

Transistor
==============

.. image:: img/npn_pnp.png
    :width: 300

Ein Transistor ist ein Halbleiterbauelement, das Strom mit Strom steuert. Er hat die Funktion, ein schwaches Signal auf ein Signal größerer Amplitude zu verstärken und wird auch als kontaktloser Schalter verwendet.

Ein Transistor besteht aus einer dreischichtigen Struktur aus P-Typ- und N-Typ-Halbleitern. Sie bilden die drei internen Regionen. Die dünnere Schicht in der Mitte ist die Basisregion; die anderen beiden sind entweder beide N-Typ oder P-Typ – die kleinere Region mit den vielen Hauptträgern ist die Emitterregion, während die andere die Kollektorregion ist. Diese Anordnung ermöglicht es dem Transistor, als Verstärker zu fungieren. 
Aus diesen drei Regionen entstehen jeweils drei Anschlüsse, nämlich Basis (b), Emitter (e) und Kollektor (c). Sie bilden zwei P-N-Übergänge, nämlich den Emitterübergang und den Kollektorübergang. Der Pfeil im Schaltsymbol des Transistors gibt die Richtung des Emitterübergangs an.

* `P-N-Übergang – Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_

Abhängig vom Halbleitertyp können Transistoren in zwei Gruppen unterteilt werden: NPN und PNP. Aus der Abkürzung können wir schließen, dass der Erstere aus zwei N-Typ-Halbleitern und einem P-Typ-Halbleiter besteht und der Letztere genau umgekehrt ist. Siehe die Abbildung unten.

.. note::
    Der s8550 ist ein PNP-Transistor und der s8050 ein NPN-Transistor. Sie sehen sehr ähnlich aus; deshalb müssen wir genau auf die Beschriftungen achten.

.. image:: img/transistor_symbol.png
    :width: 600

Wenn ein High-Level-Signal durch einen NPN-Transistor fließt, wird dieser aktiviert. Ein PNP-Transistor hingegen benötigt ein Low-Level-Signal zur Steuerung. Beide Transistortypen werden häufig für kontaktlose Schalter verwendet, wie auch in diesem Experiment.

Wenn man die beschriftete Seite zu sich hin hält und die Pins nach unten zeigt, sind die Pins von links nach rechts: Emitter(e), Basis(b) und Kollektor(c).

.. image:: img/ebc.png
    :width: 150

* `S8050 Transistor Datenblatt <https://datasheet4u.com/datasheet-pdf/WeitronTechnology/S8050/pdf.php?id=576670>`_
* `S8550 Transistor Datenblatt <https://www.mouser.com/datasheet/2/149/SS8550-118608.pdf>`_

**Beispiel**

* :ref:`1.2.1_c` (C-Projekt)
* :ref:`1.3.3_c` (C-Projekt)
* :ref:`1.2.2_py` (Python-Projekt)
* :ref:`1.3.3_py` (Python-Projekt)
* :ref:`1.14_scratch` (Scratch-Projekt)

