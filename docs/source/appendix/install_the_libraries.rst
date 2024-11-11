.. note::

    Ciao, benvenuto nella community SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 con altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anticipo a nuovi annunci di prodotti e anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni festive.

    👉 Pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_the_libraries:

Installa le librerie
============================

Per utenti C
---------------

BCM2835
~~~~~~~~~~~~~~~
Questa è una libreria C per Raspberry Pi (RPi). Fornisce l'accesso ai GPIO e ad altre funzioni IO sul chip Broadcom BCM 2835, utilizzato nel Raspberry Pi, consentendo l'accesso ai pin GPIO sul connettore a 26 pin della scheda RPi, permettendo il controllo e l'interfacciamento con vari dispositivi esterni.

Fornisce funzioni per leggere ingressi digitali, impostare uscite digitali, utilizzare SPI e I2C e accedere ai timer di sistema. Il rilevamento di eventi sui pin è supportato tramite polling (non sono supportate le interruzioni).

Funziona su tutte le versioni fino a RPI 4 e supporta tutte le versioni di Debian fino a Debian Buster 10.

Apri un terminale e scarica la libreria ``bcm2835`` nel percorso ``~``.

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~
    wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.69.tar.gz

Estrai il pacchetto.

.. raw:: html

   <run></run>

.. code-block:: 

    tar zxvf bcm2835-1.69.tar.gz

Installa la libreria BCM2835 con i seguenti comandi.

.. raw:: html

   <run></run>

.. code-block:: 

    cd bcm2835-1.69
    ./configure
    make
    sudo make check
    sudo make install

* Riferimento: `bcm2835 <http://www.airspayce.com/mikem/bcm2835/>`_  


Per utenti Python
----------------------

.. _create_virtual:

Creazione di un ambiente virtuale
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quando si utilizza Raspberry Pi o dispositivi simili, si consiglia di installare i pacchetti con ``pip`` in un ambiente virtuale. Questo offre isolamento delle dipendenze, aumenta la sicurezza del sistema, mantiene il sistema pulito e facilita la migrazione e la condivisione dei progetti, semplificando la gestione delle dipendenze. Questi vantaggi rendono gli ambienti virtuali uno strumento estremamente importante e utile nello sviluppo Python.

Di seguito i passaggi per creare un ambiente virtuale:

**1. Creazione di un ambiente virtuale**

Innanzitutto, è necessario assicurarsi che il sistema abbia Python installato. Python versione 3.3 e successive includono il modulo ``venv`` per creare ambienti virtuali, eliminando la necessità di installazioni separate. Se stai usando Python 2 o una versione precedente a Python 3.3, dovrai installare ``virtualenv``.

* Per Python 3:

Python 3.3 e versioni successive possono utilizzare direttamente il modulo ``venv``:

.. raw:: html

    <run></run>

.. code-block:: shell

    python3 -m venv myenv

Questo creerà un ambiente virtuale chiamato ``myenv`` nella directory corrente.

* Per Python 2:

Se stai ancora usando Python 2, devi prima installare ``virtualenv``:

.. raw:: html

    <run></run>

.. code-block:: shell

    pip install virtualenv

Quindi, crea un ambiente virtuale:

.. raw:: html

    <run></run>

.. code-block:: shell

    virtualenv myenv

Anche questo creerà un ambiente virtuale chiamato ``myenv`` nella directory corrente.

**2. Attivazione dell'ambiente virtuale**

Dopo aver creato l'ambiente virtuale, è necessario attivarlo per utilizzarlo.

.. note::

    Ogni volta che riavvii il Raspberry Pi o apri un nuovo terminale, dovrai eseguire nuovamente il seguente comando per attivare l'ambiente virtuale.

.. raw:: html

    <run></run>

.. code-block:: shell

    source myenv/bin/activate

Una volta attivato l'ambiente virtuale, vedrai il nome dell'ambiente prima del prompt della riga di comando, indicando che stai lavorando all'interno dell'ambiente virtuale.

**3. Uscita dall'ambiente virtuale**

Quando hai completato il tuo lavoro e desideri uscire dall'ambiente virtuale, esegui semplicemente:

.. raw:: html

    <run></run>

.. code-block:: shell

    deactivate

