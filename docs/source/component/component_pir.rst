.. _cpn_pir:

PIR Bewegungssensormodul
============================

.. image:: img/pir_pic.png
    :width: 300
    :align: center

Der PIR-Sensor erkennt infrarote Wärmestrahlung, die dazu verwendet werden kann, die Anwesenheit von Organismen zu erkennen, die infrarote Wärmestrahlung aussenden.

Der PIR-Sensor ist in zwei Schlitze unterteilt, die mit einem Differenzverstärker verbunden sind. Wenn ein stationäres Objekt vor dem Sensor steht, erhalten die beiden Schlitze die gleiche Menge an Strahlung und der Ausgang ist null. Wenn sich ein bewegliches Objekt vor dem Sensor befindet, empfängt einer der Schlitze mehr Strahlung als der andere, wodurch der Ausgang hoch oder niedrig schwankt. Diese Änderung der Ausgangsspannung ist das Ergebnis der Bewegungserkennung.

.. image:: img/PIR_working_principle.jpg
    :width: 800

Nachdem das Sensormodul verdrahtet wurde, erfolgt eine einminütige Initialisierung. Während der Initialisierung gibt das Modul 0~3 mal in Intervallen aus. Anschließend befindet sich das Modul im Standby-Modus. Bitte halten Sie die Störung durch Lichtquellen und andere Quellen von der Oberfläche des Moduls fern, um Fehlfunktionen durch das störende Signal zu vermeiden. Es ist sogar besser, das Modul ohne starken Wind zu verwenden, da der Wind den Sensor ebenfalls stören kann.

.. image:: img/pir_back.png
    :width: 600
    :align: center

**Entfernungsanpassung**

Drehen Sie das Potenziometer zur Entfernungsanpassung im Uhrzeigersinn, erhöht sich der Erfassungsbereich und die maximale Erfassungsentfernung liegt bei etwa 0-7 Metern. Drehen Sie es gegen den Uhrzeigersinn, verringert sich der Erfassungsbereich und die minimale Erfassungsentfernung liegt bei etwa 0-3 Metern.

**Verzögerungsanpassung**

Drehen Sie das Potenziometer zur Verzögerungsanpassung im Uhrzeigersinn, erhöht sich auch die Erfassungsverzögerung. Die maximale Erfassungsverzögerung kann bis zu 300s betragen. Drehen Sie es dagegen gegen den Uhrzeigersinn, kann die Verzögerung auf ein Minimum von 5s verkürzt werden.

**Zwei Trigger-Modi**

Wählen Sie unterschiedliche Modi mit der Jumperkappe.

* **H**: Wiederholbarer Trigger-Modus, nachdem der menschliche Körper erkannt wurde, gibt das Modul ein hohes Signal aus. Während der anschließenden Verzögerungszeit, wenn jemand den Erfassungsbereich betritt, bleibt der Ausgang auf hohem Niveau.

* **L**: Nicht wiederholbarer Trigger-Modus, gibt ein hohes Signal aus, wenn er den menschlichen Körper erkennt. Nach der Verzögerung wechselt der Ausgang automatisch von einem hohen zu einem niedrigen Niveau.

**Beispiel**

* :ref:`2.2.7_c` (C-Projekt)
* :ref:`2.2.7_py` (Python-Projekt)
* :ref:`4.1.4_py` (Python-Projekt)
* :ref:`1.5_scratch` (Scratch-Projekt)

