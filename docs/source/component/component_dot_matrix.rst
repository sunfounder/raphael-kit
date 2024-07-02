.. nota::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_dot_matrix:

Módulo de Matriz LED
==============================

.. image:: img/max7219_module.jpg
    :width: 400
    :align: center

Este es un módulo de matriz de puntos 8x8 de cátodo común impulsado por el MAX7219. El voltaje de operación del módulo es de 5V, el tamaño es de 50mm x 32mm x 15mm. El lado izquierdo es el puerto de entrada, el lado derecho es el puerto de salida, soporta la cascada de múltiples módulos.

* **VCC**: Voltaje de suministro positivo. Conectar a +5V.
* **GND**: Tierra (ambos pines GND deben estar conectados).
* **DIN**: Entrada de datos seriales. Los datos se cargan en el registro de desplazamiento interno de 16 bits en el flanco ascendente de CLK.
* **CS**: Entrada de selección de chip. Los datos seriales se cargan en el registro de desplazamiento mientras CS está en bajo. Los últimos 16 bits de datos seriales se bloquean en el flanco ascendente de CS.
* **CLK**: Entrada de reloj serial. Tasa máxima de 10MHz. En el flanco ascendente de CLK, los datos se desplazan hacia el registro de desplazamiento interno. En el flanco descendente de CLK, los datos se desplazan fuera de DOUT. En el MAX7221, la entrada CLK solo está activa mientras CS está en bajo.

**MAX7219**

El MAX7219 es un controlador de pantalla de cátodo común de entrada/salida serial compacta que interconecta microprocesadores (µPs) con pantallas LED numéricas de 7 segmentos de hasta 8 dígitos, pantallas de barra gráfica o 64 LEDs individuales. Incluye un decodificador de código BCD en el chip, circuitos de escaneo de multiplex, controladores de segmento y dígito, y una RAM estática de 8x8 que almacena cada dígito.

Solo se requiere una resistencia externa para establecer la corriente de segmento para todos los LEDs. El MAX7221 es compatible con SPI™, QSPI™ y MICROWIRE™ y tiene controladores de segmento con velocidad de conmutación limitada para reducir EMI.

Una interfaz serial de 4 hilos conecta todos los µPs comunes. Los dígitos individuales se pueden direccionar y actualizar sin reescribir toda la pantalla. El MAX7219/MAX7221 también permite al usuario seleccionar decodificación de código B o sin decodificación para cada dígito.

.. image:: img/max7219_sche.png

* `Hoja de datos del MAX7219 <https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf>`_

**Ejemplo**

* :ref:`1.1.6_c` (C Project)
* :ref:`3.1.12_c` (C Project)
* :ref:`1.1.6_py` (Python Project)
* :ref:`4.1.19_py` (Python Project)
