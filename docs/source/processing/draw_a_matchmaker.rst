.. _draw_a_matchmaker:

Dessiner un Entremetteur
===========================

Vous utilisez maintenant l'environnement de développement Processing (ou PDE). 
Il n'y a pas grand-chose à savoir ; la grande zone est l'éditeur de texte, et il y a une rangée de boutons en haut ; c'est la barre d'outils. 
Sous l'éditeur se trouve la zone de messages, et en dessous se trouve la console. 
La zone de messages est utilisée pour les messages d'une ligne, et la console est utilisée pour des détails plus techniques.

Familiarisons-nous avec l'utilisation de Processing et dessinons un entremetteur.

**Croquis**

Copiez le croquis ci-dessous dans Processing et exécutez-le. Une nouvelle fenêtre d'affichage apparaîtra et un entremetteur acclamant sera dessiné.

.. code-block:: arduino

    size(200,200);
    background(92, 168, 0); 
    rectMode(CENTER);
    rect(100,120,20,60);
    ellipse(100,80,45,45);
    line(90,150,80,170);
    line(110,150,120,170);
    line(90,110,70,100);
    line(110,110,130,100);

.. image:: img/draw_one1.png

.. note:: 

    Si vous l'exécutez et que la zone de messages devient rouge et rapporte des erreurs, alors il y a quelque chose qui ne va pas avec le croquis. Assurez-vous de copier exactement le croquis d'exemple : les nombres doivent être entre parenthèses, avec des virgules entre chaque nombre, et les lignes doivent se terminer par des points-virgules.


**Comment ça fonctionne ?**

L'essentiel ici est de comprendre que la fenêtre d'affichage peut être traitée comme un carré de papier.

Chaque pixel de la fenêtre d'affichage est une coordonnée (x,y) qui détermine la position d'un point dans l'espace. L'origine (0,0) des coordonnées se trouve dans le coin supérieur gauche, la direction positive de l'axe X est horizontalement vers la droite, et la direction positive de l'axe Y est verticalement vers le bas.

Ce que nous devons faire, c'est spécifier quelle forme et quelle couleur doivent apparaître à ces coordonnées de pixels.

Par exemple, dessinez un rectangle de largeur 20 et de hauteur 60 avec les coordonnées (100,120) comme point médian.

.. code-block:: arduino

    rectMode(CENTER);
    rect(100,120,20,60);

.. image:: img/draw_one_coodinate.png

Une fois que nous avons compris la relation entre la fenêtre d'affichage et les axes, ce croquis n'est pas difficile pour nous, nous devons juste comprendre quelques instructions simples de dessin graphique.

    * ``size(width, height)``: Définit les dimensions de la fenêtre d'affichage en largeur et hauteur en unités de pixels.
    * ``background(red, green, blue)``: Définit la couleur de fond de la fenêtre d'affichage.
    * ``rectMode(mode)``: Modifie l'emplacement à partir duquel les rectangles sont dessinés en changeant la manière dont les paramètres donnés à ``rect()`` sont interprétés.
    * ``rect(x, y, width, height)``: Dessine un rectangle à l'écran. 
    * ``ellipse(x, y, width, height)``: Dessine une ellipse (ovale) à l'écran. 
    * ``line(x1, y1, x2, y2)``: Dessine une ligne (un chemin direct entre deux points) à l'écran.

Pour plus d'informations, veuillez vous référer à `Processing Reference <https://processing.org/reference/>`_.
