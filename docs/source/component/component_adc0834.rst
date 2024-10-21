.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_adc0834:

ADC0834
==============

El ADC0834 es un convertidor analógico a digital de aproximación sucesiva de 8 bits, 
equipado con un multiplexor multicanal configurable de entrada y entrada/salida en serie. 
La entrada/salida en serie está configurada para interactuar con registros de desplazamiento 
estándar o microprocesadores.

.. image:: img/image309.png

**Secuencia de Operación**

Una conversión se inicia configurando CS en bajo, lo que habilita todos los circuitos lógicos. 
CS debe mantenerse en bajo durante todo el proceso de conversión. Luego, se recibe una entrada 
de reloj del procesador. En cada transición de bajo a alto de la entrada de reloj, los datos 
en DI se desplazan al registro de dirección del multiplexor. El primer alto lógico en la entrada 
es el bit de inicio. Una palabra de asignación de 3 a 4 bits sigue al bit de inicio. En cada 
transición de bajo a alto del reloj de entrada, el bit de inicio y la palabra de asignación se 
desplazan a través del registro de desplazamiento. Cuando el bit de inicio se desplaza a la 
ubicación de inicio del registro del multiplexor, se selecciona el canal de entrada y comienza 
la conversión. La salida de estado de SAR (SARS) se pone en alto para indicar que una conversión 
está en progreso, y DI del registro de desplazamiento del multiplexor se deshabilita durante la 
duración de la conversión.

Se inserta automáticamente un intervalo de un período de reloj para permitir que el canal 
multiplexado seleccionado se estabilice. La salida de datos DO sale del estado de alta impedancia 
y proporciona un bajo inicial para este período de reloj de tiempo de estabilización del multiplexor. El comparador SAR compara salidas sucesivas de la escalera resistiva con la señal analógica entrante. La salida del comparador indica si la entrada analógica es mayor o menor que la salida de la escalera resistiva. A medida que avanza la conversión, los datos de conversión se envían simultáneamente desde el pin de salida DO, con el bit más significativo (MSB) primero.

Después de ocho períodos de reloj, la conversión se completa y la salida SARS se pone en bajo. 
Finalmente, se envían los datos con el bit menos significativo primero después de la secuencia de 
datos con el bit más significativo primero.
.. image:: img/image175.png

**Tabla de Lógica de Control de Dirección MUX del ADC0834**

.. image:: img/image176.png

* `Hoja de datos de la serie ADC0831 <https://www.ti.com/lit/ds/symlink/adc0831-n.pdf>`_

**Ejemplo**

* :ref:`2.1.7_c` (C Project)
* :ref:`2.2.1_c` (C Project)
* :ref:`2.2.2_c` (C Project)
* :ref:`3.1.4_c` (C Project)
* :ref:`3.1.5_c` (C Project)
* :ref:`3.1.7_c` (C Project)
* :ref:`2.1.7_py` (Python Project)
* :ref:`2.2.1_py` (Pyhton Project)
* :ref:`2.2.2_py` (Pyhton Project)
* :ref:`4.1.10_py` (Pyhton Project)
* :ref:`4.1.11_py` (Pyhton Project)
* :ref:`4.1.13_py` (Pyhton Project)