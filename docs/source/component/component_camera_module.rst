.. _cpn_camera_module:

Module de Caméra
====================================

**Description**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

Ceci est un module caméra 5MP pour Raspberry Pi avec capteur OV5647. Il est prêt à l'emploi, il suffit de connecter le câble ruban inclus au port CSI (Camera Serial Interface) de votre Raspberry Pi et vous êtes prêt à l'utiliser.

La carte est petite, environ 25mm x 23mm x 9mm, et pèse 3g, ce qui la rend idéale pour les applications mobiles ou autres applications où la taille et le poids sont critiques. Le module caméra a une résolution native de 5 mégapixels et est équipé d'un objectif à mise au point fixe qui capture des images fixes à 2592 x 1944 pixels. Il prend également en charge les vidéos en 1080p30, 720p60 et 640x480p90.

.. note:: 

   Le module ne peut capturer que des images et des vidéos, pas de son.

**Spécifications**

* **Résolution des images statiques** : 2592×1944 
* **Résolution vidéo prise en charge** : 1080p/30 fps, 720p/ 60fps et 640x480p 60/90 enregistrement vidéo 
* **Ouverture (F)** : 1.8 
* **Angle de vue** : 65 degrés 
* **Dimensions** : 24mm x 23.5mm x 8mm 
* **Poids** : 3g 
* **Interface** : connecteur CSI 
* **OS pris en charge** : Raspberry Pi OS (dernière version recommandée) 

**Assembler le module caméra**
-------------------------------------

Sur le module caméra ou le Raspberry Pi, vous trouverez un connecteur en plastique plat. Tirez délicatement le commutateur de fixation noir jusqu'à ce qu'il soit partiellement sorti. Insérez le câble FFC dans le connecteur en plastique dans le sens indiqué et remettez le commutateur de fixation en place.

Si le câble FFC est correctement installé, il sera droit et ne se retirera pas lorsque vous le tirez doucement. Sinon, réinstallez-le à nouveau.

.. image:: img/connect_ffc.png
.. image:: img/1.10_camera.png
   :width: 700

.. warning::

   N'installez pas la caméra avec l'alimentation allumée, cela pourrait endommager votre caméra.

.. _enable_camera:

**Activer l'interface de la caméra**
---------------------------------------

Exécutez la commande suivante pour activer l'interface de la caméra de votre Raspberry Pi. Si vous l'avez déjà activée, passez cette étape ; si vous ne savez pas si cela a été fait ou non, veuillez continuer.

.. raw:: html

   <run></run>

.. code-block:: 

   sudo raspi-config

**3 Interfacing options**

.. image:: img/image282.png
   :align: center

**P1 Camera**

.. image:: img/camera_config1.png
   :align: center

**<Oui>, puis <Ok> -> <Finish>**

.. image:: img/camera_config2.png
   :align: center

Après la configuration, il est recommandé de redémarrer le Raspberry Pi.

.. raw:: html

   <run></run>

.. code-block:: 

   sudo reboot
   
**Exemple**

* :ref:`3.1.1_py` (Projet Python)
* :ref:`3.1.2_py` (Projet Python)
* :ref:`4.1.1_py` (Projet Python)
* :ref:`4.1.4_py` (Projet Python)
* :ref:`4.1.5_py` (Projet Python)
* :ref:`1.10_scratch` (Projet Scratch)
* :ref:`1.18_scratch` (Projet Scratch)

