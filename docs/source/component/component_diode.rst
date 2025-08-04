.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti speciali**: Goditi sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a concorsi e promozioni festive.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi!

.. _cpn_diode:

Diodo
=================


Un diodo è un componente elettronico con due elettrodi che consente il passaggio della corrente in una sola direzione, funzione spesso definita come "rettificazione". 
Pertanto, un diodo può essere considerato come una versione elettronica di una valvola di non ritorno.

Grazie alla sua conduttività unidirezionale, il diodo viene utilizzato in quasi tutti i circuiti elettronici di una certa complessità. È uno dei primi dispositivi a semiconduttore ed è ampiamente utilizzato.

In base all'uso, può essere suddiviso in diodi rivelatori, diodi raddrizzatori, diodi limitatori, diodi regolatori di tensione, ecc.

In questo kit sono inclusi diodi raddrizzatori e diodi regolatori di tensione.

**Diodo Raddrizzatore**

.. image:: img/in4007_diode.png
.. image:: img/symbol_rectifier_diode.png
    :width: 200

Un diodo raddrizzatore è un diodo a semiconduttore utilizzato per raddrizzare la corrente alternata (AC) in corrente continua (DC) tramite l'applicazione del ponte raddrizzatore. Nei circuiti elettronici digitali, la barriera Schottky viene spesso preferita al diodo raddrizzatore. Questo tipo di diodo può condurre valori di corrente che variano da mA a diversi kA e tensioni fino a qualche kV.

I diodi raddrizzatori sono progettati con materiale al silicio e sono in grado di condurre elevati valori di corrente elettrica. Sebbene meno noti, vengono ancora utilizzati diodi a semiconduttore a base di Ge o arseniuro di gallio. I diodi Ge presentano una minore tensione inversa consentita e una minore temperatura di giunzione consentita. Il vantaggio del diodo Ge rispetto al diodo Si è una soglia di tensione inferiore in polarizzazione diretta.

* `1N400x general-purpose diode  - Wikipedia <https://en.wikipedia.org/wiki/1N400x_general-purpose_diode>`_


**Diodo Zener**

Un diodo Zener è un tipo speciale di diodo progettato per permettere il passaggio della corrente "all'indietro" quando viene raggiunta una specifica tensione inversa, nota come tensione Zener.

Questo diodo è un dispositivo a semiconduttore che presenta un'elevata resistenza fino al punto di breakdown inverso critico. A questo punto critico di breakdown, la resistenza inversa si riduce drasticamente e la corrente aumenta, mantenendo però la tensione costante in questa regione a bassa resistenza.

.. image:: img/zener_diode.png
.. image:: img/symbol-zener-diode.jpg


* `Zener diode - Wikipedia <https://en.wikipedia.org/wiki/Zener_diode>`_



**Esempio**

* :ref:`1.3.3_c` (C Project)
* :ref:`1.3.3_py` (Python Project)
