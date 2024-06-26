.. _configuration_audio:

Configuration Audio
=========================

.. _changer_sortie_audio:

Changer la sortie audio
----------------------------

Si vos haut-parleurs ne produisent aucun son, cela peut être dû au fait que le Raspberry Pi a sélectionné la mauvaise sortie audio. La sortie correcte devrait être **Casque**. Vous pouvez changer la sortie audio en suivant ces étapes.

Entrez la commande suivante.

.. raw:: html

   <run></run>

.. code-block:: 

    sudo raspi-config

Sélectionnez **1 Options Système**.

.. image:: img/audio1.jpg

Puis **S2 Audio**.

.. image:: img/audio2.jpg

Après avoir sélectionné **1 Casque**, appuyez sur ``Enter`` pour confirmer et sélectionnez ``Finish`` pour quitter.

.. image:: img/audio3.jpg

.. _ajuster_volume:

Ajuster le volume 
--------------------

Si vous trouvez que le volume des haut-parleurs est trop faible, vous pouvez l'ajuster en entrant la commande suivante.

.. raw:: html

   <run></run>

.. code-block:: 

    alsamixer

.. image:: img/faq1.png

La page par défaut est illustrée ci-dessous.

.. image:: img/faq2.png

Appuyez sur ``F6`` pour sélectionner le mode **Casque**.

.. image:: img/faq3.png

Ensuite, utilisez les touches fléchées haut et bas pour ajuster le niveau de volume, et appuyez sur ``ESC`` pour quitter.

.. image:: img/faq4.png
