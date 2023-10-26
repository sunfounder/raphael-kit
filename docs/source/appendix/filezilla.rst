.. _filezilla:

Filezilla Software
==========================

.. image:: img/filezilla_icon.png

Das File Transfer Protocol (FTP) ist ein standardisiertes Kommunikationsprotokoll, das zum Übertragen von Computerdateien von einem Server zu einem Client in einem Computernetzwerk verwendet wird.

Filezilla ist eine Open-Source-Software, die nicht nur FTP unterstützt, sondern auch FTP über TLS (FTPS) und SFTP. Mit Filezilla können wir lokale Dateien (wie Bilder und Audio usw.) auf den Raspberry Pi hochladen oder Dateien vom Raspberry Pi auf den lokalen Rechner herunterladen.

**Schritt 1**: Filezilla herunterladen.

Laden Sie den Client von der `offiziellen Filezilla-Website <https://filezilla-project.org/>`_ herunter. Filezilla bietet ein sehr gutes Tutorial an, bitte ziehen Sie die `Dokumentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_ zurate.

**Schritt 2**: Verbindung zum Raspberry Pi herstellen.

Nach einer schnellen Installation öffnen Sie das Programm und `verbinden es mit einem FTP-Server <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Es gibt 3 Verbindungsmethoden, hier verwenden wir die **Quick Connect**. Geben Sie den **hostname/IP**, **username**, **password** und **port (22)** ein und klicken Sie dann auf **Quick Connect** oder drücken Sie **Enter**, um eine Verbindung zum Server herzustellen.

.. image:: img/filezilla_connect.png

.. note::

    Die Schnellverbindung ist eine gute Möglichkeit, Ihre Anmeldeinformationen zu testen. Wenn Sie einen permanenten Eintrag erstellen möchten, können Sie nach einer erfolgreichen Schnellverbindung **File** -> **Aktuelle Verbindung zum Site-Manager kopieren** auswählen, den Namen eingeben und auf **OK** klicken. Beim nächsten Mal können Sie eine Verbindung herstellen, indem Sie die zuvor gespeicherte Seite in **File** -> **Site Manager** auswählen.
    
    .. image:: img/ftp_site.png

**Schritt 3**: Dateien hoch- bzw. herunterladen.

Sie können lokale Dateien durch Ziehen und Ablegen auf den Raspberry Pi hochladen oder Dateien im Raspberry Pi lokal herunterladen.

.. image:: img/upload_ftp.png

