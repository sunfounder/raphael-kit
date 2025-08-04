.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi!

.. _cpn_audio_speaker:

Modulo Audio e Altoparlante
===============================

**Modulo Amplificatore Audio**

.. image:: img/audio_module.jpg
    :width: 500
    :align: center

Il modulo amplificatore audio contiene un chip amplificatore di potenza audio HXJ8002. Questo chip è un amplificatore di potenza a bassa alimentazione, in grado di fornire 3W di potenza audio media per un carico BTL da 3Ω con una bassa distorsione armonica (sotto la soglia del 10% di distorsione a 1KHz) da un'alimentazione di 5V DC. Questo chip può amplificare i segnali audio senza l'uso di condensatori di accoppiamento o di bootstrap.

Il modulo può essere alimentato con una tensione DC da 2,0V fino a 5,5V con una corrente operativa di 10mA (0,6uA come valore tipico in standby) e produrre un suono amplificato potente in un altoparlante con impedenza di 3Ω, 4Ω o 8Ω. Questo modulo è dotato di un circuito migliorato per ridurre significativamente i rumori di accensione e spegnimento. Le dimensioni ridotte, l'elevata efficienza e il basso consumo di energia lo rendono adatto a progetti portatili alimentati a batteria e microcontrollori.

* **IC**: HXJ8002
* **Tensione d'ingresso**: 2V ~ 5.5V
* **Corrente in modalità standby**: 0.6uA (valore tipico)
* **Potenza d'uscita**: 3W (carico 3Ω) , 2.5W (carico 4Ω) , 1.5W (carico 8Ω)
* **Impedenza d'uscita dell'altoparlante**: 3Ω, 4Ω, 8Ω
* **Dimensioni**: 19.8mm x 14.2mm

**Altoparlante**

.. image:: img/speaker_pic.png
    :width: 300
    :align: center

* **Dimensioni**: 20x30x7mm
* **Impedenza**: 8ohm
* **Potenza nominale d'ingresso**: 1.5W 
* **Potenza massima d'ingresso**: 2.0W
* **Lunghezza del cavo**: 10cm

.. image:: img/2030_speaker.png

Il diagramma delle dimensioni è il seguente:

* :download:`2030 Speaker Datasheet <https://github.com/sunfounder/sf-pdf/raw/master/datasheet/2030-speaker-datasheet.pdf>`

**Cavo Audio**

.. image:: img/audio_cable_pic2.png
    :width: 500
    :align: center

Questo è un cavo audio maschio da 3,5mm con una lunghezza totale di 43cm. Ha 3 connettori: rosso per il canale sinistro, bianco per il canale destro e GND al centro.

**Circuito**

.. image:: img/4.1.4fritzing.png

Dopo aver costruito il circuito secondo il diagramma sopra riportato, inserisci il cavo audio nel jack audio da 3,5mm del Raspberry Pi.

.. image:: img/audio4.png
    :width: 400
    :align: center

Se il tuo altoparlante non emette suoni, potrebbe essere perché il Raspberry Pi ha selezionato l'uscita audio sbagliata (il valore predefinito è HDMI), è necessario :ref:`change_audio_output` su **Cuffie**.

Se ritieni che il volume degli altoparlanti sia troppo basso, puoi :ref:`adjust_volume`.


**Esempio**

* :ref:`3.1.3_py` (Python Project)
* :ref:`3.1.4_py` (Python Project)
* :ref:`4.1.2_py` (Python Project)
* :ref:`4.1.3_py` (Python Project)
* :ref:`4.1.5_py` (Python Project)
* :ref:`1.8_scratch` (Scratch Project)
* :ref:`1.9_scratch` (Scratch Project)
* :ref:`1.10_scratch` (Scratch Project)
