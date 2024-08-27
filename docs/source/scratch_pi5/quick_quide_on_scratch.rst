.. note::

    Ciao, benvenuto nella Community di appassionati di SunFounder Raspberry Pi, Arduino ed ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e anteprime.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa ai giveaway e alle promozioni festive.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _quick_quide_on_scratch_pi5:

Guida rapida a Scratch
============================

.. note::

    Quando programmi con Scratch 3, potresti aver bisogno di uno schermo per una migliore esperienza, consulta: `Connect your Raspberry Pi <https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/3>`_. Naturalmente, se non hai uno schermo, puoi anche accedere al desktop di Raspberry Pi da remoto; per un tutorial dettagliato, fai riferimento a :ref:`remote_desktop`.

Inoltre, Scratch 3 richiede almeno 1GB di RAM per funzionare, e consigliamo un Raspberry Pi 4 con almeno 2GB di RAM. Anche se puoi eseguire Scratch 3 su un Raspberry Pi 2, 3, 3B+ o un Raspberry Pi 4 con 1GB di RAM, le prestazioni su questi modelli sono ridotte e, a seconda degli altri software in esecuzione contemporaneamente, Scratch 3 potrebbe non avviarsi per mancanza di memoria.

Installare Scratch 3
---------------------------
Durante l'installazione di Raspberry Pi OS (:ref:`install_os`), devi scegliere la versione con desktop, sia con solo desktop o con desktop e software raccomandati.

Se installi la versione con software raccomandati, puoi vedere Scratch 3 nel menu di sistema sotto **Programmazione**.

Se hai installato solo la versione desktop, dovrai installare Scratch 3 manualmente, come descritto di seguito.

Apri il menu, clicca su **Preferenze** -> **Software consigliato**.

.. image:: img/quick_scratch1.png

Trova Scratch 3 e selezionalo, poi clicca su **Applica** e attendi il completamento dell'installazione.

.. image:: img/quick_scratch2.png

Una volta completata l'installazione, dovresti vederlo sotto **Programmazione** nel menu di sistema.

.. image:: img/quick_scratch3.png


Interfaccia di Scratch 3
------------------------------

Scratch 3 è progettato per essere divertente, educativo e facile da imparare. Ha strumenti per creare storie interattive, giochi, arte, simulazioni e altro ancora, utilizzando la programmazione a blocchi. Scratch ha anche un editor di immagini e un editor audio integrati.

La parte superiore di Scratch 3 presenta alcune opzioni di base: la prima da sinistra a destra è l'opzione della lingua, puoi scegliere diverse lingue per programmare. La seconda è l'opzione **File**, dove puoi creare nuovi file, leggere file locali e salvare file correnti. La terza è l'opzione **Modifica**, che ti permette di ripristinare alcune operazioni di eliminazione e abilitare la modalità accelerata (in cui il movimento degli sprite diventa particolarmente veloce). La quarta è l'opzione **Tutorials**, che ti permette di visualizzare i tutorial per alcuni progetti. La quinta è l'opzione di denominazione dei file, dove puoi rinominare il progetto.

.. image:: img/quick_scratch13.png

**Codice**

Scratch 3 ha tre sezioni principali: l'area di scena, la palette dei blocchi e l'area di codifica. La programmazione avviene cliccando e trascinando i blocchi dalla palette dei blocchi all'area di codifica; infine, i risultati del tuo codice saranno mostrati nell'area di scena.

.. image:: img/quick_scratch4.png

Questa è l'area degli sprite di Scratch 3. Sopra l'area sono presenti i parametri di base degli sprite. Puoi aggiungere sprite predefiniti o caricare sprite locali.

.. image:: img/quick_scratch5.png

Questa è l'area degli sfondi di Scratch 3, principalmente utilizzata per aggiungere un sfondo adatto alla tua scena; puoi aggiungere sfondi predefiniti o caricarne di locali.

.. image:: img/quick_scratch6.png

Questo è il pulsante **Aggiungi Estensione**.

.. image:: img/quick_scratch7.png

In Scratch 3, possiamo aggiungere tutti i tipi di estensioni utili; qui prendiamo **Video Sensing** come esempio e ci clicchiamo sopra.

.. image:: img/quick_scratch8.png

Vedrai l'estensione nella palette dei blocchi e potrai usare le funzioni associate a questa estensione. Se hai una fotocamera collegata, vedrai lo schermo della fotocamera nell'area di scena.

.. image:: img/quick_scratch9.png

**Costumi**

Clicca sull'opzione **Costumi** in alto a sinistra per entrare nella palette dei costumi. Costumi diversi permettono agli sprite di avere diversi movimenti statici, e quando questi movimenti statici vengono messi insieme, formano un movimento dinamico coerente.

.. image:: img/quick_scratch10.png

**Suoni**

Potresti aver bisogno di usare alcuni clip musicali per rendere i tuoi esperimenti più interessanti. Clicca sull'opzione **Suoni** in alto a sinistra e puoi modificare il suono corrente o selezionare/caricare un nuovo suono.

.. image:: img/quick_scratch11.png
