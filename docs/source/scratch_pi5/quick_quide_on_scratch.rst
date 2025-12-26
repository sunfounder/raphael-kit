.. note::

    Hola, bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Vistas previas exclusivas**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _quick_quide_on_scratch_pi5:

Guía rápida sobre Scratch
============================

.. note::

    Al programar con Scratch 3, puede que necesites una pantalla para una mejor experiencia. Consulta: `Conecta tu Raspberry Pi <https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/3>`_. Por supuesto, si no tienes una pantalla, también puedes acceder al escritorio de Raspberry Pi de forma remota. Para un tutorial detallado, consulta :ref:`remote_desktop`.

Además, Scratch 3 necesita al menos 1GB de RAM para funcionar. Recomendamos una Raspberry Pi 4 con al menos 2GB de RAM. Aunque puedes ejecutar Scratch 3 en una Raspberry Pi 2, 3, 3B+ o una Raspberry 4 con 1GB de RAM, el rendimiento en estos modelos se reduce y, dependiendo de qué otro software ejecutes al mismo tiempo, Scratch 3 puede no iniciarse debido a la falta de memoria.

Instalar Scratch 3
----------------------
Al instalar Raspberry Pi OS (:ref:`install_os`), debes elegir la versión con escritorio, ya sea con solo escritorio o con escritorio y software recomendado.

Si instalas la versión con el software recomendado, puedes ver Scratch 3 en el menú del sistema en **Programación**.

Si instalaste la versión solo con escritorio, necesitarás instalar Scratch 3 manualmente, como se describe a continuación.

Abre el menú, haz clic en **Preferencias** -> **Software recomendado**.

.. image:: img/quick_scratch1.png


Busca Scratch 3 y márcalo, luego haz clic en **Aplicar** y espera a que la instalación termine.

.. image:: img/quick_scratch2.png


Una vez que la instalación esté completa, deberías verlo en **Programación** en el menú del sistema.

.. image:: img/quick_scratch3.png


Sobre la interfaz de Scratch 3
----------------------------------

Scratch 3 está diseñado para ser divertido, educativo y fácil de aprender. Tiene herramientas para crear historias interactivas, juegos, arte, simulaciones y más, utilizando programación basada en bloques. Scratch también tiene su propio editor de pintura y editor de sonido integrados.

La parte superior de Scratch 3 tiene algunas opciones básicas. La primera de izquierda a derecha es la opción de idioma, puedes elegir diferentes idiomas para programar. La segunda es la opción **Archivo**, donde puedes crear nuevos archivos, leer archivos locales y guardar los archivos actuales. La tercera es la opción **Editar**, que te permite reanudar algunas operaciones de eliminación y habilitar el modo de aceleración (en el cual el movimiento del sprite se vuelve particularmente rápido). La cuarta es la opción **Tutoriales**, que te permite ver tutoriales para algunos proyectos. La quinta es la opción de nombrar archivos, donde puedes renombrar el proyecto.

.. image:: img/quick_scratch13.png


**Código**

Tiene tres secciones principales: un área de escenario, una paleta de bloques y un área de codificación. Programa haciendo clic y arrastrando los bloques de la paleta de bloques al área de codificación, y finalmente tus resultados de programación se mostrarán en el área de escenario.

.. image:: img/quick_scratch4.png


Aquí está el área de sprites de Scratch 3. Encima del área están los parámetros básicos de los sprites, puedes agregar sprites que vienen con Scratch 3 o subir sprites locales.

.. image:: img/quick_scratch5.png


Aquí está el área de fondo de Scratch 3, principalmente para agregar un fondo adecuado para tu escenario, puedes agregar el fondo que viene con Scratch 3 o subir uno local.

.. image:: img/quick_scratch6.png


Este es un botón de **Agregar extensión**.

.. image:: img/quick_scratch7.png


En Scratch 3, podemos agregar todo tipo de extensiones útiles. Aquí tomamos **Detección de video** como ejemplo y hacemos clic en ella.

.. image:: img/quick_scratch8.png


Lo verás en la paleta de bloques y podrás usar las funciones asociadas con esta extensión. Si tienes una cámara conectada, verás la pantalla de la cámara en el área de escenario.

.. image:: img/quick_scratch9.png

**Disfraces**

Haz clic en la opción **Disfraces** en la esquina superior izquierda para ingresar a la paleta de disfraces. Diferentes disfraces permiten que los sprites tengan diferentes movimientos estáticos, y cuando estos movimientos estáticos se juntan, forman un movimiento dinámico coherente.

.. image:: img/quick_scratch10.png

**Sonidos**

Es posible que necesites usar algunos clips de música para hacer tus experimentos más interesantes. Haz clic en la opción **Sonidos** en la esquina superior izquierda y puedes editar el sonido actual o seleccionar/subir uno nuevo.

.. image:: img/quick_scratch11.png
