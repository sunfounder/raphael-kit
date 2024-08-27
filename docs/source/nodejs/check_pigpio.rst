.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto per esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

Verifica pigpio
==================

pigpio è un modulo utilizzato per controllare i canali GPIO del Raspberry Pi. Questo pacchetto fornisce alcuni metodi per gestire i GPIO su Raspberry Pi. Per esempi e documentazione, visita: https://www.npmjs.com/package/pigpio.

Inserisci il seguente comando per installare la libreria pigpio.

.. raw:: html

    <run></run>

.. code-block::

    npm install pigpio

Verifica se la libreria è stata installata correttamente, cambia la directory e accedi a nodejs:

.. raw:: html

    <run></run>

.. code-block::

    cd ~/raphael-kit/nodejs
    nodejs

.. image:: img/pigpio1.png

Poi inserisci require('pigpio'):

.. raw:: html

    <run></run>

.. code-block::

    require('pigpio')

.. image:: img/pigpio2.png   

Se appare la schermata sopra, l'installazione della libreria è avvenuta con successo.

Se desideri uscire dalla CLI di node, premi due volte Ctrl+C.

.. image:: img/pigpio3.png
