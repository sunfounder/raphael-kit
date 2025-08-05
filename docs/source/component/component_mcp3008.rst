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

Le MCP3008 est un convertisseur analogique‑numérique (CAN) à approximation successive sur 10 bits, avec 8 canaux d’entrée et un protocole de communication SPI (Serial Peripheral Interface).  
Il peut être interfacé avec un microcontrôleur pour convertir des signaux d’entrée analogiques en données numériques pour un traitement ultérieur.

.. image:: img/MCP3008.jpg
      :width: 40%

**Séquence de fonctionnement**

Une conversion sur le MCP3008 commence par la mise à l’état bas de la broche CS (chip select), ce qui active la communication avec le composant.  
Le microcontrôleur envoie ensuite un flux de commande de 3 octets via l’interface SPI pour spécifier la configuration et sélectionner le canal d’entrée.

Le premier octet envoyé contient le bit de démarrage et le bit de sélection simple/différentiel.  
Les bits suivants indiquent lequel des 8 canaux (CH0–CH7) doit être lu.  
Les données sont transférées dans le composant à chaque front montant de l’horloge SPI (SCLK), et le résultat de la conversion est renvoyé simultanément.

Un court délai interne est appliqué afin de stabiliser le canal d’entrée sélectionné avant de commencer la conversion.  
Le MCP3008 effectue ensuite une conversion analogique‑numérique sur 10 bits à l’aide d’un circuit d’échantillonnage et de maintien et d’un comparateur à registre d’approximation successive (SAR).

Le résultat de la conversion est transmis au microcontrôleur via la ligne MISO (Master In Slave Out).  
Le bit de poids fort (MSB) du résultat sur 10 bits est envoyé en premier, suivi des bits restants.  
Le microcontrôleur lit le résultat via le bus SPI pendant cette transmission.

Après que la valeur numérique complète sur 10 bits a été transmise, le MCP3008 termine le cycle et attend la prochaine commande.

* `Fiche technique de la série MCP3008 <https://www.alldatasheet.com/datasheet-pdf/view/304558/MICROCHIP/MCP3008-ISLASHP.html>`_

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