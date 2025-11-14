## Exercice 26 : Équation Paramétrique de la Droite d'Intersection
de Deux Plans

Pour résoudre l'**Exercice 26**, nous devons trouver l'équation paramétrique de la droite $\mathcal{D}$, qui est l'intersection des deux plans $\mathcal{P}_1$ et $\mathcal{P}_2$.

L'intersection est définie par le système d'équations cartésiennes des deux plans :
$$
\mathcal{D}: \begin{cases} \text{Équation de } \mathcal{P}_1 \\ \text{Équation de } \mathcal{P}_2 \end{cases}
$$
Pour trouver la forme paramétrique, nous résolvons ce système en exprimant deux variables en fonction de la troisième (le paramètre $t$).

***

## **Exercice 26 a)** 📐
Plans :
* $\mathcal{P}_1: x + y + z = 3$
* $\mathcal{P}_2: x - 2y + z = 0$

Système :
$$
(S) \begin{cases} x + y + z = 3 \quad (1) \\ x - 2y + z = 0 \quad (2) \end{cases}
$$

**1. Trouver le vecteur directeur** $\vec{v}$ :
Le vecteur directeur $\vec{v}$ de la droite $\mathcal{D}$ est orthogonal aux deux vecteurs normaux $\vec{n}_1$ et $\vec{n}_2$ des plans. On le trouve par le produit vectoriel $\vec{n}_1 \times \vec{n}_2$.
* $\vec{n}_1 = (1, 1, 1)$
* $\vec{n}_2 = (1, -2, 1)$

$$\vec{v} = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \times \begin{pmatrix} 1 \\ -2 \\ 1 \end{pmatrix} = \begin{pmatrix} (1)(1) - (1)(-2) \\ (1)(1) - (1)(1) \\ (1)(-2) - (1)(1) \end{pmatrix} = \begin{pmatrix} 1 - (-2) \\ 1 - 1 \\ -2 - 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 0 \\ -3 \end{pmatrix}$$
On peut simplifier le vecteur directeur à $\vec{v}' = (1, 0, -1)$.

**2. Trouver un point** $A$ **de la droite** $\mathcal{D}$ :
Cherchons un point où, par exemple, $y=0$. Substituons $y=0$ dans $(S)$ :
$$
\begin{cases} x + 0 + z = 3 \implies x + z = 3 \\ x - 2(0) + z = 0 \implies x + z = 0 \end{cases}
$$
Ce système n'a **pas de solution** (car $3 \neq 0$). Cela signifie que la droite d'intersection ne coupe pas le plan $y=0$.

Cherchons un point où $x=0$ :
$$
\begin{cases} 0 + y + z = 3 \implies y + z = 3 \quad (3) \\ 0 - 2y + z = 0 \implies z = 2y \quad (4) \end{cases}
$$
Substituons $(4)$ dans $(3)$ :
$$y + (2y) = 3 \implies 3y = 3 \implies y = 1$$
Ensuite, $z = 2(1) = 2$.
Le point d'intersection est $A = (0, 1, 2)$.

**3. Équation Paramétrique de** $\mathcal{D}$ :
En utilisant le point $A(0, 1, 2)$ et le vecteur directeur $\vec{v}'(1, 0, -1)$, l'équation paramétrique est :
$$\mathcal{D}: \begin{cases} x = 0 + 1t \\ y = 1 + 0t \\ z = 2 - 1t \end{cases}, \quad t \in \mathbb{R}$$
$$\mathcal{D}: \begin{cases} \mathbf{x = t} \\ \mathbf{y = 1} \\ \mathbf{z = 2 - t} \end{cases}, \quad t \in \mathbb{R}$$

---

## **Exercice 26 b)** 📐
Plans :
* $\mathcal{P}_1: x + y - z = -1$
* $\mathcal{P}_2: x + 2y + 3z = 0$

Système :
$$
(S) \begin{cases} x + y - z = -1 \quad (1) \\ x + 2y + 3z = 0 \quad (2) \end{cases}
$$

**1. Trouver le vecteur directeur** $\vec{v}$ :
* $\vec{n}_1 = (1, 1, -1)$
* $\vec{n}_2 = (1, 2, 3)$

