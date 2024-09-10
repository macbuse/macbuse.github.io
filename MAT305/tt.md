
<title>Exercice 4</title>



Pour la fonction $f(x) = \frac{x - 1}{x + 1}$, voici les étapes demandées :

### 1. Déterminer le domaine de définition
La fonction $f(x) = \frac{x - 1}{x + 1}$ est une fonction rationnelle. Elle est définie tant que le dénominateur n'est pas nul.  
Il faut donc résoudre :
$$x + 1 \neq 0$$
$$x \neq -1$$

Le domaine de définition est donc :  
$$D_f = \mathbb{R} \setminus \{-1\}$$

### 2. Calculer la dérivée
Pour calculer la dérivée de $f(x) = \frac{x - 1}{x + 1}$, nous utilisons la formule de la dérivée d'un quotient :
$$f'(x) = (u/v)' = \frac{u'v - uv'}{v^2}$$
où $u(x) = x - 1$ et $v(x) = x + 1$.

---

**ChatGPT made an error in the LaTeX code:**

$$f'(x) = \frac{(u/v)' = u'v - uv'}{v^2}$$

---

- La dérivée de $u(x) = x - 1$ est $u'(x) = 1$,
- La dérivée de $v(x) = x + 1$ est $v'(x) = 1$.

En appliquant la formule, nous avons :
$$f'(x) = \frac{(1)(x+1) - (x-1)(1)}{(x+1)^2}$$
Simplifions l'expression :
$$f'(x) = \frac{x + 1 - x + 1}{(x+1)^2} = \frac{2}{(x+1)^2}$$

### 3. Tableau de variations
La dérivée $f'(x) = \frac{2}{(x+1)^2}$ est toujours positive pour $x \neq -1$, car le carré est toujours positif et $2$ est un nombre positif. Cela signifie que la fonction est **strictement croissante** sur chacun des intervalles $]-\infty, -1[$ et $]-1, +\infty[$.

Il existe une asymptote verticale en $x = -1$, car la fonction n'est pas définie en ce point et tend vers $\pm \infty$ à proximité de cette valeur.

### Asymptote horizontale
Il est utile de calculer la limite de la fonction lorsque $x$ tend vers $\pm \infty$ :
$$\lim_{x \to +\infty} \frac{x - 1}{x + 1} = 1 \quad \text{et} \quad \lim_{x \to -\infty} \frac{x - 1}{x + 1} = 1$$
La fonction admet donc une asymptote horizontale en $y = 1$.

### Tableau de variations

Le tableau de variations est donc :

$$\begin{array}{c|ccccc}
x & -\infty & & -1 & & +\infty \\
\hline
f'(x) & & + & \text{ND} & + & \\
\hline
f(x) & \nearrow & & \text{asymptote verticale} & & \nearrow \\
& & & & & \\
& & & & & \\
\end{array}$$

### Conclusion
- Domaine de définition : $\mathbb{R} \setminus \{-1\}$
- Dérivée : $f'(x) = \frac{2}{(x+1)^2}$, toujours positive sauf en $x = -1$.
- La fonction est strictement croissante et présente une asymptote verticale en $x = -1$ ainsi qu'une asymptote horizontale en $y = 1$.
