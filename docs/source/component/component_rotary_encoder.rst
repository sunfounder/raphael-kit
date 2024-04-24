.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_rotary_encoder:

Drehgebermodul
=============================

.. image:: img/rotary_encoder_pic.png
    :width: 300
    :align: center

Ein Drehgeber ist ein Positionssensor, der die Rotation eines Knopfes in ein Ausgangssignal umwandelt und die Richtung anzeigt, in welche der Knopf gedreht wird.

Drehgeber sind digitale Versionen von Potentiometern und bieten eine größere Vielseitigkeit. Sie können sich kontinuierlich drehen, während Potentiometer einen begrenzten Drehbereich haben. Potentiometer zeigen die genaue Knopfposition an, während Drehgeber Veränderungen in der Position anzeigen.

Es gibt hauptsächlich zwei Arten von Drehgebern: absolute und inkrementelle (relative) Encoder. In diesem Kit wird ein inkrementeller verwendet.

Inkrementelle Encoder erzeugen zweiphasige Rechteckwellen mit einer 90-Grad-Phasendifferenz, die üblicherweise als A- und B-Kanal bezeichnet werden.

Wie unten veranschaulicht, bedeutet es beim Übergang des Kanals A von einem hohen Pegel zu einem niedrigen Pegel - wenn Kanal B auf hohem Niveau ist -, dass sich der Drehgeber im Uhrzeigersinn (CW) dreht; befindet sich Kanal B in diesem Moment auf niedrigem Niveau, bedeutet dies eine Rotation entgegen dem Uhrzeigersinn (CCW). Indem wir also den Wert des Kanals B lesen, wenn Kanal A auf niedrigem Level ist, können wir die Drehrichtrung bestimmen, in welche sich der Drehencoder bewegt.

.. image:: img/image206.png
    :width: 600
    :align: center
	
**Beispiel**

* :ref:`2.1.6_c` (C-Projekt)
* :ref:`2.1.6_py` (Python-Projekt)
