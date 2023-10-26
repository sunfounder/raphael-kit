.. _remote_desktop:

Remote Desktop
=====================

Es gibt zwei Möglichkeiten, den Desktop des Raspberry Pi aus der Ferne zu steuern:

**VNC** und **XRDP**. Sie können beide verwenden.

VNC 
--------------

Sie können die Funktion des Remote-Desktops über VNC nutzen.

**VNC-Dienst aktivieren**

Der VNC-Dienst ist im System bereits installiert. Standardmäßig ist VNC
deaktiviert. Sie müssen es in der Konfiguration aktivieren.

**Schritt 1**

Geben Sie den folgenden Befehl ein:

.. raw:: html

    <run></run>

.. code-block:: 

    sudo raspi-config

.. image:: img/image287.png
   :align: center

**Schritt 2**

Wählen Sie mit der Pfeiltaste nach unten auf Ihrer
Tastatur **3** **Interfacing Options** und drücken Sie die **Enter**.

.. image:: img/image282.png
   :align: center

**Schritt 3**

**P3 VNC**

.. image:: img/image288.png
   :align: center

**Schritt 4**

Wählen Sie **Yes -> OK -> Finish**, um die Konfiguration zu beenden.

.. image:: img/image289.png
   :align: center

**In VNC anmelden**

**Schritt 1**

Sie müssen den `VNC Viewer <https://www.realvnc.com/de/connect/download/viewer/>`_ auf Ihrem Computer herunterladen und installieren. Nach der Installation öffnen Sie diesen.

**Schritt 2**

Wählen Sie dann \"**New connection**\".

.. image:: img/image290.png
   :align: center

**Schritt 3**

Geben Sie die IP-Adresse des Raspberry Pi und einen beliebigen **Name** ein.

.. image:: img/image291.png
   :align: center

**Schritt 4**

Doppelklicken Sie auf die gerade erstellte **Verbindung**:

.. image:: img/image292.png
   :align: center

**Schritt 5**

Geben Sie den Benutzernamen (**pi**) und das Passwort (standardmäßig **raspberry**) ein.

.. image:: img/image293.png
   :align: center

**Schritt 6**

Jetzt können Sie den Desktop des Raspberry Pi sehen:

.. image:: img/image294.png
   :align: center

Das ist das Ende des VNC-Teils.


XRDP
-----------------------

Eine weitere Methode für den Remote-Desktop-Zugriff ist XRDP. Es bietet einen grafischen Login zu entfernten Maschinen über RDP (Microsoft Remote Desktop Protocol).

**XRDP installieren**

**Schritt 1**

Melden Sie sich über SSH am Raspberry Pi an.

**Schritt 2**

Geben Sie die folgenden Befehle ein, um XRDP zu installieren.

.. raw:: html

    <run></run>

.. code-block:: 

   sudo apt-get update
   sudo apt-get install xrdp

**Schritt 3**

Nachdem die Installation gestartet wurde, bestätigen Sie mit "Y" und drücken Sie die "Enter"-Taste.

.. image:: img/image295.png
   :align: center

**Schritt 4**

Nach der Installation melden Sie sich über Windows Remote-Desktop-Anwendungen an Ihrem Raspberry Pi an.

**Anmeldung bei XRDP**

**Schritt 1**

Wenn Sie ein Windows-Benutzer sind, können Sie die Remote-Desktop-Funktion nutzen, die bei Windows dabei ist. Mac-Benutzer können Microsoft Remote Desktop aus dem APP Store herunterladen. Es gibt nicht viele Unterschiede zwischen den beiden. Das folgende Beispiel zeigt den Windows Remote-Desktop.

**Schritt 2**

Geben Sie \"**mstsc**\" in Ausführen (WIN+R) ein, um die Remote-Desktop-Verbindung zu öffnen, tragen Sie die IP-Adresse des Raspberry Pi ein und klicken Sie auf "Verbinden".

.. image:: img/image296.png
   :align: center

**Schritt 3**

Das XRDP-Anmeldefenster erscheint. Bitte geben Sie Ihren Benutzernamen und Ihr Passwort ein. Klicken Sie dann auf "OK". Beim ersten Login ist Ihr Benutzername "pi" und das Passwort "raspberry".

.. image:: img/image297.png
   :align: center

**Schritt 4**

Hier haben Sie erfolgreich den RPi über den Remote-Desktop angemeldet.

.. image:: img/image20.png
   :align: center

**Urheberrechtshinweis**

Alle Inhalte, einschließlich, aber nicht beschränkt auf Texte, Bilder und Code in diesem Handbuch gehören dem SunFounder Unternehmen. Sie dürfen sie nur für persönliches Lernen, Forschung, Freizeit oder andere nicht-kommerzielle oder gemeinnützige Zwecke nutzen, unter Beachtung der entsprechenden Vorschriften und Urheberrechtsgesetze, ohne die rechtlichen Rechte des Autors und der relevanten Rechteinhaber zu verletzen. Für jede Person oder Organisation, die diese ohne Erlaubnis für kommerzielle Gewinne nutzt, behält sich das Unternehmen das Recht vor, rechtliche Schritte einzuleiten.

