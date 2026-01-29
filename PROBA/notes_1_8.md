### a) Montrer que $(F_X^{-1}(u) \leqslant t) \Leftrightarrow (u \leqslant F_X(t))$

L'inverse généralisée est définie par $F_X^{-1}(u) = \inf\{s : F_X(s) \geqslant u\}$.

* **Sens $(\Leftarrow)$ :** Si $u \leqslant F_X(t)$, alors par définition de l'ensemble $A = \{s : F_X(s) \geqslant u\}$, l'élément $t$ appartient à $A$. Comme $F_X^{-1}(u)$ est l'infimum de cet ensemble $A$, on a nécessairement $F_X^{-1}(u) \leqslant t$.
* **Sens $(\Rightarrow)$ :** Supposons $F_X^{-1}(u) \leqslant t$. La fonction de répartition $F_X$ est **croissante et continue à droite**, ce qui garantit que l'infimum est atteint : $F_X(F_X^{-1}(u)) \geqslant u$. Par la croissance de $F_X$, si $F_X^{-1}(u) \leqslant t$, alors $F_X(F_X^{-1}(u)) \leqslant F_X(t)$. Par transitivité, on en déduit $u \leqslant F_X(t)$.



---

### b) Loi de $\tilde{X} = F_X^{-1}(U)$

Soit $U \sim \mathcal{U}(]0, 1[)$. Pour déterminer la loi de $\tilde{X}$, calculons sa fonction de répartition $F_{\tilde{X}}(t)$ :

$$F_{\tilde{X}}(t) = P(\tilde{X} \leqslant t) = P(F_X^{-1}(U) \leqslant t)$$

En utilisant l'équivalence démontrée en **a)** :
$$P(F_X^{-1}(U) \leqslant t) = P(U \leqslant F_X(t))$$

Puisque pour une loi uniforme sur $[0, 1]$, on a $P(U \leqslant y) = y$ pour tout $y \in [0, 1]$, et comme $F_X(t)$ est toujours compris entre 0 et 1, il vient :
$$F_{\tilde{X}}(t) = F_X(t)$$

$\tilde{X}$ et $X$ ont la même fonction de répartition, elles suivent donc la même loi.

---

### c) Expliciter $F_X^{-1}$ (Loi exponentielle et Cauchy)

#### Loi exponentielle de paramètre $\lambda > 0$
La fonction de répartition est $F_X(t) = 1 - e^{-\lambda t}$ pour $t \geqslant 0$. 
Pour $u \in ]0, 1[$, on résout $1 - e^{-\lambda t} = u$ :
$$e^{-\lambda t} = 1 - u \implies -\lambda t = \ln(1 - u) \implies t = -\frac{\ln(1 - u)}{\lambda}$$
D'où $F_X^{-1}(u) = -\frac{\ln(1 - u)}{\lambda}$.

#### Loi de Cauchy standard
La fonction de répartition est $F_X(t) = \frac{1}{\pi} \arctan(t) + \frac{1}{2}$.
On résout $\frac{1}{\pi} \arctan(t) + \frac{1}{2} = u$ :
$$\arctan(t) = \pi \left(u - \frac{1}{2}\right) \implies t = \tan\left(\pi \left(u - \frac{1}{2}\right)\right)$$
D'où $F_X^{-1}(u) = \tan\left(\pi \left(u - \frac{1}{2}\right)\right)$.

---

### d) Existence d'une loi de probabilité

Pour prouver que $F$ est une fonction de répartition, il suffit d'exhiber une variable aléatoire qui suit cette loi.
1. Soit un espace probabilisé muni d'une variable $U \sim \mathcal{U}(]0, 1[)$.
2. On pose $Y = F^{-1}(U)$, où $F^{-1}$ est l'inverse généralisée de $F$.
3. Comme $F$ possède les propriétés requises (croissance, continuité à droite, limites en 0 et 1), le calcul de la question **b)** s'applique :
$$P(Y \leqslant t) = P(U \leqslant F(t)) = F(t)$$
La fonction $F$ est donc bien la fonction de répartition de la variable $Y$.
