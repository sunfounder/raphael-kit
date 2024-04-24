.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_rgb_led:

RGB LED
=================

.. image:: img/rgb_led.png
    :width: 100

RGB-LEDs strahlen Licht in verschiedenen Farben aus. Ein RGB-LED kombiniert drei LEDs in den Farben Rot, Grün und Blau in einem transparenten oder halbtransparenten Kunststoffgehäuse. Durch Ändern der Eingangsspannung der drei Pins und deren Überlagerung kann es, statistisch gesehen, 16.777.216 verschiedene Farben erzeugen.

.. image:: img/rgb_light.png
    :width: 600

RGB-LEDs können in gemeinsame Anode und gemeinsame Kathode unterteilt werden. In diesem Set wird die letztere verwendet. Die **gemeinsame Kathode** oder CC bedeutet, dass die Kathoden der drei LEDs verbunden sind. Wenn Sie sie mit GND verbinden und die drei Pins einstecken, wird die LED die entsprechende Farbe anzeigen.

Das Schaltungssymbol ist wie folgt dargestellt:

.. image:: img/rgb_symbol.png
    :width: 300

Ein RGB-LED hat 4 Pins: der längste ist GND; die anderen sind Rot, Grün und Blau. Wenn man die Kunststoffhülle berührt, findet man eine Kerbe. Der Pin, der der Kerbe am nächsten liegt, ist der erste Pin und als Rot markiert, gefolgt von GND, Grün und Blau.

.. image:: img/rgb_pin.jpg
    :width: 200

**Beispiel**

* :ref:`1.1.2_c` (C-Projekt)
* :ref:`1.1.2_py` (Python-Projekt)
* :ref:`1.2_scratch` (Scratch-Projekt)
