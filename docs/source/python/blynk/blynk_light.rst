.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones navideñas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _blynk_light_py:

Luz Inteligente
====================

En este proyecto, utilizamos el deslizador de Blynk para controlar el brillo del LED, encendiéndolo y apagándolo con el interruptor.

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

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_led`
        - |link_led_buy|

**1. Conexión**

.. image:: img/wiring_led1.png

**2. Crear Widget y Flujo de Datos**

1. Haz clic en el ícono del menú en la esquina superior derecha y selecciona editar tablero.

    .. image:: img/sp220913_180231.png

2. Agrega un widget de Interruptor y un widget de Deslizador al Tablero.

    .. image:: img/sp220914_160427.png

3. Crea un flujo de datos para el widget de Interruptor (utilicé V3). Se utilizará para controlar el encendido y apagado del LED.

    .. image:: img/sp220914_155911.png

4. Crea un flujo de datos para el widget de Deslizador (utilicé V2), su rango de valores es de 0 a 100, se utilizará para controlar el brillo del LED.

    .. image:: img/sp220914_160234.png

#. Cuando termines, haz clic en Guardar y Aplicar en la parte superior derecha.

    .. image:: img/sp220913_182300.png


**3. Ejecutar el Código**

1. Edita el código

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_light.py

2. Encuentra la línea siguiente y pega tu ``BLYNK_AUTH_TOKEN``.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Ejecuta el código.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_light.py

4. Ve a Blynk, opera el widget en el Tablero. ahora al hacer clic en el widget de interruptor encenderás/apagarás el LED. desliza el widget de deslizador para cambiar el brillo del LED.

#. Si deseas usar Blynk en dispositivos móviles, consulta :ref:`blynk_mobile`.
