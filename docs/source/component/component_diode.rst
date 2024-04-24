.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_diode:

Diode
=================

Eine Diode ist eine elektronische Komponente mit zwei Elektroden. Sie lässt den Strom nur in eine Richtung fließen, was oft als "Gleichrichter"-Funktion bezeichnet wird.
Man kann sich also eine Diode als elektronische Version eines Rückschlagventils vorstellen.

Aufgrund ihrer unidirektionalen Leitfähigkeit wird die Diode in fast allen elektronischen Schaltkreisen einer gewissen Komplexität verwendet. Sie ist eines der ersten Halbleiterbauelemente und hat ein breites Anwendungsspektrum.

Je nach Verwendungszweck kann sie unterteilt werden in Detektordioden, Gleichrichterdioden, Begrenzungsdioden, Spannungsreglerdioden usw.

In diesem Kit sind Gleichrichterdioden und Spannungsreglerdioden enthalten.

**Gleichrichterdiode**

.. image:: img/in4007_diode.png
.. image:: img/symbol_rectifier_diode.png
    :width: 200

Eine Gleichrichterdiode ist eine Halbleiterdiode, die verwendet wird, um Wechselstrom (AC) in Gleichstrom (DC) zu wandeln, dies geschieht mittels der Brückengleichrichter-Anwendung. Die Alternative zur Gleichrichterdiode über die Schottky-Barriere wird hauptsächlich in der Digitaltechnik geschätzt. Diese Diode kann Ströme von mA bis zu einigen kA und Spannungen bis zu einigen kV leiten.

Die Konstruktion von Gleichrichterdioden kann mit Siliziummaterial erfolgen und sie sind in der Lage, hohe elektrische Stromwerte zu leiten. Diese Dioden sind nicht berühmt, aber immer noch werden Ge- oder Galliumarsenid-basierte Halbleiterdioden verwendet. Ge-Dioden haben eine geringere zulässige Rückspannung sowie eine geringere zulässige Sperrschichttemperatur. Die Ge-Diode hat gegenüber der Si-Diode den Vorteil einer niedrigen Schwellenspannung im Vorwärtsbetrieb.

* `1N400x Universal-Diode - Wikipedia <https://en.wikipedia.org/wiki/1N400x_general-purpose_diode>`_

**Zener-Diode**

Eine Zener-Diode ist eine spezielle Art von Diode, die darauf ausgelegt ist, den Strom zuverlässig "rückwärts" fließen zu lassen, wenn eine bestimmte umgekehrte Spannung, bekannt als Zener-Spannung, erreicht wird.

Diese Diode ist ein Halbleiterbauelement, das bis zur kritischen Rückwärts-Durchbruchsspannung einen sehr hohen Widerstand aufweist. An diesem kritischen Durchbruchspunkt wird der Rückwiderstand auf einen sehr kleinen Wert reduziert, und der Strom steigt, während die Spannung in diesem niederohmigen Bereich konstant bleibt.

.. image:: img/zener_diode.png
.. image:: img/symbol-zener-diode.jpg

* `Zener-Diode - Wikipedia <https://en.wikipedia.org/wiki/Zener_diode>`_

**Beispiel**

* :ref:`1.3.3_c` (C-Projekt)
* :ref:`1.3.3_py` (Python-Projekt)

