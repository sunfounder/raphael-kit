.. nota::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_4_digit:

Pantalla de 7 segmentos y 4 dígitos
========================================

La pantalla de 7 segmentos y 4 dígitos consta de cuatro pantallas de 7 segmentos que trabajan juntas.

.. image:: img/4-digit-sche.png

La pantalla de 7 segmentos y 4 dígitos funciona de forma independiente. 
Utiliza el principio de persistencia visual humana para mostrar rápidamente 
los caracteres de cada segmento de 7 en un bucle para formar cadenas continuas.

Por ejemplo, cuando se muestra "1234" en la pantalla, "1" se muestra en el primer 
segmento de 7, y "234" no se muestra. Después de un período de tiempo, el segundo 
segmento de 7 muestra "2", el 1º, 3º y 4º de 7 segmentos no se muestran, y así 
sucesivamente, la pantalla digital muestra en turno. Este proceso es muy corto 
(normalmente 5 ms), y debido al efecto de posimagen óptica y el principio de 
residuo visual, podemos ver cuatro caracteres al mismo tiempo.

.. image:: img/image78.png

**Códigos de visualización**

Para ayudarte a conocer cómo las pantallas de 7 segmentos (Ánodo Común) muestran números, 
hemos dibujado la siguiente tabla. Los números son del 0-F mostrados en la pantalla de 7 
segmentos; (DP) GFEDCBA se refiere al conjunto de LED correspondiente configurado en 0 o 1. 
Por ejemplo, 11000000 significa que DP y G están configurados en 1, mientras que los demás 
están configurados en 0. Por lo tanto, el número 0 se muestra en la pantalla de 7 segmentos, 
mientras que el código HEX corresponde al número hexadecimal.

.. image:: img/common_anode.png

**Ejemplo**

* :ref:`1.1.5_c` (C Project)
* :ref:`3.1.1_c` (C Project)
* :ref:`3.1.6_c` (C Project)
* :ref:`3.1.12_c` (C Project)
* :ref:`1.1.5_py` (Python Project)
* :ref:`4.1.3_py` (Pyhton Project)
* :ref:`4.1.7_py` (Pyhton Project)
* :ref:`4.1.12_py` (Pyhton Project)
* :ref:`4.1.18_py` (Pyhton Project)

