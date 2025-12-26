.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso temprano a anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _1.17_scratch:

1.17 Ventilador giratorio
===================================

En este proyecto, haremos un sprite de estrella giratoria y un ventilador.

.. image:: img/1.17_header.png

Componentes necesarios
------------------------------

En este proyecto, necesitamos los siguientes componentes. 

.. image:: img/1.17_list.png

Es definitivamente conveniente comprar un kit completo, aquí está el enlace: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre	
        - ÍTEMS EN ESTE KIT
        - ENLACE
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

También puedes comprarlos por separado desde los enlaces a continuación.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUCCIÓN AL COMPONENTE
        - ENLACE DE COMPRA

    *   - :ref:`cpn_gpio_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_power_module`
        - \-
    *   - :ref:`cpn_l293d`
        - \-
    *   - :ref:`cpn_motor`
        - |link_motor_buy|

Construir el circuito
---------------------------

.. image:: img/1.17_image117.png

Cargar el código y ver qué pasa
-------------------------------------------

Carga el archivo de código (``1.17_rotating_fan.sb3``) en Scratch 3.

Después de hacer clic en la bandera verde en el escenario, haz clic en el sprite de estrella, luego este y el motor girarán en el sentido de las agujas del reloj; puedes cambiar la dirección de rotación haciendo clic en los dos sprites de **flecha**. Cuando vuelvas a hacer clic en el sprite de **estrella**, este y el motor dejarán de girar.

Consejos sobre el sprite
-------------------------------
Elimina el sprite predeterminado, luego selecciona el sprite de **estrella** y el sprite de **flecha1**, y copia Flecha1 una vez.

.. image:: img/1.17_motor1.png

En la opción **Disfraces**, cambia el sprite de Flecha2 a un disfraz de dirección diferente.

.. image:: img/1.17_motor2.png

Ajusta el tamaño y la posición del sprite de manera adecuada.

.. image:: img/1.17_motor3.png


Consejos sobre el código
-------------------------------

**Diagrama de flujo**

.. image:: img/1.17_scratch.png

En este código, verás 2 bloques rosas, girar a la izquierda y girar a la derecha, que son nuestros bloques personalizados (funciones).

.. image:: img/1.17_new_block.png

**¿Cómo hacer un bloque?**

Aprendamos cómo hacer un bloque (función). El bloque (función) se puede usar para simplificar tu programa, especialmente si realizas la misma operación varias veces. Poner estas operaciones en un bloque recién declarado puede ser muy conveniente para ti.

Primero encuentra **Mis bloques** en la paleta de bloques, luego selecciona **Crear un bloque**.

.. image:: img/1.17_motor4.png

Ingresa el nombre del nuevo bloque.

.. image:: img/1.17_motor5.png

Después de escribir la función del nuevo bloque en el área de codificación, guárdalo y luego podrás encontrar el bloque en la paleta de bloques.

.. image:: img/1.17_motor6.png

**girar a la izquierda**

Este es el código dentro del bloque girar a la izquierda para hacer que el motor gire en sentido antihorario.

.. image:: img/1.17_motor12.png
  :width: 400

**girar a la derecha**

Este es el código dentro del bloque girar a la derecha para hacer que el motor gire en sentido horario.

.. image:: img/1.17_motor11.png
  :width: 400



