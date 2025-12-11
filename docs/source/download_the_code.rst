.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!


Code herunterladen
======================

Alle Beispielprogramme, die in diesem Kit verwendet werden, befinden sich in unserem offiziellen GitHub-Repository.  
Mit dem folgenden Befehl laden Sie das gesamte Projekt auf Ihren Raspberry Pi herunter.

Repository klonen
--------------------

#. Melden Sie sich auf Ihrem Raspberry Pi an und führen Sie aus:

   .. raw:: html
   
       <run></run>
   
   .. code-block:: bash
   
      cd ~/
      git clone https://github.com/sunfounder/raphael-kit.git --depth 1

#. Wechseln Sie in das Projektverzeichnis:

   .. raw:: html
   
       <run></run>
   
   .. code-block:: bash
   
      cd ~/raphael-kit/

#. Dateien auflisten:

   .. raw:: html
   
       <run></run>
   
   .. code-block:: bash
   
      ls

#. Sie sehen eine ähnliche Struktur wie diese:

   .. code-block:: text
   
      raphael-kit/
      ├── c/
      ├── iot/
      ├── music/
      ├── nodejs/
      ├── python-pi5/
      ├── python/
      ├── scratch/
      └── README.md


Projektstruktur – Übersicht
----------------------------

Hier finden Sie eine kurze Einführung zu jedem Ordner:

* **c/**  
  C-Beispiele und Bibliotheken für Nutzer, die lieber in C auf dem Raspberry Pi programmieren.

* **iot/**  
  IoT-bezogene Beispiele, einschließlich Blynk-Anbindung, Sensordemos und Kommunikationsmodule.

* **music/** 
  Enthält Audiodateien wie ``doorbell.wav`` und ``my_music.mp3``, die in späteren Projekten verwendet werden.

* **nodejs/**  
  Node.js-Beispiele für Anwender, die JavaScript-basierte Projekte auf dem Raspberry Pi entwickeln.

* **python/**  
  Python-Beispiele, die die ``RPi.GPIO``-Bibliothek verwenden, geeignet für die meisten Raspberry-Pi-Modelle.

* **python-pi5/**  
  Python-Beispiele mit der ``GPIO Zero``-Bibliothek, speziell optimiert für den **Raspberry Pi 5**.

* **scratch/**  
  Scratch-Beispiele für Anfänger, die grafische Programmierung lernen.

* **README.md**  
  Grundinformationen über das Repository und allgemeine Hinweise.

Sie können nun in den Ordner wechseln, der Ihrer bevorzugten Programmiersprache oder Projektart entspricht, und mit dem Ausführen der Beispiele beginnen.
