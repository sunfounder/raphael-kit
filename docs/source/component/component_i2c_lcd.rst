.. _cpn_i2c_lcd:

LCD1602 I2C
==============

.. image:: img/i2c_lcd1602.png
    :width: 800

* **GND** : Masse
* **VCC** : Alimentation, 5V.
* **SDA** : Ligne de données série. Connecter à VCC via une résistance de pullup.
* **SCL** : Ligne d'horloge série. Connecter à VCC via une résistance de pullup.

Comme nous le savons tous, bien que les écrans LCD et d'autres affichages enrichissent grandement l'interaction homme-machine, ils partagent une faiblesse commune. Lorsqu'ils sont connectés à un contrôleur, plusieurs E/S du contrôleur sont occupées, ce qui limite les autres fonctions du contrôleur.

Par conséquent, le LCD1602 avec un module I2C a été développé pour résoudre ce problème. Le module I2C dispose d'une puce I2C PCF8574 intégrée qui convertit les données série I2C en données parallèles pour l'affichage LCD.

* `PCF8574 Datasheet <https://www.ti.com/lit/ds/symlink/pcf8574.pdf?ts=1627006546204&ref_url=https%253A%252F%252Fwww.google.com%252F>`_

**Adresse I2C**

L'adresse par défaut est généralement 0x27, dans quelques cas, elle peut être 0x3F.

En prenant l'adresse par défaut de 0x27 comme exemple, l'adresse de l'appareil peut être modifiée en court-circuitant les pads A0/A1/A2 ; dans l'état par défaut, A0/A1/A2 est à 1, et si le pad est court-circuité, A0/A1/A2 est à 0.

.. image:: img/i2c_address.jpg
    :width: 600

**Rétroéclairage/Contraste**

Le rétroéclairage peut être activé par un cavalier, retirez le cavalier pour désactiver le rétroéclairage. Le potentiomètre bleu à l'arrière est utilisé pour ajuster le contraste (le rapport de luminosité entre le blanc le plus lumineux et le noir le plus sombre).

.. image:: img/back_lcd1602.jpg

* **Cavalier** : Le rétroéclairage peut être activé par ce cavalier, retirez ce cavalier pour désactiver le rétroéclairage.
* **Potentiomètre** : Il est utilisé pour ajuster le contraste (la clarté du texte affiché), qui augmente dans le sens horaire et diminue dans le sens antihoraire.

**Exemple**

* :ref:`1.1.7_c` (Projet C)
* :ref:`3.1.3_c` (Projet C)
* :ref:`3.1.7_c` (Projet C)
* :ref:`3.1.8_c` (Projet C)
* :ref:`3.1.11_c` (Projet C)
* :ref:`1.1.7_py` (Projet Python)
* :ref:`4.1.9_py` (Projet Python)
* :ref:`4.1.13_py` (Projet Python)
* :ref:`4.1.14_py` (Projet Python)
* :ref:`4.1.17_py` (Projet Python)

