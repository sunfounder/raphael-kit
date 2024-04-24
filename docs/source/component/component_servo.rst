.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_servo:

Servo
===========

.. image:: img/servo.png
    :align: center

Ein Servo besteht in der Regel aus folgenden Teilen: Gehäuse, Welle, Getriebesystem, Potentiometer, Gleichstrommotor und eingebetteter Platine.

Seine Funktionsweise ist wie folgt: Der Mikrocontroller sendet PWM-Signale an den Servo. Die eingebettete Platine im Servo empfängt diese Signale über den Signaleingang und steuert den im Inneren befindlichen Motor. Dadurch treibt der Motor das Getriebesystem an, welches nach einer Drosselung die Welle antreibt. Die Welle und das Potentiometer des Servos sind miteinander verbunden. Wenn die Welle sich dreht, treibt sie das Potentiometer an, sodass dieses ein Spannungssignal an die eingebettete Platine sendet. Die Platine bestimmt daraufhin, basierend auf der aktuellen Position, die Drehrichtung und -geschwindigkeit, sodass sie genau an der vorgegebenen Position stoppen und dort verharren kann.

.. image:: img/servo_internal.png
    :align: center

Der Winkel wird durch die Dauer eines Pulses bestimmt, der auf das Steuerkabel gegeben wird. Dies wird als Pulsweitenmodulation bezeichnet. Der Servo erwartet alle 20 ms einen Puls. Die Länge des Pulses bestimmt, wie weit sich der Motor dreht. Ein 1,5 ms langer Puls beispielsweise bewirkt, dass sich der Motor in die 90-Grad-Position (Neutralstellung) dreht.
Wird ein Puls gesendet, der kürzer als 1,5 ms ist, dreht sich der Servo in eine Position und hält seine Ausgangswelle einige Grad gegen den Uhrzeigersinn von der Neutralstellung ab. Bei einem Puls, der länger als 1,5 ms ist, tritt das Gegenteil auf. Die minimal erforderliche und die maximal mögliche Pulslänge, die den Servo zu einer gültigen Position steuern, sind von jedem Servo abhängig. In der Regel liegt der Mindestpuls bei etwa 0,5 ms und der Maximalpuls bei 2,5 ms.

.. image:: img/servo_duty.png
    :width: 600
    :align: center

**Beispiel**

* :ref:`1.3.2_c` (C-Projekt)
* :ref:`3.1.2_c` (C-Projekt)
* :ref:`1.3.2_py` (Python-Projekt)
* :ref:`4.1.8_py` (Python-Projekt)
