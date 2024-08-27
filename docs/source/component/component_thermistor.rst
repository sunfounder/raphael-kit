.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_thermistor:

Termistore
===============

.. image:: img/thermistor.png
    :width: 150
    :align: center

Un termistore è un tipo di resistore la cui resistenza dipende fortemente dalla temperatura, più di quanto accade nei resistori standard. La parola è una combinazione di "thermal" e "resistor". I termistori sono ampiamente utilizzati come limitatori di corrente di spunto, sensori di temperatura (di solito del tipo NTC a coefficiente di temperatura negativo), protettori contro il sovracorrente autoripristinanti e elementi riscaldanti autorregolanti (di solito del tipo PTC a coefficiente di temperatura positivo).

* `Thermistor - Wikipedia <https://en.wikipedia.org/wiki/Thermistor>`_

Ecco il simbolo elettronico del termistore.

.. image:: img/thermistor_symbol.png
    :width: 300
    :align: center

Esistono due tipi fondamentali di termistori:

* Nei termistori NTC, la resistenza diminuisce all'aumentare della temperatura, di solito a causa di un aumento degli elettroni di conduzione provocato dall'agitazione termica. Un NTC è comunemente usato come sensore di temperatura o in serie con un circuito come limitatore di corrente di spunto.
* Nei termistori PTC, la resistenza aumenta all'aumentare della temperatura, di solito a causa di maggiori agitazioni del reticolo termico, in particolare quelle delle impurità e delle imperfezioni. I termistori PTC sono comunemente installati in serie con un circuito e utilizzati per proteggere contro condizioni di sovracorrente, come fusibili ripristinabili.

In questo kit utilizziamo un NTC. Ogni termistore ha una resistenza normale. Qui è di 10k ohm, misurata a 25 gradi Celsius.

Ecco la relazione tra resistenza e temperatura:

    RT = RN * expB(1/TK – 1/TN)   

* **RT** è la resistenza del termistore NTC quando la temperatura è TK.
* **RN** è la resistenza del termistore NTC alla temperatura nominale TN. Qui, il valore numerico di RN è 10k.
* **TK** è una temperatura in Kelvin e l'unità è K. Qui, il valore numerico di TK è 273,15 + gradi Celsius.
* **TN** è una temperatura nominale in Kelvin; anche l'unità è K. Qui, il valore numerico di TN è 273,15 + 25.
* **B(beta)**, la costante del materiale del termistore NTC, è anche chiamata indice di sensibilità termica con un valore numerico di 3950.
* **exp** è l'abbreviazione di esponenziale, e il numero base e è un numero naturale pari a circa 2,7.

Converti questa formula TK = 1/(ln(RT/RN)/B + 1/TN) per ottenere la temperatura in Kelvin; sottraendo 273,15 si ottiene la temperatura in gradi Celsius.

Questa relazione è una formula empirica. È accurata solo quando temperatura e resistenza rientrano nell'intervallo di validità.

**Esempi**

* :ref:`2.2.2_c` (C Project)
* :ref:`3.1.4_c` (C Project)
* :ref:`3.1.7_c` (C Project)
* :ref:`2.2.2_py` (Python Project)
* :ref:`4.1.10_py` (Python Project)
* :ref:`4.1.13_py` (Python Project)
