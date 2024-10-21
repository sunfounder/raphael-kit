.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_7_segment:

Pantalla de 7 segmentos
===========================

.. image:: img/7-seg.jpg

Una pantalla de 7 segmentos es un componente con forma de 8 que agrupa 7 LEDs. Cada LED se llama segmento; cuando se energiza, un segmento forma parte de un número para ser mostrado.

Hay dos tipos de conexión de pines: Cátodo Común (CC) y Ánodo Común (CA). Como su nombre indica, una pantalla CC tiene todos los cátodos de los 7 LEDs conectados, mientras que una pantalla CA tiene todos los ánodos de los 7 segmentos conectados.

En este kit, usamos la pantalla de 7 segmentos de Cátodo Común, aquí está el símbolo electrónico.

.. image:: img/segment_cathode.png
    :width: 800

Cada uno de los LEDs en la pantalla tiene un segmento posicional con uno de sus pines de conexión saliendo del paquete de plástico rectangular. Estos pines de LED están etiquetados de "a" a "g", representando cada LED individual. Los otros pines de LED están conectados juntos formando un pin común. Así, polarizando directamente los pines apropiados de los segmentos de LED en un orden particular, algunos segmentos se iluminarán y otros permanecerán apagados, mostrando así el carácter correspondiente en la pantalla. 

**Códigos de visualización** 

Para ayudarte a conocer cómo las pantallas de 7 segmentos (Cátodo Común) muestran números, hemos dibujado la siguiente tabla. Los números son del 0-F mostrados en la pantalla de 7 segmentos; (DP) GFEDCBA se refiere al conjunto de LED correspondiente configurado en 0 o 1. Por ejemplo, 00111111 significa que DP y G están configurados en 0, mientras que los demás están configurados en 1. Por lo tanto, el número 0 se muestra en la pantalla de 7 segmentos, mientras que el código HEX corresponde al número hexadecimal.

.. image:: img/segment_code.png

**Ejemplo**

* :ref:`1.1.4_c` (C Project)
* :ref:`1.1.4_py` (Python Project)
