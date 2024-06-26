.. _cpn_potentiometer:

Potentiomètre
==================

.. image:: img/potentiometer.png
    :align: center
    :width: 150

Un potentiomètre est un composant résistant à 3 terminaux dont la valeur de résistance peut être ajustée selon une variation régulière.

Les potentiomètres existent en différentes formes, tailles et valeurs, mais ils ont tous les points communs suivants :

* Ils ont trois terminaux (ou points de connexion).
* Ils possèdent un bouton, une vis ou un curseur qui peut être déplacé pour faire varier la résistance entre le terminal central et l'un des terminaux extérieurs.
* La résistance entre le terminal central et l'un des terminaux extérieurs varie de 0 Ω à la résistance maximale du potentiomètre lorsque le bouton, la vis ou le curseur est déplacé.

Voici le symbole de circuit du potentiomètre.

.. image:: img/potentiometer_symbol.png
    :align: center
    :width: 400

Les fonctions du potentiomètre dans le circuit sont les suivantes :

#. Fonction de diviseur de tension

    Le potentiomètre est une résistance ajustable en continu. Lorsque vous ajustez l'axe ou la poignée coulissante du potentiomètre, le contact mobile glisse sur la résistance. À ce moment, une tension peut être sortie en fonction de la tension appliquée au potentiomètre et de l'angle de rotation du bras mobile ou de son déplacement.

#. Fonction de rhéostat

    Lorsque le potentiomètre est utilisé comme rhéostat, connectez le pin central et l'un des deux autres pins dans le circuit. Vous pouvez ainsi obtenir une valeur de résistance lisse et continuellement variable en fonction du déplacement du contact mobile.

#. Fonction de contrôleur de courant

    Lorsque le potentiomètre agit comme contrôleur de courant, le terminal de contact coulissant doit être connecté en tant que l'un des terminaux de sortie.

Si vous souhaitez en savoir plus sur le potentiomètre, consultez : `Potentiomètre - Wikipédia <https://fr.wikipedia.org/wiki/Potentiom%C3%A8tre>`_

**Exemple**

* :ref:`2.1.7_c` (Projet C)
* :ref:`2.1.7_py` (Projet Python)
