.. _cpn_mpu6050:

Module MPU6050
===================

.. image:: img/mpu6050_pic.png
    :width: 200
    :align: center

Le MPU-6050 est un dispositif de suivi de mouvement à 6 axes (combinant un gyroscope à 3 axes et 
un accéléromètre à 3 axes).

Ses trois systèmes de coordonnées sont définis comme suit :

Placez le MPU6050 à plat sur la table, assurez-vous que la face avec l'étiquette est vers le haut 
et qu'un point sur cette surface est dans le coin supérieur gauche. Ensuite, la direction verticale
vers le haut est l'axe Z de la puce. La direction de gauche à droite est considérée comme l'axe X.
Par conséquent, la direction de l'arrière vers l'avant est définie comme l'axe Y.

.. image:: img/mpu223.png

**Accéléromètre 3 axes**

L'accéléromètre fonctionne sur le principe de l'effet piézoélectrique, c'est-à-dire la capacité de 
certains matériaux à générer une charge électrique en réponse à une contrainte mécanique appliquée.

Ici, imaginez une boîte cuboïdale contenant une petite balle à l'intérieur, comme sur l'image 
ci-dessus. Les parois de cette boîte sont faites de cristaux piézoélectriques. Chaque fois que 
vous inclinez la boîte, la balle est forcée de se déplacer dans la direction de l'inclinaison en 
raison de la gravité. La paroi avec laquelle la balle entre en collision crée de minuscules 
courants piézoélectriques. Il y a au total trois paires de parois opposées dans un cuboïde. 
Chaque paire correspond à un axe dans l'espace 3D : les axes X, Y et Z. En fonction du courant 
produit par les parois piézoélectriques, nous pouvons déterminer la direction de l'inclinaison 
et son amplitude.

Ici, imaginez une boîte cuboïdale, contenant une petite balle à l'intérieur, comme sur l'image ci-dessus. Les parois de cette boîte sont faites de cristaux piézoélectriques. Chaque fois que vous inclinez la boîte, la balle est forcée de se déplacer dans la direction de l'inclinaison, en raison de la gravité. La paroi avec laquelle la balle entre en collision crée de minuscules courants piézoélectriques. Il y a en tout trois paires de parois opposées dans un cuboïde. Chaque paire correspond à un axe dans l'espace 3D : les axes X, Y et Z. En fonction du courant produit par les parois piézoélectriques, nous pouvons déterminer la direction de l'inclinaison et son amplitude.

.. image:: img/mpu224.png

Nous pouvons utiliser le MPU6050 pour détecter son accélération sur chaque axe de coordonnées (dans l'état 
de bureau stationnaire, l'accélération de l'axe Z est de 1 unité de gravité, et les axes X et Y 
sont à 0). S'il est incliné ou en condition d'apesanteur/surchargée, la lecture correspondante changera.

Il existe quatre types de plages de mesure qui peuvent être sélectionnées 
par programmation : +/-2g, +/-4g, +/-8g et +/-16g (2g par défaut) correspondant 
à chaque précision. Les valeurs varient de -32768 à 32767.

La lecture de l'accéléromètre est convertie en valeur d'accélération en mappant la lecture de la 
plage de lecture à la plage de mesure.

Accélération = (Données brutes de l'axe de l'accéléromètre / 65536 * plage d'accélération à 
pleine échelle) g

Prenons l'axe X comme exemple, lorsque les données brutes de l'axe X de l'accéléromètre sont 
de 16384 et que la plage est sélectionnée à +/-2g :

**Accélération le long de l'axe X = (16384 / 65536 * 4) g**  **=1g**

**Gyroscope 3 axes**

Les gyroscopes fonctionnent sur le principe de l'accélération de Coriolis. Imaginez qu'il y a 
une structure en forme de fourche, qui est en mouvement constant d'avant en arrière. 
Elle est maintenue en place à l'aide de cristaux piézoélectriques. Chaque fois que vous 
essayez d'incliner cet agencement, les cristaux subissent une force dans la direction 
de l'inclinaison. Cela est causé par l'inertie de la fourche en mouvement. 
Les cristaux produisent ainsi un courant en accord avec l'effet piézoélectrique, 
et ce courant est amplifié.

.. image:: img/mpu225.png

Le gyroscope dispose également de quatre types de plages de mesure : +/- 250, +/- 500, +/- 1000, +/- 2000. 
La méthode de calcul et l'accélération sont essentiellement cohérentes.

La formule pour convertir la lecture en vitesse angulaire est la suivante :

Vitesse angulaire = (Données brutes de l'axe du gyroscope / 65536 * plage du gyroscope à 
pleine échelle) °/s

Par exemple, pour l'axe X, les données brutes de l'axe X du gyroscope sont de 16384 
et la plage est de +/- 250°/s :

**Vitesse angulaire le long de l'axe X = (16384 / 65536 \* 500)°/s** **=125°/s**

**Exemple**

* :ref:`2.2.9_c` (Projet C)
* :ref:`2.2.9_py` (Projet Python)
