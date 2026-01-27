---
title: Définition et Propriétés de la Médiane
---

Définition Mathématique
=======================

La **médiane** d'une variable aléatoire réelle $X$ est une valeur $m$
qui sépare la distribution de probabilité en deux parties égales. Elle
est définie par les deux conditions suivantes :

1.  $P(X \le m) \ge \frac{1}{2}$

2.  $P(X \ge m) \ge \frac{1}{2}$

Pour une variable aléatoire continue de fonction de répartition $F$, la
médiane est simplement la valeur $m$ telle que : $$F(m) = \frac{1}{2}$$

Lien avec les exercices
=======================

Minimisation de l'erreur absolue (Exercice 6)
---------------------------------------------

Une propriété fondamentale de la médiane est qu'elle est la valeur $a$
qui minimise la fonction d'écart absolu : $$g(a) = \mathbb{E}|X - a|$$
Comme demandé dans l'exercice 6, pour une variable discrète uniforme sur
$\{x_1, \dots, x_r\}$, cela revient à minimiser la somme des distances
aux points.

Calcul pour les lois de l'exercice 5
------------------------------------

À partir des fonctions de répartition calculées précédemment, nous
pouvons déduire les médianes théoriques :

-   **Loi Béta $B(\alpha, 1)$ :** On résout
    $F(m) = m^\alpha = \frac{1}{2}$, d'où :
    $$m = \left(\frac{1}{2}\right)^{1/\alpha}$$

-   **Loi de Weibull :** On résout
    $F(m) = 1 - e^{-\lambda m^\alpha} = \frac{1}{2}$, ce qui donne
    $e^{-\lambda m^\alpha} = \frac{1}{2}$. En passant au logarithme :
    $$-\lambda m^\alpha = \ln\left(\frac{1}{2}\right) \implies m = \left( \frac{\ln(2)}{\lambda} \right)^{1/\alpha}$$

Comparaison avec la moyenne
===========================

Contrairement à l'espérance $\mathbb{E}[X]$, la médiane est robuste aux
valeurs extrêmes (outliers). Dans l'exercice 7, bien que $X$ soit
symétrique sur $[-1, 3]$ (moyenne = médiane = $1$), la transformation
$Y = h(X)$ peut décaler ces deux valeurs l'une par rapport à l'autre
selon la forme de $h$.
