.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_i2c_lcd:

I2C LCD1602
==============

.. image:: img/i2c_lcd1602.png
    :width: 800

* **GND**: Massa
* **VCC**: Alimentazione, 5V.
* **SDA**: Linea dati seriale. Collegare al VCC tramite una resistenza di pull-up.
* **SCL**: Linea dell'orologio seriale. Collegare al VCC tramite una resistenza di pull-up.

Come sappiamo, sebbene gli LCD e altri display migliorino notevolmente l'interazione uomo-macchina, condividono una debolezza comune. Quando vengono collegati a un controller, occupano diversi pin I/O del controller, che potrebbe non avere molte porte disponibili. Ciò limita anche altre funzioni del controller.

Pertanto, l'LCD1602 con un modulo I2C è stato sviluppato per risolvere il problema. Il modulo I2C ha un chip I2C PCF8574 integrato che converte i dati seriali I2C in dati paralleli per il display LCD.

* `PCF8574 Datasheet <https://www.ti.com/lit/ds/symlink/pcf8574.pdf?ts=1627006546204&ref_url=https%253A%252F%252Fwww.google.com%252F>`_

**Indirizzo I2C**

L'indirizzo predefinito è solitamente 0x27, in alcuni casi potrebbe essere 0x3F.

Prendendo come esempio l'indirizzo predefinito 0x27, l'indirizzo del dispositivo può essere modificato cortocircuitando i pad A0/A1/A2; nello stato predefinito, A0/A1/A2 è 1, e se il pad è cortocircuitato, A0/A1/A2 diventa 0.

.. image:: img/i2c_address.jpg
    :width: 600

**Retroilluminazione/Contrasto**

La retroilluminazione può essere attivata tramite un cappuccio a ponticello; scollegare il cappuccio per disabilitare la retroilluminazione. Il potenziometro blu sul retro serve per regolare il contrasto (il rapporto tra la luminosità del bianco più chiaro e il nero più scuro).

.. image:: img/back_lcd1602.jpg

* **Cappuccio di cortocircuito**: La retroilluminazione può essere attivata tramite questo cappuccio, scollegare questo cappuccio per disabilitare la retroilluminazione.
* **Potenziometro**: Serve per regolare il contrasto (la chiarezza del testo visualizzato), che aumenta in senso orario e diminuisce in senso antiorario.


**Esempi**

* :ref:`1.1.7_c` (C Project)
* :ref:`3.1.3_c` (C Project)
* :ref:`3.1.7_c` (C Project)
* :ref:`3.1.8_c` (C Project)
* :ref:`3.1.11_c` (C Project)
* :ref:`1.1.7_py` (Python Project)
* :ref:`4.1.9_py` (Python Project)
* :ref:`4.1.13_py` (Python Project)
* :ref:`4.1.14_py` (Python Project)
* :ref:`4.1.17_py` (Python Project)
