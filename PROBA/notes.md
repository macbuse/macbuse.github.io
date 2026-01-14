
### Loi Géométrique $\mathcal{G}(p)$

La **loi géométrique** modélise le rang du premier succès dans une suite d'épreuves de Bernoulli indépendantes de paramètre $p$.

* **Support :** $k \in \{1, 2, 3, \dots\}$
* **Probabilité :** $\mathbb{P}(X = k) = (1-p)^{k-1}p$
* **Espérance :** $E(X) = \frac{1}{p}$
* **Variance :** $V(X) = \frac{1-p}{p^2}$
* **Absence de mémoire :** $\mathbb{P}(X > n+k \mid X > n) = \mathbb{P}(X > k)$

---


Une **épreuve de Bernoulli** est l'expérience aléatoire la plus simple en probabilités. Voici sa définition et ses caractéristiques fondamentales :

### 1. Définition
Une épreuve de Bernoulli est une expérience aléatoire qui ne comporte que **deux issues possibles**, généralement qualifiées de :
* **Succès** (noté $S$ ou $1$) : l'événement que l'on étudie.
* **Échec** (noté $E$ ou $0$) : l'événement contraire.



### 2. Paramètre de l'épreuve
Elle est caractérisée par un unique paramètre réel $p \in [0, 1]$, où :
* $p$ est la probabilité du succès : $\mathbb{P}(S) = p$.
* $q = 1 - p$ est la probabilité de l'échec : $\mathbb{P}(E) = 1 - p$.

### 3. La Variable Aléatoire de Bernoulli
On associe souvent à cette épreuve une variable aléatoire $X$ qui prend la valeur **1** en cas de succès et **0** en cas d'échec. Sa loi de probabilité est définie par :

| $k$ | $0$ | $1$ |
| :--- | :--- | :--- |
| $\mathbb{P}(X=k)$ | $1-p$ | $p$ |

### 4. Propriétés Mathématiques
Pour une variable aléatoire $X$ suivant une loi de Bernoulli de paramètre $p$ (notée $X \sim \mathcal{B}(p)$) :
* **Espérance :** $E(X) = p$
* **Variance :** $V(X) = p(1-p)$

---

### Exemples classiques
* **Lancer de pièce :** Si on cherche "Pile" (succès), alors $p = 0,5$.
* **Lancer de dé :** Si on cherche à obtenir un "6" (succès), alors $p = 1/6$ et l'échec (ne pas avoir 6) a une probabilité $q = 5/6$.
* **Contrôle qualité :** Vérifier si une pièce est défectueuse ou non.

### Vers la Loi Binomiale
Lorsqu'on répète $n$ fois la même épreuve de Bernoulli de manière **indépendante** et dans les mêmes conditions, on obtient un **schéma de Bernoulli**. La variable aléatoire qui compte le nombre total de succès obtenus suit alors une **loi binomiale** $\mathcal{B}(n, p)$.


---

## Exercice : Minimum de variables géométriques indépendantes

Soient $p_1, \dots, p_n \in (0,1)$ et $X_1, \dots, X_n$ des variables aléatoires indépendantes avec $X_i \sim \text{géom}(p_i)$.
On définit $M := \min\{X_1, \dots, X_n\}$.

---

### a) Détermination de $\mathbb{P}(X_i \ge k)$

Pour $k \in \mathbb{N}^*$, l'événement $\{X_i \ge k\}$ signifie que les $k-1$ premières épreuves ont été des échecs. La probabilité d'un échec pour la variable $i$ est $1 - p_i$. Par conséquent :
$$\mathbb{P}(X_i \ge k) = (1 - p_i)^{k-1}$$

Voici le texte extrait de l’image :

---

**Solution :** On peut soit procéder par un calcul direct,

$$
\mathbb{P}(X_i \ge k)
= p_i \sum_{\ell \ge k} (1 - p_i)^{\ell - 1}
= p_i (1 - p_i)^{k-1} \sum_{\ell \ge 0} (1 - p_i)^{\ell}
= (1 - p_i)^{k-1},
$$

soit observer que cette probabilité est la probabilité que (k - 1) épreuves de Bernoulli de paramètre (p_i) résultent toutes en un échec.




---

### b) Détermination de $\mathbb{P}(M \ge k)$

Par définition du minimum, l'événement $\{M \ge k\}$ est réalisé si et seulement si toutes les variables $X_i$ sont simultanément supérieures ou égales à $k$ :
$$\{M \ge k\} = \{X_1 \ge k\} \cap \{X_2 \ge k\} \cap \dots \cap \{X_n \ge k\}$$

Comme les variables $X_1, \dots, X_n$ sont indépendantes, la probabilité de l'intersection est le produit des probabilités individuelles :
$$\mathbb{P}(M \ge k) = \prod_{i=1}^n \mathbb{P}(X_i \ge k) = \prod_{i=1}^n (1 - p_i)^{k-1}$$
En utilisant les propriétés des puissances, on obtient :
$$\mathbb{P}(M \ge k) = \left[ \prod_{i=1}^n (1 - p_i) \right]^{k-1}$$

