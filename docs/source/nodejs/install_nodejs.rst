.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros aficionados.

    **¿Por qué unirse?**

    - **Soporte de Expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

¿Qué es Node.js?
=======================

Node.js fue lanzado en mayo de 2009 y desarrollado por Ryan Dahl. Es un entorno de ejecución de JavaScript basado en el motor V8 de Chrome. Utiliza un modelo de E/S no bloqueante y dirigido por eventos para permitir que JavaScript se ejecute en la plataforma de desarrollo del lado del servidor.

En pocas palabras, Node.js es JavaScript ejecutándose en el servidor. Si estás familiarizado con JavaScript, entonces aprenderás Node.js fácilmente.

Node.js generalmente utiliza el comando ``npm install xxx`` para instalar paquetes de terceros, lo que requiere que instalemos la herramienta npm, similar a la herramienta pip en Python.

Instalar o actualizar Node.js y npm
------------------------------------------

Ejecuta los siguientes comandos para instalar y actualizar Node.js y npm.

.. raw:: html

    <run></run>

.. code-block::

    sudo apt-get update
    sudo apt-get install nodejs
    sudo apt-get install npm 
    sudo npm install npm -g

Luego, verifica la versión actual de Node con el siguiente comando.

.. raw:: html

    <run></run>

.. code-block::

    node -v

El siguiente comando verifica la versión actual de npm.

.. raw:: html

    <run></run>

.. code-block::

    npm -v