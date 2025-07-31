.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_mcp3008:

MCP3008
==============

El MCP3008 es un convertidor analógico-digital (ADC) de aproximaciones sucesivas de 10 bits con 8 canales de entrada y un protocolo de comunicación SPI (Interfaz Periférica Serial). Es capaz de interactuar con un microcontrolador para convertir señales de entrada analógicas en datos digitales para su posterior procesamiento.

.. image:: img/MCP3008.jpg
      :width: 40%

**Secuencia de operación**

Una conversión en el MCP3008 comienza configurando el pin CS (chip select) en bajo, lo que activa la comunicación con el dispositivo.  
El microcontrolador envía entonces una secuencia de control de 3 bytes a través de la interfaz SPI para especificar la configuración y seleccionar el canal de entrada.

El primer byte enviado contiene el bit de inicio y el bit de selección de modo simple/diferencial.  
Los siguientes bits indican cuál de los 8 canales (CH0–CH7) se debe leer.  
Los datos se desplazan al dispositivo en cada flanco ascendente del reloj SPI (SCLK), y el resultado de la conversión se devuelve simultáneamente.

Se incluye un pequeño retardo interno para que el canal de entrada seleccionado se estabilice antes de que comience la conversión.  
El MCP3008 realiza entonces una conversión analógica-digital de 10 bits usando un circuito de muestreo y retención (sample-and-hold) y un comparador de registro de aproximaciones sucesivas (SAR).

El resultado de la conversión se transmite de vuelta al microcontrolador a través de la línea MISO (Master In Slave Out).  
El bit más significativo (MSB) del resultado de 10 bits se envía primero, seguido por los bits restantes.  
El microcontrolador lee el resultado a través del bus SPI durante este tiempo.

Después de que el valor digital completo de 10 bits se ha desplazado hacia fuera, el MCP3008 completa el ciclo y espera el siguiente comando.

* `Hoja de datos de la serie MCP3008 <https://www.alldatasheet.com/datasheet-pdf/view/304558/MICROCHIP/MCP3008-ISLASHP.html>`_

.. image:: img/MCP3008detail.png


**Example**

* :ref:`2.1.7_c_mcp3008` (C Project)
* :ref:`2.2.1_c_mcp3008` (C Project)
* :ref:`2.2.2_c_mcp3008` (C Project)
* :ref:`3.1.4_c_mcp3008` (C Project)
* :ref:`3.1.5_c_mcp3008` (C Project)
* :ref:`3.1.7_c_mcp3008` (C Project)
* :ref:`2.1.7_py_mcp3008` (Python Project)
* :ref:`2.2.1_py_mcp3008` (Pyhton Project)
* :ref:`2.2.2_py_mcp3008` (Pyhton Project)
* :ref:`4.1.10_py_mcp3008` (Pyhton Project)
* :ref:`4.1.11_py_mcp3008` (Pyhton Project)
* :ref:`4.1.13_py_mcp3008` (Pyhton Project)