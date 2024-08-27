.. note::

    Ciao, benvenuto nella comunità SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anticipo agli annunci di nuovi prodotti e anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a promozioni festive e omaggi.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _filezilla:

Software Filezilla
==========================

.. image:: img/filezilla_icon.png

Il File Transfer Protocol (FTP) è un protocollo di comunicazione standard utilizzato per il trasferimento di file da un server a un client su una rete informatica.

Filezilla è un software open source che supporta non solo FTP, ma anche FTP over TLS (FTPS) e SFTP. Possiamo utilizzare Filezilla per caricare file locali (come immagini e audio, ecc.) su Raspberry Pi, o scaricare file da Raspberry Pi al locale.

**Passo 1**: Scarica Filezilla.

Scarica il client dal `Filezilla’s official website <https://filezilla-project.org/>`_, Filezilla has a very good tutorial, please refer to: `Documentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_. Filezilla offre un ottimo tutorial, consulta: `Documentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_.

**Passo 2**: Connetti a Raspberry Pi

Dopo una rapida installazione, aprilo e `connect it to an FTP server <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Ci sono 3 modi per connettersi; qui utilizziamo la barra di **Connessione Rapida**. Inserisci **hostname/IP**, **username**, **password** e **porta (22)**, poi clicca su **Connessione Rapida** o premi **Invio** per connetterti al server.

.. image:: img/filezilla_connect.png

.. note::

    La Connessione Rapida è un buon modo per testare le tue informazioni di login. Se vuoi creare una voce permanente, puoi selezionare **File** -> **Copia connessione attuale al Gestore Siti** dopo una connessione rapida riuscita, inserisci il nome e clicca **OK**. La prossima volta potrai connetterti selezionando il sito salvato all'interno di **File** -> **Gestore Siti**.
    
    .. image:: img/ftp_site.png

**Passo 3**: Carica/scarica file.

Puoi caricare file locali su Raspberry Pi trascinandoli e rilasciandoli, o scaricare i file all'interno di Raspberry Pi
sul tuo computer.

.. image:: img/upload_ftp.png