### c) Loi de $M$ et expression de $\rho$

On reconnaît dans l'expression précédente la fonction de survie d'une loi géométrique. En effet, si $M \sim \text{géom}(\rho)$, alors $\mathbb{P}(M \ge k) = (1 - \rho)^{k-1}$.
Par identification :
$$1 - \rho = \prod_{i=1}^n (1 - p_i) \implies \rho = 1 - \prod_{i=1}^n (1 - p_i)$$
**Conclusion :** $M$ suit une loi géométrique de paramètre $\rho = 1 - (1-p_1)(1-p_2)\dots(1-p_n)$.

### d) Preuve alternative par réinterprétation

Considérons $n$ suites d'épreuves de Bernoulli menées en parallèle. À chaque instant $t \in \mathbb{N}^*$, on effectue $n$ lancers où la probabilité de succès pour la suite $i$ est $p_i$. $X_i$ est le temps du premier succès de la suite $i$.



Le minimum $M$ représente l'instant du **premier succès observé globalement** (toutes suites confondues). À chaque instant $t$, la probabilité qu'aucun succès ne survienne dans aucune des $n$ suites est :
$$\mathbb{P}(\text{aucun succès à } t) = (1-p_1) \times (1-p_2) \times \dots \times (1-p_n)$$
L'événement "avoir au moins un succès global" à l'instant $t$ est le complémentaire, de probabilité :
$$\rho = 1 - (1-p_1)(1-p_2)\dots(1-p_n)$$

---


# exercise 2

**Solution**

On suppose que $X$ et $Y$ sont indépendantes et suivent la loi géométrique de paramètre $p \in (0,1)$, c’est-à-dire
$$
\mathbb{P}(X = k) = \mathbb{P}(Y = k) = p(1-p)^{k-1}, \quad k \in \mathbb{N}^*.
$$

---

### a) Calcul de $\mathbb{P}(U \le u, V \ge v)$ et lois de $U$ et $V$

On a
$$
\{U \le u, V \ge v\} = \{v \le X \le u, \; v \le Y \le u\}.
$$
Par indépendance de $X$ et $Y$,
$$
\mathbb{P}(U \le u, V \ge v)
= \mathbb{P}(v \le X \le u)^2.
$$
Or
$$
\mathbb{P}(v \le X \le u)
= \mathbb{P}(X \ge v) - \mathbb{P}(X \ge u+1)
= (1-p)^{v-1} - (1-p)^u.
$$
Donc
$$
\mathbb{P}(U \le u, V \ge v)
= \left((1-p)^{v-1} - (1-p)^u\right)^2.
$$

**Loi de $V$**

On a
$$
\mathbb{P}(V \ge v) = \mathbb{P}(X \ge v, Y \ge v)
= (1-p)^{2(v-1)}.
$$
Ainsi $V$ suit une loi géométrique de paramètre
$$
\rho = 1 - (1-p)^2 = 2p - p^2.
$$

**Loi de $U$**

On a
$$
\mathbb{P}(U \le u) = \mathbb{P}(X \le u, Y \le u)
= \left(1 - (1-p)^u\right)^2.
$$
Donc
$$
\mathbb{P}(U = u)
= \mathbb{P}(U \le u) - \mathbb{P}(U \le u-1)
= (1-p)^{u-1}\bigl(2p - p^2(1-p)^{u-1}\bigr).
$$

---

### b) Loi de $D = |X - Y|$ et indépendance avec $V$

Pour $k \ge 1$,
$$
\mathbb{P}(D = k)
= 2 \sum_{n \ge 1} \mathbb{P}(X = n+k, Y = n)
= 2 \sum_{n \ge 1} p^2 (1-p)^{2n+k-2}.
$$
Ainsi,
$$
\mathbb{P}(D = k)
= 2p^2 (1-p)^k \sum_{n \ge 0} (1-p)^{2n}
= \frac{2p^2 (1-p)^k}{1 - (1-p)^2}
= \frac{2p (1-p)^k}{2-p}.
$$
Pour $k = 0$,
$$
\mathbb{P}(D = 0)
= \sum_{n \ge 1} p^2 (1-p)^{2n-2}
= \frac{p}{2-p}.
$$

**Indépendance de $D$ et $V$**

Pour $v \ge 1$ et $k \ge 0$,
$$
\mathbb{P}(D = k, V = v)
= 
\begin{cases}
p^2 (1-p)^{2v-2}, & k = 0, \\
2 p^2 (1-p)^{2v+k-2}, & k \ge 1.
\end{cases}
$$
On vérifie alors que
$$
\mathbb{P}(D = k, V = v)
= \mathbb{P}(D = k)\,\mathbb{P}(V = v),
$$
ce qui montre que $D$ et $V$ sont indépendantes.

