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
