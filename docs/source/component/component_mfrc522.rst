.. _cpn_mfrc522:

MFRC522 Modul
=====================

**RFID**

Radiofrequenz-Identifikation (RFID) bezieht sich auf Technologien, die den drahtlosen Datenaustausch zwischen einem Objekt (oder Tag) und einem Abfragegerät (oder Lesegerät) nutzen, um solche Objekte automatisch zu verfolgen und zu identifizieren. Die Übertragungsreichweite des Tags ist auf mehrere Meter vom Lesegerät begrenzt. Eine direkte Sichtverbindung zwischen dem Lesegerät und dem Tag ist nicht unbedingt erforderlich.

Die meisten Tags enthalten mindestens einen integrierten Schaltkreis (IC) und eine Antenne. Der Mikrochip speichert Informationen und ist für die Verwaltung der Funkkommunikation mit dem Lesegerät verantwortlich. Passive Tags verfügen nicht über eine unabhängige Energiequelle und sind auf ein externes elektromagnetisches Signal angewiesen, das vom Lesegerät bereitgestellt wird, um ihren Betrieb zu ermöglichen. Aktive Tags besitzen eine eigene Energiequelle, wie z.B. eine Batterie. Daher können sie über erweiterte Verarbeitungs-, Übertragungsfähigkeiten und Reichweite verfügen.

.. image:: img/image230.png

**MFRC522**

MFRC522 ist eine Art integrierter Lese- und Schreibkarten-Chip, der häufig im 13,56 MHz Funkbereich eingesetzt wird. Eingeführt von der Firma NXP, handelt es sich um einen nieder­spannungs-, kostengünstigen und kleinformatigen kontaktlosen Kartenchip, der ideal für intelligente Instrumente und tragbare Handgeräte ist.

Der MF RC522 verwendet fortschrittliche Modulations- und Demodulationskonzepte, die in allen Arten von passiven kontaktlosen Kommunikationsmethoden und -protokollen bei 13,56 MHz voll zur Geltung kommen. Darüber hinaus unterstützt er den schnellen CRYPTO1-Verschlüsselungsalgorithmus zur Überprüfung von MIFARE-Produkten. MFRC522 unterstützt auch die hochgeschwindigkeits-kontaktlose Kommunikation der MIFARE-Serie mit einer bidirektionalen Datenübertragungsrate von bis zu 424 kbit/s. Als neues Mitglied der hochintegrierten 13,56 MHz Lesekarten-Serie ähnelt der MF RC522 den bestehenden MF RC500 und MF RC530, weist jedoch auch erhebliche Unterschiede auf. Er kommuniziert in serieller Art mit der Host-Maschine, was weniger Verdrahtungsaufwand erfordert. Sie können zwischen SPI, I2C und serieller UART-Modus (ähnlich wie RS232) wählen, was die Anbindung reduziert, Platz auf der Leiterplatte spart (kleinere Größe) und Kosten senkt.

**Beispiel**

* :ref:`2.2.10_c` (C-Projekt)
* :ref:`2.2.10_py` (Python-Projekt)
* :ref:`4.1.19_py` (Python-Projekt)
