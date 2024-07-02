.. nota::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _blynk_temp_py:

Registrador de Temperatura
=================================

En este proyecto, puedes ver la temperatura actual y el gráfico de línea de cambio de temperatura desde Blynk.

.. nota:: Antes de comenzar este proyecto, te recomendamos que completes :ref:`bk_start_py`. Lo siguiente te dará una comprensión clara de Blynk.

**Componentes Requeridos**

En este proyecto, necesitamos los siguientes componentes. 

Es muy conveniente comprar un kit completo, aquí tienes el enlace: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre	
        - ELEMENTOS EN ESTE KIT
        - ENLACE
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

También puedes comprarlos por separado en los enlaces a continuación.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUCCIÓN DEL COMPONENTE
        - ENLACE DE COMPRA

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_humiture_sensor`
        - |link_humiture_buy|


**1. Cableado**

.. image:: img/wiring_blynk_temp.png


**2. Crear Widget y Datastream**

1. Haz clic en el icono del menú en la esquina superior derecha y selecciona editar tablero.

    .. image:: img/sp220913_180231.png

2. Agrega un widget de Medidor y un widget de Gráfico al Tablero.

    .. image:: img/sp220914_175437.png

3. Crea un Datastream para el widget de Medidor (utilicé V5). Se utilizará para mostrar la temperatura. Configura **DATA TYPE** en ``Double``, **DECIMALS** en ``#. #`` (dos decimales válidos).

    .. image:: img/sp220914_182300.png

4. Agrega el Datastream V5 que acabas de crear al widget de Gráfico.

    .. image:: img/sp220914_183039.png

#. Cuando termines, haz clic en Guardar y Aplicar en la esquina superior derecha.

    .. image:: img/sp220913_182300.png


**3. Ejecutar el Código**

1. Edita el código

.. raw:: html

   <run></run>

.. code-block:: 

    cd ~/blynk-raspberrypi-python
    sudo nano blynk_temp.py

2. Encuentra la línea a continuación y pega tu ``BLYNK_AUTH_TOKEN``.

.. code-block:: python

    BLYNK_AUTH = 'YourAuthToken'

3. Ejecuta el código.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo python3 blynk_temp.py

4. Ve a Blynk. Ahora puedes ver la temperatura y el gráfico de línea de cambio de temperatura en el Tablero.

    .. image:: img/sp220915_101137.png


#. Si deseas utilizar Blynk en dispositivos móviles, consulta :ref:`blynk_mobile`.

