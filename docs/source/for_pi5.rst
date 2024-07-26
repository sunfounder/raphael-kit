.. note::

    Bonjour et bienvenue dans la Communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez plus profondément dans l'univers des Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et cadeaux** : Participez à des cadeaux et des promotions de vacances.

    👉 Prêt à explorer et à créer avec nous ? Cliquez [|link_sf_facebook|] et rejoignez-nous aujourd'hui !



For Pi 5
============================

The release of the Raspberry Pi 5 has brought us a more powerful model, but it also introduced some changes, 
most notably to the GPIO.Although it retains its standard 40-pin interface, functionality has shifted due to 
its connection with the newly integrated RP1 southbridge chip. This custom RP1 chip now handles peripherals 
on the Pi 5 and has resulted in various compatibility concerns.Currently, only the GPIO Zero library, maintained 
officially by the Raspberry Pi organization, is fully compatible. We have developed a series of courses 
specifically focused on this library.

.. toctree::
    :maxdepth: 1
    
    python_pi5/play_with_python_pi5
    c_pi5/play_with_c
    scratch_pi5/play_with_scratch

For compatibility issues with other programming languages, please see the detailed information below:

**C language**

.. note::

    * The wiringPi library has been compatible with the Raspberry Pi 5 starting from version 3.0. However, as of the latest version, the PWM functionality is still under development.
    * We are currently using the latest version of wiringPi to update our courses for compatibility with the Raspberry Pi 5. Please stay tuned for updates.

The C language implementation relies on the wiringPi library. However, the wiringPi community library is now archived and no longer receives updates, rendering it unsuitable for Raspberry Pi 5 projects. For additional information, refer to: https://github.com/WiringPi/WiringPi.

.. image:: img/pi5_c_language.png

**Processing**

When using Processing 4 on Raspberry Pi 5, GPIO programming encounters challenges. Errors such as "Invalid argument" and "GPIO pin 17 seems to be unavailable on your platform" arise during the execution of GPIO-related code (as depicted in the accompanying image). For further details, visit: https://github.com/benfry/processing4/issues/807

.. image:: img/pi5_processing.png

**Node.js**

Node.js utilizes the pigpio library, which, as of now, does not support Raspberry Pi 5. For more insights, visit: https://github.com/joan2937/pigpio/issues/589

.. image:: img/pi5_nodejs.png
    :width: 700

**Scratch**

.. note::
 
    * Version 3.30.8 of Scratch 3 is now compatible with the Raspberry Pi 5. 
    * We are also in the process of updating our courses to be compatible with the Raspberry Pi 5. Please wait for these updates.


On a 64-bit system, the importation of the Raspberry Pi GPIO library faces issues, leading to unresponsiveness. For more information, visit: https://github.com/raspberrypi/bookworm-feedback/issues/91.