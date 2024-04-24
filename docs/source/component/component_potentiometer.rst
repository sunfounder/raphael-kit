.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_potentiometer:

Potentiometer
===============

.. image:: img/potentiometer.png
    :align: center
    :width: 150

Ein Potentiometer ist ebenfalls ein Widerstandselement mit 3 Anschlüssen, dessen Widerstandswert entsprechend einer regelmäßigen Variation angepasst werden kann.

Potentiometer gibt es in verschiedenen Formen, Größen und Werten, aber sie alle haben Folgendes gemeinsam:

* Sie haben drei Anschlüsse (oder Verbindungspunkte).
* Sie verfügen über einen Drehknopf, eine Schraube oder einen Schieber, mit dem der Widerstand zwischen dem mittleren Anschluss und einem der beiden äußeren Anschlüsse variiert werden kann.
* Der Widerstand zwischen dem mittleren Anschluss und einem der beiden äußeren Anschlüsse variiert zwischen 0 Ω und dem maximalen Widerstand des Potentiometers, wenn der Drehknopf, die Schraube oder der Schieber bewegt wird.

Hier ist das Schaltsymbol des Potentiometers.

.. image:: img/potentiometer_symbol.png
    :align: center
    :width: 400

Die Funktionen des Potentiometers in der Schaltung sind wie folgt:

#. Als Spannungsteiler dienen

    Ein Potentiometer ist ein kontinuierlich einstellbarer Widerstand. Wenn Sie die Welle oder den Schiebegriff des Potentiometers verstellen, rutscht der bewegliche Kontakt über den Widerstand. In diesem Moment kann eine Spannung ausgegeben werden, abhängig von der am Potentiometer angelegten Spannung und dem Winkel, um den sich der bewegliche Arm gedreht hat, oder dem Weg, den er zurückgelegt hat.

#. Als Rheostat dienen

    Wird das Potentiometer als Rheostat verwendet, verbinden Sie den mittleren Pin und einen der anderen 2 Pins in der Schaltung. So erhalten Sie einen sanft und kontinuierlich veränderten Widerstandswert innerhalb des Wegs des beweglichen Kontakts.

#. Als Stromregler dienen

    Wenn das Potentiometer als Stromregler fungiert, muss der Schiebkontaktanschluss als einer der Ausgangsanschlüsse angeschlossen werden.

Wenn Sie mehr über Potentiometer wissen möchten, verweisen Sie auf: `Potentiometer - Wikipedia <https://en.wikipedia.org/wiki/Potentiometer>`_

**Beispiel**

* :ref:`2.1.7_c` (C-Projekt)
* :ref:`2.1.7_py` (Python-Projekt)
