.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_mfrc522:

Módulo MFRC522
=====================

**RFID**

La identificación por radiofrecuencia (RFID) se refiere a tecnologías que
implican el uso de comunicación inalámbrica entre un objeto (o etiqueta) y un
dispositivo interrogador (o lector) para rastrear e identificar automáticamente
dichos objetos. El rango de transmisión de la etiqueta está limitado a varios metros
del lector. No es necesariamente requerido una línea de visión clara entre el lector y la etiqueta.

La mayoría de las etiquetas contienen al menos un circuito integrado (IC) y una antena.
El microchip almacena información y es responsable de gestionar la comunicación de
radiofrecuencia (RF) con el lector. Las etiquetas pasivas no tienen una fuente de energía independiente
y dependen de una señal electromagnética externa, proporcionada por el lector, para alimentar sus
operaciones. Las etiquetas activas contienen una fuente de energía independiente, como una
batería. Por lo tanto, pueden tener capacidades de procesamiento, transmisión y rango aumentados.

.. image:: img/image230.png


**MFRC522**

El MFRC522 es un tipo de chip integrado de lectura y escritura de tarjetas. Es comúnmente
utilizado en la radio a 13.56MHz. Lanzado por la empresa NXP, es un chip de tarjeta de bajo voltaje, bajo costo y tamaño pequeño, una
mejor opción para instrumentos inteligentes y dispositivos portátiles de mano.

El MFRC522 utiliza un concepto avanzado de modulación y demodulación que
se presenta completamente en todos los tipos de métodos y protocolos de comunicación sin contacto pasiva
a 13.56MHz. Además, soporta el algoritmo de encriptación rápida CRYPTO1 para verificar productos MIFARE. MFRC522 también
soporta la comunicación sin contacto de alta velocidad de la serie MIFARE, con una
tasa de transmisión de datos bidireccional de hasta 424kbit/s. Como nuevo miembro de la serie de lectores de tarjetas
altamente integrados a 13.56MHz, el MFRC522 es muy similar al MFRC500 y MFRC530 existentes, pero también existen grandes
diferencias. Se comunica con la máquina anfitriona a través de un modo serial
que necesita menos cableado. Puedes elegir entre los modos SPI, I2C y UART serial
(similar a RS232), lo que ayuda a reducir la conexión, ahorrar espacio en la placa PCB (tamaño más pequeño) y reducir costos.

**Ejemplo**

* :ref:`2.2.10_c` (C Project)
* :ref:`2.2.10_py` (Python Project)
* :ref:`4.1.19_py` (Python Project)