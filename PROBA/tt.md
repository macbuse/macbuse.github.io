## Exercice 3 - Urne de Polya


---

### Résumé de la structure logique

La résolution de ce problème repose sur un enchaînement de propriétés qui permettent de passer d'un tirage local à une loi générale :

* **Initialisation (a) :** On établit la loi pour les deux premiers tirages ($n=1$ et $n=2$). On remarque déjà que $P(X_1=1) = P(X_2=1)$, ce qui suggère la stationnarité du processus.
* **Analyse de l'état du système (b & c) :** On montre que la probabilité de succès au tirage $n+1$ ne dépend pas de l'ordre des tirages précédents, mais uniquement du nombre cumulé de boules bleues obtenues ($S_n$). On établit la relation fondamentale : 
    $$P(X_{n+1} = 1) = \frac{b + d \cdot E[S_n]}{b + r + nd}$$
* **Dynamique de l'espérance (d) :** On utilise la linéarité de l'espérance pour lier $E[S_n]$ au tirage précédent, créant ainsi une structure de récurrence.
* **Hérédité et Conclusion (e & f) :** Par substitution algébrique, on prouve que si la probabilité est constante jusqu'au rang $n$, elle l'est aussi au rang $n+1$. Par récurrence, on conclut que chaque tirage suit la même loi de Bernoulli :
    $$X_n \sim \mathcal{B}\left(\frac{b}{b+r}\right)$$

---

Une **loi de Bernoulli** est une loi de probabilité très simple qui modélise une expérience aléatoire avec **seulement deux issues possibles**.

## Définition
On parle de **loi de Bernoulli de paramètre $p$** lorsque :
- il y a un **succès** (noté 1) avec une probabilité $p$,
- il y a un **échec** (noté 0) avec une probabilité $1 - p$,

où $0 \le p \le 1$.

On note alors :
$$
X \sim \mathcal{B}(p)
$$

## Exemple
- Lancer une pièce :
  - $X = 1$ si on obtient *pile* (succès),
  - $X = 0$ si on obtient *face* (échec),
  - si la pièce est équilibrée, $p = 0{,}5$.

- Test médical :
  - $X = 1$ si le test est positif,
  - $X = 0$ s’il est négatif.

## Propriétés importantes
Pour une variable aléatoire $X$ suivant une loi de Bernoulli de paramètre $p$ :
- **Espérance** :
$$
\mathbb{E}(X) = p
$$
- **Variance** :
$$
\mathrm{Var}(X) = p(1 - p)
$$

**Résumé :** la loi de Bernoulli modélise une situation « oui / non », « succès / échec ».





### Analyse du problème
L'urne évolue à chaque tirage. Initialement, nous avons :
* $b$ : nombre de boules bleues.
* $r$ : nombre de boules rouges.
* $N = b + r$ : nombre total de boules.

À chaque fois qu'on tire une boule d'une couleur, on la remet avec $d$ boules supplémentaires de la **même** couleur.

---

### 1. Loi de $X_1$
Le premier tirage s'effectue dans l'urne initiale. La probabilité de tirer une boule bleue est simplement le ratio du nombre de boules bleues sur le total.

* $P(X_1 = 1) = \frac{b}{b + r}$
* $P(X_1 = 0) = \frac{r}{b + r}$

La loi de $X_1$ est une **loi de Bernoulli** de paramètre $p = \frac{b}{b + r}$. On note :
$$X_1 \sim \mathcal{B}\left(\frac{b}{b+r}\right)$$

---

### 2. Loi de $X_2$
Pour calculer la probabilité que la deuxième boule soit bleue, nous devons utiliser la **formule des probabilités totales** en passant par le résultat du premier tirage ($X_1$).



#### Cas 1 : La première boule était bleue ($X_1 = 1$)
On a ajouté $d$ boules bleues. L'urne contient maintenant $b+d$ boules bleues et $r$ boules rouges. Le total est $b+r+d$.
$$P(X_2 = 1 \mid X_1 = 1) = \frac{b + d}{b + r + d}$$

#### Cas 2 : La première boule était rouge ($X_1 = 0$)
On a ajouté $d$ boules rouges. L'urne contient maintenant $b$ boules bleues et $r+d$ boules rouges. Le total est $b+r+d$.
$$P(X_2 = 1 \mid X_1 = 0) = \frac{b}{b + r + d}$$

#### Calcul final :
$$P(X_2 = 1) = P(X_2 = 1 \mid X_1 = 1)P(X_1 = 1) + P(X_2 = 1 \mid X_1 = 0)P(X_1 = 0)$$

