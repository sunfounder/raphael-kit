.. nota::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_relay:

Relé
==========================================

.. image:: img/relay_pic.png
    :width: 200
    :align: center

Como sabemos, el relé es un dispositivo que se utiliza para proporcionar 
conexión entre dos o más puntos o dispositivos en respuesta a la señal de 
entrada aplicada. En otras palabras, los relés proporcionan aislamiento entre 
el controlador y el dispositivo, ya que los dispositivos pueden funcionar tanto 
con CA como con CC. Sin embargo, reciben señales de un microcontrolador que funciona 
con CC, por lo que se requiere un relé para cerrar la brecha. El relé es extremadamente 
útil cuando necesitas controlar una gran cantidad de corriente o voltaje con una pequeña 
señal eléctrica.

Hay 5 partes en cada relé:

.. image:: img/relay142.jpeg

**Electroimán** - Consiste en un núcleo de hierro rodeado por una bobina de alambres. 
Cuando la electricidad pasa a través de él, se vuelve magnético. Por lo tanto, se llama electroimán.

**Armadura** - La tira magnética móvil se conoce como armadura. Cuando la corriente fluye a través 
de ellas, la bobina se energiza, produciendo un campo magnético que se usa para hacer o romper los 
puntos normalmente abiertos (N/O) o normalmente cerrados (N/C). La armadura puede moverse con 
corriente continua (CC) así como con corriente alterna (CA).

**Resorte** - Cuando no fluye corriente a través de la bobina en el electroimán, el resorte 
aleja la armadura, por lo que el circuito no puede completarse.

Conjunto de **contactos eléctricos** - Hay dos puntos de contacto:

- Normalmente abierto - conectado cuando el relé está activado y desconectado cuando está inactivo.
- Normalmente cerrado - no conectado cuando el relé está activado y conectado cuando está inactivo.

**Marco moldeado** - Los relés están cubiertos con plástico para su protección.

El principio de funcionamiento del relé es simple. Cuando se suministra energía al relé, 
la corriente comienza a fluir a través de la bobina de control; como resultado, el electroimán 
comienza a energizarse. Luego, la armadura es atraída hacia la bobina, tirando hacia abajo del 
contacto móvil y conectándose con los contactos normalmente abiertos. Así, el circuito con la 
carga se energiza. Luego, romper el circuito sería un caso similar, ya que el contacto móvil 
se elevará hacia los contactos normalmente cerrados bajo la fuerza del resorte. De esta manera, 
el encendido y apagado del relé puede controlar el estado de un circuito de carga.

**Ejemplo**

* :ref:`1.3.3_c` (C Project)
* :ref:`1.3.3_py` (Python Project)