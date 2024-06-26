.. _login_windows:

PuTTY
=========================

Si vous êtes un utilisateur Windows, vous pouvez utiliser certaines applications SSH. Ici, nous recommandons `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_.

**Étape 1**

Téléchargez PuTTY.

**Étape 2**

Ouvrez PuTTY et cliquez sur **Session** dans la structure en arborescence à gauche. Entrez
l'adresse IP du RPi dans la zone de texte sous **Host Name (or IP
address)** et **22** sous **Port** (par défaut, c'est 22).

.. image:: img/image25.png
    :align: center

**Étape 3**

Cliquez sur **Open**. Notez que lors de la première connexion au Raspberry Pi avec
l'adresse IP, un rappel de sécurité s'affiche. Cliquez simplement sur **Yes**.

**Étape 4**

Lorsque la fenêtre PuTTY affiche \"**login as:**\", tapez
\"**pi**\" (le nom d'utilisateur du RPi), et **password**: \"raspberry\"
(par défaut, si vous ne l'avez pas changé).

.. note::

    Lorsque vous saisissez le mot de passe, les caractères ne s'affichent pas dans la fenêtre, ce qui est normal. Vous devez simplement saisir le mot de passe correct.
    
    Si inactif apparaît à côté de PuTTY, cela signifie que la connexion a été interrompue et doit être rétablie.
    
.. image:: img/image26.png
    :align: center

**Étape 5**

Maintenant que nous avons connecté le Raspberry Pi, il est temps de passer aux étapes suivantes.