$$\vec{v} = \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} \times \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = \begin{pmatrix} (1)(3) - (-1)(2) \\ (-1)(1) - (1)(3) \\ (1)(2) - (1)(1) \end{pmatrix} = \begin{pmatrix} 3 + 2 \\ -1 - 3 \\ 2 - 1 \end{pmatrix} = \begin{pmatrix} 5 \\ -4 \\ 1 \end{pmatrix}$$
Vecteur directeur : $\vec{v} = (5, -4, 1)$.

**2. Trouver un point** $A$ **de la droite** $\mathcal{D}$ :
Choisissons $z=0$ (paramètre $t=0$).
$$
\begin{cases} x + y - 0 = -1 \implies x + y = -1 \quad (3) \\ x + 2y + 3(0) = 0 \implies x + 2y = 0 \quad (4) \end{cases}
$$
Soustraire $(3)$ de $(4)$:
$$(x + 2y) - (x + y) = 0 - (-1) \implies y = 1$$
Substituer $y=1$ dans $(3)$:
$$x + 1 = -1 \implies x = -2$$
Le point d'intersection est $A = (-2, 1, 0)$.

**3. Équation Paramétrique de** $\mathcal{D}$ :
En utilisant le point $A(-2, 1, 0)$ et le vecteur directeur $\vec{v}(5, -4, 1)$, l'équation paramétrique est :
$$\mathcal{D}: \begin{cases} x = -2 + 5t \\ y = 1 - 4t \\ z = 0 + 1t \end{cases}, \quad t \in \mathbb{R}$$
$$\mathcal{D}: \begin{cases} \mathbf{x = -2 + 5t} \\ \mathbf{y = 1 - 4t} \\ \mathbf{z = t} \end{cases}, \quad t \in \mathbb{R}$$

---

## **Exercice 26 c)** 📐
Plans :
* $\mathcal{P}_1: 2x - z = 1$
* $\mathcal{P}_2: x + y = 2$

Système :
$$
(S) \begin{cases} 2x - z = 1 \quad (1) \\ x + y = 2 \quad (2) \end{cases}
$$

**1. Trouver le vecteur directeur** $\vec{v}$ :
* $\vec{n}_1 = (2, 0, -1)$ (Attention, $y$ n'apparaît pas, donc son coefficient est 0)
* $\vec{n}_2 = (1, 1, 0)$ (Attention, $z$ n'apparaît pas, donc son coefficient est 0)

$$\vec{v} = \begin{pmatrix} 2 \\ 0 \\ -1 \end{pmatrix} \times \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix} = \begin{pmatrix} (0)(0) - (-1)(1) \\ (-1)(1) - (2)(0) \\ (2)(1) - (0)(1) \end{pmatrix} = \begin{pmatrix} 0 - (-1) \\ -1 - 0 \\ 2 - 0 \end{pmatrix} = \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}$$
Vecteur directeur : $\vec{v} = (1, -1, 2)$.

**2. Trouver un point** $A$ **de la droite** $\mathcal{D}$ :
Choisissons $x=0$ (ce choix peut être remplacé par $y=0$ ou $z=0$).
Substituons $x=0$ dans $(S)$:
$$
\begin{cases} 2(0) - z = 1 \implies z = -1 \\ 0 + y = 2 \implies y = 2 \end{cases}
$$
Le point d'intersection est $A = (0, 2, -1)$.

**3. Équation Paramétrique de** $\mathcal{D}$ :
En utilisant le point $A(0, 2, -1)$ et le vecteur directeur $\vec{v}(1, -1, 2)$, l'équation paramétrique est :
$$\mathcal{D}: \begin{cases} x = 0 + 1t \\ y = 2 - 1t \\ z = -1 + 2t \end{cases}, \quad t \in \mathbb{R}$$
$$\mathcal{D}: \begin{cases} \mathbf{x = t} \\ \mathbf{y = 2 - t} \\ \mathbf{z = -1 + 3t} \end{cases}, \quad t \in \mathbb{R}$$


---

## Exercice 27 : Projection Orthogonale d'un Point sur un Plan


