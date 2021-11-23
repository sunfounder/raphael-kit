LED Matrix Module
==============================

.. image:: img/max7219_module.jpg
    :width: 400
    :align: center

This is a common cathode 8x8 dot matrix module driven by MAX7219, the module operating voltage is 5V, the size is 50mmx32mmx15mm, the left side is input port, the right side is output port, support multiple modules cascade.

* **VCC**: Positive Supply Voltage. Connect to +5V.
* **GND**: Ground (both GND pins must be connected)
* **DIN**: Serial-Data Input. Data is loaded into the internal 16-bit shift register on CLK’s rising edge.
* **CS**: Chip-Select Input. Serial data is loaded into the shift register while CS is low. The last 16 bits of serial data are latched on CS’s rising edge.
* **CLK**: Serial-Clock Input. 10MHz maximum rate. On CLK’s rising edge, data is shifted into the internal shift register. On CLK’s falling edge, data is clocked out of DOUT. On the MAX7221, the CLK input is active only while CS is low.

**MAX7219**

The MAX7219 is a compact, serial input/output common-cathode display drivers that interface microprocessors (µPs) to 7-segment numeric LED displays of up to 8 digits, bar-graph displays, or 64 individual LEDs. Included on-chip are a BCD code-B
decoder, multiplex scan circuitry, segment and digit drivers, and an 8x8 static RAM that stores each digit.

Only one external resistor is required to set the segment current for all LEDs. The MAX7221 is compatible with SPI™, QSPI™, and MICROWIRE™, and has slewrate-limited segment drivers to reduce EMI.

A convenient 4-wire serial interface connects to all common µPs. Individual digits may be addressed and updated without rewriting the entire display. The MAX7219/MAX7221 also allow the user to select codeB decoding or no-decode for each digit.

.. image:: img/max7219_sche.png

* `MAX7219 Datasheet <https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf>`_

**Example**

* :ref:`1.1.6_c` (C Project)
* :ref:`3.1.12 GAME - 10 Second` (C Project)
* :ref:`1.1.6_py` (Python Project)
* :ref:`4.1.19 AttendanceSystem` (Python Project)