Substituons les valeurs :
$$P(X_2 = 1) = \left( \frac{b + d}{b + r + d} \cdot \frac{b}{b + r} \right) + \left( \frac{b}{b + r + d} \cdot \frac{r}{b + r} \right)$$

Factorisons par $\frac{b}{(b+r)(b+r+d)}$ :
$$P(X_2 = 1) = \frac{b(b + d + r)}{(b + r)(b + r + d)}$$

En simplifiant par $(b + r + d)$ au numérateur et au dénominateur, on obtient :
$$P(X_2 = 1) = \frac{b}{b + r}$$

**Conclusion :**
La loi de $X_2$ est identique à celle de $X_1$. C'est une **loi de Bernoulli** de paramètre $\frac{b}{b + r}$.


### c) En déduire une expression pour $P(X_{n+1} = 1)$ en termes de $E[S_n]$

Pour calculer $P(X_{n+1} = 1)$, on utilise la **loi des probabilités totales** en conditionnant par les valeurs possibles de $S_n$ :

$$P(X_{n+1} = 1) = \sum_{k=0}^{n} P(X_{n+1} = 1 \mid S_n = k) \cdot P(S_n = k)$$

D'après le résultat de la question **b)**, nous savons que :
$$P(X_{n+1} = 1 \mid S_n = k) = \frac{b + kd}{b + r + nd}$$

En injectant cette expression dans la somme :
$$P(X_{n+1} = 1) = \sum_{k=0}^{n} \frac{b + kd}{b + r + nd} \cdot P(S_n = k)$$

Par linéarité de la somme :
$$P(X_{n+1} = 1) = \frac{b}{b + r + nd} \sum_{k=0}^{n} P(S_n = k) + \frac{d}{b + r + nd} \sum_{k=0}^{n} k \cdot P(S_n = k)$$

Sachant que $\sum_{k=0}^{n} P(S_n = k) = 1$ et que $\sum_{k=0}^{n} k \cdot P(S_n = k) = E[S_n]$, on obtient :
$$P(X_{n+1} = 1) = \frac{b + d \cdot E[S_n]}{b + r + nd}$$

---

### d) Exprimer $E[S_n]$ en termes de $E[S_{n-1}]$ et $P(X_n = 1)$

Par définition, $S_n = S_{n-1} + X_n$. Par linéarité de l'espérance :
$$E[S_n] = E[S_{n-1}] + E[X_n]$$

Puisque $X_n$ est une variable de Bernoulli, $E[X_n] = P(X_n = 1)$. On a donc :
$$E[S_n] = E[S_{n-1}] + P(X_n = 1)$$

---

### e) En déduire que $P(X_{n+1} = 1) = P(X_n = 1)$

Utilisons l'expression de la question **c)** au rang $n$ :
$$P(X_{n+1} = 1) = \frac{b + d \cdot E[S_n]}{b + r + nd}$$

Substituons $E[S_n]$ par l'expression trouvée en **d)** :
$$P(X_{n+1} = 1) = \frac{b + d(E[S_{n-1}] + P(X_n = 1))}{b + r + nd}$$
$$P(X_{n+1} = 1) = \frac{b + d \cdot E[S_{n-1}] + d \cdot P(X_n = 1)}{b + r + nd}$$

Or, d'après la formule de la question **c)** appliquée au tirage précédent :
$$P(X_n = 1) = \frac{b + d \cdot E[S_{n-1}]}{b + r + (n-1)d}$$
Ce qui implique : $b + d \cdot E[S_{n-1}] = P(X_n = 1) \cdot (b + r + (n-1)d)$.

En remplaçant dans notre équation :
$$P(X_{n+1} = 1) = \frac{P(X_n = 1)(b + r + (n-1)d) + d \cdot P(X_n = 1)}{b + r + nd}$$
$$P(X_{n+1} = 1) = \frac{P(X_n = 1) [b + r + nd - d + d]}{b + r + nd}$$
$$P(X_{n+1} = 1) = P(X_n = 1) \cdot \frac{b + r + nd}{b + r + nd} = P(X_n = 1)$$

---

### f) Quelle est la loi de $X_n$ ?

Nous avons montré par récurrence à la question précédente que $P(X_n = 1)$ est constant pour tout $n$. 
Comme $P(X_1 = 1) = \frac{b}{b+r}$, alors pour tout $n \in \mathbb{N}^*$ :
$$P(X_n = 1) = \frac{b}{b+r}$$

La variable $X_n$ suit donc une **loi de Bernoulli** de paramètre $p = \frac{b}{b+r}$ :

$$X_n \sim \mathcal{B}\left(\frac{b}{b+r}\right)$$

