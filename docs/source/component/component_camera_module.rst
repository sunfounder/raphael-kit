.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi!

.. _cpn_camera_module:

Modulo Fotocamera
====================================


**Descrizione**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

Questo è un modulo fotocamera Raspberry Pi da 5MP con sensore OV5647. È plug and play: collega il cavo a nastro incluso alla porta CSI (Camera Serial Interface) sul tuo Raspberry Pi e sei pronto per iniziare.

La scheda è piccola, circa 25mm x 23mm x 9mm, e pesa 3g, il che la rende ideale per applicazioni mobili o altre applicazioni in cui dimensioni e peso sono critici. Il modulo fotocamera ha una risoluzione nativa di 5 megapixel e dispone di un obiettivo a fuoco fisso che cattura immagini statiche a 2592 x 1944 pixel e supporta anche video a 1080p30, 720p60 e 640x480p90.

.. note:: 

   Il modulo è in grado di catturare solo immagini e video, non l'audio.



**Specifiche**

* **Risoluzione immagini statiche**: 2592×1944 
* **Risoluzione video supportata**: 1080p/30 fps, 720p/60fps e 640x480p 60/90 registrazione video 
* **Apertura (F)**: 1.8 
* **Angolo visivo**: 65 gradi 
* **Dimensioni**: 24mmx23.5mmx8mm 
* **Peso**: 3g 
* **Interfaccia**: connettore CSI 
* **Sistema operativo supportato**: Raspberry Pi OS (versione più recente consigliata)



**Assemblaggio del Modulo Fotocamera**
----------------------------------------


Sul modulo fotocamera o sul Raspberry Pi, troverai un connettore di plastica piatto. Estrarre con attenzione l'interruttore di fissaggio nero finché non è parzialmente estratto. Inserire il cavo FFC nel connettore di plastica nella direzione indicata e spingere l'interruttore di fissaggio nuovamente in posizione.

Se il filo FFC è installato correttamente, sarà dritto e non si staccherà tirandolo delicatamente. In caso contrario, reinstallalo nuovamente.


.. image:: img/connect_ffc.png
.. image:: img/1.10_camera.png
   :width: 700

.. warning::

   Non installare la fotocamera con l'alimentazione accesa, potrebbe danneggiare il modulo.

   
**Esempio**

* :ref:`3.1.1_py` (Python Project)
* :ref:`3.1.2_py` (Python Project)
* :ref:`4.1.1_py` (Python Project)
* :ref:`4.1.4_py` (Python Project)
* :ref:`4.1.5_py` (Python Project)
* :ref:`1.10_scratch` (Scratch Project)
* :ref:`1.18_scratch` (Scratch Project)