Questo ti riporterà all'ambiente Python globale del sistema.

**4. Eliminazione dell'ambiente virtuale**

Se non hai più bisogno di un particolare ambiente virtuale, puoi semplicemente eliminare la directory che contiene l'ambiente virtuale:

.. raw:: html

    <run></run>

.. code-block:: shell

    rm -rf myenv


Luma.LED_Matrix
~~~~~~~~~~~~~~~~~~~~~~~

Questa è una libreria Python 3 per interfacciare display a matrice LED utilizzando il driver MAX7219 (tramite SPI), WS2812 (NeoPixels, inclusi Pimoroni Unicorn pHat/Hat e Unicorn Hat HD) e APA102 (DotStar) su Raspberry Pi e altri computer a scheda singola basati su Linux.

#. Aggiungi l'utente ai gruppi ``spi`` e ``gpio`` per garantire che l'utente corrente (sostituisci "pi" con il tuo nome utente) abbia il permesso di accedere alle interfacce SPI e GPIO.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell

        sudo usermod -a -G spi,gpio pi

   Dopo aver eseguito questo comando, è consigliato riavviare il sistema o disconnettersi e riconnettersi per applicare le modifiche di gruppo.

#. Installa le dipendenze necessarie: usa ``apt`` per installare strumenti di sviluppo e librerie correlate. Queste librerie sono essenziali per compilare e installare determinati pacchetti Python.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
    
        sudo apt update
        sudo apt install -y build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff-dev

#. Crea un ambiente virtuale. Qui, ``~/my_env`` è il percorso per l'ambiente virtuale, ma può essere personalizzato.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       python3 -m venv ~/my_env

#. Dopo aver creato l'ambiente virtuale, attivalo per l'uso.

   .. note::
   
       Ogni volta che riavvii il Raspberry Pi o apri un nuovo terminale, dovrai eseguire nuovamente il seguente comando per attivare l'ambiente virtuale.

   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       source ~/my_env/bin/activate
   
   Una volta attivato l'ambiente virtuale, vedrai il nome dell'ambiente prima del prompt dei comandi, indicando che stai lavorando all'interno dell'ambiente virtuale.

#. All'interno dell'ambiente virtuale, aggiorna ``pip`` e ``setuptools`` per assicurarti che le versioni più recenti dei pacchetti siano installate.
   
   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell

        pip install --upgrade pip setuptools

#. Quindi, installa ``luma.led_matrix``:
   
   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell
   
        pip install luma.led_matrix

#. Dopo l'installazione, puoi verificare che ``luma.led_matrix`` sia installato correttamente eseguendo il seguente comando. Se l'installazione è corretta, verrà visualizzato il numero di versione di ``luma.led_matrix``.
   
   .. raw:: html
   
      <run></run>
   
   .. code-block:: shell

        python3 -c "import luma.led_matrix; print(luma.led_matrix.__version__)"

#. Quando hai finito di lavorare e desideri uscire dall'ambiente virtuale, esegui semplicemente:
   
   .. raw:: html
   
       <run></run>
   
   .. code-block:: shell
   
       deactivate


* Riferimento: `Luma.LED_Matrix <https://luma-led-matrix.readthedocs.io/en/latest/install.html>`_

Spidev e MFRC522
~~~~~~~~~~~~~~~~~~~~~~~~~~~

La libreria ``spidev`` aiuta a gestire le interazioni con l'interfaccia SPI ed è un componente chiave in questo tutorial poiché è necessaria affinché il Raspberry Pi possa interagire con il modulo RFID RC522.

Esegui il seguente comando per installare ``spidev`` sul tuo Raspberry Pi tramite ``pip``.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install spidev


Continua installando la libreria MFRC522.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo pip3 install mfrc522

La libreria MFRC522 contiene due file: ``MFRC522.py`` e ``SimpleMFRC522.py``.

Tra questi, ``MFRC522.py`` è l'implementazione dell'interfaccia RFID RC522; questa libreria gestisce tutto il lavoro di comunicazione con RFID tramite l'interfaccia SPI del Raspberry Pi.

``SimpleMFRC522.py`` semplifica notevolmente ``MFRC522.py``, consentendo di gestire solo poche funzioni invece che molte.
