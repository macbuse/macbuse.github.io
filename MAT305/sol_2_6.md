Pour la fonction \( f(x) = \exp(-x^2) \), voici les étapes demandées :

### 1. Déterminer le domaine de définition
La fonction exponentielle \( \exp(x) \) est définie pour tout réel, et comme \( -x^2 \) est un polynôme défini pour tout réel, la fonction \( f(x) = \exp(-x^2) \) est également définie sur tout \( \mathbb{R} \).

Le domaine de définition est donc :
\[ D_f = \mathbb{R} \]

### 2. Calculer la dérivée
Pour calculer la dérivée de \( f(x) = \exp(-x^2) \), nous devons appliquer la règle de la dérivée d'une fonction composée. Si \( f(x) = \exp(g(x)) \), alors la dérivée est :
\[
f'(x) = \exp(g(x)) \cdot g'(x)
\]
Ici, \( g(x) = -x^2 \), donc sa dérivée est \( g'(x) = -2x \).

Ainsi, la dérivée de \( f(x) = \exp(-x^2) \) est :
\[
f'(x) = \exp(-x^2) \cdot (-2x)
\]
Simplifions :
\[
f'(x) = -2x \exp(-x^2)
\]

### 3. Tableau de variations

Pour déterminer le tableau de variations, analysons le signe de la dérivée \( f'(x) = -2x \exp(-x^2) \). Notons que \( \exp(-x^2) \) est toujours strictement positif pour tout \( x \in \mathbb{R} \).

Le signe de \( f'(x) \) dépend donc uniquement de \( -2x \) :
- Si \( x > 0 \), alors \( -2x < 0 \), donc \( f'(x) < 0 \) (la fonction est décroissante).
- Si \( x < 0 \), alors \( -2x > 0 \), donc \( f'(x) > 0 \) (la fonction est croissante).
- Si \( x = 0 \), alors \( f'(0) = 0 \).

La fonction présente un maximum local en \( x = 0 \). Calculons la valeur de la fonction à ce point :
\[
f(0) = \exp(0) = 1
\]

### Tableau de variations

Le tableau de variations de la fonction est :

\[
\begin{array}{c|ccccc}
x & -\infty & & 0 & & +\infty \\
\hline
f'(x) & & + & 0 & - & \\
\hline
f(x) & \nearrow & & 1 & & \searrow \\
\end{array}
\]

### Conclusion
- Domaine de définition : \( \mathbb{R} \)
- Dérivée : \( f'(x) = -2x \exp(-x^2) \)
- Tableau de variations : la fonction est croissante sur \( ]-\infty, 0[ \), décroissante sur \( ]0, +\infty[ \), et atteint un maximum en \( x = 0 \) où \( f(0) = 1 \).
