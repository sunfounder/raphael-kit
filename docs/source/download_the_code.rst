.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!


Scaricare il codice
=================================

Tutti i programmi di esempio utilizzati in questo kit sono archiviati nel nostro repository ufficiale su GitHub.  
Usa il seguente comando per scaricare il progetto completo sul tuo Raspberry Pi.

Clonare il repository
----------------------------------

#. Accedi al tuo Raspberry Pi ed esegui:

   .. raw:: html
   
       <run></run>
   
   .. code-block:: bash
   
      cd ~/
      git clone https://github.com/sunfounder/raphael-kit.git --depth 1

#. Entra nella directory del progetto:

   .. raw:: html
   
       <run></run>
   
   .. code-block:: bash
   
      cd ~/raphael-kit/

#. Elenca i file:

   .. raw:: html
   
       <run></run>
   
   .. code-block:: bash
   
      ls

#. Vedrai una struttura simile a questa:

   .. code-block:: text
   
      raphael-kit/
      ├── c/
      ├── iot/
      ├── music/
      ├── nodejs/
      ├── python-pi5/
      ├── python/
      ├── scratch/
      └── README.md


Panoramica della struttura del progetto
---------------------------------------

Ecco una breve introduzione a ciascuna cartella:

* **c/**  

  Esempi e librerie in linguaggio C per gli utenti che preferiscono programmare in C su Raspberry Pi.

* **iot/**  

  Esempi relativi all’IoT, inclusa la connettività con la piattaforma Blynk, dimostrazioni di sensori e moduli di comunicazione.

* **music/** 

  Contiene risorse audio come ``doorbell.wav`` e ``my_music.mp3`` utilizzate nei progetti successivi.

* **nodejs/**

  Esempi Node.js per utenti che sviluppano progetti basati su JavaScript su Raspberry Pi.

* **python/**  

  Programmi di esempio in Python scritti utilizzando la libreria ``RPi.GPIO``, adatti alla maggior parte delle schede Raspberry Pi.

* **python-pi5/**  

  Esempi Python scritti utilizzando la libreria ``GPIO Zero``, specificamente ottimizzati per **Raspberry Pi 5**.

* **scratch/** 

  Esempi di programmazione Scratch progettati per principianti che imparano la programmazione grafica.

* **README.md**  

  Informazioni di base sul repository e istruzioni generali.

Ora puoi entrare nella cartella corrispondente al linguaggio di programmazione o al tipo di progetto che preferisci e iniziare a eseguire gli esempi.
