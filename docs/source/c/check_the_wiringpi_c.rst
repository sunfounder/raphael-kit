.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Immergiti più a fondo nel mondo di Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirsi a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni festive.

    👉 Sei pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_wiringpi:

Installa e Controlla wiringPi
=======================================

``wiringPi`` è una libreria GPIO in linguaggio C applicata al Raspberry Pi. È conforme a GUN Lv3. Le funzioni di wiringPi
sono simili a quelle del sistema wiring di Arduino, facilitando l'utilizzo di wiringPi per gli utenti già familiari con Arduino.

``wiringPi`` include numerosi comandi GPIO che ti permettono di controllare tutti
i tipi di interfacce su Raspberry Pi. 

Esegui il seguente comando per installare la libreria ``wiringPi``.

.. raw:: html

   <run></run>

.. code-block::

    sudo apt-get update
    git clone https://github.com/WiringPi/WiringPi
    cd WiringPi 
    ./build

Puoi verificare se la libreria wiringPi è stata installata correttamente 
con il seguente comando.

.. raw:: html

   <run></run>

.. code-block::

    gpio -v

.. image:: ../img/image30.png


Controlla i GPIO con il seguente comando:

.. raw:: html

   <run></run>

.. code-block::

    gpio readall

.. image:: ../img/image31.png


Per maggiori dettagli su wiringPi, puoi fare riferimento a `WiringPi <https://github.com/WiringPi/WiringPi>`_.
