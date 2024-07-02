.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones navideñas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _blynk_reed_py:

Sensor de Puerta y Ventana
===============================

Cuando estás fuera de casa, probablemente te hayas preguntado: "¿Están cerradas las puertas y ventanas de mi casa?"

Para resolver este problema, en este proyecto, construiremos un sensor de puertas y ventanas con un interruptor Reed y un imán.

Instala este sensor y el imán a ambos lados de la puerta o ventana. Podrás verificar si tus puertas y ventanas están cerradas desde la aplicación Blynk en tu teléfono.

.. note:: Antes de comenzar este proyecto, recomendamos que completes :ref:`bk_start_py`. Lo siguiente te dará una comprensión clara de Blynk.

**Componentes necesarios**

En este proyecto, necesitamos los siguientes componentes. 

Es definitivamente conveniente comprar un kit completo, aquí está el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre	
        - ELEMENTOS EN ESTE KIT
        - ENLACE
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

También puedes comprarlos por separado desde los enlaces a continuación.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUCCIÓN DE COMPONENTES
        - ENLACE DE COMPRA

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_reed_switch`
        - |link_reed_switch_buy|


**1. Conexión**

.. image:: img/wiring_blynk_reed.png

**2. Crear Datastream**

1. Haz clic en el icono del menú en la esquina superior derecha y selecciona editar el panel de control.

    .. image:: img/sp220913_180231.png

2. Ve a la página de Datastreams y crea un Nuevo Datastream.

    .. image:: img/sp220914_165911.png

3. Crea un Pin Virtual V4.

    .. image:: img/sp220914_170113.png

#. Cuando termines, haz clic en Guardar y Aplicar en la esquina superior derecha.

    .. image:: img/sp220913_182300.png

**3. Ejecutar el Código**

1. Edita el código

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_reed.py

2. Encuentra la siguiente línea y pega tu ``BLYNK_AUTH_TOKEN``.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Ejecuta el código.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_reed.py

**4. Abre la APP de Blynk**

.. note::

    Como los datastreams solo se pueden crear en Blynk en la web, necesitarás referenciar diferentes proyectos para crear datastreams en la web y luego seguir el tutorial a continuación para crear widgets en Blynk en tu dispositivo móvil.

#. Abre Google Play o APP Store en tu dispositivo móvil y busca "Blynk IoT" (no Blynk(legacy)) para descargar.
#. Después de abrir la APP, inicia sesión; esta cuenta debe ser la misma que la cuenta utilizada en el cliente web.
#. Luego ve a **Dashboard** (si no tienes uno, crea uno) y verás que el **Dashboard** para móvil y web son independientes entre sí.

    .. image:: img/APP_1.jpg

#. Haz clic en el Icono de **Editar**.
#. Haz clic en el área en blanco. 
#. Elige el widget **LED**.

    .. image:: img/APP_2.jpg      

#. Ahora verás un widget **LED** aparecer en el área en blanco, aunque parezca una cuadrícula en blanco, haz clic en él.
#. Aparecerán los ajustes del **LED**, selecciona los **V4** datastreams que acabas de configurar en la página web. Ten en cuenta que cada widget corresponde a un datastream diferente en cada proyecto.
#. Vuelve a la página del **Dashboard**. Ahora, si ves que el widget **LED** está lleno de color, tu puerta o ventana está abierta; si el widget **LED** no está lleno de color, la puerta o ventana está cerrada.

    .. image:: img/APP_3.jpg


