
# Fiche Synthétique : La Loi de Poisson

La loi de Poisson, notée $\mathcal{P}(\lambda)$, est une loi de probabilité discrète. Le paramètre $\lambda$ (avec $\lambda > 0$) représente le nombre moyen d'occurrences sur un intervalle donné.

### 1. Définition et Support
Si $X \sim \mathcal{P}(\lambda)$, alors $X$ peut prendre n'importe quelle valeur entière naturelle.

* **Support :** $X(\Omega) = \mathbb{N} = \{0, 1, 2, \dots\}$

### 2. Fonction de masse (Densité discrète)
La probabilité d'obtenir exactement $k$ succès est donnée par :
$$ \mathbb{P}(X = k) = e^{-\lambda} \frac{\lambda^k}{k!} $$

### 3. Moments (Espérance et Variance)
Une propriété remarquable de la loi de Poisson est que son espérance et sa variance sont égales à son paramètre :


* **Espérance :** $E[X] = \lambda$
* **Variance :** $V(X) := E(X^2) - E(X)^2 = \lambda$
* **Écart-type :** $\sigma_X = \sqrt{\lambda}$

### 4. Propriétés Fondamentales

* **Stabilité (Somme de variables) :** 

Si $X \sim \mathcal{P}(\lambda_1)$ et $Y \sim \mathcal{P}(\lambda_2)$ sont indépendantes,
<br> alors $X + Y \sim \mathcal{P}(\lambda_1 + \lambda_2)$.

* **Approximation de la loi Binomiale :** 

Si $n \ge 30$, $p \le 0,1$ et $np \le 10$, 
<br> alors la loi $\mathcal{B}(n, p)$ peut être approximée par $\mathcal{P}(np)$. On l'appelle souvent la "loi des événements rares".

### 5. Allure de la distribution
La forme de la distribution dépend fortement de $\lambda$ :

* Si $\lambda < 1$, la probabilité décroît strictement.
* Si $\lambda$ est grand, la distribution devient symétrique et se rapproche d'une loi normale $\mathcal{N}(\lambda, \lambda)$.



### 6. Fonction Génératrice
La fonction génératrice des moments est :
$$ G_X(t) = E[t^X] = e^{\lambda(t-1)} $$


---

### Approximation de la Loi Binomiale par la Loi de Poisson

Cette règle, souvent appelée **Théorème de la limite de Poisson**, établit qu'une loi binomiale peut être remplacée par une loi de Poisson sous certaines conditions. On l'appelle "loi des événements rares" car elle modélise des phénomènes où un grand nombre d'essais ($n$) est combiné à une probabilité de succès ($p$) très faible.

### 1. Les Conditions d'application
L'approximation est jugée robuste et fiable lorsque les trois critères suivants sont réunis :

* $n \ge 30$ : Le nombre d'essais doit être suffisamment grand.
* $p \le 0,1$ : La probabilité de succès doit être faible (événement rare).
* $np \le 10$ : La moyenne attendue (le paramètre $\lambda$) ne doit pas être trop élevée.



### 2. La Formule
Si $X \sim \mathcal{B}(n, p)$ et que les conditions ci-dessus sont respectées, alors on peut approcher $X$ par une loi de Poisson de paramètre $\lambda = np$ :

$$ X \sim \mathcal{P}(np) $$

Ce qui signifie que pour tout entier $k$ :
$$ \binom{n}{k} p^k (1-p)^{n-k} \approx e^{-np} \frac{(np)^k}{k!} $$

### 3. Pourquoi ces critères ?

* **Stabilité de la forme :** Si $p$ est proche de $0,5$, la distribution binomiale est symétrique. En revanche, si $p$ est petit, elle devient asymétrique avec une "queue" vers la droite, ce qui est la caractéristique exacte de la loi de Poisson.

* **Convergence de la variance :** * Variance Binomiale : $V(X) = np(1-p)$
    * Variance Poisson : $V(X) = np$
    Si $p$ est très petit (par exemple $0,01$), alors $(1-p)$ est proche de $1$ (ici $0,99$), et les deux variances deviennent quasiment identiques.



