.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _audio_configuration:

Audio-Konfiguration
=========================

.. _change_audio_output:

Audio-Ausgabe ändern
----------------------------

Wenn aus Ihrem Lautsprecher kein Ton kommt, liegt es möglicherweise daran, dass der Raspberry Pi die falsche Audio-Ausgabe gewählt hat. Die richtige Auswahl sollte **Kopfhörer** sein. Sie können die Audio-Ausgabe mit den folgenden Schritten ändern.

Geben Sie den folgenden Befehl ein.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo raspi-config

Wählen Sie **1 System Options** aus.

.. image:: img/audio1.jpg

Dann **S2 Audio**.

.. image:: img/audio2.jpg

Nachdem Sie **1 Headphones** ausgewählt haben, drücken Sie ``Enter``, um zu bestätigen und wählen Sie ``Finish`` zum Beenden.

.. image:: img/audio3.jpg

.. _adjust_volume:

Lautstärke anpassen
------------------------

Wenn Sie der Meinung sind, dass die Lautstärke des Lautsprechers zu niedrig ist, können Sie diese durch Eingabe des folgenden Befehls anpassen.

.. raw:: html

   <run></run>

.. code-block:: 

    alsamixer

.. image:: img/faq1.png

Die Standardansicht wird unten gezeigt.

.. image:: img/faq2.png

Drücken Sie ``F6``, um den Modus **Headphones** auszuwählen.

.. image:: img/faq3.png

Verwenden Sie dann die Pfeiltasten nach oben und unten, um die Lautstärke einzustellen, und drücken Sie ``ESC``, um zu beenden.

.. image:: img/faq4.png
