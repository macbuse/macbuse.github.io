Voici les solutions étape par étape pour chaque expression de l'**Exercice 16** :

---

### a) $\displaystyle\sum_{p=1}^{n} (1 + 2ip)$

* **Séparation de la somme :**

$$\sum_{p=1}^{n} 1 + 2i \sum_{p=1}^{n} p$$



* **Calcul des sommes usuelles :**

$$\sum_{p=1}^{n} 1 = n \quad \text{et} \quad \sum_{p=1}^{n} p = \frac{n(n+1)}{2}$$



* **Résultat sous forme algébrique :**

$$n + 2i \left(\frac{n(n+1)}{2}\right) = n + i\,n(n+1) = n + (n^2 + n)i$$




---

### b) $\displaystyle\sum_{k=1}^{10} (2 + ik)$

* **Séparation de la somme :**

$$\sum_{k=1}^{10} 2 + i \sum_{k=1}^{10} k$$



* **Calcul des sommes :**

$$\sum_{k=1}^{10} 2 = 2 \times 10 = 20 \quad \text{et} \quad \sum_{k=1}^{10} k = \frac{10 \times 11}{2} = 55$$



* **Résultat sous forme algébrique :**

$$20 + 55i$$




---

### c) $\displaystyle\sum_{l=1}^{n} \frac{5l}{2+i}$

* **Factorisation des termes indépendants de $l$ et rationalisation du dénominateur :**

$$\frac{5}{2+i} = \frac{5(2-i)}{2^2 + 1^2} = \frac{5(2-i)}{5} = 2 - i$$



* **Application à la somme :**

$$(2 - i) \sum_{l=1}^{n} 5l \quad \text{ou plus simplement} \quad (2 - i) \times \frac{5n(n+1)}{2}$$



* **Résultat sous forme algébrique :**

$$\frac{5n(n+1)}{2}(2 - i) = 5n(n+1) - \frac{5n(n+1)}{2}i$$




---

### d) $\displaystyle\sum_{n=1}^{p} \frac{n+i}{1+i}$

* **Rationalisation du dénominateur et séparation de la somme :**

$$\frac{1}{1+i} = \frac{1-i}{1^2 + 1^2} = \frac{1-i}{2}$$



* **Réécriture de l'expression :**

$$\sum_{n=1}^{p} \frac{(n+i)(1-i)}{2} = \sum_{n=1}^{p} \frac{n - ni + i - i^2}{2} = \sum_{n=1}^{p} \frac{(n+1) + (1-n)i}{2}$$



* **Calcul des sommes pour $n$ de $1$ à $p$ :**
* Partie réelle : $\frac{1}{2} \left( \sum_{n=1}^{p} n + \sum_{n=1}^{p} 1 \right) = \frac{1}{2} \left( \frac{p(p+1)}{2} + p \right) = \frac{p(p+3)}{4}$

* Partie imaginaire : $\frac{1}{2} \left( \sum_{n=1}^{p} 1 - \sum_{n=1}^{p} n \right) = \frac{1}{2} \left( p - \frac{p(p+1)}{2} \right) = \frac{p(1-p)}{4}$



* **Résultat sous forme algébrique :**

$$\frac{p(p+3)}{4} + \frac{p(1-p)}{4}i$$
