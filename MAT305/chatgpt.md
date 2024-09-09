### Résolution de l'équation $Z^2 = 1 + i$ via deux méthodes : forme algébrique et forme exponentielle.

#### 1. **Forme exponentielle** :

L'équation donnée est $Z^2 = 1 + i$.

- **Étape 1 : Conversion de $1 + i$ en forme exponentielle**.

La forme exponentielle d'un nombre complexe est donnée par :
$$z = r \cdot e^{i \theta} $$
où $r$ est le module et $\theta$ est l'argument.

Pour $1 + i$, on calcule le module :
$$r = |1 + i| = \sqrt{1^2 + 1^2} = \sqrt{2}$$
L'argument $\theta$ est l'angle que fait le nombre complexe avec l'axe réel. Pour $1 + i$, il est dans le premier quadrant et on a :
$$\theta = \arg(1 + i) = \frac{\pi}{4}
$$
Ainsi, $1 + i$ en forme exponentielle est :
$$1 + i = \sqrt{2} \cdot e^{i \frac{\pi}{4}}
$$
- **Étape 2 : Résolution de $Z^2 = \sqrt{2} \cdot e^{i \frac{\pi}{4}}$**

Nous cherchons $Z$ tel que $Z^2 = r \cdot e^{i \theta}$. En prenant la racine carrée des deux côtés, on obtient :

$$Z = \sqrt{\sqrt{2}} \cdot e^{i \frac{\frac{\pi}{4} + 2k\pi}{2}}$$

Cela donne :
$$Z = 2^{1/4} \cdot e^{i \frac{\pi}{8} + k\pi} $$
où $k = 0, 1$ pour les deux solutions principales.

- Pour $k = 0$ :
$$Z_1 = 2^{1/4} \cdot e^{i \frac{\pi}{8}}$$
- Pour $k = 1$ :
$$Z_2 = 2^{1/4} \cdot e^{i \frac{9\pi}{8}}$$

#### 2. **Forme algébrique** :

L'équation est toujours $Z^2 = 1 + i$. Supposons que $Z = x + iy$ (forme algébrique), où $x$ et $y$ sont réels.

- **Étape 1 : Développement de $Z^2$**.

Nous avons :
$$Z^2 = (x + iy)^2 = x^2 - y^2 + 2ixy$$
Cela doit être égal à $1 + i$. En identifiant la partie réelle et la partie imaginaire, on obtient deux équations :

- Partie réelle :
$$x^2 - y^2 = 1
$$
- Partie imaginaire :
$$2xy = 1
$$
- **Étape 2 : Résolution du système**.

De $2xy = 1$, on trouve :
$$xy = \frac{1}{2}$$
Remplaçons $y$ par $\frac{1}{2x}$ dans la première équation :
$$x^2 - \left(\frac{1}{2x}\right)^2 = 1$$
Cela donne :
$$x^4 - 1 = \frac{1}{4x^2}$$
En multipliant par $4x^2$ de chaque côté :
$$4x^6 - 4x^2 = 1$$
qui est une équation en $x^2$. Posons $u = x^2$, on obtient :
$$4u^3 - 4u - 1 = 0
$$
Cette équation doit être résolue numériquement ou à l'aide de méthodes algébriques spécifiques. Les solutions de ce système donneraient les valeurs de $x$ et $y$, puis les deux solutions pour $Z$.

### Conclusion :
- La forme exponentielle permet d'obtenir les solutions $Z_1 = 2^{1/4} \cdot e^{i \frac{\pi}{8}}$ et $Z_2 = 2^{1/4} \cdot e^{i \frac{9\pi}{8}}$.
- En forme algébrique, la résolution d'un système d'équations différentielles donne les solutions pour $x$ et $y$.
