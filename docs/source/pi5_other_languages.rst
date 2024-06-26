Autres Langages (pour Pi 5)
================================

La sortie du Raspberry Pi 5 nous a apporté un modèle plus puissant, mais elle a également introduit quelques changements, notamment au niveau des GPIO.

Bien qu'il conserve son interface standard à 40 broches, la fonctionnalité a évolué en raison de sa connexion avec la nouvelle puce southbridge RP1 intégrée. Cette puce RP1 personnalisée gère désormais les périphériques sur le Pi 5, entraînant divers problèmes de compatibilité.

Langage C
--------------
L'implémentation du langage C repose sur la bibliothèque wiringPi. Cependant, la bibliothèque communautaire wiringPi est désormais archivée et ne reçoit plus de mises à jour, la rendant inadaptée aux projets sur Raspberry Pi 5. Pour plus d'informations, consultez : https://github.com/WiringPi/WiringPi

.. image:: img/pi5_c_language.png

Processing
--------------
Lors de l'utilisation de Processing 4 sur Raspberry Pi 5, la programmation des GPIO rencontre des défis. Des erreurs telles que "Invalid argument" et "GPIO pin 17 seems to be unavailable on your platform" surviennent lors de l'exécution du code lié aux GPIO (comme illustré dans l'image ci-jointe). Pour plus de détails, visitez : https://github.com/benfry/processing4/issues/807

.. image:: img/pi5_processing.png

Node.js
-----------
Node.js utilise la bibliothèque pigpio, qui, à ce jour, ne prend pas en charge le Raspberry Pi 5. Pour plus d'informations, visitez : https://github.com/joan2937/pigpio/issues/589

.. image:: img/pi5_nodejs.png
    :width: 700

Scratch
-----------
Sur un système 64 bits, l'importation de la bibliothèque GPIO du Raspberry Pi rencontre des problèmes, entraînant une absence de réponse. Pour plus d'informations, visitez : https://github.com/raspberrypi/bookworm-feedback/issues/91
