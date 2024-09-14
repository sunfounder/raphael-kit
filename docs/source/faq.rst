FAQ
======================

.. _faq_soc:

Si "gpiozero" ne fonctionne pas.
-----------------------------------------------------------------------

Le didacticiel Raspberry Pi 5 GPIO Python est basé sur la bibliothèque gpiozero et a été minutieusement testé pendant le processus de conception.

Cependant, les modifications récentes apportées au noyau Linux sur le système d'exploitation Raspberry Pi [1] ont modifié la façon dont les appels système GPIO sont gérés, rendant la bibliothèque Python d'origine incapable d'accéder au GPIO sur le Raspberry Pi 5.

Nos développeurs ont signalé ce problème à la bibliothèque gpiozero, et les développeurs gpiozero sont conscients de ce problème et travaillent activement sur les mises à jour [2].

* [1] https://github.com/raspberrypi/linux/pull/6144
* [2] https://github.com/gpiozero/gpiozero/issues/1166

entre-temps,
J'ai trouvé une solution temporaire. Lorsque j'exécute la commande ci-dessous, GPIO fonctionne correctement.

.. code-block::

    sudo ln -s gpiochip0 /dev/gpiochip4

Cette solution fonctionnera jusqu'à ce que la bibliothèque gpiozero publie un correctif approprié.