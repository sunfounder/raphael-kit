.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

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
