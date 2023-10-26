.. _rotary_encoder:

Drehgebermodul
=============================

.. image:: img/rotary_encoder_pic.png
    :width: 300
    :align: center

Das Drehgebermodul zählt die Anzahl der Impulse, die während der Drehung in Vorwärts- und Rückwärtsrichtung ausgegeben werden. Im Gegensatz zu einem Potentiometer ist diese Drehzahl unbegrenzt und die Anzahl der Impulse pro Zyklus beträgt 20. Durch Drücken der Taste (SW) auf dem Drehgeber beginnt die Zählung von null.

Es gibt hauptsächlich zwei Arten von Drehgebern: Absolut- und Inkrementalgeber (relative Geber). In diesem Set wird ein Inkrementalgeber verwendet.

Inkrementalgeber erzeugen zweiphasige Rechteckwellen, deren Phasendifferenz 90 Grad beträgt, normalerweise als Kanal A und B bezeichnet.

Wie rechts dargestellt, wenn Kanal A von hohem auf niedriges Niveau wechselt und Kanal B dabei auf hohem Niveau ist, zeigt dies an, dass der Drehgeber im Uhrzeigersinn (CW) dreht. Wenn jedoch zu diesem Zeitpunkt Kanal B auf niedrigem Niveau ist, bedeutet dies, dass er gegen den Uhrzeigersinn (CCW) dreht. Wenn wir also den Wert von Kanal B lesen, während Kanal A auf niedrigem Niveau ist, können wir feststellen, in welche Richtung der Drehgeber dreht.

.. image:: img/image206.png
    :width: 600
    :align: center
	
**Beispiel**

* :ref:`2.1.6_c` (C-Projekt)
* :ref:`2.1.6_py` (Python-Projekt)
