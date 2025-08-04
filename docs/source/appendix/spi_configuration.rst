.. note::

    Ciao, benvenuto nella community SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci dei nuovi prodotti e alle anticipazioni.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa agli omaggi e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _spi_configuration:

Configurazione SPI
-----------------------

#. Abilita l'interfaccia SPI sul tuo Raspberry Pi. Se l'hai già abilitata, puoi saltare questo passaggio. Se non sei sicuro, segui le istruzioni riportate di seguito.

   * Apri lo strumento di configurazione di Raspberry Pi:

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         sudo raspi-config

   * **3 Opzioni di interfacciamento**

     .. image:: img/image282.png
        :align: center

   * **I3 SPI**

     .. image:: img/i3spi.png
        :align: center
     
   * **<SÌ>, quindi fare clic su <OK> e <Finish>.**

     .. image:: img/image286.png
        :align: center 

#. Verifica che i moduli SPI siano attivi.

   * Esegui il seguente comando:

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         ls /dev/sp*

   * Dovresti vedere un output simile a:


     .. code-block:: 
     
         /dev/spidev0.0  /dev/spidev0.1

   Se questi dispositivi compaiono, l'interfaccia SPI è attiva e pronta.

#. Installa la libreria Python ``spidev``.

   * Esegui il seguente comando per installarla usando ``pip``:

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         sudo pip3 install spidev
     
   Questa libreria fornisce l'interfaccia Python per comunicare con i dispositivi SPI utilizzando /dev/spidevX.Y.
