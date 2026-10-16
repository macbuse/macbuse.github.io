Voici les solutions détaillées pour mettre chaque nombre complexe sous forme exponentielle $r e^{i\theta}$ (avec $r > 0$).

---

## Première ligne

### 1. $(e^{i\frac{3\pi}{4}})^3$

* **Règle :** $(e^{i\theta})^n = e^{in\theta}$

* **Calcul :**

$$(e^{i\frac{3\pi}{4}})^3 = e^{i \cdot 3 \cdot \frac{3\pi}{4}} = e^{i\frac{9\pi}{4}}$$


* **Forme canonique (modulo $2\pi$) :** $\frac{9\pi}{4} = 2\pi + \frac{\pi}{4}$

$$e^{i\frac{9\pi}{4}} = e^{i\frac{\pi}{4}}$$



---

### 2. $(2e^{-i\frac{\pi}{6}})^{-3}$

* **Règle :** $(a \cdot b)^n = a^n \cdot b^n$

* **Calcul :**

$$(2e^{-i\frac{\pi}{6}})^{-3} = 2^{-3} \cdot e^{-i\frac{\pi}{6} \cdot (-3)} = \frac{1}{8} e^{i\frac{3\pi}{6}} = \frac{1}{8} e^{i\frac{\pi}{2}}$$



---

### 3. $\frac{e^{i\frac{\pi}{3}}}{(e^{i\frac{\pi}{8}})^2}$

* **Calcul du dénominateur :** $(e^{i\frac{\pi}{8}})^2 = e^{i\frac{2\pi}{8}} = e^{i\frac{\pi}{4}}$

* **Règle de division :** $\frac{e^{ia}}{e^{ib}} = e^{i(a-b)}$
* **Calcul :**

$$\frac{e^{i\frac{\pi}{3}}}{e^{i\frac{\pi}{4}}} = e^{i(\frac{\pi}{3} - \frac{\pi}{4})} = e^{i\frac{4\pi - 3\pi}{12}} = e^{i\frac{\pi}{12}}$$



---

### 4. $(e^{i\frac{\pi}{3}})^3 (e^{i\frac{\pi}{2}})^3$

* **Calcul des puissances :**
* $(e^{i\frac{\pi}{3}})^3 = e^{i\pi}$

* $(e^{i\frac{\pi}{2}})^3 = e^{i\frac{3\pi}{2}}$



* **Produit :**

$$e^{i\pi} \cdot e^{i\frac{3\pi}{2}} = e^{i(\pi + \frac{3\pi}{2})} = e^{i\frac{5\pi}{2}} = e^{i\frac{\pi}{2}}$$



---

### 5. $(e^{-i\frac{\pi}{4}})^6 (e^{i\frac{\pi}{2}})^6$

* **Méthode directe (regroupement des termes) :**

$$\left( e^{-i\frac{\pi}{4}} \cdot e^{i\frac{\pi}{2}} \right)^6 = \left( e^{i(-\frac{\pi}{4} + \frac{\pi}{2})} \right)^6 = \left( e^{i\frac{\pi}{4}} \right)^6 = e^{i\frac{6\pi}{4}} = e^{i\frac{3\pi}{2}}$$



---

### 6. $(\overline{3e^{i\frac{\pi}{3}}})^2$

* **Règle du conjugué :** $\overline{r e^{i\theta}} = r e^{-i\theta}$
* **Calcul :**
* Conjugué : $\overline{3e^{i\frac{\pi}{3}}} = 3e^{-i\frac{\pi}{3}}$
* Élévation au carré : $(3e^{-i\frac{\pi}{3}})^2 = 3^2 e^{-i\frac{2\pi}{3}} = 9 e^{-i\frac{2\pi}{3}}$ (ou $9 e^{i\frac{4\pi}{3}}$)



---

## Seconde ligne

### 7. $\overline{(2e^{i\frac{3\pi}{4}})^{-2}}$

