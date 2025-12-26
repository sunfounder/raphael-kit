.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.14_scratch:

1.14 123 Hombre de Madera
=============================

Hoy vamos a jugar a 123 Hombre de Madera.

Haz clic en la bandera verde para comenzar el juego, mantén presionada la tecla de flecha derecha en el teclado para hacer que el sprite se desplace hacia la derecha. Si la luz verde está encendida, el sprite puede moverse; pero cuando el LED rojo esté encendido, debes detener el movimiento del sprite; de lo contrario, el buzzer seguirá sonando.

.. image:: img/1.14_header.png

Componentes necesarios
-------------------------

En este proyecto, necesitamos los siguientes componentes.

.. image:: img/1.14_component.png

Es definitivamente conveniente comprar un kit completo, aquí está el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre
        - ARTÍCULOS EN ESTE KIT
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

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_buzzer`
        - |link_passive_buzzer_buy|
    *   - :ref:`cpn_led`
        - |link_led_buy|
    *   - :ref:`cpn_transistor`
        - |link_transistor_buy|

Construir el circuito
------------------------

.. image:: img/1.14_fritzing.png

Cargar el código y ver qué pasa
-----------------------------------

Carga el archivo de código (``1.14_123_wooden_man.sb3``) a Scratch 3.

Cuando el LED verde esté encendido, puedes usar la tecla de flecha derecha para controlar a **Avery** para que camine hacia la derecha; cuando el LED rojo esté encendido, si continúas moviendo a **Avery** hacia la derecha, sonará una alarma.

Consejos sobre sprites
-------------------------

Elimina el sprite predeterminado, luego elige el sprite **Avery Walking**.

.. image:: img/1.14_wooden1.png
  :width: 400

Consejos sobre los códigos
-------------------------------

.. image:: img/1.14_wooden2.png
  :width: 400

Inicializa todos los pines a alto.

.. image:: img/1.14_wooden3.png
  :width: 400

Cuando el juego comience, asigna la variable de estado a 1, indicando que el sprite Avery Walking es movible, y luego establece gpio18 en bajo, lo que enciende el LED verde durante 5 segundos.

.. image:: img/1.14_wooden4.png
  :width: 400

Establece gpio18 en alto, luego establece gpio27 en bajo, lo que significa apagar el LED verde y encender el LED amarillo durante 0.5 segundos.

.. image:: img/1.14_wooden5.png
  :width: 400

Asigna la variable de estado a 0, lo que significa que el sprite Avery Walking no se está moviendo; luego establece gpio27 en bajo y gpio17 en alto, lo que apaga el LED amarillo y luego enciende el LED rojo durante 3 segundos. Finalmente, establece gpio17 en alto para apagar el LED rojo.

.. image:: img/1.14_wooden6.png
  :width: 400

Cuando presionamos la tecla de flecha derecha en el teclado, necesitamos cambiar el disfraz del sprite **Avery Walking** al siguiente disfraz para que podamos ver a Avery caminando hacia la derecha. Luego necesitamos determinar el valor de la variable **estado**. Si es 0, significa que el sprite Avery Walking no se está moviendo en este momento, y el buzzer sonará para advertirte que no puedes presionar la tecla de flecha derecha nuevamente.
