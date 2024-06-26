 
.. _cpn_audio_speaker:

Module Audio et Haut-parleur
=================================

**Module Amplificateur Audio**

.. image:: img/audio_module.jpg
    :width: 500
    :align: center

Le module amplificateur audio contient une puce amplificatrice de puissance audio HXJ8002. Cette puce est un amplificateur de puissance à faible consommation qui peut fournir une puissance audio moyenne de 3W pour une charge BTL de 3Ω avec une distorsion harmonique faible (sous le seuil de 10% à 1KHz) à partir d'une alimentation de 5V DC. Cette puce peut amplifier les signaux audio sans aucun condensateur de couplage ou de bootstrap.

Le module peut être alimenté par une source de 2,0V à 5,5V DC avec un courant de fonctionnement de 10mA (0,6uA pour le courant de veille typique) et produire un son amplifié puissant dans un haut-parleur d'impédance 3Ω, 4Ω ou 8Ω. Ce module dispose d'un circuit amélioré de réduction des bruits de transition pour réduire significativement les bruits à l'allumage et à l'extinction. Sa petite taille, son efficacité élevée et sa faible consommation le rendent applicable dans de nombreux projets portables et alimentés par batterie ainsi que pour les microcontrôleurs.

* **IC**: HXJ8002
* **Tension d'entrée**: 2V ~ 5.5V
* **Courant en mode veille**: 0.6uA (valeur typique)
* **Puissance de sortie**: 3W (charge de 3Ω), 2.5W (charge de 4Ω), 1.5W (charge de 8Ω)
* **Impédance du haut-parleur de sortie**: 3Ω, 4Ω, 8Ω
* **Dimensions**: 19.8mm x 14.2mm

**Haut-parleur**

.. image:: img/speaker_pic.png
    :width: 300
    :align: center

* **Dimensions**: 20x30x7mm
* **Impédance**：8 ohms
* **Puissance d'entrée nominale**: 1.5W 
* **Puissance d'entrée maximale**: 2.0W
* **Longueur du fil**: 10 cm

.. image:: img/2030_speaker.png

Le tableau des dimensions est le suivant :

* :download:`Fiche technique du haut-parleur 2030 <https://github.com/sunfounder/sf-pdf/raw/master/datasheet/2030-speaker-datasheet.pdf>`

**Câble Audio**

.. image:: img/audio_cable_pic2.png
    :width: 500
    :align: center

Il s'agit d'un câble audio mâle de 3,5mm d'une longueur totale de 43cm. Il comporte 3 connecteurs : rouge pour le canal gauche, blanc pour le canal droit et GND au milieu.

**Circuit**

.. image:: img/4.1.4fritzing.png

Après avoir construit le circuit selon le schéma ci-dessus, branchez le câble audio dans la prise audio de 3,5 mm du Raspberry Pi.

.. image:: img/audio4.png
    :width: 400
    :align: center

Si votre haut-parleur ne produit aucun son, cela peut être dû au fait que le Raspberry Pi a sélectionné la mauvaise sortie audio (par défaut, c'est HDMI). Vous devez :ref:`changer_la_sortie_audio` pour **Casque**.

Si vous trouvez que le volume des haut-parleurs est trop bas, vous pouvez :ref:`ajuster_le_volume`.

**Exemple**

* :ref:`3.1.3_py` (Projet Python)
* :ref:`3.1.4_py` (Projet Python)
* :ref:`4.1.2_py` (Projet Python)
* :ref:`4.1.3_py` (Projet Python)
* :ref:`4.1.5_py` (Projet Python)
* :ref:`1.8_scratch` (Projet Scratch)
* :ref:`1.9_scratch` (Projet Scratch)
* :ref:`1.10_scratch` (Projet Scratch)
