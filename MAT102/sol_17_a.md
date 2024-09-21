Soit \( z = x + iy \), un nombre complexe où \( x \) et \( y \) sont respectivement les parties réelle et imaginaire de \( z \). Nous voulons étudier l'équation suivante :

\[
\text{Im} \left( \frac{z + 2i}{z - 1} \right) = 0
\]

Cela signifie que la partie imaginaire du quotient est nulle, ce qui implique que le quotient est un nombre réel. Pour montrer que cela représente une droite dans le plan complexe, nous allons procéder étape par étape.

### Étape 1 : Calculer \( \frac{z + 2i}{z - 1} \)

Remplaçons \( z \) par \( x + iy \) dans l'expression :

\[
\frac{z + 2i}{z - 1} = \frac{(x + iy) + 2i}{(x + iy) - 1}
\]

Cela devient :

\[
\frac{(x + i(y + 2))}{(x - 1) + iy}
\]

Pour simplifier cette expression, multiplions le numérateur et le dénominateur par le conjugué du dénominateur :

\[
\frac{(x + i(y + 2))}{(x - 1) + iy} \times \frac{(x - 1) - iy}{(x - 1) - iy} = \frac{(x + i(y + 2))((x - 1) - iy)}{((x - 1)^2 + y^2)}
\]

### Étape 2 : Simplifier le numérateur

Développons le numérateur :

\[
(x + i(y + 2))((x - 1) - iy) = x(x - 1) - xiy + i(y + 2)(x - 1) + i^2(y + 2)y
\]

En simplifiant, rappelons que \( i^2 = -1 \) :

\[
= x(x - 1) - xiy + i(y + 2)(x - 1) - (y + 2)y
\]
\[
= x(x - 1) - xiy + i(y + 2)(x - 1) - y^2 - 2y
\]

Le numérateur est donc :

\[
= (x(x - 1) - y^2 - 2y) + i\left((y + 2)(x - 1) - xy \right)
\]

### Étape 3 : Partie imaginaire de l'expression

La partie imaginaire de l'expression totale est donnée par :

\[
\text{Im} \left( \frac{z + 2i}{z - 1} \right) = \frac{(y + 2)(x - 1) - xy}{(x - 1)^2 + y^2}
\]

Nous devons résoudre l'équation :

\[
(y + 2)(x - 1) - xy = 0
\]

### Étape 4 : Résolution de l'équation

Développons l'équation :

\[
(y + 2)(x - 1) - xy = (y + 2)x - (y + 2) - xy = 0
\]
\[
yx + 2x - y - 2 - xy = 0
\]
\[
2x - y - 2 = 0
\]

Cette équation est celle d'une droite dans le plan réel \( \mathbb{R}^2 \), où \( x \) et \( y \) sont les coordonnées de \( z = x + iy \). Elle peut être réarrangée comme suit :

\[
y = 2x - 2
\]

### Conclusion

L'équation \( \text{Im} \left( \frac{z + 2i}{z - 1} \right) = 0 \) représente donc une droite dans le plan complexe, décrite par l'équation \( y = 2x - 2 \).
