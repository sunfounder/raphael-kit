.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_resistor:

Widerstand
==========

.. image:: img/resistor.png
    :width: 300

Ein Widerstand ist ein elektronisches Element, das den Strom in einem Zweig begrenzen kann.
Ein fester Widerstand ist eine Art von Widerstand, dessen Widerstandswert nicht verändert werden kann, wohingegen der Widerstand eines Potentiometers oder eines variablen Widerstands verstellbar ist.

Es gibt zwei häufig verwendete Schaltsymbole für Widerstände. Normalerweise ist der Widerstand darauf gekennzeichnet. Wenn Sie diese Symbole in einer Schaltung sehen, steht dies für einen Widerstand.

.. image:: img/resistor_symbol.png
    :width: 400

**Ω** ist die Einheit des Widerstands und größere Einheiten sind KΩ, MΩ usw.
Ihre Beziehung ist wie folgt: 1 MΩ = 1000 KΩ, 1 KΩ = 1000 Ω. Normalerweise ist der Widerstandswert darauf gekennzeichnet.

Bevor man einen Widerstand verwendet, sollte man seinen Widerstandswert kennen. Hier sind zwei Methoden: Sie können die Ringe auf dem Widerstand beobachten oder ein Multimeter verwenden, um den Widerstand zu messen. Es wird empfohlen, die erste Methode zu verwenden, da sie bequemer und schneller ist.

.. image:: img/resistance_card.jpg

Wie auf der Karte dargestellt, steht jede Farbe für eine Zahl.

.. list-table::

   * - Schwarz
     - Braun
     - Rot
     - Orange
     - Gelb
     - Grün
     - Blau
     - Violett
     - Grau
     - Weiß
     - Gold
     - Silber
   * - 0
     - 1
     - 2
     - 3
     - 4
     - 5
     - 6
     - 7
     - 8
     - 9
     - 0,1
     - 0,01

4- und 5-Ring-Widerstände sind häufig verwendet. An ihnen sind 4 bzw. 5 farbige Ringe.

Normalerweise, wenn Sie einen Widerstand erhalten, könnte es schwierig sein, zu entscheiden, von welchem Ende aus man die Farben lesen sollte.
Ein Tipp ist, dass der Abstand zwischen dem 4. und 5. Ring vergleichsweise größer sein wird.

Daher können Sie die Lücke zwischen den zwei farbigen Ringen an einem Ende des Widerstands beobachten; 
wenn diese Lücke größer ist als die anderen, sollten Sie von der gegenüberliegenden Seite lesen.

Sehen Sie sich an, wie man den Widerstandswert eines 5-Ring-Widerstands wie unten gezeigt abliest.

.. image:: img/220ohm.jpg
    :width: 500

Für diesen Widerstand sollte der Widerstand von links nach rechts gelesen werden.
Der Wert sollte im folgenden Format sein: 1. Ring 2. Ring 3. Ring x 10^Multiplikator (Ω) und der zulässige Fehler ist ±Toleranz%. 
Der Widerstandswert dieses Widerstands beträgt also 2(rot) 2(rot) 0(schwarz) x 10^0(schwarz) Ω = 220 Ω, 
und der zulässige Fehler ist ± 1% (braun).

.. list-table:: Übliche Widerstandsfarbringe
    :header-rows: 1

    * - Widerstand 
      - Farbringe  
    * - 10Ω   
      - braun schwarz schwarz silber braun
    * - 100Ω   
      - braun schwarz schwarz schwarz braun
    * - 220Ω 
      - rot rot schwarz schwarz braun
    * - 330Ω 
      - orange orange schwarz schwarz braun
    * - 1kΩ 
      - braun schwarz schwarz braun braun
    * - 2kΩ 
      - rot schwarz schwarz braun braun
    * - 5.1kΩ 
      - grün braun schwarz braun braun
    * - 10kΩ 
      - braun schwarz schwarz rot braun 
    * - 100kΩ 
      - braun schwarz schwarz orange braun 
    * - 1MΩ 
      - braun schwarz schwarz grün braun 

Weitere Informationen über Widerstände finden Sie bei Wiki: `Widerstand - Wikipedia <https://en.wikipedia.org/wiki/Resistor>`_.
