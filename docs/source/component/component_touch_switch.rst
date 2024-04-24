.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_touch_switch:

Berührungsschalter Modul
==================================

.. image:: img/touch168.png
    :width: 300
    :align: center

Das Berührungsschalter-Modul funktioniert durch die Erkennung einer Kapazitätsänderung aufgrund des Einflusses eines externen Objekts. Die Berührungsplatte ist mit einem Isoliermaterial überzogen, sodass der Benutzer keinen Kontakt mit dem elektrischen Stromkreis hat.

Ein kapazitiver Berührungsschalter verfügt über verschiedene Schichten – eine obere isolierende Abdeckplatte gefolgt von der Berührungsplatte, einer weiteren Isolierschicht und schließlich einer Erdplatte.

.. image:: img/touch169.jpeg

In der Praxis kann ein kapazitiver Sensor auf einer doppelseitigen Leiterplatte angefertigt werden, wobei eine Seite als Berührungssensor und die gegenüberliegende Seite als Erdplatte des Kondensators betrachtet wird. Wird Strom über diese Platten angelegt, werden die beiden Platten geladen. Im Gleichgewichtszustand haben die Platten die gleiche Spannung wie die Stromquelle.

Die Berührungserkennungsschaltung verfügt über einen Oszillator, dessen Frequenz von der Kapazität des Touchpads abhängt. Wenn ein Finger sich dem Touchpad nähert, verursacht die zusätzliche Kapazität eine Änderung der Frequenz dieses internen Oszillators. Die Erkennungsschaltung überwacht die Oszillatorfrequenz in zeitlichen Abständen, und wenn die Verschiebung den Schwellenwert überschreitet, löst die Schaltung ein Tastendruckereignis aus.

**Beispiel**

* :ref:`2.1.3_c` (C-Projekt)
* :ref:`2.1.3_py` (Python-Projekt)
* :ref:`1.9_scratch` (Scratch-Projekt)
