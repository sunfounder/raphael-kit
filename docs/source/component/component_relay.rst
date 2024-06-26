.. _cpn_relay:

Relais
==========================================

.. image:: img/relay_pic.png
    :width: 200
    :align: center

Comme nous le savons, un relais est un dispositif utilisé pour établir une connexion entre deux 
ou plusieurs points ou dispositifs en réponse au signal d'entrée appliqué. En d'autres termes, 
les relais assurent l'isolation entre le contrôleur et le dispositif, car les dispositifs peuvent 
fonctionner en courant alternatif (AC) ainsi qu'en courant continu (DC). Cependant, ils reçoivent 
des signaux d'un microcontrôleur fonctionnant en DC, nécessitant ainsi un relais pour combler le 
fossé. Le relais est extrêmement utile lorsque vous avez besoin de contrôler une grande quantité 
de courant ou de tension avec un petit signal électrique.


Chaque relais se compose de 5 parties :

.. image:: img/relay142.jpeg

**Électroaimant** - Il se compose d'un noyau de fer entouré d'une bobine de fils. Lorsque 
l'électricité passe à travers, il devient magnétique. Par conséquent, il est appelé électroaimant.

**Armature** - La bande magnétique mobile est connue sous le nom d'armature. Lorsque le courant 
passe à travers elle, la bobine est énergisée, produisant ainsi un champ magnétique utilisé pour 
établir ou interrompre les points normalement ouverts (N/O) ou normalement fermés (N/C). L'armature 
peut être déplacée par un courant continu (DC) ainsi qu'un courant alternatif (AC).


**Ressort** - Lorsque aucun courant ne passe à travers la bobine de l'électroaimant, le ressort 
tire l'armature de sorte que le circuit ne peut pas être complété.

Ensemble de **contacts électriques** - Il y a deux points de contact :

-  Normalement ouvert - connecté lorsque le relais est activé, et déconnecté lorsqu'il est inactif.

-  Normalement fermé - non connecté lorsque le relais est activé, et connecté lorsqu'il est inactif.

**Cadre moulé** - Les relais sont recouverts de plastique pour la protection.

Le principe de fonctionnement du relais est simple. Lorsqu'une alimentation est 
fournie au relais, le courant commence à circuler à travers la bobine de commande ; 
en conséquence, l'électroaimant commence à s'énergiser. Ensuite, l'armature est 
attirée par la bobine, abaissant le contact mobile et se connectant ainsi aux contacts 
normalement ouverts. Le circuit avec la charge est alors énergisé. L'interruption du 
circuit se fait de manière similaire, le contact mobile étant remonté vers les 
contacts normalement fermés sous l'effet du ressort. De cette manière, l'activation 
et la désactivation du relais peuvent contrôler l'état d'un circuit de charge.

**Exemple**

* :ref:`1.3.3_c` (Projet C)
* :ref:`1.3.3_py` (Projet Python)
