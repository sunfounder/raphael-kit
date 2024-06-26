.. _cpn_thermistor:

Thermistance
=================

.. image:: img/thermistor.png
    :width: 150
    :align: center

Une thermistance est un type de résistance dont la valeur dépend fortement de la température, bien plus que dans les résistances standards. Le mot est une combinaison de thermique et résistance. Les thermistances sont largement utilisées comme limiteurs de courant d'appel, capteurs de température (type à coefficient de température négatif ou NTC typiquement), protecteurs de surintensité auto-réarmables, et éléments chauffants auto-régulants (type à coefficient de température positif ou PTC typiquement).

* `Thermistance - Wikipédia <https://en.wikipedia.org/wiki/Thermistor>`_

Voici le symbole électronique de la thermistance.

.. image:: img/thermistor_symbol.png
    :width: 300
    :align: center

Il existe deux types fondamentaux de thermistances :

* Avec les thermistances NTC, la résistance diminue à mesure que la température augmente, généralement en raison d'une augmentation des électrons de conduction stimulés par l'agitation thermique de la bande de valence. Une NTC est couramment utilisée comme capteur de température ou en série avec un circuit comme limiteur de courant d'appel.
* Avec les thermistances PTC, la résistance augmente à mesure que la température augmente, généralement en raison de l'augmentation des agitations thermiques du réseau, en particulier celles des impuretés et des imperfections. Les thermistances PTC sont couramment installées en série avec un circuit et utilisées pour se protéger contre les conditions de surintensité, comme des fusibles réarmables.

Dans ce kit, nous utilisons une NTC. Chaque thermistance a une résistance normale. Ici, elle est de 10k ohms, mesurée à 25 degrés Celsius.

Voici la relation entre la résistance et la température :

    RT = RN * expB(1/TK – 1/TN)   

* **RT** est la résistance de la thermistance NTC lorsque la température est TK. 
* **RN** est la résistance de la thermistance NTC à la température nominale TN. Ici, la valeur numérique de RN est de 10k.
* **TK** est une température en Kelvin et l'unité est K. Ici, la valeur numérique de TK est de 273,15 + degrés Celsius.
* **TN** est une température nominale en Kelvin ; l'unité est également K. Ici, la valeur numérique de TN est de 273,15 + 25.
* Et **B(bêta)**, la constante matérielle de la thermistance NTC, est également appelée indice de sensibilité thermique avec une valeur numérique de 3950.      
* **exp** est l'abréviation de exponentielle, et le nombre de base e est un nombre naturel et vaut approximativement 2,7.  

Convertissez cette formule TK=1/(ln(RT/RN)/B+1/TN) pour obtenir la température en Kelvin, moins 273,15 égale degrés Celsius.

Cette relation est une formule empirique. Elle est précise uniquement lorsque la température et la résistance sont dans la plage effective.

**Exemple**

* :ref:`2.2.2_c` (Projet C)
* :ref:`3.1.4_c` (Projet C)
* :ref:`3.1.7_c` (Projet C)
* :ref:`2.2.2_py` (Projet Python)
* :ref:`4.1.10_py` (Projet Python)
* :ref:`4.1.13_py` (Projet Python)

