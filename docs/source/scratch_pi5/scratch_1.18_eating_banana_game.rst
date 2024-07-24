.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso temprano a anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _1.18_scratch_pi5:

1.18 Juego de Comer Plátano
==================================

Descripción
------------------

Scratch tiene un módulo de expansión de detección de video, que puede activar la cámara en Scratch y detectar el movimiento de objetos en la pantalla de la cámara.

Hoy, usaremos la cámara para hacer un juego de comer plátanos. En el tiempo estipulado, ayuda al Mono a comer más plátanos.

Para jugar el juego contra un fondo blanco, haz clic en la bandera verde para comenzar. Mueve objetos coloreados frente a la cámara para controlar el sprite del Mono.

.. image:: img/1.18_header.png

Componentes necesarios
---------------------------------

En este proyecto, necesitamos los siguientes componentes.

.. image:: img/1.18_photo1.png

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

    *   - :ref:`cpn_camera_module`
        - |link_camera_buy|

Construir el circuito
-----------------------------

.. image:: img/1.10_camera.png

.. note::

    Debes consultar :ref:`cpn_camera_module` para conectar el módulo de la cámara y habilitar la interfaz de la cámara de Raspberry Pi.

Cargar el código y ver qué pasa
--------------------------------------------

Carga el archivo de código (``1.18_eating_banana_game.sb3``) en Scratch 3.

Consejos sobre el código
---------------------------------

Organizar monos y plátanos

Primero, eliminamos el sprite original, luego agregamos el sprite del Mono y el sprite de Plátanos, y cambiamos sus tamaños a 50.

Deja que los Plátanos aparezcan al azar.

.. image:: img/1.18_code1.png

Los Plátanos desaparecen después de encontrarse con el Mono, lo que significa que fueron comidos por el Mono y reaparecen al azar.

.. image:: img/1.18_code2.png

Haz que el Mono aparezca en el centro del escenario e inicializa los datos de la cámara (la transparencia se establece en 20).

.. image:: img/1.18_code3.png

Si la cámara detecta un objeto en movimiento, haz que el Mono se mueva hacia el objeto.

.. image:: img/1.18_code4.png

Ahora, haz clic en la bandera verde en la parte superior del área del escenario para comenzar el juego.

Deja que el Mono coma plátanos, ¡está muy hambriento! Intenta jugar este juego en un fondo blanco para evitar interferencias de otros objetos.


Desafío
----------------

Creo que serás lo suficientemente inteligente como para programar e implementar este juego pronto. A continuación, agregaremos algunos desafíos para enriquecer nuestro contenido del juego.

· Cuando el Mono come un plátano, sumamos 1 al puntaje. ¡Dentro de 30 segundos, veamos quién tiene el puntaje más alto!

· Cuando el Mono come un plátano, emite un efecto de sonido adecuado.
