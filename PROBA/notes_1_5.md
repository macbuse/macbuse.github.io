## exo 5


Bien sûr — voici **exactement la même réponse**, mais avec **$ … $** pour les maths en ligne et **$$ … $$** pour les équations affichées.

---

## La loi de Weibull

La **loi de Weibull** est une loi de probabilité continue très utilisée en **fiabilité**, **analyse de survie**, **mécanique des matériaux** et **modélisation des durées de vie**. Elle est appréciée pour sa grande flexibilité : selon ses paramètres, elle peut modéliser des comportements très différents.

Elle est définie pour une variable aléatoire continue $X \ge 0$.

---

## Paramètres

La loi de Weibull dépend de **deux paramètres positifs** :

* **Paramètre de forme** : $k > 0$ (souvent noté $\beta$)
* **Paramètre d’échelle** : $\lambda > 0$ (souvent noté $\eta$)

---

## Densité de probabilité (PDF)

$$
f(x) =
\begin{cases}
\dfrac{k}{\lambda}\left(\dfrac{x}{\lambda}\right)^{k-1}
e^{-(x/\lambda)^k}, & x \ge 0 \
0, & x < 0
\end{cases}
$$

---

## Fonction de répartition (CDF)

La **fonction de répartition** $F(x)$ donne la probabilité que la variable aléatoire soit inférieure ou égale à $x$ :

$$
F(x) = P(X \le x)
$$

Pour la loi de Weibull :

$$
F(x) =
\begin{cases}
1 - e^{-(x/\lambda)^k}, & x \ge 0 \
0, & x < 0
\end{cases}
$$

---

## Interprétation du paramètre de forme $k$

Le paramètre $k$ contrôle l’évolution du **taux de défaillance** :

* **$k < 1$**
  $\rightarrow$ taux de défaillance décroissant
  (défaillances précoces, « mortalité infantile »)

* **$k = 1$**
  $\rightarrow$ taux de défaillance constant
  (cas particulier : loi exponentielle)

* **$k > 1$**
  $\rightarrow$ taux de défaillance croissant
  (usure, vieillissement)

---

## Rôle du paramètre d’échelle $\lambda$

* $\lambda$ étire ou contracte la distribution sur l’axe du temps
* Plus $\lambda$ est grand, plus les événements surviennent tard

Propriété utile :
$$
F(\lambda) = 1 - e^{-1} \approx 0{,}632
$$

Environ **63,2 %** des observations sont inférieures à $\lambda$.

---

## Fonction de survie

On utilise souvent la fonction de survie :

$$
S(x) = 1 - F(x) = e^{-(x/\lambda)^k}
$$

Elle représente la probabilité que le système fonctionne **au-delà** du temps $x$.



Of course — here it is again, with **$ … $** for inline math and **$$ … $$** for displayed equations.

---

## Quantile function of the Weibull distribution

For a **Weibull distribution** with shape parameter $k>0$ and scale parameter $\lambda>0$, the **quantile function** (inverse of the CDF) is obtained by inverting the cumulative distribution function.

---

### Starting from the CDF

$$
F(x) = 1 - e^{-(x/\lambda)^k}, \qquad x \ge 0
$$

Let $p \in (0,1)$. Set $F(x)=p$:

$$
p = 1 - e^{-(x/\lambda)^k}
$$

---

### Solving for $x$

$$
e^{-(x/\lambda)^k} = 1 - p
$$

$$
-(x/\lambda)^k = \ln(1 - p)
$$

$$
(x/\lambda)^k = -\ln(1 - p)
$$

$$
x = \lambda , \big[-\ln(1 - p)\big]^{1/k}
$$

---

### Quantile function

$$
\boxed{
Q(p) = F^{-1}(p)
= \lambda , \big[-\ln(1 - p)\big]^{1/k},
\qquad 0 < p < 1
}
$$

---

### Useful special cases

* **Median** ($p=0.5$):
  $$
  \text{Med} = \lambda (\ln 2)^{1/k}
  $$

* **Exponential distribution** (case $k=1$):
  $$
  Q(p) = -\lambda \ln(1-p)
  $$

---

### Remarks

* The quantile function is widely used for **inverse transform sampling**
* It is essential for **Weibull probability plots**
* Common in **simulation** and **reliability threshold analysis**

---

## exo 7

## Énoncé

