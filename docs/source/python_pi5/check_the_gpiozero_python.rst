.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Überprüfung von ``GPIO Zero``
=================================

Wenn Sie ein Raspberry Pi 5 Python-Nutzer sind, können Sie die GPIOs mit der API von
``GPIO Zero`` programmieren.

``GPIO Zero`` ist ein Modul zur Steuerung der GPIO-Pins eines Raspberry Pi. Dieses Paket bietet eine Reihe von benutzerfreundlichen Klassen und Funktionen zur Steuerung der GPIOs auf einem Raspberry Pi. Für Beispiele und Dokumentation besuchen Sie: https://gpiozero.readthedocs.io/en/latest/.

Um zu testen, ob GPIO Zero installiert ist, geben Sie in Python ein:

.. raw:: html

   <run></run>

.. code-block::

    python

.. image:: ../python_pi5/img/zero_01.png
    :width: 100%


Im Python-CLI geben Sie ``import gpiozero`` ein. Wenn kein Fehler angezeigt wird, bedeutet dies,
dass GPIO Zero installiert ist.

.. raw:: html

   <run></run>

.. code-block::

    import gpiozero

.. image:: ../python_pi5/img/zero_02.png
    :width: 100%


Wenn Sie die Python-CLI verlassen möchten, geben Sie ein:

.. raw:: html

   <run></run>

.. code-block::

    exit()

.. image:: ../python_pi5/img/zero_03.png
    :width: 100%




