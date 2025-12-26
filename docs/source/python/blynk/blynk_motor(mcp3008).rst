.. note::

    ¡Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _blynk_motor2_py_mcp3008:

Ventilador Inteligente (MCP3008)
================================

En este proyecto, puedes ver la temperatura desde Blynk y encender el ventilador de forma remota.

.. note:: Antes de comenzar este proyecto, te recomendamos completar :ref:`bk_start_py`. Lo siguiente te dará una comprensión clara de Blynk.

**Componentes requeridos**

En este proyecto, necesitamos los siguientes componentes. 

Es definitivamente conveniente comprar un kit completo, aquí tienes el enlace: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre	
        - ELEMENTOS EN ESTE KIT
        - ENLACE
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

También puedes comprarlos por separado en los siguientes enlaces.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUCCIÓN DEL COMPONENTE
        - ENLACE DE COMPRA

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_power_module`
        - \-
    *   - :ref:`cpn_l293d`
        - \-
    *   - :ref:`cpn_mcp3008`
        - \-
    *   - :ref:`cpn_thermistor`
        - |link_thermistor_buy|
    *   - :ref:`cpn_motor`
        - |link_motor_buy|

**1. Cableado**

.. image:: img/3.1.4_smart_fan_iot.png


**2. Crear Widget y Flujo de Datos (Datastream)**

1. Haz clic en el icono del menú en la esquina superior derecha y selecciona **Editar Dashboard**.

    .. image:: img/sp220913_180231.png

2. Agrega un widget **Switch** y un widget **Label** al Dashboard.

    .. image:: img/sp220914_175437.png

3. Crea un flujo de datos (Datastream) (usé V3) para el widget Switch. Este se usará para encender el motor.

    .. image:: img/sp220914_155911.png

4. Crea un flujo de datos (Datastream) para el widget Label (usé V0). Este se usará para mostrar la temperatura. Configura **DATA TYPE** en **String**.

    .. image:: img/sp220914_175616.png

#. Una vez terminado, haz clic en **Save And Apply** en la parte superior derecha.

    .. image:: img/sp220913_182300.png


**3. Ejecutar el código**

1. Edita el código

.. raw:: html

   <run></run>

.. code-block::

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_motor(mcp3008).py

2. Busca la siguiente línea y pega tu ``BLYNK_AUTH_TOKEN``.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Ejecuta el código.

.. raw:: html

   <run></run>

.. code-block::

    sudo python3 blynk_motor(mcp3008).py

4. Ve a Blynk; en el Dashboard puedes comprobar la temperatura a través del widget Label y encender/apagar el ventilador mediante el widget Switch.

#. Si deseas usar Blynk en dispositivos móviles, por favor consulta :ref:`blynk_mobile`.
