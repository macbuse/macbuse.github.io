Nous voulons montrer que les solutions de l'équation suivante sont un cercle dans le plan complexe :

\[
\text{Re} \left( \frac{z + 2i}{z - 1} \right) = 0
\]

où \( z = x + iy \), avec \( x \) et \( y \) les parties réelle et imaginaire de \( z \). 


### Étape 1 : Partie réelle de l'expression

D'après les calculs pour la partie **a)**
la partie réelle de l'expression totale est :

\[
\text{Re} \left( \frac{z + 2i}{z - 1} \right) 
= \frac{x(x - 1) + y^2 + 2y}{(x - 1)^2 + y^2}
\]

---

**ChatGPT made a mistake in the sign**

$$\text{Re} \left( \frac{z + 2i}{z - 1} \right) = \frac{x(x - 1) - y^2 - 2y}{(x - 1)^2 + y^2}$$

---

Nous devons résoudre l'équation suivante :

\[
 (x(x - 1) + y^2 + 2y) = 0
\]

---

## Centre et rayon du cercle
L'équation \(x(x - 1) + y^2 + 2y = 0\) peut être réécrite sous une forme plus classique pour identifier le centre du cercle.

### Étape 1 : Réarranger l'équation
L'équation actuelle est :

\[
x(x - 1) + y^2 + 2y = 0
\]

Développons le terme en \(x\) :

\[
x^2 - x + y^2 + 2y = 0
\]

Nous cherchons à mettre cette équation sous la forme classique d'un cercle \((x - h)^2 + (y - k)^2 = r^2\), où \((h, k)\) est le centre et \(r\) est le rayon.

### Étape 2 : Compléter le carré
Commençons par compléter le carré pour les termes en \(y\). Nous avons :

\[
y^2 + 2y
\]

Complétons le carré pour cela. Le terme manquant est \(\left(\frac{2}{2}\right)^2 = 1\). Nous ajoutons et soustrayons 1 :

\[
y^2 + 2y + 1 - 1 = (y + 1)^2 - 1
\]

Ainsi, l'équation devient :

\[
x^2 - x + (y + 1)^2 - 1 = 0
\]

### Étape 3 : Compléter le carré pour \(x\)
Pour le terme en \(x\), nous avons \(x^2 - x\). Complétons le carré :

Le terme manquant est \(\left(\frac{1}{2}\right)^2 = \frac{1}{4}\). Nous ajoutons et soustrayons \(\frac{1}{4}\) :

\[
x^2 - x + \frac{1}{4} - \frac{1}{4} = \left(x - \frac{1}{2}\right)^2 - \frac{1}{4}
\]

L'équation devient donc :

\[
\left(x - \frac{1}{2}\right)^2 - \frac{1}{4} + (y + 1)^2 - 1 = 0
\]

### Étape 4 : Simplifier l'équation
Regroupons les constantes :

\[
\left(x - \frac{1}{2}\right)^2 + (y + 1)^2 = \frac{5}{4}
\]

### Conclusion
L'équation est maintenant sous la forme classique d'un cercle \((x - h)^2 + (y - k)^2 = r^2\), où :


- Le centre est \(\left(\frac{1}{2}, -1\right)\)
- Le rayon est \(\frac{\sqrt{5}}{2}\)

Le centre du cercle est donc \(\left(\frac{1}{2}, -1\right)\).
