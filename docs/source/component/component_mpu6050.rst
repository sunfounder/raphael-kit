.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Avances exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más nuevos.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones festivas.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _cpn_mpu6050:

Módulo MPU6050
===================

.. image:: img/mpu6050_pic.png
    :width: 200
    :align: center

El MPU-6050 es un dispositivo de seguimiento de movimiento de 6 ejes 
(combina un giroscopio de 3 ejes y un acelerómetro de 3 ejes).

Sus tres sistemas de coordenadas se definen de la siguiente manera:

Coloca el MPU6050 plano sobre la mesa, asegurándote de que la cara con la 
etiqueta esté hacia arriba y que un punto en esta superficie esté en la 
esquina superior izquierda. Entonces, la dirección vertical hacia arriba 
es el eje Z del chip. La dirección de izquierda a derecha se considera el 
eje X. En consecuencia, la dirección de atrás hacia adelante se define como el eje Y.

.. image:: img/mpu223.png

**Acelerómetro de 3 ejes**

El acelerómetro funciona con el principio del efecto piezoeléctrico, 
la capacidad de ciertos materiales para generar una carga eléctrica 
en respuesta a un estrés mecánico aplicado.

Imagina una caja cúbica, que tiene una pequeña bola dentro, como en 
la imagen anterior. Las paredes de esta caja están hechas de cristales 
piezoeléctricos. Siempre que inclines la caja, la bola se verá obligada 
a moverse en la dirección de la inclinación debido a la gravedad. 
La pared con la que la bola colisiona crea pequeñas corrientes piezoeléctricas. 
Hay en total tres pares de paredes opuestas en un cuboide. Cada par corresponde 
a un eje en el espacio 3D: los ejes X, Y y Z. Dependiendo de la corriente producida 
por las paredes piezoeléctricas, podemos determinar la dirección de la inclinación y su magnitud.

.. image:: img/mpu224.png

Podemos usar el MPU6050 para detectar su aceleración en cada eje de coordenadas 
(en estado estacionario sobre el escritorio, la aceleración del eje Z es de 1 
unidad de gravedad, y los ejes X e Y son 0). Si se inclina o está en una condición 
de ingravidez/sobrecarga, la lectura correspondiente cambiará.

Hay cuatro tipos de rangos de medición que se pueden seleccionar programáticamente: 
+/-2g, +/-4g, +/-8g y +/-16g (2g por defecto) correspondientes a cada precisión. 
Los valores varían de -32768 a 32767.

La lectura del acelerómetro se convierte en un valor de aceleración mapeando la 
lectura desde el rango de lectura al rango de medición.

Aceleración = (Datos brutos del eje del acelerómetro / 65536 * Rango completo de aceleración) g

Tomemos el eje X como ejemplo, cuando los datos brutos del eje X del acelerómetro son 16384 y 
el rango es seleccionado como +/-2g:

**Aceleración a lo largo del eje X = (16384 / 65536 * 4) g**  **= 1g**

**Giroscopio de 3 ejes**

Los giroscopios funcionan con el principio de la aceleración de Coriolis. Imagina una estructura 
similar a un tenedor que está en constante movimiento de vaivén. Está sostenida en su lugar usando 
cristales piezoeléctricos. Siempre que intentes inclinar esta disposición, los cristales experimentan 
una fuerza en la dirección de la inclinación. Esto se debe a la inercia del tenedor en movimiento. 
Los cristales, por lo tanto, producen una corriente de acuerdo con el efecto piezoeléctrico, 
y esta corriente se amplifica.

.. image:: img/mpu225.png

El giroscopio también tiene cuatro tipos de rangos de medición: +/- 250, +/- 500, 
+/- 1000, +/- 2000. El método de cálculo y la aceleración son básicamente consistentes.

La fórmula para convertir la lectura en velocidad angular es la siguiente:

Velocidad angular = (Datos brutos del eje del giroscopio / 65536 * Rango completo del giroscopio) °/s

Por ejemplo, para el eje X, si los datos brutos del eje X del giroscopio son 16384 y el rango es +/- 250°/s:

**Velocidad angular a lo largo del eje X = (16384 / 65536 * 500)°/s** **= 125°/s**

**Ejemplo**

* :ref:`2.2.9_c` (C Project)
* :ref:`2.2.9_py` (Python Project)