Résoudre l'**Exercice 27** consiste à calculer les coordonnées $H(x_H, y_H, z_H)$ de la projection orthogonale d'un point $M$ sur un plan $\mathcal{P}$.

La méthode générale pour trouver la projection orthogonale $H$ est la suivante :
1.  Trouver le **vecteur normal** $\vec{n}$ du plan $\mathcal{P}$.
2.  Déterminer la **droite** $\mathcal{D}$ qui passe par $M$ et qui est **orthogonale** à $\mathcal{P}$. Le vecteur normal $\vec{n}$ est le vecteur directeur de cette droite $\mathcal{D}$.
3.  L'intersection de la droite $\mathcal{D}$ et du plan $\mathcal{P}$ est le point de projection $H$.

***

## **Exercice 27 a)** 🎯
Point : $M = (1, 1, 0)$
Plan : $\mathcal{P}: x - y + 2z = 3$

### **1. Vecteur Normal** $\vec{n}$
L'équation cartésienne du plan est $x - y + 2z = 3$. Le vecteur normal est donné par les coefficients de $x, y, z$ :
$$\vec{n} = (1, -1, 2)$$

### **2. Droite Orthogonale** $\mathcal{D}$
La droite $\mathcal{D}$ passe par $M(1, 1, 0)$ et a pour vecteur directeur $\vec{n}(1, -1, 2)$.
L'équation paramétrique de $\mathcal{D}$ est :
$$\mathcal{D}: \begin{cases} x = 1 + t \\ y = 1 - t \\ z = 0 + 2t \end{cases}, \quad t \in \mathbb{R}$$

### **3. Point de Projection** $H$
$H$ est le point d'intersection de $\mathcal{D}$ et $\mathcal{P}$. On substitue les expressions de $x, y, z$ de la droite $\mathcal{D}$ dans l'équation du plan $\mathcal{P}$ :
$$x - y + 2z = 3$$
$$(1 + t) - (1 - t) + 2(2t) = 3$$
$$1 + t - 1 + t + 4t = 3$$
$$6t = 3 \implies t = \frac{3}{6} = \frac{1}{2}$$

On substitue $t = 1/2$ dans l'équation paramétrique de $\mathcal{D}$ pour trouver les coordonnées de $H$:
$$x_H = 1 + \frac{1}{2} = \frac{3}{2}$$
$$y_H = 1 - \frac{1}{2} = \frac{1}{2}$$
$$z_H = 2 \left( \frac{1}{2} \right) = 1$$

Les coordonnées de la projection orthogonale $H$ sont :
$$\mathbf{H = \left( \frac{3}{2}, \frac{1}{2}, 1 \right)}$$

***

## **Exercice 27 b)** 🎯
Point : $M = (2, -1, 1)$
Plan : $\mathcal{P}: 2x + y = 1$

### **1. Vecteur Normal** $\vec{n}$
L'équation cartésienne du plan est $2x + y = 1$ (le coefficient de $z$ est 0).
$$\vec{n} = (2, 1, 0)$$

### **2. Droite Orthogonale** $\mathcal{D}$
La droite $\mathcal{D}$ passe par $M(2, -1, 1)$ et a pour vecteur directeur $\vec{n}(2, 1, 0)$.
L'équation paramétrique de $\mathcal{D}$ est :
$$\mathcal{D}: \begin{cases} x = 2 + 2t \\ y = -1 + 1t \\ z = 1 + 0t \end{cases}, \quad t \in \mathbb{R}$$

### **3. Point de Projection** $H$
On substitue les expressions de $x, y, z$ de la droite $\mathcal{D}$ dans l'équation du plan $\mathcal{P}$ :
$$2x + y = 1$$
$$2(2 + 2t) + (-1 + t) = 1$$
$$4 + 4t - 1 + t = 1$$
$$3 + 5t = 1$$
$$5t = 1 - 3 \implies 5t = -2 \implies t = -\frac{2}{5}$$

