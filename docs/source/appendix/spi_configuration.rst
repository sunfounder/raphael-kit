.. _spi_configuration:

Configuration SPI
-----------------------

#. Activez l’interface SPI sur votre Raspberry Pi. Si elle est déjà activée, vous pouvez ignorer cette étape. Si vous n’êtes pas sûr, suivez les instructions ci‑dessous.

   * Ouvrez l’outil de configuration du Raspberry Pi :

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         sudo raspi-config

   * **3 Options d’interfaçage**

     .. image:: img/image282.png
        :align: center

   * **I3 SPI**

     .. image:: img/i3spi.png
        :align: center
     
   * **<OUI>, puis cliquez sur <OK> et <Finish>.**

     .. image:: img/image286.png
        :align: center 

#. Vérifiez que les modules SPI sont actifs.

   * Exécutez la commande suivante :

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         ls /dev/sp*

   * Vous devriez obtenir un résultat similaire :

     .. code-block:: 
     
         /dev/spidev0.0  /dev/spidev0.1

   Si ces périphériques apparaissent, l’interface SPI est active et prête à l’emploi.

#. Installez la bibliothèque Python ``spidev``.

   * Exécutez la commande suivante pour l’installer via ``pip`` :

     .. raw:: html
     
        <run></run>
     
     .. code-block:: 
     
         sudo pip3 install spidev
     
   Cette bibliothèque fournit l’interface Python pour communiquer avec les périphériques SPI via /dev/spidevX.Y.
