.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_audio_speaker:

Audio-Modul und Lautsprecher
================================

**Audio-Verstärker-Modul**

.. image:: img/audio_module.jpg
    :width: 500
    :align: center

Das Audio-Verstärker-Modul enthält einen HXJ8002 Audio-Leistungsverstärker-Chip. Dieser Chip ist ein Verstärker mit geringer Stromversorgung, der bei einer 5V DC Stromversorgung 3W durchschnittliche Audioleistung für eine 3Ω BTL-Last bereitstellen kann, mit geringer harmonischer Verzerrung (unter 10% Schwellenwertverzerrung bei 1KHz). Dieser Chip kann Audiosignale ohne Kopplungskondensatoren oder Bootstrap-Kondensatoren verstärken.

Das Modul kann mit einer Stromversorgung von 2,0V bis 5,5V DC bei einem Betriebsstrom von 10mA (0,6uA für den typischen Standby-Strom) betrieben werden und einen leistungsstarken verstärkten Ton in einen Lautsprecher mit 3Ω, 4Ω oder 8Ω Impedanz erzeugen. Dieses Modul verfügt über eine verbesserte Pop- und Klick-Schaltung, die das Übergangsrauschen beim Ein- und Ausschalten erheblich reduziert. Die geringe Größe, die hohe Effizienz und die geringe Stromversorgung machen es in vielen tragbaren und batteriebetriebenen Projekten sowie Mikrocontrollern weit verbreitet.

* **IC**: HXJ8002
* **Eingangsspannung**: 2V ~ 5.5V
* **Standby-Modus Strom**: 0.6uA (typischer Wert)
* **Ausgangsleistung**: 3W (3Ω Last), 2.5W (4Ω Last), 1.5W (8Ω Last)
* **Ausgang Lautsprecher Impedanz**: 3Ω, 4Ω, 8Ω
* **Größe**: 19.8mm x 14.2mm

**Lautsprecher**

.. image:: img/speaker_pic.png
    :width: 300
    :align: center

* **Größe**: 20x30x7mm
* **Impedanz**: 8ohm
* **Nenn-Eingangsleistung**: 1.5W 
* **Max. Eingangsleistung**: 2.0W
* **Kabellänge**: 10cm

.. image:: img/2030_speaker.png

Die Größentabelle finden Sie unten:

* :download:`2030 Lautsprecher Datenblatt <https://github.com/sunfounder/sf-pdf/raw/master/datasheet/2030-speaker-datasheet.pdf>`

**Audiokabel**

.. image:: img/audio_cable_pic2.png
    :width: 500
    :align: center

Es handelt sich um ein 3,5mm männliches Audiokabel mit einer Gesamtlänge von 43cm. Es verfügt über 3 Anschlüsse: Rot für den linken Kanal, Weiß für den rechten Kanal und GND in der Mitte.

**Schaltplan**

.. image:: img/4.1.4fritzing.png

Nachdem Sie die Schaltung gemäß dem obigen Diagramm aufgebaut haben, stecken Sie das Audiokabel in die 3,5mm Audio-Buchse des Raspberry Pi.

.. image:: img/audio4.png
    :width: 400
    :align: center

Wenn Ihr Lautsprecher keinen Ton von sich gibt, könnte es daran liegen, dass der Raspberry Pi den falschen Audio-Ausgang ausgewählt hat (Standardmäßig ist HDMI ausgewählt). Sie müssen dann :ref:`change_audio_output` auf **Kopfhörer** ändern.

Wenn Sie das Gefühl haben, dass die Lautstärke der Lautsprecher zu niedrig ist, können Sie :ref:`adjust_volume`.

**Beispiel**

* :ref:`3.1.3_py` (Python-Projekt)
* :ref:`3.1.4_py` (Python-Projekt)
* :ref:`4.1.2_py` (Python-Projekt)
* :ref:`4.1.3_py` (Python-Projekt)
* :ref:`4.1.5_py` (Python-Projekt)
* :ref:`1.8_scratch` (Scratch-Projekt)
* :ref:`1.9_scratch` (Scratch-Projekt)
* :ref:`1.10_scratch` (Scratch-Projekt)

