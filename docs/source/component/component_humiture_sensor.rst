.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi!

.. _cpn_humiture_sensor:

Modulo Sensore di Umidità e Temperatura
==========================================================

.. image:: img/dht11_pic.png
    :width: 400
    :align: center

Il sensore digitale di temperatura e umidità DHT11 è un sensore composito che contiene un'uscita di segnale digitale calibrata di temperatura e umidità.
La tecnologia di raccolta dei moduli digitali dedicati e la tecnologia di rilevamento della temperatura e dell'umidità sono applicate per garantire un'elevata affidabilità e un'eccellente stabilità a lungo termine.

Sono disponibili solo tre pin per l'uso: VCC, GND e DATA.
Il processo di comunicazione inizia con la linea DATA che invia segnali di avvio al DHT11, il quale riceve i segnali e restituisce un segnale di risposta.
Quindi l'host riceve il segnale di risposta e inizia a ricevere i dati di umidità e temperatura a 40 bit (8 bit di umidità intera + 8 bit di umidità decimale + 8 bit di temperatura intera + 8 bit di temperatura decimale + 8 bit di checksum).

.. image:: img/Dht11.png


* `DHT11 Datasheet <https://components101.com/sites/default/files/component_datasheet/DHT11-Temperature-Sensor.pdf>`_

**Esempio**


* :ref:`2.2.3_c` (C Project)
* :ref:`2.2.3_py` (Python Project)