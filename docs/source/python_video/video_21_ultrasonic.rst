.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Video 21: Verwendung eines HC-SR04 Ultraschallsensors zur Echolokalisierung
=======================================================================================

Dieses Tutorial zeigt die Erstellung eines Ultraschall-Abstandssensors mit einem Raspberry Pi und dem HC-SR04 Sensor. Es erklärt die Prinzipien der Echolokalisierung, stellt die benötigten Komponenten vor, richtet die Verdrahtung ein und führt durch den Codierungsprozess. Besonderes Augenmerk liegt auf präzisen Zeitabläufen für genaue Distanzmessungen und guten Ingenieurpraktiken.

1. **Echolokalisierung**: Schall zur Erfassung von Objektpositionen, inspiriert von Fledermäusen und Walen.
2. **Komponenten**: Einführung des HC-SR04 Ultraschallsensors und dessen Anschluss an den Raspberry Pi.
3. **Verdrahtung**: Anschließen des HC-SR04 Sensors an die GPIO-Pins des Raspberry Pi.
4. **Codierung**: Python-Code für Ultraschallimpulse, Sensorauslösung und Messung der Echolaufzeit.
5. **Zeitliche Genauigkeit**: Wichtigkeit präziser Zeitabläufe für genaue Distanzmessungen.
6. **Ingenieurpraktiken**: Betonung der Planung und des Verständnisses des Codes vor der Implementierung.
7. **Warten auf Echo**: Nutzung einer While-Schleife, um das Echo des Sensors abzuwarten.
8. **Startzeit erfassen**: Markierung des Messstarts durch Erfassen der Systemzeit beim Echo.
9. **Ping-Laufzeit messen**: Berechnung der Ping-Laufzeit aus der Zeitdifferenz zwischen Echo-Hoch und -Tief.
10. **Einheiten umrechnen**: Multiplikation der Ping-Laufzeit für bessere Lesbarkeit.
11. **Verzögerung**: Einführung einer Pause nach jeder Messung, um Mehrfachechos zu verhindern.
12. **Entfernung berechnen**: Nutzung von Schallgeschwindigkeit und Ping-Laufzeit zur Entfernungsberechnung.


**Video**

.. raw:: html

    <iframe width="100%" 
    style="aspect-ratio: 16/9; max-width: 100%;"
    src="https://www.youtube.com/embed/SoAGLXoQ5XI?si=OPMqLtQ53hKNHs4j" 
    title="YouTube video player" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    allowfullscreen>
    </iframe>
