.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _1.13_scratch_pi5:

1.13 Timbre
====================

Hoy haremos un timbre, haz clic en el sprite Button3 en el escenario, el buzzer sonará; haz clic nuevamente, el buzzer dejará de sonar.

.. image:: img/1.13_header.png

Componentes necesarios
---------------------------

En este proyecto, necesitamos los siguientes componentes.

.. image:: img/1.13_list.png

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

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_buzzer`
        - \-
    *   - :ref:`cpn_transistor`
        - |link_transistor_buy|

Construir el circuito
------------------------

.. image:: img/1.13_image106.png

Cargar el código y ver qué pasa
-------------------------------------

Carga el archivo de código (``1.13_doorbell.sb3``) a Scratch 3.

Haz clic en la bandera verde en el escenario. Cuando hagamos clic en el sprite Button 3, se pondrá azul y luego el buzzer sonará; cuando volvamos a hacer clic, el sprite **Button3** volverá a gris y el buzzer dejará de sonar.


Consejos sobre sprites
------------------------------

Elimina el sprite predeterminado, luego elige el sprite **Button 3**.

.. image:: img/1.13_scratch_button3.png

Luego ajusta el tamaño a 200.

.. image:: img/1.13_scratch_button3_size.png

Consejos sobre los códigos
------------------------------

.. image:: img/1.13_buzzer4.png
  :width: 400

Este bloque te permite cambiar el disfraz del sprite.

.. image:: img/1.13_buzzer5.png
  :width: 400


Configura gpio17 a bajo para hacer sonar el buzzer; configúralo a alto y el buzzer no sonará.

El **interruptor de estado** se usa aquí, y utilizaremos un diagrama de flujo para ayudarte a entender todo el código.

Cuando se hace clic en la bandera verde, el **estado** se establecerá primero en 0 y esperará a que se haga clic en el sprite; si se hace clic en el sprite **button3**, cambiará al disfraz **button-b** (azul) y el **estado** se establecerá en 1. Cuando el programa principal reciba el **estado** como 1, hará que el buzzer suene a intervalos de 0.1s. Si se vuelve a hacer clic en **button3**, cambiará al disfraz **button-a** (gris) y el **estado** se establecerá nuevamente en 0.

.. image:: img/1.13_scratch_code.png