* **Calcul de l'intérieur :**

$$(2e^{i\frac{3\pi}{4}})^{-2} = 2^{-2} e^{-i\frac{6\pi}{4}} = \frac{1}{4} e^{-i\frac{3\pi}{2}} = \frac{1}{4} e^{i\frac{\pi}{2}}$$


* **Conjugué :**

$$\overline{\frac{1}{4} e^{i\frac{\pi}{2}}} = \frac{1}{4} e^{-i\frac{\pi}{2}}$$



---

### 8. $\left(\frac{e^{i\frac{\pi}{3}}}{2e^{i\frac{\pi}{6}}}\right)^{-2}$

* **Simplification du quotient intérieur :**

$$\frac{e^{i\frac{\pi}{3}}}{2e^{i\frac{\pi}{6}}} = \frac{1}{2} e^{i(\frac{\pi}{3} - \frac{\pi}{6})} = \frac{1}{2} e^{i\frac{\pi}{6}}$$


* **Puissance $-2$ :**

$$\left(\frac{1}{2} e^{i\frac{\pi}{6}}\right)^{-2} = (1/2)^{-2} \cdot e^{-i\frac{2\pi}{6}} = 2^2 e^{-i\frac{\pi}{3}} = 4 e^{-i\frac{\pi}{3}}$$



---

### 9. $\frac{(e^{i\frac{\pi}{3}})^5}{(e^{i\frac{2\pi}{3}})^7 (e^{-i\frac{\pi}{3}})^4}$

* **Numerateur :** $e^{i\frac{5\pi}{3}}$

* **Dénominateur :** $e^{i\frac{14\pi}{3}} \cdot e^{-i\frac{4\pi}{3}} = e^{i\frac{10\pi}{3}}$

* **Quotient :**

$$\frac{e^{i\frac{5\pi}{3}}}{e^{i\frac{10\pi}{3}}} = e^{i(\frac{5\pi}{3} - \frac{10\pi}{3})} = e^{-i\frac{5\pi}{3}} = e^{i\frac{\pi}{3}}$$



---

### 10. $(2e^{i\frac{\pi}{3}})^{-3} (\sqrt{2}e^{i\frac{\pi}{6}})^4$

* **Premier terme :** $(2e^{i\frac{\pi}{3}})^{-3} = 2^{-3} e^{-i\pi} = \frac{1}{8} e^{-i\pi}$

* **Second terme :** $(\sqrt{2}e^{i\frac{\pi}{6}})^4 = (\sqrt{2})^4 e^{i\frac{4\pi}{6}} = 4 e^{i\frac{2\pi}{3}}$

* **Produit :**

$$\frac{1}{8} \cdot 4 \cdot e^{i(-\pi + \frac{2\pi}{3})} = \frac{1}{2} e^{-i\frac{\pi}{3}}$$



---

### 11. $\frac{(i e^{i\frac{\pi}{3}})^6}{(-e^{i\frac{2\pi}{3}})^{-2}}$

* **Numerateur :**
* Comme $i = e^{i\frac{\pi}{2}}$, on a $i e^{i\frac{\pi}{3}} = e^{i(\frac{\pi}{2} + \frac{\pi}{3})} = e^{i\frac{5\pi}{6}}$

* $(e^{i\frac{5\pi}{6}})^6 = e^{i5\pi} = e^{i\pi} = -1$



* **Dénominateur :**
* $(-e^{i\frac{2\pi}{3}})^{-2} = (-1)^{-2} \cdot (e^{i\frac{2\pi}{3}})^{-2} = 1 \cdot e^{-i\frac{4\pi}{3}}$



* **Quotient :**

$$\frac{e^{i5\pi}}{e^{-i\frac{4\pi}{3}}} = e^{i(5\pi + \frac{4\pi}{3})} = e^{i\frac{19\pi}{3}} = e^{i(6\pi + \frac{\pi}{3})} = e^{i\frac{\pi}{3}}$$
