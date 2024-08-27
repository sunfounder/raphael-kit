.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_transistor:

Transistor
============

.. image:: img/npn_pnp.png
    :width: 300

Il transistor è un dispositivo a semiconduttore che controlla la corrente tramite corrente. Funziona amplificando un segnale debole in un segnale di ampiezza maggiore ed è utilizzato anche come interruttore senza contatto.

Un transistor è una struttura a tre strati composta da semiconduttori di tipo P e tipo N. Essi formano tre regioni internamente. La più sottile, al centro, è la regione di base; le altre due sono entrambe di tipo N o tipo P – la regione più piccola, con una maggiore concentrazione di portatori di maggioranza, è la regione emettitore, mentre l'altra è la regione collettore. Questa composizione permette al transistor di funzionare come amplificatore. Da queste tre regioni derivano rispettivamente tre terminali: base (b), emettitore (e) e collettore (c). Formano due giunzioni P-N, la giunzione dell'emettitore e quella del collettore. La direzione della freccia nel simbolo del circuito del transistor indica quella della giunzione emettitore.

* `P–N junction - Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_

In base al tipo di semiconduttore, i transistor possono essere suddivisi in due gruppi: NPN e PNP. Come si può dedurre dall'abbreviazione, il primo è composto da due semiconduttori di tipo N e uno di tipo P, mentre il secondo è l'opposto. Vedi la figura seguente.

.. note::
    Il s8550 è un transistor PNP e il s8050 è di tipo NPN. Sembrano molto simili, quindi bisogna fare attenzione a leggere le loro etichette.

.. image:: img/transistor_symbol.png
    :width: 600

Quando un segnale di alto livello passa attraverso un transistor NPN, esso si attiva. Ma un transistor PNP richiede un segnale di basso livello per funzionare. Entrambi i tipi di transistor sono frequentemente utilizzati per interruttori senza contatto, come in questo esperimento.

Posiziona il lato con l'etichetta verso di te e i pin rivolti verso il basso. I pin, da sinistra a destra, sono: emettitore (e), base (b) e collettore (c).

.. image:: img/ebc.png
    :width: 150

* `S8050 Transistor Datasheet <https://datasheet4u.com/datasheet-pdf/WeitronTechnology/S8050/pdf.php?id=576670>`_
* `S8550 Transistor Datasheet <https://www.mouser.com/datasheet/2/149/SS8550-118608.pdf>`_

**Esempi**

* :ref:`1.2.1_c` (C Project)
* :ref:`1.3.3_c` (C Project)
* :ref:`1.2.2_py` (Python Project)
* :ref:`1.3.3_py` (Python Project)
* :ref:`1.14_scratch` (Scratch Project)