On substitue $t = -2/5$ dans l'équation paramétrique de $\mathcal{D}$ pour trouver les coordonnées de $H$:
$$x_H = 2 + 2 \left( -\frac{2}{5} \right) = 2 - \frac{4}{5} = \frac{10 - 4}{5} = \frac{6}{5}$$
$$y_H = -1 + \left( -\frac{2}{5} \right) = -1 - \frac{2}{5} = \frac{-5 - 2}{5} = -\frac{7}{5}$$
$$z_H = 1 + 0t = 1$$

Les coordonnées de la projection orthogonale $H$ sont :
$$\mathbf{H = \left( \frac{6}{5}, -\frac{7}{5}, 1 \right)}$$

***

## **Exercice 27 c)** 🎯
Point : $M = (-1, 5, -1)$
Plan : $\mathcal{P}$ est donné sous **forme paramétrique** :
$$\mathcal{P} = \{ (2 - t + s, 1 + 2t - s, 3t + 2s), t, s \in \mathbb{R} \}$$

### **1. Équation Cartésienne du Plan** $\mathcal{P}$
Pour trouver le vecteur normal, il faut d'abord extraire deux vecteurs directeurs du plan $\mathcal{P}$.
$$
\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} -1 \\ 2 \\ 3 \end{pmatrix} + s \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}
$$
* Point du plan : $A = (2, 1, 0)$
* Vecteurs directeurs : $\vec{u} = (-1, 2, 3)$ et $\vec{v} = (1, -1, 2)$.

Le vecteur normal $\vec{n}$ est le produit vectoriel de $\vec{u}$ et $\vec{v}$ :
$$\vec{n} = \vec{u} \times \vec{v} = \begin{pmatrix} -1 \\ 2 \\ 3 \end{pmatrix} \times \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} = \begin{pmatrix} (2)(2) - (3)(-1) \\ (3)(1) - (-1)(2) \\ (-1)(-1) - (2)(1) \end{pmatrix} = \begin{pmatrix} 4 - (-3) \\ 3 - (-2) \\ 1 - 2 \end{pmatrix} = \begin{pmatrix} 7 \\ 5 \\ -1 \end{pmatrix}$$
L'équation cartésienne de $\mathcal{P}$ est donc $7x + 5y - 1z + d = 0$.
En utilisant le point $A(2, 1, 0)$ pour trouver $d$:
$$7(2) + 5(1) - 1(0) + d = 0$$
$$14 + 5 + 0 + d = 0 \implies 19 + d = 0 \implies d = -19$$
**Équation Cartésienne de** $\mathcal{P}$: $7x + 5y - z - 19 = 0$.

### **2. Droite Orthogonale** $\mathcal{D}$
La droite $\mathcal{D}$ passe par $M(-1, 5, -1)$ et a pour vecteur directeur $\vec{n}(7, 5, -1)$.
L'équation paramétrique de $\mathcal{D}$ est :
$$\mathcal{D}: \begin{cases} x = -1 + 7k \\ y = 5 + 5k \\ z = -1 - 1k \end{cases}, \quad k \in \mathbb{R}$$
(Nous utilisons le paramètre $k$ pour éviter la confusion avec $t$ et $s$ du plan).

### **3. Point de Projection** $H$
On substitue les expressions de $x, y, z$ de la droite $\mathcal{D}$ dans l'équation cartésienne du plan $\mathcal{P}$ :
$$7x + 5y - z - 19 = 0$$
$$7(-1 + 7k) + 5(5 + 5k) - (-1 - k) - 19 = 0$$
$$-7 + 49k + 25 + 25k + 1 + k - 19 = 0$$
Regroupons les termes en $k$ :
$$(49 + 25 + 1)k = 75k$$
Regroupons les constantes :
$$(-7 + 25 + 1 - 19) = 0$$
Donc :
$$75k + 0 = 0 \implies k = 0$$

On substitue $k = 0$ dans l'équation paramétrique de $\mathcal{D}$ pour trouver les coordonnées de $H$:
$$x_H = -1 + 7(0) = -1$$
$$y_H = 5 + 5(0) = 5$$
$$z_H = -1 - 1(0) = -1$$

Les coordonnées de la projection orthogonale $H$ sont :
$$\mathbf{H = (-1, 5, -1)}$$
(Le point de projection est $M$ lui-même, car $M$ est déjà dans le plan $\mathcal{P}$.)
