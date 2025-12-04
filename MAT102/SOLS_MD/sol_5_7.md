
---

## Solutions des Intégrales par Changement de Variable

### Intégrale $I_1$

$$I_1 = \int_{0}^{\pi/2} \sin^3 x \cos x \, dx$$

1.  **Changement de variable :**
    * Posons $u = \sin x$.
    * Alors la différentielle est $du = \cos x \, dx$.
2.  **Changement des bornes :**
    * Si $x = 0$, $u = \sin(0) = 0$.
    * Si $x = \pi/2$, $u = \sin(\pi/2) = 1$.
3.  **Calcul :**
    $$I_1 = \int_{0}^{1} u^3 \, du = \left[ \frac{u^4}{4} \right]_{0}^{1} = \frac{1^4}{4} - \frac{0^4}{4} = \frac{1}{4}$$

$$\mathbf{I_1 = \frac{1}{4}}$$

---

### Intégrale $I_2$

$$I_2 = \int_{0}^{1} e^u \cos(e^u) \, du$$

1.  **Changement de variable :**
    * Posons $v = e^u$.
    * Alors la différentielle est $dv = e^u \, du$.
2.  **Changement des bornes :**
    * Si $u = 0$, $v = e^0 = 1$.
    * Si $u = 1$, $v = e^1 = e$.
3.  **Calcul :**
    $$I_2 = \int_{1}^{e} \cos(v) \, dv = \left[ \sin(v) \right]_{1}^{e} = \sin(e) - \sin(1)$$

$$\mathbf{I_2 = \sin(e) - \sin(1)}$$

---

### Intégrale $I_3$

$$I_3 = \int_{0}^{\pi/4} \tan^3 x \, dx$$

On décompose $\tan^3 x = \tan x \cdot \tan^2 x = \tan x (\sec^2 x - 1) = \tan x \sec^2 x - \tan x$.

$$I_3 = \int_{0}^{\pi/4} \tan x \sec^2 x \, dx - \int_{0}^{\pi/4} \tan x \, dx$$

#### Partie 1: $\int_{0}^{\pi/4} \tan x \sec^2 x \, dx$
1.  **Changement de variable :** $u = \tan x$, donc $du = \sec^2 x \, dx$.
2.  **Bornes :** $x=0 \to u=0$; $x=\pi/4 \to u=1$.
3.  **Calcul :** $\int_{0}^{1} u \, du = \left[ \frac{u^2}{2} \right]_{0}^{1} = \frac{1}{2}$.

#### Partie 2: $\int_{0}^{\pi/4} \tan x \, dx = \int_{0}^{\pi/4} \frac{\sin x}{\cos x} \, dx$
1.  **Changement de variable :** $v = \cos x$, donc $dv = -\sin x \, dx$, soit $\sin x \, dx = -dv$.
2.  **Bornes :** $x=0 \to v=\cos(0)=1$; $x=\pi/4 \to v=\cos(\pi/4)=\frac{\sqrt{2}}{2}$.
3.  **Calcul :** $\int_{1}^{\sqrt{2}/2} \frac{-dv}{v} = - \left[ \ln|v| \right]_{1}^{\sqrt{2}/2} = \ln(1) - \ln\left(\frac{\sqrt{2}}{2}\right) = 0 - \ln\left(\frac{1}{\sqrt{2}}\right) = \ln(\sqrt{2}) = \frac{1}{2} \ln(2)$.

#### Résultat final :
$$I_3 = \frac{1}{2} - \frac{1}{2} \ln(2) = \frac{1}{2} \left( 1 - \ln(2) \right)$$

$$\mathbf{I_3 = \frac{1}{2} \left( 1 - \ln(2) \right)}$$

---

### Intégrale $I_4$

$$I_4 = \int_{1}^{2} (3t - 1)^{-2/3} \, dt$$

1.  **Changement de variable :**
    * Posons $u = 3t - 1$.
    * Alors $du = 3 \, dt$, soit $dt = \frac{1}{3} du$.
2.  **Changement des bornes :**
    * Si $t = 1$, $u = 3(1) - 1 = 2$.
    * Si $t = 2$, $u = 3(2) - 1 = 5$.
3.  **Calcul :**
    $$I_4 = \int_{2}^{5} u^{-2/3} \cdot \frac{1}{3} \, du = \frac{1}{3} \int_{2}^{5} u^{-2/3} \, du$$
    $$\frac{1}{3} \left[ \frac{u^{-2/3 + 1}}{1/3} \right]_{2}^{5} = \left[ u^{1/3} \right]_{2}^{5} = \sqrt[3]{5} - \sqrt[3]{2}$$

