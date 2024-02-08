.. _camera_module:

Kameramodul
====================================

**Beschreibung**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

Dies ist ein 5MP Raspberry Pi Kameramodul mit OV5647 Sensor. Es ist Plug-and-Play; schließen Sie das beiliegende Flachbandkabel an den CSI (Camera Serial Interface) Anschluss Ihres Raspberry Pi an, und Sie können loslegen.

Die Platine ist klein, etwa 25mm x 23mm x 9mm, und wiegt 3g. Das macht sie ideal für mobile Anwendungen oder andere Anwendungen, bei denen Größe und Gewicht kritisch sind. Das Kameramodul hat eine native Auflösung von 5 Megapixeln und verfügt über eine fest eingestellte Linse, die Standbilder mit 2592 x 1944 Pixel aufnimmt. Es unterstützt auch 1080p30, 720p60 und 640x480p90 Video.

.. note:: 

   Das Modul kann nur Bilder und Videos aufnehmen, keinen Ton.

**Spezifikation**

* **Auflösung statischer Bilder**: 2592×1944 
* **Unterstützte Videoauflösung**: 1080p/30 fps, 720p/60fps und 640x480p 60/90 Videoaufnahme 
* **Blende (F)**: 1.8 
* **Betrachtungswinkel**: 65 Grad 
* **Maße**: 24mmx23.5mmx8mm 
* **Gewicht**: 3g 
* **Schnittstelle**: CSI Anschluss 
* **Unterstütztes Betriebssystem**: Raspberry Pi OS(neueste Version empfohlen) 

Montage des Kameramoduls
---------------------------------------


Am Kameramodul oder Raspberry Pi finden Sie einen flachen Kunststoffanschluss. Ziehen Sie vorsichtig den schwarzen Befestigungsschalter heraus, bis er teilweise herausgezogen ist. Führen Sie das FFC-Kabel in die gezeigte Richtung in den Kunststoffanschluss ein und schieben Sie den Befestigungsschalter wieder zurück.

Wenn das FFC-Kabel korrekt installiert ist, wird es gerade sein und sich nicht herausziehen lassen, wenn Sie leicht daran ziehen. Wenn nicht, installieren Sie es erneut.

.. image:: img/connect_ffc.png
.. image:: img/1.10_camera.png
   :width: 700

.. warning::

   Schließen Sie die Kamera nicht an, wenn die Stromversorgung eingeschaltet ist. Dies kann Ihre Kamera beschädigen.


.. _enable_camera:

Kamera-Schnittstelle aktivieren
-------------------------------------------


Führen Sie den folgenden Befehl aus, um die Kamera-Schnittstelle Ihres Raspberry Pi zu aktivieren. Wenn Sie dies bereits getan haben, überspringen Sie diesen Schritt. Wenn Sie nicht sicher sind, ob Sie dies getan haben, fahren Sie bitte fort.

.. raw:: html

   <run></run>

.. code-block:: 

   sudo raspi-config

**3 Interfacing options**

.. image:: img/image282.png
   :align: center

**P1 Camera**

.. image:: img/camera_config1.png
   :align: center

**<Yes>, dann <Ok> -> <Finish>**

.. image:: img/camera_config2.png
   :align: center

Nach Abschluss der Konfiguration wird empfohlen, den Raspberry Pi neu zu starten.

.. raw:: html

   <run></run>

.. code-block:: 

   sudo reboot
   
**Beispiel**

* :ref:`3.1.1_py` (Python-Projekt)
* :ref:`3.1.2_py` (Python-Projekt)
* :ref:`4.1.1_py` (Python-Projekt)
* :ref:`4.1.4_py` (Python-Projekt)
* :ref:`4.1.5_py` (Python-Projekt)
* :ref:`1.10_scratch` (Scratch-Projekt)
* :ref:`1.18_scratch` (Scratch-Projekt)
