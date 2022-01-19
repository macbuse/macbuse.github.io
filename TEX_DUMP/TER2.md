## Titre : l'Algorithme Zipper

## Résumé :

En analyse complexe, le théorème de l'application conforme, dû à Bernhard Riemann, assure que toutes les parties ouvertes simplement connexes du plan complexe qui ne sont ni vides ni égales au plan tout entier sont conformes entre elles.
Autrement dit, étant donné un domaine homéomorphe au disque unité il existe une
bijection  holomorphe entre ce disque et le disque unité.


Le théorème fut énoncé (sous l'hypothèse plus forte d'une frontière formés d'arcs différentiables) par Bernhard Riemann dans sa thèse, en 1851. 
La démonstration de Riemann dépendait 
de l'existence d'une solution du problème de Dirichlet
sur le domaine,
qui était considéré comme àdmis à  cette époque.
Pourtant la méthode de Riemann ne s'applique pas aux domaines simplement connexes de frontière non suffisamment lisse ; de tels domaines furent étudiés en 1900 par W. F. Osgood.


Au début des années 80, un algorithme élémentaire pour  trouver une bijection holomorphe a été découvert par R. Kühnau et D.E. Marshall. 
L'algorithme est rapide et précis et relativement facile à programmer.
Soit 
$z_0, ..., z_n$
des points distincts dans le plan complexe. 
L'algorithme donne une suite de bijections holomorphes toute explicite
qui converge vers une bijection holomorphe entre le disque unité et une région délimitée par une courbe de Jordan $\gamma$ avec 
$z_0, ..., z_n \in \gamma$.
La complexité de l'algorithme depende de $n$ mais pas de la courbe $\gamma$ et
ça converge rapidement même pour la courbe de Koch.

On va étudier la méthode utilisée pour établir la convergence dans l'article de Rohde et Marshall. En particulier on va voir comment le taux de convergence varie selon la regularité de la courbe $\gamma$. Si le temps nous le permet on développera les applications en informatiques et fera une comparaison avec d'autre méthodes numériques : transformations de Schwarz-Christoffel et empilements de cercles.


## Prérequis : 

Fonctions holomorphes

## Références :

1.  Donald E. Marshall, Steffen Rohde,
Convergence of the Zipper algorithm for conformal mapping
[arxiv](https://arxiv.org/abs/math/0605532)
2. Sharon, E., and David Bryant Mumford, 2D-shape analysis
using conformal mapping. International Journal of Computer Vision, 2006
