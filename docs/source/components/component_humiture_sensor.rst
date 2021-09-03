Humiture Sensor Module
=============================

.. image:: img/dht11_pic.png
    :width: 400
    :align: center

The digital temperature and humidity sensor DHT11 is a composite sensor that contains a calibrated digital signal output of temperature and humidity. 
The technology of a dedicated digital modules collection and the temperature and humidity sensing technology are applied to ensure that the product has high reliability and excellent long-term stability.


Only three pins are available for use: VCC, GND, and DATA. 
The communication process begins with the DATA line sending start signals to DHT11, and DHT11 receives the signals and returns an answer signal. 
Then the host receives the answer signal and begins to receive 40-bit humiture data (8-bit humidity integer + 8-bit humidity decimal + 8-bit temperature integer + 8-bit temperature decimal + 8-bit checksum).

.. image:: img/Dht11.png


* `DHT11 Datasheet <https://components101.com/sites/default/files/component_datasheet/DHT11-Temperature-Sensor.pdf>`_

**Example**

* :ref:`2.2.3 DHT-11` (C Project)
* :ref:`2.2.3 DHT-11` (Python Project)