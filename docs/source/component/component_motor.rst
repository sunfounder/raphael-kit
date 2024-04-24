.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_motor:

Gleichstrommotor
===================

.. image:: img/image114.jpeg
    :align: center

Dies ist ein 3V Gleichstrommotor. Wenn Sie einem der beiden Anschlüsse ein hohes und ein niedriges Signal geben, wird er sich drehen.

* **Größe**: 25*20*15MM
* **Betriebsspannung**: 1-6V
* **Leerlaufstrom** (3V): 70m
* **Leerlaufdrehzahl** (3V): 13000RPM
* **Blockierstrom** (3V): 800mA
* **Wellendurchmesser**: 2mm

Ein Gleichstrommotor ist ein kontinuierlicher Aktuator, der elektrische Energie in mechanische Energie umwandelt. Gleichstrommotoren treiben durch kontinuierliche Winkelrotation Rotationspumpen, Ventilatoren, Kompressoren, Laufräder und andere Geräte an.

Ein Gleichstrommotor besteht aus zwei Teilen, dem festen Teil des Motors, der als **Stator** bezeichnet wird, und dem inneren Teil des Motors, der als **Rotor** (oder **Anker** eines Gleichstrommotors) bezeichnet wird und sich dreht, um Bewegung zu erzeugen.
Der Schlüssel zur Erzeugung von Bewegung ist die Positionierung des Ankers im Magnetfeld des Permanentmagneten (dessen Feld sich vom Nordpol zum Südpol erstreckt). Die Wechselwirkung des Magnetfelds mit den bewegten geladenen Teilchen (der stromführende Draht erzeugt das Magnetfeld) erzeugt das Drehmoment, das den Anker dreht.

.. image:: img/motor_sche.png
    :align: center

Der Strom fließt vom positiven Pol der Batterie durch den Schaltkreis, durch die Kupferbürsten zum Kommutator und dann zum Anker.
Aber wegen der zwei Lücken im Kommutator kehrt dieser Fluss bei jeder vollständigen Drehung zur Hälfte um.
Diese ständige Umkehrung wandelt im Wesentlichen die Gleichspannung der Batterie in Wechselspannung um, wodurch der Anker zum richtigen Zeitpunkt in die richtige Richtung ein Drehmoment erfährt, um die Rotation aufrechtzuerhalten.

**Beispiel**

* :ref:`1.3.1_c` (C-Projekt)
* :ref:`3.1.4_c` (C-Projekt)
* :ref:`1.3.1_py` (Python-Projekt)
* :ref:`4.1.10_py` (Python-Projekt)
* :ref:`1.17_scratch` (Scratch-Projekt)