### 4. Intérêt pratique
Le calcul d'une loi binomiale nécessite de manipuler des factorielles très grandes (comme $100!$) et des puissances élevées, ce qui peut être complexe sans ordinateur. La loi de Poisson simplifie le calcul en n'utilisant qu'une seule exponentielle et une puissance plus simple :

**Exemple :** Soit un lot de $n=100$ composants avec un risque de défaut $p=0,02$.
Calculer la probabilité d'avoir exactement 2 défauts :

* **Méthode Binomiale :** $\mathbb{P}(X=2) = \binom{100}{2} (0,02)^2 (0,98)^{98}$
* **Méthode Poisson ($\lambda = 2$) :** $\mathbb{P}(X=2) \approx e^{-2} \frac{2^2}{2!} = 2e^{-2} \approx 0,2707$

L'erreur entre ces deux calculs est négligeable, ce qui justifie l'approximation.


---

# Solution de l'exercice : Somme de variables de Poisson et Processus de fautes

| Question | Description de la probabilité | Formule ou Loi |
| :--- | :--- | :--- |
| **a)** | Somme de deux variables $X+Y$ | $X+Y \sim \mathrm{Poisson}(\lambda + \mu)$ |
| **b)** | Somme de $n$ variables $S_n$ | $S_n \sim \mathrm{Poisson}(n\lambda)$ |
| **c) i.** | Première faute à la page $k$ | $P(F=k) = e^{-(k-1)\lambda}(1 - e^{-\lambda})$ |
| **c) ii.** | Au moins $\ell$ fautes dans $r$ pages | $P(S_r \ge \ell) = 1 - \sum_{j=0}^{\ell-1} e^{-r\lambda} \frac{(r\lambda)^j}{j!}$ |
| **c) iii.** | $\ell$-ième faute à la page $k$ | $P(G_\ell = k) = P(S_k \ge \ell) - P(S_{k-1} \ge \ell)$ |


### Question a)
**Soit $X \sim \mathrm{Poisson}(\lambda)$ et $Y \sim \mathrm{Poisson}(\mu)$ deux variables aléatoires indépendantes. 

Montrer que $X + Y \sim \mathrm{Poisson}(\lambda + \mu)$.**

Soit $n \in \mathbb{N}$. Comme $X$ et $Y$ sont indépendantes et à valeurs dans $\mathbb{N}$, nous utilisons la formule de convolution :

$$ \mathbb{P}(X+Y = n) = \sum_{k=0}^{n} \mathbb{P}(X=k) \mathbb{P}(Y=n-k) $$

En remplaçant par les fonctions de masse de la loi de Poisson :

$$ \mathbb{P}(X+Y = n) = \sum_{k=0}^{n} \left( e^{-\lambda} \frac{\lambda^k}{k!} \right) \left( e^{-\mu} \frac{\mu^{n-k}}{(n-k)!} \right) $$

$$ \mathbb{P}(X+Y = n) = e^{-(\lambda+\mu)} \sum_{k=0}^{n} \frac{\lambda^k \mu^{n-k}}{k!(n-k)!} $$

On multiplie et on divise par $n!$ pour faire apparaître le coefficient binomial $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ :

$$ \mathbb{P}(X+Y = n) = \frac{e^{-(\lambda+\mu)}}{n!} \sum_{k=0}^{n} \binom{n}{k} \lambda^k \mu^{n-k} $$

D'après la formule du binôme de Newton, la somme est égale à $(\lambda + \mu)^n$. On obtient donc :

$$ \mathbb{P}(X+Y = n) = e^{-(\lambda+\mu)} \frac{(\lambda+\mu)^n}{n!} $$

Ceci correspond exactement à la loi de **$\mathrm{Poisson}(\lambda + \mu)$**.

---

### Question b)
**Soit $X_1, \ldots, X_n$ des variables aléatoires indépendantes suivant chacune une loi de Poisson de paramètre $\lambda$. Montrer que $X_1 + \cdots + X_n \sim \mathrm{Poisson}(n\lambda)$.**

