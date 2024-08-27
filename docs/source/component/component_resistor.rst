.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima a nuovi annunci di prodotti e anticipazioni.
    - **Sconti speciali**: Godi di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e omaggi**: Partecipa a omaggi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!

.. _cpn_resistor:

Resistore
============

.. image:: img/resistor.png
    :width: 300

Il resistore è un elemento elettronico che può limitare la corrente in un ramo del circuito. 
Un resistore fisso è un tipo di resistore la cui resistenza non può essere modificata, mentre quella di un potenziometro o di un resistore variabile può essere regolata.

Ecco due simboli circuitali comunemente usati per rappresentare il resistore. Di solito, il valore della resistenza è indicato direttamente sul componente. Quindi, se vedi questi simboli in un circuito, rappresentano un resistore.

.. image:: img/resistor_symbol.png
    :width: 400

**Ω** è l'unità di resistenza e le unità più grandi includono KΩ, MΩ, ecc. 
La loro relazione può essere rappresentata così: 1 MΩ = 1000 KΩ, 1 KΩ = 1000 Ω. Di solito, il valore della resistenza è indicato sul resistore.

Quando si utilizza un resistore, è necessario conoscerne prima il valore di resistenza. Ecco due metodi: puoi osservare le bande colorate sul resistore oppure utilizzare un multimetro per misurare la resistenza. Si consiglia di usare il primo metodo, poiché è più conveniente e veloce.

.. image:: img/resistance_card.jpg

Come mostrato nella scheda, ogni colore rappresenta un numero.

.. list-table::

   * - Nero
     - Marrone
     - Rosso
     - Arancione
     - Giallo
     - Verde
     - Blu
     - Viola
     - Grigio
     - Bianco
     - Oro
     - Argento
   * - 0
     - 1
     - 2
     - 3
     - 4
     - 5
     - 6
     - 7
     - 8
     - 9
     - 0,1
     - 0,01

I resistori a 4 e 5 bande sono i più usati e presentano rispettivamente 4 e 5 bande cromatiche.

Di solito, quando ricevi un resistore, potresti trovare difficile capire da quale estremità iniziare a leggere i colori. 
Il suggerimento è che il divario tra la quarta e la quinta banda sarà relativamente più grande.

Pertanto, puoi osservare lo spazio tra le due bande cromatiche a un'estremità del resistore; 
se è più ampio rispetto agli altri spazi tra le bande, allora puoi iniziare a leggere dal lato opposto.

Vediamo come leggere il valore di resistenza di un resistore a 5 bande come mostrato di seguito.

.. image:: img/220ohm.jpg
    :width: 500

Per questo resistore, il valore della resistenza dovrebbe essere letto da sinistra a destra.
Il valore dovrebbe essere nel seguente formato: 1a Banda 2a Banda 3a Banda x 10^Moltiplicatore (Ω) e l'errore consentito è ±Tolleranza%. 
Quindi il valore di resistenza di questo resistore è 2(rosso) 2(rosso) 0(nero) x 10^0(nero) Ω = 220 Ω, 
e l'errore consentito è ± 1% (marrone).

.. list-table:: Bande di colore comuni dei resistori
    :header-rows: 1

    * - Resistore
      - Bande di Colore
    * - 10Ω   
      - marrone nero nero argento marrone
    * - 100Ω   
      - marrone nero nero nero marrone
    * - 220Ω 
      - rosso rosso nero nero marrone
    * - 330Ω 
      - arancione arancione nero nero marrone
    * - 1kΩ 
      - marrone nero nero marrone marrone
    * - 2kΩ 
      - rosso nero nero marrone marrone
    * - 5.1kΩ 
      - verde marrone nero marrone marrone
    * - 10kΩ 
      - marrone nero nero rosso marrone 
    * - 100kΩ 
      - marrone nero nero arancione marrone 
    * - 1MΩ 
      - marrone nero nero verde marrone 


Puoi saperne di più sui resistori su Wiki: `Resistore - Wikipedia <https://en.wikipedia.org/wiki/Resistor>`_.

