.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_reed_switch:

Reed-Schalter-Modul
======================

.. image:: img/reed_switch.png
    :width: 300
    :align: center

* Verwendung eines normalerweise offenen Reed-Schalters.
* Komparatorausgang, klares Signal, gutes Wellenbild, starke Antriebsfähigkeit, mehr als 15mA.
* Arbeitspannung: 3,3V-5V
* Ausgabeform: digitaler Schalterausgang (0 und 1).
* Mit festen Befestigungslöchern für einfache Installation.
* Kleine PCB-Größe: 3,2cm x 1,4cm.
* Verwendet den Weitspannungs-Komparator LM393.

Das Reed-Schalter-Modul besteht aus einem Reed-Schalter, einem Potentiometer, einem LM393-Komparator, einer LED usw. Die interne Schaltung wird unten gezeigt. Wenn ein Magnet dem Modul nahe kommt, schaltet es ein und das Modul gibt ein niedriges Signal aus; ist kein Magnetfeld vorhanden, schaltet es aus und gibt ein hohes Signal aus. Die Erkennungsdistanz zwischen dem Reed-Schalter und dem Magneten sollte innerhalb von 1,5cm liegen; darüber hinaus wird er unempfindlich oder löst nicht aus. Die Empfindlichkeit kann auch über das Potentiometer am Modul angepasst werden.

.. image:: img/reedswitch_sche.jpg
    :width: 600
    :align: center

Der Reed-Schalter, auch als Magnetischer Schalter oder Reed-Kontakt bekannt.

Er hat zwei innenliegende Metallzungen, die in einem Glasröhrchen versiegelt sind, welches mit einem Inertgas gefüllt ist. Normalerweise überlappen sich die beiden Zungen, werden jedoch durch eine Lücke getrennt und der Stromkreis ist unterbrochen. Befindet sich ein magnetisches Objekt in der Nähe, erzeugen die beiden Zungen aufgrund der magnetischen Anziehungskraft eine Verbindung und der Stromkreis schließt. Daher kann der Reed-Schalter als magnetischer Sensor verwendet werden.

.. image:: img/HowItWorksReed.jpg

**Beispiel**

* :ref:`2.2.4_c` (C-Projekt)
* :ref:`2.2.4_py` (Python-Projekt)
* :ref:`4.1.6_py` (Python-Projekt)
* :ref:`1.6_scratch` (Scratch-Projekt)
