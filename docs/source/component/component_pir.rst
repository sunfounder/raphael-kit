.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_pir:

Módulo Sensor de Movimiento PIR
==================================

.. image:: img/pir_pic.png
    :width: 300
    :align: center

El sensor PIR detecta la radiación de calor infrarrojo que puede ser utilizada para detectar la presencia de organismos que emiten radiación de calor infrarrojo.

El sensor PIR está dividido en dos ranuras que están conectadas a un amplificador diferencial. Cuando un objeto estático se encuentra frente al sensor, las dos ranuras reciben la misma cantidad de radiación y la salida es cero. Cuando un objeto en movimiento se encuentra frente al sensor, una de las ranuras recibe más radiación que la otra, lo que hace que la salida fluctúe hacia arriba o hacia abajo. Este cambio en el voltaje de salida es el resultado de la detección de movimiento.

.. image:: img/PIR_working_principle.jpg
    :width: 800

Después de cablear el módulo sensor, hay una inicialización de un minuto. Durante la inicialización, el módulo se activará de 0 a 3 veces en intervalos. Luego, el módulo estará en modo de espera. Por favor, mantén alejadas las interferencias de fuentes de luz y otras fuentes de la superficie del módulo para evitar la operación incorrecta causada por la señal de interferencia. Incluso es mejor usar el módulo sin demasiado viento, ya que el viento también puede interferir con el sensor.

.. image:: img/pir_back.png
    :width: 600
    :align: center

**Ajuste de Distancia**

Girando la perilla del potenciómetro de ajuste de distancia en el sentido de las agujas del reloj, el rango de distancia de detección aumenta, y el rango máximo de distancia de detección es de aproximadamente 0-7 metros. Si se gira en sentido antihorario, el rango de distancia de detección se reduce, y el rango mínimo de distancia de detección es de aproximadamente 0-3 metros.

**Ajuste de Retardo**

Girando la perilla del potenciómetro de ajuste de retardo en el sentido de las agujas del reloj, también se puede ver que el retardo de detección aumenta. El máximo del retardo de detección puede llegar hasta 300 segundos. Por el contrario, si se gira en sentido antihorario, se puede reducir el retardo con un mínimo de 5 segundos.

**Dos Modos de Disparo**

Seleccionando diferentes modos usando el puente.

* **H**: Modo de disparo repetible, después de detectar el cuerpo humano, el módulo emite un nivel alto. Durante el período de retardo subsiguiente, si alguien entra en el rango de detección, la salida seguirá siendo de nivel alto.

* **L**: Modo de disparo no repetible, emite un nivel alto cuando detecta el cuerpo humano. Después del retardo, la salida cambiará automáticamente de nivel alto a nivel bajo.

**Ejemplo**

* :ref:`2.2.7_c` (C Project)
* :ref:`2.2.7_py` (Python Project)
* :ref:`4.1.4_py` (Python Project)
* :ref:`1.5_scratch` (Scratch Project)

