.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_74hc595:

74HC595
===========

.. image:: img/74HC595.png

El 74HC595 consiste en un registro de desplazamiento de 8 bits y un registro de almacenamiento con salidas paralelas de tres estados. Convierte la entrada en serie en salida paralela para que puedas ahorrar puertos IO de un MCU.
Cuando MR (pin10) está en alto nivel y OE (pin13) está en bajo nivel, los datos se ingresan en el borde ascendente de SHcp y pasan al registro de memoria a través del borde ascendente de SHcp. Si los dos relojes están conectados, el registro de desplazamiento siempre está un pulso antes que el registro de memoria. Hay un pin de entrada de desplazamiento en serie (Ds), un pin de salida en serie (Q) y un botón de reinicio asíncrono (nivel bajo) en el registro de memoria. El registro de memoria genera un bus con un paralelo de 8 bits y en tres estados. Cuando OE está habilitado (nivel bajo), los datos en el registro de memoria se envían al bus.

* `Hoja de datos del 74HC595 <https://www.ti.com/lit/ds/symlink/cd74hc595.pdf?ts=1617341564801>`_

.. image:: img/74hc595_pin.png
    :width: 600

Pines del 74HC595 y sus funciones:

* **Q0-Q7**: Pines de salida de datos paralelos de 8 bits, capaces de controlar 8 LEDs o 8 pines de una pantalla de 7 segmentos directamente.
* **Q7’**: Pin de salida en serie, conectado a DS de otro 74HC595 para conectar múltiples 74HC595 en serie.
* **MR**: Pin de reinicio, activo en nivel bajo.
* **SHcp**: Entrada de secuencia de tiempo del registro de desplazamiento. En el borde ascendente, los datos en el registro de desplazamiento se mueven sucesivamente un bit, es decir, los datos en Q1 se mueven a Q2, y así sucesivamente. Mientras que en el borde descendente, los datos en el registro de desplazamiento permanecen sin cambios.
* **STcp**: Entrada de secuencia de tiempo del registro de almacenamiento. En el borde ascendente, los datos en el registro de desplazamiento se mueven al registro de memoria.
* **CE**: Pin de habilitación de salida, activo en nivel bajo.
* **DS**: Pin de entrada de datos en serie.
* **VCC**: Voltaje de alimentación positivo.
* **GND**: Tierra.

**Ejemplo**

* :ref:`1.1.4_c` (C Project)
* :ref:`1.1.5_c` (C Project)
* :ref:`3.1.1_c` (C Project)
* :ref:`3.1.6_c` (C Project)
* :ref:`3.1.12_c` (C Project)
* :ref:`1.1.4_py` (Python Project)
* :ref:`1.1.5_py` (Python Project)
* :ref:`4.1.7_py` (Pyhton Project)
* :ref:`4.1.12_py` (Python Project)
* :ref:`4.1.18_py` (Pyhton Project)



