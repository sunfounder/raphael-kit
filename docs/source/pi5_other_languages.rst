.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso temprano a anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Otros Lenguajes (para Pi 5)
==============================

El lanzamiento del Raspberry Pi 5 nos ha traído un modelo más potente, pero también ha introducido algunos cambios, especialmente en el GPIO.

Aunque mantiene su interfaz estándar de 40 pines, la funcionalidad ha cambiado debido a su conexión con el nuevo chip RP1 southbridge integrado. Este chip RP1 personalizado ahora maneja los periféricos en el Pi 5 y ha resultado en varias preocupaciones de compatibilidad.

Lenguaje C
-----------
La implementación en lenguaje C depende de la biblioteca wiringPi. Sin embargo, la biblioteca de la comunidad wiringPi ahora está archivada y ya no recibe actualizaciones, lo que la hace inadecuada para proyectos con Raspberry Pi 5. Para más información, consulta: https://github.com/WiringPi/WiringPi

.. image:: img/pi5_c_language.png

Processing
-------------
Al usar Processing 4 en Raspberry Pi 5, la programación GPIO enfrenta desafíos. Errores como "Invalid argument" y "GPIO pin 17 seems to be unavailable on your platform" surgen durante la ejecución de código relacionado con GPIO (como se muestra en la imagen adjunta). Para más detalles, visita: https://github.com/benfry/processing4/issues/807

.. image:: img/pi5_processing.png

Node.js
----------
Node.js utiliza la biblioteca pigpio, que, por ahora, no es compatible con Raspberry Pi 5. Para más información, visita: https://github.com/joan2937/pigpio/issues/589

.. image:: img/pi5_nodejs.png
    :width: 700

Scratch
----------
En un sistema de 64 bits, la importación de la biblioteca GPIO de Raspberry Pi enfrenta problemas, lo que lleva a la falta de respuesta. Para más información, visita: https://github.com/raspberrypi/bookworm-feedback/issues/91
