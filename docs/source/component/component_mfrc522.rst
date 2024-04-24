.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _cpn_mfrc522:

MFRC522 Module
=====================

**RFID**

Radio Frequency Identification (RFID) refers to technologies that
involve using wireless communication between an object (or tag) and an
interrogating device (or reader) to automatically track and identify
such objects. The tag transmission range is limited to several meters
from the reader. A clear line of sight between the reader and tag is not
necessarily required.

Most tags contain at least one integrated circuit (IC) and an antenna.
The microchip stores information and is responsible for managing the
radio frequency (RF) communication with the reader. Passive tags do not
have an independent energy source and depend on an external
electromagnetic signal, provided by the reader, to power their
operations. Active tags contain an independent energy source, such as a
battery. Thus, they may have increased processing, transmission
capabilities and range.

.. image:: img/image230.png


**MFRC522**

MFRC522 is a kind of integrated read and write card chip. It is commonly
used in the radio at 13.56MHz. Launched by the NXP Company, it is a
low-voltage, low-cost, and small-sized non-contact card chip, a best
choice of intelligent instrument and portable handheld device.

The MF RC522 uses advanced modulation and demodulation concept which
fully presented in all types of 13.56MHz passive contactless
communication methods and protocols. In addition, it supports rapid
CRYPTO1 encryption algorithm to verify MIFARE products. MFRC522 also
supports MIFARE series of high-speed non-contact communication, with a
two-way data transmission rate up to 424kbit/s. As a new member of the
13.56MHz highly integrated reader card series, MF RC522 is much similar
to the existing MF RC500 and MF RC530 but there also exists great
differences. It communicates with the host machine via the serial manner
which needs less wiring. You can choose between SPI, I2C and serial UART
mode (similar to RS232), which helps reduce the connection, save PCB
board space (smaller size), and reduce cost.

**Example**

* :ref:`2.2.10_c` (C Project)
* :ref:`2.2.10_py` (Python Project)
* :ref:`4.1.19_py` (Python Project)