.. _cpn_speed_sensor:

Geschwindigkeitssensormodul
===============================

.. image:: img/speed_sensor1.png
    :width: 300
    :align: center

Der Geschwindigkeitssensor besteht aus zwei Teilen: einem Sender und einem Empfänger. Der Sender emittiert Licht, das anschließend in den Empfänger eindringt.

Wird der Lichtstrahl zwischen Sender und Empfänger durch ein Hindernis unterbrochen, erkennt der Empfänger das einfallende Licht nicht, woraufhin der D0-Pin ein niedriges Signal ausgibt.

.. note::
    Der A0-Pin auf diesem Modul ist leer und es gibt keinen Schaltkreis.

.. image:: img/speed_sensor2.png

**Beispiel**

* :ref:`2.2.6_c` (C-Projekt)
* :ref:`2.2.6_py` (Python-Projekt)
* :ref:`1.7_scratch` (Scratch-Projekt)
