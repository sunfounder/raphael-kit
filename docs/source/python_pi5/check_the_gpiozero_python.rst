.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci il mondo di Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto tecnico esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a giveaway e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Verifica ``GPIO Zero``
=================================

Se sei un utente Python su Raspberry Pi 5, puoi programmare i GPIO 
utilizzando le API fornite da ``GPIO Zero``.

``GPIO Zero`` è un modulo per il controllo dei pin GPIO di Raspberry Pi. Questo 
pacchetto offre una gamma di classi e funzioni facili da usare per gestire i GPIO 
su un Raspberry Pi. Per esempi e documentazione, visita: https://gpiozero.readthedocs.io/en/latest/.

Per verificare se GPIO Zero è installato o meno, digita in python:

.. raw:: html

   <run></run>

.. code-block::

    python

.. image:: ../python_pi5/img/zero_01.png
    :width: 100%


Nella CLI di Python, inserisci ``import gpiozero``. Se non viene visualizzato alcun errore, significa che GPIO Zero è installato.

.. raw:: html

   <run></run>

.. code-block::

    import gpiozero

.. image:: ../python_pi5/img/zero_02.png
    :width: 100%


Se vuoi uscire dalla CLI di Python, digita:

.. raw:: html

   <run></run>

.. code-block::

    exit()

.. image:: ../python_pi5/img/zero_03.png
    :width: 100%


