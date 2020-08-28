# Linux/OS X


## Quelques commandes Unix.

Si vous n’avez pas d’interpréteur de commande, il faut utiliser l’interface graphique pour en lancer une:

- Si vous êtes loggué sur une machine CARISM, en appuyant sur le bouton droit de la souris sur le fond de l’écran, et selectionner “xterm”.
- Si vous êtes sur un PC Linux avec KDE, en cliquant sur l’icone représentant une fenêtre terminal ou en cliquant avec le bouton droit, puis Executer une commande puis tapez xterm puis Entree
- Sous Windows, installez un [unix subsystème](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
- Sous OS X lancez l'application
    [terminal](https://support.apple.com/en-ie/guide/terminal/welcome/mac)

    Attention, les conventions des interfaces graphiques Unix peuvent différer des interfaces que vous connaissez : par exemple, on utilise le click avec le bouton du milieu (ou click simultané sur les boutons droits et gauche) pour insérer le contenu du “presse-papier”.

### Les répertoires:

- pwd: afficher le nom du répertoire où vous êtes (le répertoire courant).
- ~ : désigne votre répertoire d’origine.
- ~miasn1 : désigne le répertoire d’origine de l’utilisateur dont le nom de login est miasn1
- ls: afficher la liste des fichiers et des sous répertoires du répertoire courant. Pour avoir plus de détails, ls -l.
- cd: changer de répertoire.
- cd rep : pour aller dans le sous répertoire appelé rep;
- cd ou cd ~ : pour aller dans votre répertoire d’origine.
- cd ~miasn1 : pour aller dans le répertoire d’origine de l’utilisateur miasn1.
- cd .. : pour aller dans le répertoire parent.
- cd /usr/local : pour aller dans le répertoire /usr/local
- mkdir: Pour créer un sous répertoire, par exemple
- mkdir rep crée un sous-répertoire appelé rep
- rmdir: effacer un répertoire vide, par exemple rmdir rep.

####    Exercice:

A l’aide des commandes expliquées ci-dessus:

1. Placez vous dans votre répertoire d’origine: cd. Vérifiez que vous y êtes bien: pwd. 
1. Regardez la liste des fichiers par: ls , puis avec: ls -al
En utilisant la commande mkdir, créer un répertoire de nom: essai Vérifier son existence (avec ls).
1. Aller dans ce répertoire: cd essai Vérifier que vous y êtes (avec pwd).
Revenir dans le répertoire d’origine par cd .. 
1. Vérifiez que vous y etes. Détruire (rmdir) le répertoire essai.

### Les fichiers


- cp: Copier un fichier:
- cp essai.cc test.cc : crée une copie du fichier essai.cc nommée test.cc (dans le répertoire courant)
- cp fichier1.cc .. : copie le fichier1.cc dans le répertoire parent (situé juste avant le répertoire courant).
- mv: Déplace ou/et renomme un fichier.
- mv fichier1.cc fichier2.cc : renomme le fichier fichier1.cc
Si rep est un répertoire, mv fichier1.cc rep déplace le fichier1.cc dans le sous répertoire rep.
- rm: effacer un fichier
- rm fichier.cc : efface le fichier fichier.cc.
- rm -r rep : efface le répertoire rep et tous ses sous-répertoires
- wget : copier un fichier depuis un serveur web
- curl : copier un fichier depuis un serveur web
- more : afficher le contenu d'un fichier
- less : afficher le contenu d'un fichier
- emacs: éditer un fichier texte
- emacs fichier.cc & : ouvre le fichier fichier.cc (le crée s’il n’existe pas).

    Remarques:

1. Notez que l’appui sur la touche de tabulation (à gauche de la touche A sur un clavier français) est un raccourci clavier qui permet de compléter automatiquement le début d’un nom de fichier ou d’afficher les différentes possibilités de complétion.
1. Le caractère & placé à la fin d’une commande permet de l’exécuter en tâche de fonds.
1. La lettre * à une signification spéciale: elle permet de remplacer n’importe quel morceau de chaine de caractères, par exemple ls m*.cc listera tous les fichiers dont le nom commence par m et se termine par .cc
1. Pour avoir plus de détails sur une commande Unix, vous pouvez utiliser la commande man, par exemple, taper dans une fenetre de commande:
man ls
pour en savoir plus sur la commande ls.

### Exercice :

Copier une page web avec wget et afficher son contenu avec less.

---
Pour savoir plus : 

- [commandes unix](https://www.guru99.com/must-know-linux-commands.html)
- wget

    <iframe width="560" height="315" src="https://www.youtube.com/embed/9qkipzxX1sQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Noms et fonction de quelques logiciels.
Ces noms de commande vous permettront de lancer les logiciels correspondants depuis n’importe quel interpréteur de commande (ce qui permet de les lancer indépendemment de l’environnement, il suffit de connaitre leur nom et non pas dans quel menu ils se trouvent).

1. emacs: éditeur de texte.
1. firefox: navigateur Internet. Pour utiliser le courrier électronique avec netscape, il vous faudra configurer votre adresse électronique. Permet également de lire des fichiers .html
1. texmacs ou lyx: traitement de texte scientifique particulièrement adapté à la saisie d’équations. Attention à ne pas confondre éditeur de texte et traitement de texte on n’utilise pas lyx pour écrire un programme en C++ (cf. section 3.1).
1. gnumeric (GNU/Linux): tableur, permet par exemple de lire des fichiers .xls
1. xpdf ou acroread: pour lire des fichiers PDF (d’extension .pdf)
1. gv ou ghostview: visualiser des fichiers Postscript (d’extension .ps)
1. gimp (GNU/Linux): traitement d’images par exemple de fichiers d’extension .gif, .png
1. lp ou lpr: imprime un fichier.
1. zip/unzip (GNU/Linux): utilitaires de compression/décompression d’archives au format zip, très répandu sur les machines Windows.
1. scilab: logiciels de calcul numérique
1. xcas: logiciel de calcul formel et géométrie interactive
etc.

