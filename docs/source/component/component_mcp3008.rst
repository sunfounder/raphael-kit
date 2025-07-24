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

MCP3008 is a 10-bit successive approximation analog-to-digital converter (ADC) with 8 input channels and an SPI (Serial Peripheral Interface) communication protocol. It is capable of interfacing with a microcontroller to convert analog input signals into digital data for further processing.

.. image:: img/MCP3008.jpg
      :width: 40%

**Sequence of Operation**

A conversion on the MCP3008 begins by setting the CS (chip select) pin low, which activates communication with the device. The microcontroller then sends a 3-byte control stream via the SPI interface to specify the configuration and select the input channel.

The first byte sent contains the start bit and the single/differential selection bit. The next bits indicate which of the 8 channels (CH0–CH7) to read from. Data is shifted into the device on each rising edge of the SPI clock (SCLK), and the conversion result is returned simultaneously.

A short delay is included internally for the selected input channel to settle before conversion begins. The MCP3008 then performs a 10-bit analog-to-digital conversion using a sample-and-hold circuit and a successive approximation register (SAR) comparator.

The conversion result is transmitted back to the microcontroller through the MISO (Master In Slave Out) line. The most significant bit (MSB) of the 10-bit result is sent first, followed by the remaining bits. The microcontroller reads the result over the SPI bus during this time.

After the full 10-bit digital value is shifted out, the MCP3008 completes the cycle and waits for the next command.

* `MCP3008 series Datasheet <https://www.alldatasheet.com/datasheet-pdf/view/304558/MICROCHIP/MCP3008-ISLASHP.html>`_

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