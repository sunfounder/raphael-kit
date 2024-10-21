.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprender y compartir**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_audio_speaker:

Módulo de Audio y Altavoz
==============================

**Módulo Amplificador de Audio**

.. image:: img/audio_module.jpg
    :width: 500
    :align: center

El Módulo Amplificador de Audio contiene un chip amplificador de audio HXJ8002. Este chip es un amplificador de potencia con bajo consumo de energía, que puede proporcionar 3W de potencia de audio promedio para una carga BTL de 3Ω con baja distorsión armónica (bajo el umbral de distorsión del 10% a 1KHz) a partir de una fuente de alimentación de 5V DC. Este chip puede amplificar señales de audio sin ningún condensador de acoplamiento o condensador bootstrap.

El módulo puede ser alimentado por una fuente de alimentación de 2.0V hasta 5.5V DC con una corriente operativa de 10mA (0.6uA para corriente típica en modo de espera) y producir un sonido amplificado potente en un altavoz de 3Ω, 4Ω u 8Ω de impedancia. Este módulo tiene un circuito mejorado de reducción de ruidos para minimizar significativamente el ruido de transición al encenderse y apagarse. El tamaño pequeño, además de la alta eficiencia y bajo consumo de energía, lo hace aplicable en una amplia variedad de proyectos portátiles y alimentados por batería, así como en microcontroladores.

* **IC**: HXJ8002
* **Voltaje de Entrada**: 2V ~ 5.5V
* **Corriente en Modo de Espera**: 0.6uA (valor típico)
* **Potencia de Salida**: 3W (carga de 3Ω), 2.5W (carga de 4Ω), 1.5W (carga de 8Ω)
* **Impedancia de Salida del Altavoz**: 3Ω, 4Ω, 8Ω
* **Tamaño**: 19.8mm x 14.2mm

**Altavoz**

.. image:: img/speaker_pic.png
    :width: 300
    :align: center

* **Tamaño**: 20x30x7mm
* **Impedancia**：8 ohmios
* **Potencia de Entrada Nominal**: 1.5W 
* **Potencia de Entrada Máxima**: 2.0W
* **Longitud del Cable**: 10cm

.. image:: img/2030_speaker.png

La tabla de tamaños es la siguiente：

* :download:`Hoja de Datos del Altavoz 2030 <https://github.com/sunfounder/sf-pdf/raw/master/datasheet/2030-speaker-datasheet.pdf>`

**Cable de Audio**

.. image:: img/audio_cable_pic2.png
    :width: 500
    :align: center

Este es un cable de audio macho de 3.5mm con una longitud total de 43cm. Tiene 3 conectores: rojo para el canal izquierdo, blanco para el canal derecho y GND en el medio.

**Circuito**

.. image:: img/4.1.4fritzing.png

Después de construir el circuito según el diagrama anterior, conecta el cable de audio en el conector de audio de 3.5mm de la Raspberry Pi.

.. image:: img/audio4.png
    :width: 400
    :align: center

Si tu altavoz no emite sonido, puede ser porque la Raspberry Pi ha seleccionado la salida de audio incorrecta (por defecto es HDMI), necesitas :ref:`change_audio_output` a **Auriculares**.

Si sientes que el volumen de los altavoces es muy bajo, puedes :ref:`adjust_volume`.

**Ejemplo**

* :ref:`3.1.3_py` (Python Project)
* :ref:`3.1.4_py` (Python Project)
* :ref:`4.1.2_py` (Python Project)
* :ref:`4.1.3_py` (Python Project)
* :ref:`4.1.5_py` (Python Project)
* :ref:`1.8_scratch` (Scratch Project)
* :ref:`1.9_scratch` (Scratch Project)
* :ref:`1.10_scratch` (Scratch Project)
