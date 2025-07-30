.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _bk_start_py:

Mit Blynk beginnen
=========================

In diesem Projekt erfahren Sie, wie Sie Blynk verwenden können.

Wenn Sie Widgets in Blynk auslösen, wird Ihr Raspberry Pi deren Werte ausgeben.

Befolgen Sie die untenstehenden Schritte und beachten Sie, dass Sie diese in der angegebenen Reihenfolge ausführen und kein Kapitel überspringen sollten.



1. Blynk konfigurieren
--------------------------

1. Besuchen Sie die `BLYNK <https://blynk.io/>`_ Webseite und klicken Sie auf **START FREE**.

    .. image:: img/sp220607_142551.png

#. Geben Sie Ihre E-Mail-Adresse ein, um ein Konto zu registrieren.

    .. image:: img/sp220607_142807.png

#. Überprüfen Sie Ihre E-Mail, um die Konto-Registrierung abzuschließen.

    .. image:: img/sp220607_142936.png

#. Anschließend erscheint der **Blynk Tour**. Sie können diesen lesen, um grundlegende Informationen über Blynk zu erfahren.

    .. image:: img/sp220607_143244.png

#. Als Nächstes müssen wir eine Vorlage und ein Gerät erstellen. Klicken Sie auf **Cancel**.

    .. image:: img/sp220607_143608.png

#. Gehen Sie über die Navigationsleiste zur Entwicklerzone.

    .. image:: img/develop_zone.png

#. Neue Vorlage erstellen.

    .. image:: img/new_template.png




#. Füllen Sie das Feld **NAME** aus, wie Sie möchten; bei **HARDWARE** sollte **Raspberry Pi** ausgewählt werden. Klicken Sie anschließend auf **Done**.

    .. image:: img/sp220913_170402.png

#. Sie werden zur Informationsseite weitergeleitet, klicken Sie oben rechts einfach auf Speichern.

    .. image:: img/sp220913_171202.png


#. Gehen Sie zur **Devices**-Seite über die Navigationsleiste.

    .. image:: img/devices.jpg

#. Neues Gerät erstellen.

    .. image:: img/new_devices.png

#. Aus Vorlage.

    .. image:: img/create_new_device.png

#. Wählen Sie bei **TEMPLATE** die von Ihnen erstellte aus, den **DEVICE NAME** können Sie individuell festlegen. Dann auf Erstellen klicken.

    .. image:: img/sp220913_173507.png


#. Wenn Sie eine Seite wie diese sehen, bedeutet das, dass Ihre erste Blynk-Einrichtung abgeschlossen ist.

    .. image:: img/my_device.png


2. Dashboard bearbeiten
--------------------------------

1. Klicken Sie auf das Bearbeitungs-Dashboard.

    .. image:: img/edit_dashboard.png

#. Ziehen Sie anschließend beliebige CONTROL Widgets, die Sie möchten, auf das Dashboard. Ich habe einen Schalter und einen Schieberegler hinzugefügt.

    .. image:: img/sp220913_180725.png

#. Tippen Sie auf das Einstellungssymbol des Widgets.

    .. image:: img/sp220913_180806.png

#. Datenstrom erstellen, wählen Sie Virtual Pin.

    .. image:: img/sp220913_180906.png

#. Schließen Sie die Datenstromeinrichtung ab. Hier wurde der Datenstrom für den Schalter erstellt, daher wählen Sie bei **DATA TYPE** ``Interger``, **MIN** und **MAX** auf ``0`` und ``1`` einstellen. Erstellen und dann speichern.

    .. image:: img/sp220913_181113.png

#. Verwenden Sie die gleichen Schritte, um einen Datenstrom für das Schieberegler-Widget zu erstellen und ändern Sie erneut **DATA TYPE**, **MIN** und **MAX** nach Ihren Bedürfnissen.

    .. image:: img/sp220913_182042.png

#. Wenn Sie fertig sind, klicken Sie oben rechts auf Speichern und Anwenden.

    .. image:: img/sp220913_182300.png


3. Die Blynk-Bibliothek installieren
---------------------------------------

Führen Sie den folgenden Befehl zur Installation aus.

.. raw:: html

   <run></run>

.. code-block::

    cd ~
    git clone https://github.com/vshymanskyy/blynk-library-python.git
    cd blynk-library-python
    sudo python3 setup.py

4. Das Beispiel herunterladen
---------------------------------

Wir haben einige Beispiele bereitgestellt. Bitte führen Sie den folgenden Befehl aus, um sie herunterzuladen.

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~
    git clone https://github.com/sunfounder/blynk-raspberrypi-python.git


5. Den Code ausführen
---------------------------

1. Gehen Sie zur Geräte-Info-Seite von Blynk. Unter **FIRMWARE CONFIGURATION** sehen Sie einige Informationen. Sie müssen den **BLYNK_AUTH_TOKEN** kopieren.

    .. image:: img/sp220913_182456.png

2. Bearbeiten Sie den Code.

.. raw:: html

    <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_start.py

3. Suchen Sie die untenstehende Zeile und fügen Sie Ihren ``BLYNK_AUTH_TOKEN`` ein.

.. code-block:: 

    BLYNK_AUTH = 'YourAuthToken'

4. Führen Sie den Code aus.

.. raw:: html

    <run></run>

.. code-block:: 

    sudo python3 blynk_start.py

5. Öffnen Sie Blynk und bedienen Sie das Widget im Dashboard.

    .. image:: img/sp220913_183529.png

6. Jetzt können Sie Ihre Aktionen im Terminal sehen.

.. code-block:: 

    ..
       ___  __          __
      / _ )/ /_ _____  / /__
     / _  / / // / _ \/  '_/
    /____/_/\_, /_//_/_/\_\
            /___/ for Python v1.0.0 (linux)

    Connecting to blynk.cloud:443...
    Blynk ready. Ping: 142 ms
    V0 value: ['1']
    V0 value: ['0']
    V1 value: ['3']
    V1 value: ['8']
    V0 value: ['1']