Nous procédons par récurrence sur $n$.

* **Initialisation ($n=1$) :** $X_1 \sim \mathrm{Poisson}(\lambda)$, ce qui est bien $\mathrm{Poisson}(1 \cdot \lambda)$.
* **Hérédité :** Supposons que pour un entier $n \ge 1$, $S_n = \sum_{i=1}^{n} X_i \sim \mathrm{Poisson}(n\lambda)$.

    Considérons $S_{n+1} = S_n + X_{n+1}$.
    Puisque les $X_i$ sont indépendantes, $S_n$ est indépendante de $X_{n+1}$.
    En appliquant le résultat de la question **a)** avec $\lambda_1 = n\lambda$ et $\lambda_2 = \lambda$ :
    $$ S_{n+1} \sim \mathrm{Poisson}(n\lambda + \lambda) = \mathrm{Poisson}((n+1)\lambda) $$

La propriété est donc démontrée pour tout $n \in \mathbb{N}^*$.

---

### Question c)
**Notons $X_k$ le nombre de fautes sur la $k$-ième page. $X_k \sim \mathrm{Poisson}(\lambda)$ indépendantes.**

**i. Probabilité que la première faute se trouve sur la $k$-ième page.**

Soit $F$ l'indice de la page contenant la première faute. L'événement $\{F=k\}$ signifie qu'il n'y a aucune faute sur les $k-1$ premières pages et au moins une faute sur la page $k$ :
$$ \mathbb{P}(F = k) = \mathbb{P}(X_1=0, \dots, X_{k-1}=0, X_k \ge 1) $$
Par indépendance :
$$ \mathbb{P}(F = k) = \left( \prod_{i=1}^{k-1} \mathbb{P}(X_i=0) \right) \cdot \mathbb{P}(X_k \ge 1) $$
$$ \mathbb{P}(F = k) = (e^{-\lambda})^{k-1} (1 - e^{-\lambda}) $$
$$ \mathbb{P}(F = k) = e^{-(k-1)\lambda} (1 - e^{-\lambda}) $$

**ii. Pour $1 \le r \le n$, soit $S_r = X_1 + \cdots + X_r$. Calculer $\mathbb{P}(S_r \ge \ell)$.**

D'après **b)**, $S_r \sim \mathrm{Poisson}(r\lambda)$.
$$ \mathbb{P}(S_r \ge \ell) = 1 - \mathbb{P}(S_r < \ell) = 1 - \sum_{j=0}^{\ell-1} e^{-r\lambda} \frac{(r\lambda)^j}{j!} $$

**iii. Probabilité que la $\ell$-ième faute se trouve sur la $k$-ième page.**

Soit $G_\ell$ l'indice de la page contenant la $\ell$-ième faute. La $\ell$-ième faute est à la page $k$ si et seulement si il y a au moins $\ell$ fautes au total dans les $k$ premières pages, mais moins de $\ell$ fautes dans les $k-1$ premières pages.
$$ \mathbb{P}(G_\ell = k) = \mathbb{P}(S_k \ge \ell \text{ et } S_{k-1} < \ell) $$
Comme $\{S_{k-1} \ge \ell\} \subset \{S_k \ge \ell\}$, on peut écrire :
$$ \mathbb{P}(G_\ell = k) = \mathbb{P}(S_k \ge \ell) - \mathbb{P}(S_{k-1} \ge \ell) $$
En utilisant le résultat de la question précédente :
$$ \mathbb{P}(G_\ell = k) = \left( 1 - \sum_{j=0}^{\ell-1} e^{-k\lambda} \frac{(k\lambda)^j}{j!} \right) - \left( 1 - \sum_{j=0}^{\ell-1} e^{-(k-1)\lambda} \frac{((k-1)\lambda)^j}{j!} \right) $$
$$ \mathbb{P}(G_\ell = k) = \sum_{j=0}^{\ell-1} \left( e^{-(k-1)\lambda} \frac{((k-1)\lambda)^j}{j!} - e^{-k\lambda} \frac{(k\lambda)^j}{j!} \right) $$
