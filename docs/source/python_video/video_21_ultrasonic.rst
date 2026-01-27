.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y avances.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Video 21: Uso de un Sensor Ultrasónico HC-SR04 para Ecolocación
=======================================================================================

Este tutorial cubre el proceso de crear un sensor de distancia ultrasónico con una Raspberry Pi usando el sensor HC-SR04. 
El video explica los principios de la ecolocación, introduce los componentes necesarios, demuestra la configuración del cableado 
y guía paso a paso el proceso de codificación. 
Se enfatiza la importancia de la sincronización precisa en la ejecución del código para obtener mediciones de distancia exactas y se promueven buenas prácticas de ingeniería.

1. **Introducción a la Ecolocación**: Uso del sonido para detectar la posición de objetos, inspirado por murciélagos y ballenas.
2. **Descripción de los Componentes**: Introducción al sensor ultrasónico HC-SR04 y su conexión a la Raspberry Pi.
3. **Configuración del Cableado**: Conexión del sensor HC-SR04 a los pines GPIO de la Raspberry Pi para energía, tierra, disparo y eco.
4. **Proceso de Codificación**: Recorrido por el código en Python para generar pulsos ultrasónicos, activar el sensor y medir el tiempo de retorno del eco.
5. **Consideraciones de Tiempo**: Importancia de la sincronización precisa para la medición exacta de distancias.
6. **Buenas Prácticas de Ingeniería**: Enfatiza la planificación y comprensión del código antes de la implementación.
7. **Esperando el Pin de Eco**: Uso de un bucle while para esperar a que el pin de eco se active.
8. **Registro del Tiempo de Inicio**: Captura del tiempo del sistema cuando el pin de eco se activa para marcar el inicio de la medición.
9. **Medición del Tiempo de Viaje del Ping**: Cálculo del tiempo de viaje del ping determinando la diferencia de tiempo entre la activación y desactivación del pin de eco.
10. **Conversión de Unidades**: Multiplicación del tiempo de viaje del ping por un millón para mejorar la legibilidad.
11. **Añadiendo Retraso**: Introducción de un retraso después de cada medición para evitar múltiples ecos.
12. **Cálculo de la Distancia**: Uso de la velocidad del sonido y el tiempo de viaje del ping para calcular la distancia al objetivo.

**Video**

.. raw:: html

    <iframe width="100%" 
    style="aspect-ratio: 16/9; max-width: 100%;"
    src="https://www.youtube.com/embed/SoAGLXoQ5XI?si=OPMqLtQ53hKNHs4j" 
    title="YouTube video player" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    allowfullscreen>
    </iframe>
