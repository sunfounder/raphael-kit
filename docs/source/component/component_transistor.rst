.. note::

    ¡Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más profundamente en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a anuncios de nuevos productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _cpn_transistor:

Transistor
===============

.. image:: img/npn_pnp.png
    :width: 300

Un transistor es un dispositivo semiconductor que controla la corriente mediante la corriente. Funciona amplificando una señal débil a una señal de mayor amplitud y también se utiliza como interruptor sin contacto.

Un transistor es una estructura de tres capas compuesta por semiconductores de tipo P y N. Estas forman tres regiones internamente. La más delgada en el medio es la región base; las otras dos son ambas de tipo N o tipo P: la región más pequeña con la mayoría de los portadores es la región emisor, mientras que la otra es la región colector. Esta composición permite que el transistor sea un amplificador.
De estas tres regiones, se generan respectivamente tres polos, que son base (b), emisor (e) y colector (c). Forman dos uniones P-N, a saber, la unión emisor y la unión colector. La dirección de la flecha en el símbolo del circuito del transistor indica la de la unión emisor.

* `Unión P–N - Wikipedia <https://es.wikipedia.org/wiki/Unión_p-n>`_

Según el tipo de semiconductor, los transistores se pueden dividir en dos grupos: los NPN y los PNP. A partir de la abreviatura, podemos decir que el primero está hecho de dos semiconductores tipo N y uno tipo P, y que el segundo es lo contrario. Vea la figura a continuación.

.. note::
    El s8550 es un transistor PNP y el s8050 es uno NPN. Se ven muy similares y debemos revisar cuidadosamente para ver sus etiquetas.

.. image:: img/transistor_symbol.png
    :width: 600

Cuando una señal de nivel alto pasa a través de un transistor NPN, se energiza. Pero uno PNP necesita una señal de nivel bajo para manejarlo. Ambos tipos de transistores se utilizan frecuentemente para interruptores sin contacto, como en este experimento.

Coloca el lado de la etiqueta hacia nosotros y los pines hacia abajo. Los pines de izquierda a derecha son emisor (e), base (b) y colector (c).

.. image:: img/ebc.png
    :width: 150


* `Hoja de datos del transistor S8050 <https://datasheet4u.com/datasheet-pdf/WeitronTechnology/S8050/pdf.php?id=576670>`_
* `Hoja de datos del transistor S8550 <https://www.mouser.com/datasheet/2/149/SS8550-118608.pdf>`_

**Ejemplo**

* :ref:`1.2.1_c` (C Project)
* :ref:`1.3.3_c` (C Project)
* :ref:`1.2.2_py` (Python Project)
* :ref:`1.3.3_py` (Python Project)
* :ref:`1.14_scratch` (Scratch Project)
