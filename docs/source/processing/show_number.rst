.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi & Arduino & ESP32 en Facebook! Profundiza en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y avances exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _show_number:

Mostrar Número
==============================

En este proyecto, utilizamos Processing para controlar un display de 7 segmentos y mostrar números del 0 al 9 y letras de la A a la F.

**Componentes necesarios**

En este proyecto, necesitamos los siguientes componentes.

Es definitivamente conveniente comprar un kit completo, aquí está el enlace:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Nombre	
        - ARTÍCULOS EN ESTE KIT
        - ENLACE
    *   - Kit Raphael
        - 337
        - |link_Raphael_kit|

También puedes comprarlos por separado en los enlaces a continuación.

.. list-table::
    :widths: 30 20
    :header-rows: 1

    *   - INTRODUCCIÓN DE COMPONENTES
        - ENLACE DE COMPRA

    *   - :ref:`cpn_gpio_extension_board`
        - |link_gpio_board_buy|
    *   - :ref:`cpn_breadboard`
        - |link_breadboard_buy|
    *   - :ref:`cpn_wires`
        - |link_wires_buy|
    *   - :ref:`cpn_resistor`
        - |link_resistor_buy|
    *   - :ref:`cpn_7_segment`
        - |link_7segment_buy|
    *   - :ref:`cpn_74hc595`
        - |link_74hc595_buy|

**Cableado**

.. image:: img/image125.png

**Esquema**

.. code-block:: arduino

    import processing.io.*;

	int SDI=17;   //serial data input
	int RCLK=18;  //memory clock input(STCP)
	int SRCLK =27;   //shift register clock input(SHCP)


    int[] SegCode= {0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71};

    void hc595_shift(int dat){
      int i;

      for(i=0;i<8;i++){
        int n=(0x80 & (dat << i)); 
        if ( n==0){
          GPIO.digitalWrite(SDI, 0);
        } else {
          GPIO.digitalWrite(SDI, 1);
        }
        GPIO.digitalWrite(SRCLK, 1);
        delay(1);
        GPIO.digitalWrite(SRCLK, 0);
      }

        GPIO.digitalWrite(RCLK, 1);
        delay(1);
        GPIO.digitalWrite(RCLK, 0);
    }

    void setup() {
        size(400, 200);
        frameRate(10);
        
        GPIO.pinMode(SDI, GPIO.OUTPUT); 
        GPIO.pinMode(RCLK, GPIO.OUTPUT); 
        GPIO.pinMode(SRCLK, GPIO.OUTPUT); 
      
        GPIO.digitalWrite(SDI, 0);
        GPIO.digitalWrite(RCLK, 0);
        GPIO.digitalWrite(SRCLK, 0);
        
        fill(0,25,88);
        textAlign(CENTER,CENTER);
        textSize(height*0.8);
    }

    void draw() {

        background(255);
        int number = (frameCount%100)/10;
        text(number, width/2, height/2);
        hc595_shift(SegCode[number]);
    }

**¿Cómo funciona?**

Importa ``processing.io.*`` y utiliza la biblioteca de funciones GPIO para controlar los pines del tubo digital.

Define el array ``SegCode = {0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71}``, 
que representa un array de códigos de segmentos desde 0 hasta F en hexadecimal (cátodo común).

La función ``setup()`` configura los tres pines SDI, RCLK y SRCLK como salida, y los datos iniciales como 0.

La función ``hc595_shift(int dat)`` se utiliza para desplazar el ``SegCode`` al 74HC595.
 
.. code:: 

    void hc595_shift(int dat){
      int i;

      for(i=0;i<8;i++){
        int n=(0x80 & (dat << i));
        if ( n==0){
          GPIO.digitalWrite(SDI, 0);
        } else {
          GPIO.digitalWrite(SDI, 1);
        }
        GPIO.digitalWrite(SRCLK, 1);
        delay(1);
        GPIO.digitalWrite(SRCLK, 0);
      }

        GPIO.digitalWrite(RCLK, 1);
        delay(1);
        GPIO.digitalWrite(RCLK, 0);
    }
 
``n=(0x80 & (dat << i))`` significa desplazar ``dat`` a la izquierda por ``i`` bits y luego hacer la operación ``&`` con 0x80.

La regla de la operación ``&`` es que cuando ambos lados de ``&`` son 1, el resultado es 1, de lo contrario, el resultado es 0.

Por ejemplo, asumimos dat=0x3f,i=2 (0011 1111 << 2 desplaza a 1111 1100), entonces 1111 1100 & 1000 0000 (0x80)) = 1000 0000.

Finalmente, asigna los datos de ``dat`` a SDI (DS) por bits.
 
 
``digitalWrite(SRCLK, 1)`` cuando SRCLK genera un pulso de flanco ascendente de 0 a 1, los datos se transferirán del registro DS al registro de desplazamiento;
 
``digitalWrite(RCLK, 1)`` cuando RCLK genera un pulso de flanco ascendente de 0 a 1, los datos se transferirán del registro de desplazamiento al registro de almacenamiento.

.. code::

    fill(0,25,88);
    textAlign(CENTER,CENTER);
    textSize(height*0.8);

La función ``fill()`` utilizada en ``setup()`` puede llenar el color del texto, ``textAlign(CENTER,CENTER)`` se usa para centrar el texto, ``textSize(height*0.8)`` cambia la altura del texto a 0.8 veces la original.
Estas funciones pueden personalizar el estilo del texto mostrado en Processing.

.. code::

    void draw() {

        background(255);
        int number = (frameCount%100)/10;
        text(number, width/2, height/2);
        hc595_shift(SegCode[number]);
    }

El ``frameCount`` es una semilla, que está relacionada con ``frameRate``.
Por defecto, ``frameRate`` es 60, lo que significa que ``frameCount`` se acumulará 60 veces por segundo.

Luego, podemos hacer que Processing y el display de 7 segmentos muestren la cifra de 0 a 9 y de la A a la F simultáneamente.
