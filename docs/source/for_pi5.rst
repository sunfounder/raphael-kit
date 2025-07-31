.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y Compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y Sorteos Festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Para todos los modelos (recomendado)
==================================================

El lanzamiento del Raspberry Pi 5 nos ha traído un modelo más potente, pero también ha introducido algunos cambios, 
especialmente en el GPIO. Aunque conserva su interfaz estándar de 40 pines, su funcionalidad ha cambiado debido a 
su conexión con el nuevo chip RP1 southbridge integrado. Este chip RP1 personalizado ahora maneja los periféricos 
en el Pi 5, lo que ha generado varias preocupaciones de compatibilidad. Actualmente, solo la biblioteca GPIO Zero, 
mantenida oficialmente por la organización Raspberry Pi, es totalmente compatible. Hemos desarrollado una serie de 
cursos específicamente enfocados en esta biblioteca.

.. toctree::
    :maxdepth: 1
    
    python_pi5/play_with_python_pi5
    c_pi5/play_with_c
    scratch_pi5/play_with_scratch

Para problemas de compatibilidad con otros lenguajes de programación, consulte la información detallada a continuación:

**Lenguaje C**

.. note::

    * La biblioteca wiringPi ha sido compatible con el Raspberry Pi 5 a partir de la versión 3.0. Sin embargo, en la última versión, la funcionalidad PWM aún está en desarrollo.
    * Actualmente estamos utilizando la última versión de wiringPi para actualizar nuestros cursos y hacerlos compatibles con el Raspberry Pi 5. Por favor, manténgase atento a las actualizaciones.

La implementación en lenguaje C depende de la biblioteca wiringPi. Sin embargo, la biblioteca comunitaria wiringPi ahora está archivada y ya no recibe actualizaciones, lo que la hace inadecuada para proyectos en Raspberry Pi 5. Para obtener más información, consulte: https://github.com/WiringPi/WiringPi.

.. image:: img/pi5_c_language.png

**Processing**

Al usar Processing 4 en Raspberry Pi 5, la programación GPIO enfrenta desafíos. Durante la ejecución del código relacionado con GPIO, surgen errores como "Invalid argument" y "GPIO pin 17 seems to be unavailable on your platform" (como se muestra en la imagen adjunta). Para obtener más detalles, visite: https://github.com/benfry/processing4/issues/807

.. image:: img/pi5_processing.png

**Node.js**

Node.js utiliza la biblioteca pigpio, que hasta ahora no es compatible con Raspberry Pi 5. Para más información, visite: https://github.com/joan2937/pigpio/issues/589

.. image:: img/pi5_nodejs.png
    :width: 700

**Scratch**

.. note::
 
    * La versión 3.30.8 de Scratch 3 ahora es compatible con Raspberry Pi 5. 
    * También estamos actualizando nuestros cursos para que sean compatibles con Raspberry Pi 5. Espere estas actualizaciones.

En un sistema de 64 bits, la importación de la biblioteca GPIO de Raspberry Pi presenta problemas, lo que provoca falta de respuesta. Para obtener más información, visite: https://github.com/raspberrypi/bookworm-feedback/issues/91.
