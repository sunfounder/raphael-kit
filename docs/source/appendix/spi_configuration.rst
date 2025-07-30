.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _spi_configuration:

SPI Konfiguration
========================


#. Aktivieren Sie die SPI-Schnittstelle auf Ihrem Raspberry Pi.  
   Wenn Sie diese bereits aktiviert haben, können Sie diesen Schritt überspringen.  
   Falls Sie unsicher sind, folgen Sie den untenstehenden Anweisungen.

   * Öffnen Sie das Raspberry Pi-Konfigurationstool:

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         sudo raspi-config

   * **3 Schnittstellenoptionen (Interfacing Options)**

     .. image:: img/image282.png
        :align: center

   * **I3 SPI**

     .. image:: img/i3spi.png
        :align: center
     
   * **<JA>, dann auf <OK> und <Finish> klicken.**

     .. image:: img/image286.png
        :align: center 

#. Überprüfen Sie, ob die SPI-Module aktiv sind.

   * Führen Sie den folgenden Befehl aus:

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         ls /dev/sp*

   * Sie sollten eine ähnliche Ausgabe sehen wie:

     .. code-block:: 
     
         /dev/spidev0.0  /dev/spidev0.1

   Wenn diese Geräte erscheinen, ist die SPI-Schnittstelle aktiv und einsatzbereit.

#. Installieren Sie die ``spidev`` Python-Bibliothek.

   * Führen Sie den folgenden Befehl aus, um sie mit ``pip`` zu installieren:

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         sudo pip3 install spidev
     
   Diese Bibliothek stellt das Python-Interface zur Kommunikation mit SPI-Geräten über /dev/spidevX.Y bereit.
