
---

## **Exercice 7. Orthogonalité des vecteurs**



Deux vecteurs $\vec{u}$ et $\vec{v}$ sont orthogonaux si et seulement si leur produit scalaire est nul : $\vec{u} \cdot \vec{v} = 0$.

### **a)** $\vec{u} = (t - 1, 2t - 3)$, $\vec{v} = (3, -1)$



$$\vec{u} \cdot \vec{v} = 3(t - 1) - 1(2t - 3) = 3t - 3 - 2t + 3 = t$$

$$\vec{u} \cdot \vec{v} = 0 \iff t = 0$$

---

### **b)** $\vec{u} = (3t, 2 + t, -t)$, $\vec{v} = (1, 1, 2)$



$$\vec{u} \cdot \vec{v} = 1(3t) + 1(2 + t) + 2(-t) = 3t + 2 + t - 2t = 2t + 2$$

$$\vec{u} \cdot \vec{v} = 0 \iff 2t + 2 = 0 \iff t = -1$$

---

### **c)** $\vec{u} = (t - 1, 2t, 2)$, $\vec{v} = (1, 2, -1)$



$$\vec{u} \cdot \vec{v} = 1(t - 1) + 2(2t) - 1(2) = t - 1 + 4t - 2 = 5t - 3$$

$$\vec{u} \cdot \vec{v} = 0 \iff 5t - 3 = 0 \iff t = \frac{3}{5}$$

---

### **d)** $\vec{u} = (t^2 + 1, 2t, t^2 - 1)$, $\vec{v} = (t^2, -t, 1)$



$$\vec{u} \cdot \vec{v} = t^2(t^2 + 1) - t(2t) + 1(t^2 - 1) = t^4 + t^2 - 2t^2 + t^2 - 1 = t^4 - 1$$

$$\vec{u} \cdot \vec{v} = 0 \iff t^4 - 1 = 0 \iff (t^2 - 1)(t^2 + 1) = 0$$

Comme $t^2 + 1 > 0$ pour tout $t \in \mathbb{R}$, l'équation équivaut à $t^2 - 1 = 0$, soit :

$$t = 1 \quad \text{ou} \quad t = -1$$

---

## **Exercice 9. Colinéarité des vecteurs**



Deux vecteurs $(x, y)$ et $(x', y')$ dans $\mathbb{R}^2$ sont colinéaires si et seulement si leur déterminant est nul : $xy' - x'y = 0$.

### **a)** $\vec{u} = (1 - t, 2 + t)$, $\vec{v} = (3, 4)$



$$\det(\vec{u}, \vec{v}) = 4(1 - t) - 3(2 + t) = 4 - 4t - 6 - 3t = -7t - 2$$

$$\det(\vec{u}, \vec{v}) = 0 \iff -7t - 2 = 0 \iff t = -\frac{2}{7}$$

---

### **b)** $\vec{u} = (5t, 6)$, $\vec{v} = (6t, 7)$



$$\det(\vec{u}, \vec{v}) = 7(5t) - 6(6t) = 35t - 36t = -t$$

$$\det(\vec{u}, \vec{v}) = 0 \iff t = 0$$

---

### **c)** $\vec{u} = (2, 1)$, $\vec{v} = (3 - t, 2 - t)$



$$\det(\vec{u}, \vec{v}) = 2(2 - t) - 1(3 - t) = 4 - 2t - 3 + t = 1 - t$$

$$\det(\vec{u}, \vec{v}) = 0 \iff 1 - t = 0 \iff t = 1$$
