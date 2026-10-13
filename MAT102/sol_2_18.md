## Exo 18

---

### a) $\displaystyle\prod_{k=1}^{20} e^{ik\pi/3}$

* **Somme des exposants :**

$$\prod_{k=1}^{20} e^{ik\pi/3} = \exp\left( \frac{i\pi}{3} \sum_{k=1}^{20} k \right)$$


* **Calcul de la somme :**

$$\sum_{k=1}^{20} k = \frac{20 \times 21}{2} = 210$$


* **Évaluation :**

$$\exp\left( \frac{i\pi}{3} \times 210 \right) = \exp(i \times 70\pi) = e^{i(35 \times 2\pi)} = 1$$



---

### b) $\displaystyle\prod_{p=1}^{7} 2e^{ip\pi/8}$

* **Séparation du produit :**

$$\prod_{p=1}^{7} 2e^{ip\pi/8} = \left(\prod_{p=1}^{7} 2\right) \times \exp\left( \frac{i\pi}{8} \sum_{p=1}^{7} p \right)$$


* **Calcul des parties :**
* Produit de la constante : $2^7 = 128$
* Somme des exposants : $\sum_{p=1}^{7} p = \frac{7 \times 8}{2} = 28$


* **Évaluation :**

$$128 \times \exp\left( \frac{i\pi}{8} \times 28 \right) = 128 \times \exp\left( \frac{7i\pi}{2} \right) = 128 \times e^{i(3\pi + \pi/2)} = 128 \times (-i) = -128i$$



---

### c) $\displaystyle\prod_{k=1}^{6} (1+i)^k$

* **Somme des exposants :**

$$\prod_{k=1}^{6} (1+i)^k = (1+i)^{\sum_{k=1}^{6} k} = (1+i)^{21}$$


* **Forme polaire de $(1+i)$ :**

$$1+i = \sqrt{2} e^{i\pi/4}$$


* **Évaluation :**

$$(1+i)^{21} = \left(\sqrt{2} e^{i\pi/4}\right)^{21} = 2^{21/2} \exp\left( \frac{21i\pi}{4} \right)$$


$$\frac{21\pi}{4} = 5\pi + \frac{\pi}{4} \implies \exp\left( \frac{21i\pi}{4} \right) = e^{i\pi} e^{i\pi/4} = -1 \times \frac{\sqrt{2}+i\sqrt{2}}{2}$$



Résultat : $-1024\sqrt{2} \, e^{i\pi/4} = -1024(1+i) = -1024 - 1024i$

---

### d) $\displaystyle\sum_{l=0}^{7} \left(-2 + \sqrt{2}e^{i\pi/4}\right)^l$

* **Simplification de la base ($q$) :**

$$\sqrt{2}e^{i\pi/4} = \sqrt{2}\left(\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}\right) = 1 + i$$


$$q = -2 + (1+i) = -1 + i$$


* **Somme d'une suite géométrique :**

$$\sum_{l=0}^{7} q^l = \frac{1 - q^8}{1 - q}$$


* **Calcul de $q^8$ :**
On écrit $q = -1 + i = \sqrt{2}e^{i3\pi/4}$.

$$q^8 = \left(\sqrt{2}e^{i3\pi/4}\right)^8 = 2^4 e^{i6\pi} = 16 \times 1 = 16$$


* **Évaluation :**

$$\frac{1 - 16}{1 - (-1 + i)} = \frac{-15}{2 - i} = \frac{-15(2 + i)}{2^2 + (-1)^2} = \frac{-30 - 15i}{5} = -6 - 3i$$



---

### e) $\displaystyle\sum_{k=0}^{7} \left(\sqrt{2}e^{i\pi/4}\right)^k$

* **Identification de la base ($q$) :**

$$q = \sqrt{2}e^{i\pi/4} = 1 + i$$


* **Somme d'une suite géométrique :**

$$\sum_{k=0}^{7} q^k = \frac{1 - q^8}{1 - q}$$


* **Calcul de $q^8$ :**

$$q = \sqrt{2}e^{i\pi/4} \implies q^8 = \left(\sqrt{2}\right)^8 e^{i2\pi} = 16 \times 1 = 16$$


* **Évaluation :**

$$\frac{1 - 16}{1 - (1 + i)} = \frac{-15}{-i} = \frac{15}{i} = -15i$$



---

### f) $\displaystyle\sum_{m=0}^{12} \left(-1 + e^{i\pi/3}\right)^m$

* **Simplification de la base ($q$) :**

$$e^{i\pi/3} = \frac{1}{2} + i\frac{\sqrt{3}}{2}$$


$$q = -1 + \left(\frac{1}{2} + i\frac{\sqrt{3}}{2}\right) = -\frac{1}{2} + i\frac{\sqrt{3}}{2} = e^{i2\pi/3}$$


* **Somme d'une suite géométrique :**

$$\sum_{m=0}^{12} q^m = \frac{1 - q^{13}}{1 - q}$$


* **Calcul de $q^{13}$ :**

$$q^{13} = \left(e^{i2\pi/3}\right)^{13} = \exp\left( \frac{26i\pi}{3} \right) = \exp\left( 8i\pi + \frac{2i\pi}{3} \right) = e^{i2\pi/3} = q$$


* **Évaluation :**
Puisque $q^{13} = q$, le numérateur est $1 - q$, ce qui se simplifie avec le dénominateur (en supposant $q \neq 1$) :

$$\frac{1 - q}{1 - q} = 1$$
