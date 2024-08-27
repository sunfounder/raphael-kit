.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_pir:

Modulo Sensore di Movimento PIR
====================================

.. image:: img/pir_pic.png
    :width: 300
    :align: center

Il sensore PIR rileva la radiazione termica infrarossa che può essere utilizzata per rilevare la presenza di organismi che emettono radiazione termica infrarossa.

Il sensore PIR è diviso in due slot collegati a un amplificatore differenziale. Ogni volta che un oggetto stazionario si trova di fronte al sensore, i due slot ricevono la stessa quantità di radiazione e l'uscita è zero. Ogni volta che un oggetto in movimento si trova di fronte al sensore, uno degli slot riceve più radiazione dell'altro, il che fa oscillare l'uscita tra alto e basso. Questa variazione della tensione di uscita è il risultato del rilevamento del movimento.

.. image:: img/PIR_working_principle.jpg
    :width: 800

Dopo che il modulo di rilevamento è stato cablato, c'è un'inizializzazione di un minuto. Durante l'inizializzazione, il modulo emetterà da 0 a 3 volte a intervalli. Successivamente il modulo entrerà in modalità standby. Si prega di mantenere lontana l'interferenza di fonti di luce e altre fonti dalla superficie del modulo per evitare che il segnale interferente causi un'operazione errata. È meglio usare il modulo senza troppo vento, poiché anche il vento può interferire con il sensore.

.. image:: img/pir_back.png
    :width: 600
    :align: center

**Regolazione della Distanza**

Ruotando la manopola del potenziometro di regolazione della distanza in senso orario, l'intervallo di rilevamento aumenta, e l'intervallo massimo di rilevamento è di circa 0-7 metri. Se lo ruoti in senso antiorario, l'intervallo di rilevamento si riduce e l'intervallo minimo di rilevamento è di circa 0-3 metri.

**Regolazione del Ritardo**

Ruotando la manopola del potenziometro di regolazione del ritardo in senso orario, puoi vedere aumentare anche il ritardo di rilevamento. Il ritardo massimo di rilevamento può arrivare fino a 300s. Al contrario, se lo ruoti in senso antiorario, puoi ridurre il ritardo con un minimo di 5s.

**Due Modalità di Trigger**

Scegli modalità diverse utilizzando il cappuccio a ponticello.

* **H**: Modalità di trigger ripetibile, dopo aver rilevato il corpo umano, il modulo emette un livello alto. Durante il periodo di ritardo successivo, se qualcuno entra nell'intervallo di rilevamento, l'uscita continuerà a mantenere il livello alto.

* **L**: Modalità di trigger non ripetibile, emette un livello alto quando rileva il corpo umano. Dopo il ritardo, l'uscita cambierà automaticamente da livello alto a livello basso.

**Esempi**

* :ref:`2.2.7_c` (C Project)
* :ref:`2.2.7_py` (Python Project)
* :ref:`4.1.4_py` (Python Project)
* :ref:`1.5_scratch` (Scratch Project)

