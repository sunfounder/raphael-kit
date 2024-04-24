.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_relay:

Relais
==========================================

.. image:: img/relay_pic.png
    :width: 200
    :align: center

Wie uns vielleicht bekannt ist, ist ein Relais ein Gerät, das dazu dient, Verbindungen
zwischen zwei oder mehr Punkten oder Geräten in Reaktion auf das angelegte Eingangssignal
herzustellen. Mit anderen Worten, Relais bieten eine Isolation zwischen dem Steuergerät
und dem Endgerät, da Endgeräte sowohl mit Wechselstrom (AC) als auch mit Gleichstrom (DC) arbeiten können. Sie erhalten jedoch
Signale von einem Mikrocontroller, der mit Gleichstrom arbeitet, weshalb
ein Relais zur Überbrückung notwendig ist. Relais sind äußerst nützlich, wenn man eine große Strom- oder Spannungsmenge mit einem kleinen elektrischen
Signal steuern muss.

Ein Relais besteht aus 5 Teilen:

.. image:: img/relay142.jpeg

**Elektromagnet** - Er besteht aus einem Eisenkern, um den eine Drahtspule gewickelt ist.
Wird Strom hindurch geleitet, wird er magnetisch.
Daher wird er als Elektromagnet bezeichnet.

**Anker** - Der bewegliche magnetische Streifen wird als Anker bezeichnet. Wenn
Strom durch ihn fließt, wird die Spule energisiert und erzeugt so ein
magnetisches Feld, das verwendet wird, um die normalerweise offenen (N/O) oder
normalerweise geschlossenen (N/C) Kontakte herzustellen oder zu unterbrechen. Der Anker kann sowohl mit Gleichstrom (DC) als auch mit Wechselstrom (AC) bewegt werden.

**Feder** - Fließt kein Strom durch die Spule am
Elektromagneten, zieht die Feder den Anker weg, sodass der Stromkreis nicht
geschlossen werden kann.

Set von elektrischen **Kontakten** - Es gibt zwei Kontaktpunkte:

-  Normalerweise offen - verbunden, wenn das Relais aktiviert ist, und getrennt, wenn es inaktiv ist.

-  Normalerweise geschlossen - nicht verbunden, wenn das Relais aktiviert ist, und verbunden, wenn es inaktiv ist.

**Gegossener Rahmen** - Relais sind zum Schutz mit Kunststoff überzogen.

Das Funktionsprinzip eines Relais ist einfach. Wird das Relais mit Strom versorgt, beginnen Ströme durch die Steuerspule zu fließen; infolgedessen
beginnt sich der Elektromagnet zu aktivieren. Dann wird der Anker zur
Spule hingezogen und zieht den beweglichen Kontakt herunter, sodass er sich mit den normalerweise offenen Kontakten verbindet. So wird der Stromkreis mit der Last energisiert. Das Unterbrechen des Stromkreises wäre ein ähnlicher Fall, da der bewegliche Kontakt durch die Kraft der Feder zu den normalerweise geschlossenen Kontakten hochgezogen wird.
Auf diese Weise kann das Ein- und Ausschalten des Relais den Zustand eines Lastkreises steuern.

**Beispiel**

* :ref:`1.3.3_c` (C-Projekt)
* :ref:`1.3.3_py` (Python-Projekt)
