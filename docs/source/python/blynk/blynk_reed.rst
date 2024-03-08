.. _blynk_reed_py:

Tür- und Fenstersensor
======================

Wenn Sie unterwegs sind, hatten Sie sicherlich schon einmal diese Unsicherheit: "Sind die Türen und Fenster meines Hauses geschlossen?"

Um dieses Problem zu lösen, werden wir in diesem Projekt einen Tür- und Fenstersensor mit Reed-Schalter und Magneten bauen.

Installieren Sie diesen Sensor und den Magneten an beiden Seiten der Tür oder des Fensters. Mit der Blynk-APP auf Ihrem Handy können Sie dann überprüfen, ob Ihre Türen und Fenster geschlossen sind oder nicht.

.. note:: Bevor Sie mit diesem Projekt beginnen, empfehlen wir Ihnen, :ref:`bk_start_py` abzuschließen. Dies wird Ihnen ein klares Verständnis für Blynk vermitteln.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Raphael Kit
        - 337
        - |link_Raphael_kit|

Sie können sie auch einzeln über die untenstehenden Links kaufen.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - KOMPONENTENBESCHREIBUNG
        - KAUF-LINK

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_reed_switch`
        - |link_reed_switch_buy|



**1. Verdrahtung**

.. image:: img/wiring_blynk_reed.png

**2. Datenstrom erstellen**

1. Klicken Sie auf das Menü-Symbol in der oberen rechten Ecke und wählen Sie "Dashboard bearbeiten".

    .. image:: img/sp220913_180231.png

2. Gehen Sie zur Seite "Datenströme" und erstellen Sie einen neuen Datenstrom.

    .. image:: img/sp220914_165911.png

3. Erstellen Sie einen virtuellen Pin V4.

    .. image:: img/sp220914_170113.png

#. Wenn Sie fertig sind, klicken Sie oben rechts auf "Speichern und Anwenden".

    .. image:: img/sp220913_182300.png

**3. Code ausführen**

1. Den Code bearbeiten

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_reed.py

2. Suchen Sie die untenstehende Zeile und fügen Sie Ihren ``BLYNK_AUTH_TOKEN`` ein.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Führen Sie den Code aus.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_reed.py

**4. Blynk APP öffnen**

.. note::

    Da Datenströme nur in Blynk im Web erstellt werden können, müssen Sie verschiedene Projekte referenzieren, um Datenströme im Web zu erstellen. Befolgen Sie dann das untenstehende Tutorial, um Widgets in Blynk auf Ihrem mobilen Gerät zu erstellen.

#. Öffnen Sie Google Play oder den APP Store auf Ihrem Mobilgerät und suchen Sie nach "Blynk IoT" (nicht Blynk(legacy)) zum Herunterladen.
#. Nachdem Sie die APP geöffnet haben, melden Sie sich an. Dieses Konto sollte mit dem Konto, das Sie im Web-Client verwendet haben, identisch sein.
#. Gehen Sie dann zum **Dashboard** (wenn Sie keines haben, erstellen Sie eins). Sie werden feststellen, dass das **Dashboard** für Mobilgeräte und Web unabhängig voneinander sind.

    .. image:: img/APP_1.jpg

#. Klicken Sie auf das **Edit**-Symbol.
#. Klicken Sie auf den leeren Bereich.
#. Wählen Sie das **LED**-Widget.

    .. image:: img/APP_2.jpg      

#. Nun sehen Sie ein **LED**-Widget im leeren Bereich, auch wenn es wie ein leeres Gitter aussieht, klicken Sie darauf.
#. Die **LED**-Einstellungen erscheinen, wählen Sie die Datenströme **V4**, die Sie gerade auf der Webseite eingerichtet haben. Beachten Sie, dass jedes Widget einem anderen Datenstrom in jedem Projekt entspricht.
#. Gehen Sie zurück zur **Dashboard**-Seite. Wenn das **LED**-Widget jetzt mit Farbe gefüllt ist, ist Ihre Tür oder Ihr Fenster offen; wenn das **LED**-Widget nicht mit Farbe gefüllt ist, sind die Tür oder das Fenster geschlossen.

    .. image:: img/APP_3.jpg

