
---

### **Décomposition en éléments simples**

On cherche $\alpha$ et $\beta$ tels que pour tout $a \in \mathbb{R}^*$ et $k \notin \{0, -a\}$ :

$$\frac{1}{k(k+a)} = \frac{\alpha}{k} + \frac{\beta}{k+a}$$

Voici la résolution rédigée selon votre méthode (en multipliant par le dénominateur puis en utilisant les valeurs particulières $k = 0$ et $k = -a$) :

---

### **Calcul de $\alpha$ et $\beta$**

On cherche $\alpha$ et $\beta$ tels que pour tout $a \in \mathbb{R}^*$ et $k \notin \{0, -a\}$ :

$$\frac{1}{k(k+a)} = \frac{\alpha}{k} + \frac{\beta}{k+a}$$



En multipliant l'égalité par le dénominateur commun $k(k+a)$, on obtient une égalité polynomiale vraie pour tout $k \in \mathbb{R}$ :

$$1 = \alpha(k+a) + \beta k$$

Pour déterminer $\alpha$ et $\beta$, on évalue cette égalité pour des valeurs particulières de $k$ :

* **Pour $k = 0$ :**

$$1 = \alpha(0 + a) + \beta(0) \implies 1 = \alpha a \implies \alpha = \frac{1}{a}$$


* **Pour $k = -a$ :**

$$1 = \alpha(-a + a) + \beta(-a) \implies 1 = -\beta a \implies \beta = -\frac{1}{a}$$



On retrouve bien la décomposition générale pour tout $a \neq 0$ :

$$\frac{1}{k(k+a)} = \frac{1}{a} \left( \frac{1}{k} - \frac{1}{k+a} \right)$$

---

### **a)** $\sum_{k=1}^{n} \frac{1}{k(k+1)}$



Ici $a = 1$. La décomposition s'écrit :

$$\frac{1}{k(k+1)} = \frac{1}{k} - \frac{1}{k+1}$$

La somme est télescopique :

$$\sum_{k=1}^{n} \frac{1}{k(k+1)} = \sum_{k=1}^{n} \left( \frac{1}{k} - \frac{1}{k+1} \right) = \left(1 - \frac{1}{2}\right) + \left(\frac{1}{2} - \frac{1}{3}\right) + \dots + \left(\frac{1}{n} - \frac{1}{n+1}\right)$$

Tous les termes s'annulent deux à deux sauf le premier et le dernier :

$$\sum_{k=1}^{n} \frac{1}{k(k+1)} = 1 - \frac{1}{n+1} = \frac{n}{n+1}$$

---

### **b)** $\sum_{k=1}^{n} \frac{1}{k(k+2)}$



Ici $a = 2$. La décomposition s'écrit :

$$\frac{1}{k(k+2)} = \frac{1}{2} \left( \frac{1}{k} - \frac{1}{k+2} \right)$$

En développant la somme télescopique :

$$\sum_{k=1}^{n} \frac{1}{k(k+2)} = \frac{1}{2} \left[ \sum_{k=1}^{n} \frac{1}{k} - \sum_{k=1}^{n} \frac{1}{k+2} \right]$$

Par décalage d'indice dans la seconde somme ($j = k+2$) :

$$\sum_{k=1}^{n} \frac{1}{k+2} = \sum_{j=3}^{n+2} \frac{1}{j}$$

Il reste les deux premiers termes de la première somme et les deux derniers de la seconde :

$$\sum_{k=1}^{n} \frac{1}{k(k+2)} = \frac{1}{2} \left( 1 + \frac{1}{2} - \frac{1}{n+1} - \frac{1}{n+2} \right) = \frac{1}{2} \left( \frac{3}{2} - \frac{2n+3}{(n+1)(n+2)} \right) = \frac{3}{4} - \frac{2n+3}{2(n+1)(n+2)}$$

Forme factorisée unique :

$$\sum_{k=1}^{n} \frac{1}{k(k+2)} = \frac{n(3n+5)}{4(n+1)(n+2)}$$

---

### **c)** $\sum_{k=2}^{n} \frac{1}{k^2 - 1}$



En factorisant le dénominateur : $k^2 - 1 = (k-1)(k+1)$.

Effectuons le changement d'indice $j = k-1$ (donc $k = j+1$) :

$$\sum_{k=2}^{n} \frac{1}{(k-1)(k+1)} = \sum_{j=1}^{n-1} \frac{1}{j(j+2)}$$

C'est exactement la somme du **b)** calculée au rang $n-1$ :

$$\sum_{k=2}^{n} \frac{1}{k^2 - 1} = \frac{1}{2} \left( \frac{3}{2} - \frac{1}{n} - \frac{1}{n+1} \right)$$

Sous forme réduite :

$$\sum_{k=2}^{n} \frac{1}{k^2 - 1} = \frac{3}{4} - \frac{2n+1}{2n(n+1)} = \frac{(n-1)(3n+2)}{4n(n+1)}$$
