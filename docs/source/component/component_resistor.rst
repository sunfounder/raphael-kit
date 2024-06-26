.. _cpn_resistor:

Résistance
===============

.. image:: img/resistor.png
    :width: 300

Une résistance est un composant électronique qui peut limiter le courant dans une branche de circuit. 
Une résistance fixe est un type de résistance dont la valeur ne peut être modifiée, tandis que celle d'un potentiomètre ou d'une résistance variable peut être ajustée. 

Voici deux symboles de circuit généralement utilisés pour une résistance. Normalement, la valeur de la résistance y est indiquée. Donc, si vous voyez ces symboles dans un circuit, cela représente une résistance. 

.. image:: img/resistor_symbol.png
    :width: 400

**Ω** est l'unité de résistance et les unités plus grandes incluent KΩ, MΩ, etc. 
Leur relation est la suivante : 1 MΩ = 1000 KΩ, 1 KΩ = 1000 Ω. Normalement, la valeur de la résistance est marquée dessus. 

Lors de l'utilisation d'une résistance, il est nécessaire de connaître sa valeur. Voici deux méthodes : vous pouvez observer les bandes sur la résistance ou utiliser un multimètre pour mesurer la résistance. Il est recommandé d'utiliser la première méthode car elle est plus pratique et plus rapide. 

.. image:: img/resistance_card.jpg

Comme indiqué sur la carte, chaque couleur représente un chiffre. 

.. list-table::

   * - Noir
     - Marron
     - Rouge
     - Orange
     - Jaune
     - Vert
     - Bleu
     - Violet
     - Gris
     - Blanc
     - Or
     - Argent
   * - 0
     - 1
     - 2
     - 3
     - 4
     - 5
     - 6
     - 7
     - 8
     - 9
     - 0,1
     - 0,01

Les résistances à 4 et 5 bandes sont fréquemment utilisées, avec respectivement 4 et 5 bandes colorées. 

Normalement, lorsque vous prenez une résistance, vous pouvez avoir du mal à décider de quel côté commencer pour lire les couleurs. 
L'astuce est que l'écart entre la 4e et la 5e bande sera comparativement plus grand.

Par conséquent, vous pouvez observer l'écart entre les deux bandes colorées à une extrémité de la résistance ; 
si cet écart est plus grand que les autres, vous pouvez lire à partir du côté opposé. 

Voyons comment lire la valeur d'une résistance à 5 bandes comme illustré ci-dessous.

.. image:: img/220ohm.jpg
    :width: 500

Pour cette résistance, la valeur doit être lue de gauche à droite. 
La valeur devrait être dans ce format : 1ère Bande 2e Bande 3e Bande x 10^Multiplicateur (Ω) et l'erreur admissible est ±Tolérance%. 
Ainsi, la valeur de cette résistance est 2(rouge) 2(rouge) 0(noir) x 10^0(noir) Ω = 220 Ω, 
et l'erreur admissible est ± 1% (marron). 

.. list-table:: Bandes de couleur communes des résistances
    :header-rows: 1

    * - Résistance 
      - Bande de couleur  
    * - 10Ω   
      - marron noir noir argent marron
    * - 100Ω   
      - marron noir noir noir marron
    * - 220Ω 
      - rouge rouge noir noir marron
    * - 330Ω 
      - orange orange noir noir marron
    * - 1kΩ 
      - marron noir noir marron marron
    * - 2kΩ 
      - rouge noir noir marron marron
    * - 5.1kΩ 
      - vert marron noir marron marron
    * - 10kΩ 
      - marron noir noir rouge marron 
    * - 100kΩ 
      - marron noir noir orange marron 
    * - 1MΩ 
      - marron noir noir vert marron 



Vous pouvez en apprendre davantage sur les résistances sur Wiki : `Resistor - Wikipedia <https://en.wikipedia.org/wiki/Resistor>`_.