Soit $X$ une variable aléatoire suivant une loi uniforme sur $[-1, 3]$, notée $X \sim \mathcal{U}([-1, 3])$. On définit la variable $Y$ par :
$$Y = \frac{1}{2}(|X - 1| + |X|)$$
L'objectif est de déterminer l'espérance $\mathbb{E}[Y]$ et la variance $\text{Var}(Y)$.

### Analyse de la fonction de transformation
La densité de $X$ est donnée par $f_X(x) = \frac{1}{4} \mathbf{1}_{[-1, 3]}(x)$. Posons $h(x) = \frac{1}{2}(|x - 1| + |x|)$. Étudions $h(x)$ par morceaux sur l'intervalle $[-1, 3]$ :

-   **Sur $[-1, 0]$ :** $x \le 0$ et $x-1 \le 0$ \\
    $h(x) = \frac{1}{2}(-(x-1) - x) = \frac{1}{2}(1 - 2x) = \frac{1}{2} - x$.
-   **Sur $[0, 1]$ :** $x \ge 0$ et $x-1 \le 0$ \\
    $h(x) = \frac{1}{2}(-(x-1) + x) = \frac{1}{2}(1) = \frac{1}{2}$.
-   **Sur $[1, 3]$ :** $x \ge 1$ et $x-1 \ge 0$ \\
    $h(x) = \frac{1}{2}(x-1 + x) = \frac{1}{2}(2x - 1) = x - \frac{1}{2}$.

 ### Calcul de l'espérance $\mathbb{E}[Y]$
Par le théorème de transfert :
$$\mathbb{E}[Y] = \int_{-1}^{3} h(x) f_X(x) dx = \frac{1}{4} \left[ \int_{-1}^{0} \left(\frac{1}{2}-x\right) dx + \int_{0}^{1} \frac{1}{2} dx + \int_{1}^{3} \left(x-\frac{1}{2}\right) dx \right]$$

Calculons chaque intégrale :
-  $\int_{-1}^{0} (\frac{1}{2}-x) dx = \left[ \frac{1}{2}x - \frac{1}{2}x^2 \right]_{-1}^0 = 0 - (-\frac{1}{2} - \frac{1}{2}) = 1$
-   $\int_{0}^{1} \frac{1}{2} dx = \frac{1}{2}$
-   $\int_{1}^{3} (x-\frac{1}{2}) dx = \left[ \frac{1}{2}x^2 - \frac{1}{2}x \right]_1^3 = (\frac{9}{2} - \frac{3}{2}) - (\frac{1}{2} - \frac{1}{2}) = 3$

D'où :
$$\mathbb{E}[Y] = \frac{1}{4} (1 + 0.5 + 3) = \frac{4.5}{4} = 1.125$$

### Calcul de la variance $\text{Var}(Y)$

Calculons d'abord le moment d'ordre 2, $\mathbb{E}[Y^2]$ :
$$\mathbb{E}[Y^2] = \frac{1}{4} \left[ \int_{-1}^{0} \left(\frac{1}{2}-x\right)^2 dx + \int_{0}^{1} \left(\frac{1}{2}\right)^2 dx + \int_{1}^{3} \left(x-\frac{1}{2}\right)^2 dx \right]$$
-   $\int_{-1}^{0} (\frac{1}{4} - x + x^2) dx = \left[ \frac{1}{4}x - \frac{1}{2}x^2 + \frac{1}{3}x^3 \right]_{-1}^0 = 0 - (-\frac{1}{4} - \frac{1}{2} - \frac{1}{3}) = \frac{13}{12}$
-   $\int_{0}^{1} \frac{1}{4} dx = \frac{1}{4}$
-   $\int_{1}^{3} (x^2 - x + \frac{1}{4}) dx = \left[ \frac{1}{3}x^3 - \frac{1}{2}x^2 + \frac{1}{4}x \right]_1^3 = (9 - 4.5 + 0.75) - (\frac{1}{3} - \frac{1}{2} + \frac{1}{4}) = \frac{62}{12}$

$$\mathbb{E}[Y^2] = \frac{1}{4} \left( \frac{13}{12} + \frac{3}{12} + \frac{62}{12} \right) = \frac{78}{48} = 1.625$$

Enfin, la variance est :
$$\text{Var}(Y) = \mathbb{E}[Y^2] - (\mathbb{E}[Y])^2 = 1.625 - (1.125)^2 = 0.359375$$

