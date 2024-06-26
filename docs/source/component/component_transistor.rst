.. _cpn_transistor:

Transistor
============

.. image:: img/npn_pnp.png
    :width: 300

Un transistor est un dispositif semi-conducteur qui contrôle le courant par le courant. Il fonctionne en amplifiant un signal faible en un signal de plus grande amplitude et est également utilisé comme interrupteur sans contact.

Un transistor est une structure à trois couches composée de semi-conducteurs de type P et de type N. Ils forment trois régions internes. La région la plus mince au milieu est la base ; les deux autres sont soit des régions de type N soit de type P – la plus petite région avec une forte concentration de porteurs majoritaires est la région émettrice, tandis que l'autre est la région collectrice. Cette composition permet au transistor d'être un amplificateur.
À partir de ces trois régions, trois pôles sont générés respectivement : base (b), émetteur (e) et collecteur (c). Ils forment deux jonctions P-N, à savoir la jonction émettrice et la jonction collectrice. La direction de la flèche dans le symbole du circuit du transistor indique celle de la jonction émettrice.

* `Jonction P-N - Wikipédia <https://fr.wikipedia.org/wiki/Jonction_p-n>`_

En fonction du type de semi-conducteur, les transistors peuvent être divisés en deux groupes : les NPN et les PNP. À partir de l'abréviation, on peut dire que le premier est composé de deux semi-conducteurs de type N et d'un de type P, tandis que le second est l'inverse. Voir la figure ci-dessous.

.. note::
    Le s8550 est un transistor PNP et le s8050 est un transistor NPN. Ils se ressemblent beaucoup et il faut vérifier attentivement leurs étiquettes.

.. image:: img/transistor_symbol.png
    :width: 600

Lorsqu'un signal de niveau haut traverse un transistor NPN, il est activé. Mais un transistor PNP nécessite un signal de niveau bas pour fonctionner. Les deux types de transistors sont fréquemment utilisés comme interrupteurs sans contact, comme dans cette expérience.

Placez l'étiquette face à vous et les broches vers le bas. Les broches de gauche à droite sont l'émetteur (e), la base (b) et le collecteur (c).

.. image:: img/ebc.png
    :width: 150


* `S8050 Transistor Datasheet <https://datasheet4u.com/datasheet-pdf/WeitronTechnology/S8050/pdf.php?id=576670>`_
* `S8550 Transistor Datasheet <https://www.mouser.com/datasheet/2/149/SS8550-118608.pdf>`_

**Exemple**

* :ref:`1.2.1_c` (Projet C)
* :ref:`1.3.3_c` (Projet C)
* :ref:`1.2.2_py` (Projet Python)
* :ref:`1.3.3_py` (Projet Python)
* :ref:`1.14_scratch` (Projet Scratch)

