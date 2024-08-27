.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi!

.. _cpn_gpio_extension_board:

Scheda di estensione GPIO
=============================

Prima di iniziare a imparare i comandi, è necessario conoscere meglio i pin del 
Raspberry Pi, fondamentali per gli studi successivi.

Possiamo facilmente portare i pin del Raspberry Pi sulla breadboard utilizzando 
la scheda di estensione GPIO, evitando danni ai GPIO causati da frequenti collegamenti 
e scollegamenti. Questa è la nostra scheda di estensione GPIO a 40 pin e il cavo GPIO 
per i modelli Raspberry Pi B+, 2 B, 3 e 4 B.

.. image:: img/image32.png
    :align: center

**Numero di Pin**

I pin del Raspberry Pi hanno tre modi di essere nominati: wiringPi, BCM e Board.

Tra questi metodi di nomenclatura, la scheda di estensione GPIO a 40 pin utilizza il 
metodo BCM. Tuttavia, per alcuni pin speciali, come le porte I2C e SPI, si utilizza il 
nome che essi portano intrinsecamente.

La seguente tabella mostra i metodi di denominazione di WiringPi, Board e il nome 
intrinseco di ogni pin sulla scheda di estensione GPIO. Ad esempio, per il GPIO17, 
il metodo di denominazione Board è 11, il metodo WiringPi è 0, e il nome intrinseco è GPIO0.

.. note::

    1) Nel linguaggio C, si utilizza il metodo di denominazione WiringPi.
    
    2) Nel linguaggio Python, i metodi di denominazione applicati sono **Board** e **BCM**, e la funzione ``GPIO.setmode()`` viene utilizzata per impostarli.

    3) In Scratch 3 e Processing, il metodo di denominazione applicato è **BCM**.

.. image:: img/gpio_board.png  
