.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_gpio_board:

GPIO-Erweiterungsplatine
========================

Bevor Sie mit dem Erlernen der Befehle beginnen, müssen Sie sich zuerst näher mit 
den Pins des Raspberry Pi beschäftigen, da diese für das nachfolgende Studium von zentraler Bedeutung sind.

Mit Hilfe der GPIO-Erweiterungsplatine können wir die Pins des Raspberry Pi problemlos auf ein Steckbrett führen, um Schäden am GPIO durch häufiges Ein- und Ausstecken zu vermeiden. Dies ist unsere 40-polige GPIO-Erweiterungsplatine und das GPIO-Kabel für Raspberry Pi Modell B+, Modell B 2 und Modell B 3, 4.

.. image:: img/image32.png
    :align: center

**Pin-Nummerierung**

Die Pins des Raspberry Pi können auf drei verschiedene Arten benannt werden: WiringPi, BCM und Board.

Von diesen Benennungsmethoden verwendet die 40-polige GPIO-Erweiterungsplatine die Methode BCM. Einige spezielle Pins, wie der I2C-Port und der SPI-Port, verwenden jedoch den Namen, der ihnen bereits zugeordnet ist.

Die folgende Tabelle zeigt die Benennungsmethoden von WiringPi, Board und den eigentlichen Namen jedes Pins auf der GPIO-Erweiterungsplatine. Zum Beispiel hat der GPIO17 im Board-Namensschema die Bezeichnung 11, im WiringPi-Namensschema die Bezeichnung 0 und im eigentlichen Namensschema die Bezeichnung GPIO0.

.. note::

    1）In der C-Sprache wird das Namensschema WiringPi verwendet.
    
    2）In der Python-Sprache werden die Namensschemata **Board** und **BCM** angewendet, und die Funktion ``GPIO.setmode()`` dient zur Einstellung dieser.
    
    3）In Scratch 3 und Processing wird das Namensschema **BCM** verwendet.

.. image:: img/gpio_board.png
