.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_thermistor:

Thermistor
===============

.. image:: img/thermistor.png
    :width: 150
    :align: center

Ein Thermistor ist eine Art Widerstand, dessen Widerstand stark temperaturabhängig ist, stärker als bei Standardwiderständen. Das Wort ist eine Kombination aus den Worten "thermal" und "Resistor". Thermistoren werden häufig als Anlaufstrombegrenzer, Temperatursensoren (meist vom Typ mit negativem Temperaturkoeffizienten oder NTC), selbstzurücksetzende Überstromschutzgeräte und selbstregulierende Heizelemente (meist vom Typ mit positivem Temperaturkoeffizienten oder PTC) eingesetzt.

* `Thermistor - Wikipedia <https://en.wikipedia.org/wiki/Thermistor>`_

Hier ist das elektronische Symbol für einen Thermistor.

.. image:: img/thermistor_symbol.png
    :width: 300
    :align: center

Es gibt zwei grundsätzlich entgegengesetzte Typen von Thermistoren:

* Bei NTC-Thermistoren sinkt der Widerstand mit steigender Temperatur, in der Regel aufgrund einer Zunahme der durch thermische Anregung aus dem Valenzband angeregten Leitungselektronen. Ein NTC wird häufig als Temperatursensor eingesetzt oder in Serie zu einer Schaltung als Anlaufstrombegrenzer.
* Bei PTC-Thermistoren steigt der Widerstand mit steigender Temperatur, meist aufgrund erhöhter thermischer Gitteranregungen, insbesondere von Unreinheiten und Unvollkommenheiten. PTC-Thermistoren werden in der Regel in Serie zu einer Schaltung eingebaut und dienen zum Schutz vor Überstrombedingungen, als rücksetzbare Sicherungen.

In diesem Bausatz verwenden wir einen vom NTC-Typ. Jeder Thermistor hat einen normalen Widerstand. Hier beträgt er 10k Ohm, gemessen bei 25 Grad Celsius.

Hier ist die Beziehung zwischen Widerstand und Temperatur:

    RT = RN * expB(1/TK – 1/TN)

* **RT** ist der Widerstand des NTC-Thermistors bei der Temperatur TK.
* **RN** ist der Widerstand des NTC-Thermistors bei der Nenntemperatur TN. Hier beträgt der numerische Wert von RN 10k.
* **TK** ist eine Kelvin-Temperatur und die Einheit ist K. Hier beträgt der numerische Wert von TK 273,15 + Grad Celsius.
* **TN** ist eine Nenn-Kelvin-Temperatur; die Einheit ist ebenfalls K. Hier beträgt der numerische Wert von TN 273,15+25.
* Und **B(beta)**, die Materialkonstante des NTC-Thermistors, wird auch als Wärmeempfindlichkeitsindex bezeichnet und hat einen numerischen Wert von 3950.
* **exp** steht für Exponentialfunktion, und die Basiszahl e ist eine natürliche Zahl und beträgt ungefähr 2,7.

Wandeln Sie diese Formel TK=1/(ln(RT/RN)/B+1/TN) um, um die Kelvin-Temperatur zu erhalten, die minus 273,15 gleich Grad Celsius ist.

Dieser Zusammenhang ist eine empirische Formel. Sie ist nur dann genau, wenn Temperatur und Widerstand im wirksamen Bereich liegen.

**Beispiel**

* :ref:`2.2.2_c` (C-Projekt)
* :ref:`3.1.4_c` (C-Projekt)
* :ref:`3.1.7_c` (C-Projekt)
* :ref:`2.2.2_py` (Python-Projekt)
* :ref:`4.1.10_py` (Python-Projekt)
* :ref:`4.1.13_py` (Python-Projekt)
