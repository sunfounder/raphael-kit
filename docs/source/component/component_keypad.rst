.. _cpn_keypad:

Tastenfeld
========================

Ein Tastenfeld ist ein rechteckiges Array aus 12 oder 16 AUS-(EIN)-Tasten. 
Ihre Kontakte können über eine Kopfleiste erreicht werden, die sich für den Anschluss mit einem Flachbandkabel eignet oder in eine Leiterplatte eingefügt werden kann. 
Bei einigen Tastenfeldern verbindet sich jede Taste mit einem separaten Kontakt im Kopf, während alle Tasten einen gemeinsamen Ground teilen.

.. image:: img/keypad314.png

Häufiger sind die Tasten matrixcodiert, das heißt, jede von ihnen überbrückt ein einzigartiges Paar von Leitern in einer Matrix. 
Diese Konfiguration eignet sich für das Polling durch einen Mikrocontroller, der so programmiert werden kann, dass er einen Ausgangsimpuls nacheinander an jede der vier horizontalen Drähte sendet. 
Während jedes Impulses überprüft er die verbleibenden vier vertikalen Drähte nacheinander, um festzustellen, welcher davon, falls vorhanden, ein Signal führt. 
Pullup- oder Pulldown-Widerstände sollten zu den Eingangsdrähten hinzugefügt werden, um zu verhindern, dass die Eingänge des Mikrocontrollers unvorhersehbar reagieren, wenn kein Signal vorhanden ist.

**Beispiel**

* :ref:`2.1.8_c` (C-Projekt)
* :ref:`3.1.8_c` (C-Projekt)
* :ref:`3.1.11_c` (C-Projekt)
* :ref:`2.1.8_py` (Python-Projekt)
* :ref:`4.1.14_py` (Python-Projekt)
* :ref:`4.1.17_py` (Python-Projekt)
