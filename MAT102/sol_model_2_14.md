
### Exercice 14, question c)

**Problème :** Calculer la somme suivante :


$$S = \sum_{k=1}^{n} 2^k$$

#### 1. Identification de la nature de la somme

Il s'agit d'une somme de termes d'une suite géométrique de raison $q = 2$.

#### 2. Détermination des éléments clés

* **Premier terme ($u_{\text{début}}$) :** On remplace l'indice de départ $k = 1$ dans l'expression :

$$u_1 = 2^1 = 2$$


* **Raison ($q$) :** $2$
* **Nombre de termes ($N$) :** Calculé par $\text{indice final} - \text{indice initial} + 1$, soit :

$$n - 1 + 1 = n$$



#### 3. Application de la formule de la somme

Pour une suite géométrique, la formule est :


$$\text{Somme} = (\text{Premier terme}) \times \frac{1 - q^{\text{Nombre de termes}}}{1 - q}$$

En substituant nos valeurs :


$$S = 2 \times \frac{1 - 2^n}{1 - 2} = 2 \times \frac{1 - 2^n}{-1} = -2(1 - 2^n)$$

#### Résultat final

$$S = 2^{n+1} - 2$$

---

### Exercice 15, question b)

**Problème :** Calculer la somme suivante :


$$S = \sum_{k=1}^{n} (2k + 5)$$

#### 1. Identification de la nature de la somme

Le terme général $u_k = 2k + 5$ est une expression affine en $k$, ce qui signifie qu'il s'agit d'une somme de termes d'une **suite arithmétique**.

#### 2. Détermination des éléments clés

* **Premier terme ($u_1$) :** Pour $k = 1$,

$$u_1 = 2(1) + 5 = 7$$


* **Dernier terme ($u_n$) :** Pour $k = n$,

$$u_n = 2n + 5$$


* **Nombre de termes ($N$) :** De $k = 1$ à $k = n$, il y a :

$$n - 1 + 1 = n \text{ termes}$$



#### 3. Application de la formule de la somme

Pour une suite arithmétique, la formule est :


$$\text{Somme} = \text{Nombre de termes} \times \frac{\text{Premier terme} + \text{Dernier terme}}{2}$$

En substituant nos valeurs :


$$S = n \times \frac{7 + (2n + 5)}{2} = n \times \frac{2n + 12}{2}$$

En simplifiant par 2 :


$$S = n(n + 6)$$

#### Résultat final

$$S = n^2 + 6n$$
