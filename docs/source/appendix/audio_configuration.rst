.. note::

    Ciao, benvenuto nella comunità SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anticipo agli annunci di nuovi prodotti e anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a promozioni festive e omaggi.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _audio_configuration:

Configurazione Audio
===========================

.. _change_audio_output:

Modificare l'Uscita Audio
------------------------------

Se il tuo altoparlante non emette suoni, potrebbe essere che il Raspberry Pi abbia selezionato l'uscita audio sbagliata; quella corretta dovrebbe essere **Cuffie**. Puoi modificare l'uscita audio seguendo questi passaggi.

Inserisci il seguente comando.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo raspi-config

Seleziona **1 Opzioni di Sistema**.

.. image:: img/audio1.jpg

Poi **S2 Audio**.

.. image:: img/audio2.jpg

Dopo aver selezionato **1 Cuffie**, premi ``Invio`` per confermare e seleziona ``Finish`` per uscire.

.. image:: img/audio3.jpg

.. _adjust_volume:

Regolare il Volume
-------------------------

Se ritieni che il volume degli altoparlanti sia troppo basso, puoi regolarlo inserendo il seguente comando.

.. raw:: html

   <run></run>

.. code-block:: 

    alsamixer

.. image:: img/faq1.png

La pagina predefinita è mostrata di seguito.

.. image:: img/faq2.png

Premi ``F6`` per selezionare la modalità **Cuffie**.

.. image:: img/faq3.png

Poi premi i tasti freccia su e giù per regolare il livello del volume e premi ``ESC`` per uscire.

.. image:: img/faq4.png
