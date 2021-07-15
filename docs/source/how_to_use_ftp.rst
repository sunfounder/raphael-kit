Use Filezilla Software
========================

The File Transfer Protocol (FTP) is a standard communication protocol used for the transfer of computer files from a server to a client on a computer network.

Filezilla is an open source software that not only supports FTP, but also FTP over TLS (FTPS) and SFTP. We can use Filezilla to upload local files (such as pictures and audio, etc.) to the Raspberry Pi, or download files from the Raspberry Pi to the local.

**step1:** Download the client from  `Filezilla's official website <https://filezilla-project.org/>`_ .

**step2:** Start FileZilla then enter Host: 192.168.18.152 (your Raspberry Pi's IP), Usename: pi, Password: raspberry, Port: 22 and click Quickconnect.

.. image:: media/ftp1.png


**step3:** Select the directory of the file to be transferred, the left is the local directory, and the right is the Raspberry Pi directory.

.. image:: media/ftp2.png


**step4:** Right-click the file, and then click Upload/Download to start uploading or downloading.

.. image:: media/ftp3.png

