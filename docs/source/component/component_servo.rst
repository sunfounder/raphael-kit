.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_servo:

Servo
===========

.. image:: img/servo.png
    :align: center

Un servo è generalmente composto dalle seguenti parti: case, albero, sistema di ingranaggi, potenziometro, motore DC e scheda embedded.

Funziona così: il microcontrollore invia segnali PWM al servo, quindi la scheda embedded nel servo riceve i segnali attraverso il pin di segnale e controlla il motore interno per farlo girare. Di conseguenza, il motore aziona il sistema di ingranaggi e poi motiva l'albero dopo la riduzione della velocità. L'albero e il potenziometro del servo sono collegati insieme. Quando l'albero ruota, aziona il potenziometro, quindi il potenziometro emette un segnale di tensione alla scheda embedded. La scheda determina quindi la direzione e la velocità di rotazione in base alla posizione corrente, in modo che il servo possa fermarsi esattamente nella posizione definita e mantenerla.

.. image:: img/servo_internal.png
    :align: center

L'angolo è determinato dalla durata di un impulso applicato al filo di controllo. Questo è chiamato modulazione della larghezza di impulso (PWM). Il servo si aspetta di vedere un impulso ogni 20 ms. La lunghezza dell'impulso determinerà quanto si gira il motore. Ad esempio, un impulso di 1,5 ms farà girare il motore fino alla posizione di 90 gradi (posizione neutra).
Quando viene inviato un impulso a un servo inferiore a 1,5 ms, il servo ruota in una posizione e mantiene il suo albero di uscita a un numero di gradi in senso antiorario rispetto al punto neutro. Quando l'impulso è più ampio di 1,5 ms, avviene l'opposto. La larghezza minima e la larghezza massima dell'impulso che comanda il servo a girare verso una posizione valida sono funzioni di ciascun servo. Generalmente, l'impulso minimo sarà largo circa 0,5 ms e l'impulso massimo sarà largo 2,5 ms.

.. image:: img/servo_duty.png
    :width: 600
    :align: center

**Esempi**

* :ref:`1.3.2_c` (C Project)
* :ref:`3.1.2_c` (C Project)
* :ref:`1.3.2_py` (Python Project)
* :ref:`4.1.8_py` (Python Project)


