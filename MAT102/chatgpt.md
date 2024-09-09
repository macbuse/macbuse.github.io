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

1. Partie réelle :
$$x^2 - y^2 = 1$$
2. Partie imaginaire :
$$2xy = 1
$$
3. Module
$$x^2 + y^2 = \sqrt{2}$$

- **Étape 2 : Résolution du système**.

De (1),(3), on trouve :
$$2x^2 = \sqrt{2} + 1 \Rightarrow x^2 = \frac{\sqrt{2} + 1}{2} = \frac{1}{2} + \frac{\sqrt{2}}{2}$$
$$2y^2 = \sqrt{2} - 1 \Rightarrow y^2 = \frac{\sqrt{2} - 1}{2}
$$
On a que $xy>0$ donc $x$ et $y$ ont le même signe. Les solutions
sont donc :
$$Z_1 = x + iy = \sqrt{\frac{1}{2} + \frac{\sqrt{2}}{2}} +
\sqrt{\frac{\sqrt{2} - 1}{2}}i$$


### Conclusion :

ChatGPT  ne sait pas tout.
