.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !

.. _cpn_humiture_sensor:

Module Capteur d'Humidité et de Température
==================================================

.. image:: img/dht11_pic.png
    :width: 400
    :align: center

Le capteur numérique de température et d'humidité DHT11 est un capteur composite qui contient une sortie de signal numérique calibrée de la température et de l'humidité.
La technologie de collecte de modules numériques dédiés et la technologie de détection de température et d'humidité sont appliquées pour garantir que le produit a une haute fiabilité et une excellente stabilité à long terme.

Seules trois broches sont disponibles pour l'utilisation : VCC, GND et DATA.
Le processus de communication commence par l'envoi de signaux de démarrage à DHT11 via la ligne DATA, et DHT11 reçoit les signaux et renvoie un signal de réponse.
Ensuite, l'hôte reçoit le signal de réponse et commence à recevoir les données d'humidité et de température sur 40 bits (8 bits pour l'humidité entière + 8 bits pour l'humidité décimale + 8 bits pour la température entière + 8 bits pour la température décimale + 8 bits pour la somme de contrôle).

.. image:: img/Dht11.png

* `DHT11 Datasheet <https://components101.com/sites/default/files/component_datasheet/DHT11-Temperature-Sensor.pdf>`_

**Exemple**

* :ref:`2.2.3_c` (Projet C)
* :ref:`2.2.3_py` (Projet Python)
