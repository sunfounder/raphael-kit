.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _filezilla:

Software Filezilla
==========================

.. image:: img/filezilla_icon.png

El Protocolo de Transferencia de Archivos (FTP) es un protocolo de comunicación estándar utilizado para la transferencia de archivos de computadora desde un servidor a un cliente en una red de computadoras.

Filezilla es un software de código abierto que no solo soporta FTP, sino también FTP sobre TLS (FTPS) y SFTP. Podemos usar Filezilla para subir archivos locales (como imágenes y audio, etc.) a la Raspberry Pi, o descargar archivos de la Raspberry Pi al local.

**Paso 1**: Descargar Filezilla.

Descarga el cliente desde `el sitio web oficial de Filezilla <https://filezilla-project.org/>`_, Filezilla tiene un tutorial muy completo, por favor consulta: `Documentación - Filezilla <https://wiki.filezilla-project.org/Documentation>`_.

**Paso 2**: Conectar a Raspberry Pi

Después de una instalación rápida, ábrelo y `conéctalo a un servidor FTP <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Tiene 3 formas de conectarse, aquí usamos la barra de **Conexión rápida**. Ingresa el **nombre del host/IP**, **nombre de usuario**, **contraseña** y **puerto (22)**, luego haz clic en **Conexión rápida** o presiona **Enter** para conectarte al servidor.

.. image:: img/filezilla_connect.png

.. note::

    Conexión rápida es una buena manera de probar tu información de inicio de sesión. Si deseas crear una entrada permanente, puedes seleccionar **Archivo** -> **Copiar conexión actual al administrador de sitios** después de una Conexión rápida exitosa, ingresa el nombre y haz clic en **OK**. La próxima vez podrás conectarte seleccionando el sitio guardado previamente dentro de **Archivo** -> **Administrador de sitios**.
    
    .. image:: img/ftp_site.png

**Paso 3**: Subir/descargar archivos.

Puedes subir archivos locales a la Raspberry Pi arrastrándolos y soltándolos, o descargar los archivos dentro de la Raspberry Pi a tu computadora local.

.. image:: img/upload_ftp.png