$$\mathbf{I_4 = \sqrt[3]{5} - \sqrt[3]{2}}$$

---

### Intégrale $I_5$

$$I_5 = \int_{1}^{2} \frac{u + 1}{\sqrt{u^2 + 2u}} \, du$$

On remarque que la dérivée du terme sous la racine est $(u^2 + 2u)' = 2u + 2 = 2(u + 1)$.

1.  **Changement de variable :**
    * Posons $v = u^2 + 2u$.
    * Alors $dv = (2u + 2) \, du = 2(u + 1) \, du$, soit $(u + 1) \, du = \frac{1}{2} dv$.
2.  **Changement des bornes :**
    * Si $u = 1$, $v = 1^2 + 2(1) = 3$.
    * Si $u = 2$, $v = 2^2 + 2(2) = 8$.
3.  **Calcul :**
    $$I_5 = \int_{3}^{8} \frac{1}{\sqrt{v}} \cdot \frac{1}{2} \, dv = \frac{1}{2} \int_{3}^{8} v^{-1/2} \, dv$$
    $$\frac{1}{2} \left[ \frac{v^{-1/2 + 1}}{1/2} \right]_{3}^{8} = \left[ v^{1/2} \right]_{3}^{8} = \left[ \sqrt{v} \right]_{3}^{8} = \sqrt{8} - \sqrt{3} = 2\sqrt{2} - \sqrt{3}$$

$$\mathbf{I_5 = 2\sqrt{2} - \sqrt{3}}$$

---

### Intégrale $I_6$

$$I_6 = \int_{0}^{\sqrt{3}/2} \sqrt{\frac{1 + x}{1 - x}} \, dx$$

1.  **Changement de variable :**
    * Posons la substitution trigonométrique $x = \sin \theta$.
    * Alors $dx = \cos \theta \, d\theta$.
    * L'intégrande devient :
        $$\sqrt{\frac{1 + \sin \theta}{1 - \sin \theta}} = \sqrt{\frac{(1 + \sin \theta)^2}{1 - \sin^2 \theta}} = \sqrt{\frac{(1 + \sin \theta)^2}{\cos^2 \theta}} = \frac{1 + \sin \theta}{\cos \theta} = \sec \theta + \tan \theta$$
        *(Puisque $x \in [0, \sqrt{3}/2]$, $\theta \in [0, \pi/3]$, donc $\cos \theta > 0$)*.
    * Le nouvel intégrant est : $(\sec \theta + \tan \theta) \cos \theta \, d\theta = (1 + \sin \theta) \, d\theta$.
2.  **Changement des bornes :**
    * Si $x = 0$, $0 = \sin \theta$, donc $\theta = 0$.
    * Si $x = \sqrt{3}/2$, $\sqrt{3}/2 = \sin \theta$, donc $\theta = \pi/3$.
3.  **Calcul :**
    $$I_6 = \int_{0}^{\pi/3} (1 + \sin \theta) \, d\theta = \left[ \theta - \cos \theta \right]_{0}^{\pi/3}$$
    $$I_6 = \left( \frac{\pi}{3} - \cos\left(\frac{\pi}{3}\right) \right) - (0 - \cos(0))$$
    $$I_6 = \left( \frac{\pi}{3} - \frac{1}{2} \right) - (0 - 1) = \frac{\pi}{3} - \frac{1}{2} + 1 = \frac{\pi}{3} + \frac{1}{2}$$

$$\mathbf{I_6 = \frac{\pi}{3} + \frac{1}{2}}$$

---

### Intégrale $I_7$

$$I_7 = \int_{0}^{1} \frac{e^x}{e^x + 1} \, dx$$

On remarque que le numérateur est la dérivée du dénominateur $(e^x + 1)' = e^x$.

1.  **Changement de variable :**
    * Posons $u = e^x + 1$.
    * Alors la différentielle est $du = e^x \, dx$.
2.  **Changement des bornes :**
    * Si $x = 0$, $u = e^0 + 1 = 2$.
    * Si $x = 1$, $u = e^1 + 1 = e + 1$.
3.  **Calcul :**
    $$I_7 = \int_{2}^{e + 1} \frac{1}{u} \, du = \left[ \ln|u| \right]_{2}^{e + 1}$$
    $$I_7 = \ln(e + 1) - \ln(2) = \ln\left(\frac{e + 1}{2}\right)$$

$$\mathbf{I_7 = \ln\left(\frac{e + 1}{2}\right)}$$
